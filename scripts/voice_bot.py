#!/usr/bin/env python3
"""Voice-bot game engine for the profile README.

Handles two kinds of issues (title is untrusted input, read from env):
  ttt|<cell>   a tic-tac-toe move, e.g. ttt|A1
  ask|<topic>  a question from game/answers.json, e.g. ask|voice

Updates game/state.json and the marked blocks in README.md, and writes the
reply for the issue to the file given in $REPLY_FILE.
"""
import json
import os
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "game" / "state.json"
ANSWERS = ROOT / "game" / "answers.json"
README = ROOT / "README.md"
REPO = os.environ.get("GITHUB_REPOSITORY", "hemanth2416-byte/hemanth2416-byte")

CELLS = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
HUMAN, BOT = "X", "O"
BLUNDER = 0.2  # chance the bot "barges in" with a random move, so it can be beaten

BOT_LINES = {
    "move": [
        "Heard you. My turn.",
        "Silence detected. Responding.",
        "Streaming my answer back.",
        "Interesting choice. Logged as evidence.",
    ],
    "blunder": ["Oops, I barged in before you finished. That one's on me."],
    "bot_win": ["Three in a row. Evidence attached. New game, center's mine again."],
    "human_win": ["You beat me. I'll add that to the transcript. New game started."],
    "draw": ["Draw. Nobody interrupted anybody. New game started."],
}


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return new_state()


def new_state():
    s = {"game": 1, "board": [""] * 9, "moves": [], "leaderboard": {}, "asked": [], "bot_line": ""}
    start_game(s)
    return s


def start_game(s):
    s["board"] = [""] * 9
    s["board"][4] = BOT  # the interviewer always speaks first
    s["move_no"] = 1
    s["bot_line"] = "Center's mine. Your turn. I'll wait for silence before I answer."


def winner(b):
    for a, c, d in LINES:
        if b[a] and b[a] == b[c] == b[d]:
            return b[a]
    return "draw" if all(b) else None


def minimax(b, player):
    w = winner(b)
    if w == BOT:
        return 1, None
    if w == HUMAN:
        return -1, None
    if w == "draw":
        return 0, None
    best = (-2, None) if player == BOT else (2, None)
    for i in range(9):
        if b[i]:
            continue
        b[i] = player
        score, _ = minimax(b, HUMAN if player == BOT else BOT)
        b[i] = ""
        if (player == BOT and score > best[0]) or (player == HUMAN and score < best[0]):
            best = (score, i)
    return best


def bot_move(b, rng):
    free = [i for i in range(9) if not b[i]]
    if rng.random() < BLUNDER:
        return rng.choice(free), True
    return minimax(b, BOT)[1], False


def record(s, user, result):
    entry = s["leaderboard"].setdefault(user, {"wins": 0, "draws": 0})
    if result in ("wins", "draws"):
        entry[result] += 1


def log_move(s, user, cell, reply):
    s["moves"].insert(0, {"n": s["game"], "user": user, "cell": cell, "reply": reply})
    s["moves"] = s["moves"][:5]


def play(s, user, cell, rng):
    idx = CELLS.index(cell)
    b = s["board"]
    if b[idx]:
        return None
    b[idx] = HUMAN
    w = winner(b)
    if w == HUMAN:
        log_move(s, user, cell, "—")
        record(s, user, "wins")
        msg = f"🏆 **@{user} wins game #{s['game']}!** " + BOT_LINES["human_win"][0]
        s["game"] += 1
        start_game(s)
        s["bot_line"] = BOT_LINES["human_win"][0]
        return msg
    if w == "draw":
        log_move(s, user, cell, "—")
        record(s, user, "draws")
        s["game"] += 1
        start_game(s)
        s["bot_line"] = BOT_LINES["draw"][0]
        return "🤝 **Draw.** " + BOT_LINES["draw"][0]

    reply_idx, blundered = bot_move(b, rng)
    b[reply_idx] = BOT
    reply = CELLS[reply_idx]
    log_move(s, user, cell, reply)
    s["move_no"] += 2
    w = winner(b)
    if w == BOT:
        s["game"] += 1
        start_game(s)
        s["bot_line"] = BOT_LINES["bot_win"][0]
        return f"🔊 Bot played **{reply}** and won. " + BOT_LINES["bot_win"][0]
    if w == "draw":
        record(s, user, "draws")
        s["game"] += 1
        start_game(s)
        s["bot_line"] = BOT_LINES["draw"][0]
        return f"🔊 Bot played **{reply}**. 🤝 **Draw.** " + BOT_LINES["draw"][0]
    line = BOT_LINES["blunder"][0] if blundered else rng.choice(BOT_LINES["move"])
    s["bot_line"] = line
    return f"🔊 Bot replied **{reply}**. *\"{line}\"* Your move: [back to the board](https://github.com/{REPO})."


def ask(s, user, topic, answers):
    a = answers[topic]
    s["asked"].insert(0, {"user": user, "topic": topic})
    s["asked"] = s["asked"][:5]
    return f"🎙️ **{a['question']}**\n\n{a['answer']}\n\n`✓ evidence · {a['evidence']}`"


# ---------- README rendering ----------

def cell_md(s, i):
    v = s["board"][i]
    if v == HUMAN:
        return "🎤"
    if v == BOT:
        return "🔊"
    return f"[⬜](https://github.com/{REPO}/issues/new?title=ttt%7C{CELLS[i]}&body=Just+press+Submit)"


def render_board(s):
    rows = ["|   | 1 | 2 | 3 |", "|:-:|:-:|:-:|:-:|"]
    for r, label in enumerate("ABC"):
        rows.append(f"| **{label}** | " + " | ".join(cell_md(s, r * 3 + c) for c in range(3)) + " |")
    return (
        '<div align="center">\n\n' + "\n".join(rows) + "\n\n"
        f"> 🔊 **bot:** *\"{s['bot_line']}\"*\n\n"
        f"<sub>Game #{s['game']} · move {s['move_no']} · 🎤 to play</sub>\n\n</div>"
    )


def render_moves(s):
    out = ["| game | player | move | bot reply |", "|:-:|---|:-:|:-:|"]
    if not s["moves"]:
        out.append("| 1 | 🔊 bot | B2 | — |")
    for m in s["moves"]:
        out.append(f"| {m['n']} | [@{m['user']}](https://github.com/{m['user']}) | {m['cell']} | {m['reply']} |")
    return "\n".join(out)


def render_leaderboard(s):
    out = ["| player | wins | draws |", "|---|:-:|:-:|"]
    ranked = sorted(s["leaderboard"].items(), key=lambda kv: (-kv[1]["wins"], -kv[1]["draws"], kv[0]))
    ranked = [kv for kv in ranked if kv[1]["wins"] or kv[1]["draws"]][:5]
    if not ranked:
        out.append("| *nobody yet* | 0 | 0 |")
    for user, e in ranked:
        out.append(f"| [@{user}](https://github.com/{user}) | {e['wins']} | {e['draws']} |")
    return "\n".join(out)


def render_asked(s, answers):
    if not s["asked"]:
        return "<sub>Recently asked: <i>nothing yet</i></sub>"
    items = " · ".join(f"@{a['user']} asked <i>{answers[a['topic']]['question']}</i>" for a in s["asked"])
    return f"<sub>Recently asked: {items}</sub>"


def replace_block(text, name, body):
    pat = re.compile(rf"(<!-- {name}:START -->\n).*?(\n<!-- {name}:END -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"marker {name} not found in README")
    return pat.sub(lambda m: m.group(1) + body + m.group(2), text)


def render_readme(s, answers):
    t = README.read_text()
    t = replace_block(t, "TTT", render_board(s))
    t = replace_block(t, "TTT-MOVES", render_moves(s))
    t = replace_block(t, "TTT-BOARD", render_leaderboard(s))
    t = replace_block(t, "ASK", render_asked(s, answers))
    README.write_text(t)


def main():
    title = os.environ.get("ISSUE_TITLE", "").strip().lower()
    user = re.sub(r"[^A-Za-z0-9-]", "", os.environ.get("ISSUE_USER", "someone"))[:39] or "someone"
    reply_file = Path(os.environ.get("REPLY_FILE", "reply.md"))
    rng = random.Random()
    s = load_state()
    answers = json.loads(ANSWERS.read_text())

    m_ttt = re.fullmatch(r"ttt\|([abc][123])", title)
    m_ask = re.fullmatch(r"ask\|([a-z]+)", title)
    if m_ttt:
        cell = m_ttt.group(1).upper()
        reply = play(s, user, cell, rng)
        if reply is None:
            reply_file.write_text(f"⚠️ **{cell}** is already taken. Pick an empty square on the board and try again.")
            return
    elif m_ask and m_ask.group(1) in answers:
        reply = ask(s, user, m_ask.group(1), answers)
    else:
        reply = "🤔 I didn't understand that move. Use the links in the README to play."
        reply_file.write_text(reply)
        return

    STATE.write_text(json.dumps(s, indent=2) + "\n")
    render_readme(s, answers)
    reply_file.write_text(reply + "\n\n<sub>Thanks for playing. The board in the README is updated.</sub>")


if __name__ == "__main__":
    main()
