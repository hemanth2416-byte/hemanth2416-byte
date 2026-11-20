<p align="center">
  <img src="assets/hero.svg" width="900" alt="Hemanth Kumar Gajagiri: animated soundwave. Full-Stack and Forward Deployed AI Engineer. AI is easy to demo. Engineering is making it last, safely."/>
</p>

<p align="center">
  <a href="https://hireanex.com"><img src="assets/badge-hireanex.svg" alt="Now at hireanex.com"/></a>
  <a href="https://www.linkedin.com/in/hemanth-kumar-gajagiri-829497233/"><img src="assets/badge-linkedin.svg" alt="LinkedIn"/></a>
  <img src="assets/badge-location.svg" alt="SF Bay Area"/>
  <img src="assets/badge-years.svg" alt="7+ years"/>
</p>

<h3 align="center">AI is easy to demo. Engineering is making it last — safely.</h3>

<p align="center">
  <b>Software engineer first. AI is how I build, not a substitute for engineering.</b><br/>
  <sub>I build voice AI that talks to people in real time, and the systems that make what it says explainable, auditable and durable.</sub>
</p>

<p align="center"><img src="assets/divider.svg" width="900" alt=""/></p>

## 🎙️ Live transcript

<sub>A mock session. The AI interviewer gets interviewed about me, and every answer cites where it came from.</sub>

<p align="center">
  <img src="assets/transcript.svg" width="900" alt="Mock transcript. A visitor asks the AI interviewer about Hemanth; each answer comes with an evidence tag."/>
</p>

<details>
<summary><b>Read the transcript as text</b></summary>

> **Visitor:** Who is Hemanth, in one line?<br/>
> **AI interviewer:** Software engineer first. AI is how he builds, not a substitute for engineering. 7+ years; Lead Full-Stack AI Engineer at Hireanex since May 2022. <kbd>evidence: Hireanex · May 2022 – present</kbd>
>
> **Visitor:** Has he actually shipped real-time voice?<br/>
> **AI interviewer:** Yes. He built Hireanex's voice engine: streaming STT → LLM → streaming TTS, with voice activity detection and barge-in handling. It is live with real users and pilot customers. <kbd>evidence: real-time voice engine</kbd>
>
> **Visitor:** Why should anyone trust an AI hiring score?<br/>
> **AI interviewer:** Every score on his platform is tied to transcript evidence, so it is explainable and auditable. <kbd>evidence: LLM evaluation layer</kbd>
>
> **Visitor:** And underneath the AI?<br/>
> **AI interviewer:** Infrastructure roots. At Zingaro AI he moved services to Docker/Kubernetes across 5+ environments (~60% less config drift) and cut cloud cost by 15%+. <kbd>evidence: Zingaro AI · 2019 – 2022</kbd>

</details>

<p align="center"><img src="assets/divider.svg" width="900" alt=""/></p>

## ⚡ The pipeline behind the voice

<p align="center">
  <img src="assets/pipeline.svg" width="900" alt="Real-time lane: mic, VAD, STT, LLM, TTS, speaker, all streaming, with barge-in. Async lane: audio, transcript, evidence, scores, report on BullMQ workers."/>
</p>

| Lane | What it has to get right |
|---|---|
| **Real-time** | Streaming STT → LLM → streaming TTS. Voice activity detection decides when the candidate is done talking. Barge-in: if they speak over the bot, the bot stops and listens. |
| **Async** | BullMQ queues and idempotent workers turn audio → transcript → evidence → scores, so any step can be retried safely. |
| **Trust** | An LLM evaluation layer ties every score to transcript evidence, so every report is explainable and auditable. |

<p align="center"><img src="assets/divider.svg" width="900" alt=""/></p>

## 🏗️ Now: [Hireanex](https://hireanex.com)

<p align="center">
  <a href="https://hireanex.com"><img src="assets/hireanex.svg" width="900" alt="Hireanex: real-time voice interviews in, evidence-backed hiring reports out. Live with real users and pilot customers."/></a>
</p>

**Lead Full-Stack AI Engineer · May 2022 – present.** An AI interview platform, live with real users and pilot customers.

- 🎧 **Voice engine** — streaming STT → LLM → streaming TTS, VAD, barge-in handling
- 🧱 **Backend** — Node/Fastify + PostgreSQL (Neon), REST + WebSocket APIs, an interview lifecycle state machine
- 🔁 **Pipelines** — BullMQ queues, idempotent workers: audio → transcript → evidence → scores
- 🧠 **Models** — fine-tuned open-source models with LoRA (PyTorch, Hugging Face, CUDA), served with vLLM
- 🧾 **Evals** — every score tied to transcript evidence: explainable, auditable
- 🤝 **Forward deployed** — on the ground with pilot customers: requirements, integrations into hiring workflows, feedback shipped in days
- ☁️ **Ops** — AWS, Docker, Kubernetes, Terraform, CI/CD, tests, observability
- 🤖 **AI-native workflow** — Claude Code, Codex, MCP agents. I own the architecture, the specs and the code review.

<p align="center"><img src="assets/divider.svg" width="900" alt=""/></p>

## 📼 Signal history

<p align="center">
  <img src="assets/career.svg" width="900" alt="Timeline: Zingaro AI 2019 to 2022, cloud infrastructure and distributed systems in Hyderabad; Hireanex 2022 to present, Lead Full-Stack AI Engineer."/>
</p>

## 🎚️ Stack mixer

<p align="center">
  <img src="assets/stack.svg" width="900" alt="Stack: TypeScript, React, Next.js, Tailwind; Python/FastAPI, Node/Fastify, Java/Spring Boot; PostgreSQL, Redis, vector DBs, ETL; LLMs, RAG, LangGraph, STT/TTS, evals; LoRA/QLoRA, PyTorch, Hugging Face, CUDA, vLLM; AWS, Azure, Docker, Kubernetes, Terraform, Prometheus/Grafana; Claude Code, Codex, MCP."/>
</p>

<p align="center"><img src="assets/divider.svg" width="900" alt=""/></p>

## 🕹️ Beat the voice bot

The interviewer always speaks first, so the bot has taken the center. You are **🎤**, the bot is **🔊**.
Click an empty square, then press **Submit** on the issue that opens. A GitHub Action plays the bot's reply and updates this board.

<!-- TTT:START -->
<div align="center">

|   | 1 | 2 | 3 |
|:-:|:-:|:-:|:-:|
| **A** | [⬜](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ttt%7CA1&body=Just+press+Submit) | [⬜](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ttt%7CA2&body=Just+press+Submit) | [⬜](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ttt%7CA3&body=Just+press+Submit) |
| **B** | [⬜](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ttt%7CB1&body=Just+press+Submit) | 🔊 | [⬜](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ttt%7CB3&body=Just+press+Submit) |
| **C** | [⬜](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ttt%7CC1&body=Just+press+Submit) | [⬜](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ttt%7CC2&body=Just+press+Submit) | [⬜](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ttt%7CC3&body=Just+press+Submit) |

> 🔊 **bot:** *"Center's mine. Your turn. I'll wait for silence before I answer."*

<sub>Game #1 · move 1 · 🎤 to play</sub>

</div>
<!-- TTT:END -->

<table>
<tr>
<td valign="top" width="50%">

**📜 Last moves**

<!-- TTT-MOVES:START -->
| game | player | move | bot reply |
|:-:|---|:-:|:-:|
| 1 | 🔊 bot | B2 | — |
<!-- TTT-MOVES:END -->

</td>
<td valign="top" width="50%">

**🏆 Beat the bot**

<!-- TTT-BOARD:START -->
| player | wins | draws |
|---|:-:|:-:|
| *nobody yet* | 0 | 0 |
<!-- TTT-BOARD:END -->

</td>
</tr>
</table>

### 🗣️ Or interview the interviewer

Pick a question. The Action replies on your issue with an answer and the evidence behind it, then logs it below.

| Question | |
|---|:-:|
| 🎙️ Has he shipped real-time voice? | [<kbd>ask</kbd>](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ask%7Cvoice&body=Just+press+Submit) |
| 🧾 How are AI scores made trustworthy? | [<kbd>ask</kbd>](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ask%7Cevidence&body=Just+press+Submit) |
| 🧠 Does he fine-tune models? | [<kbd>ask</kbd>](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ask%7Cmodels&body=Just+press+Submit) |
| ☁️ What's under the AI: infra? | [<kbd>ask</kbd>](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ask%7Cinfra&body=Just+press+Submit) |
| 🤝 What does forward deployed mean for him? | [<kbd>ask</kbd>](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ask%7Cfde&body=Just+press+Submit) |
| ⚙️ How does he use AI to build? | [<kbd>ask</kbd>](https://github.com/hemanth2416-byte/hemanth2416-byte/issues/new?title=ask%7Cworkflow&body=Just+press+Submit) |

<!-- ASK:START -->
<sub>Recently asked: <i>nothing yet</i></sub>
<!-- ASK:END -->

<details>
<summary><b>How the game works</b></summary>

1. Each link opens a pre-filled issue. Titles look like `ttt|A1` (a move) or `ask|voice` (a question).
2. `.github/workflows/voice-bot.yml` runs on `issues: opened` and checks the title.
3. **`ttt|<cell>`**: it validates the move against the board saved in `game/state.json`, plays the bot's reply (minimax, with a small chance of a "barge-in blunder" so it can be beaten), rewrites the block between `TTT:START` and `TTT:END`, adds a row to *Last moves*, updates the win counts on a win or draw, and starts a new game.
4. **`ask|<topic>`**: it posts the matching answer from a fixed, fact-checked answer bank (`game/answers.json`, every answer with its evidence) and adds it to *Recently asked*.
5. It comments on the issue with the result and closes it. Invalid moves get a friendly reply and nothing changes.

</details>

<p align="center"><img src="assets/divider.svg" width="900" alt=""/></p>

## 🐍 Contribution waveform

<p align="center">
  <img src="https://raw.githubusercontent.com/hemanth2416-byte/hemanth2416-byte/output/github-contribution-grid-snake.svg" alt="Contribution snake animation"/>
</p>

<p align="center">
  <img src="assets/divider.svg" width="900" alt=""/><br/>
  <i>AI is easy to demo.<br/>Engineering is making it last — safely.</i><br/><br/>
  <a href="https://hireanex.com">hireanex.com</a> · <a href="https://www.linkedin.com/in/hemanth-kumar-gajagiri-829497233/">LinkedIn</a>
</p>
