
# 🤖 Slack_MCP Server

A smart Slack toolset that supports **manual commands** and **AI-powered interactions** via **Claude** and **Agno**, acting as a Middleware Command Processor (MCP).

---

## ⚙️ Project Overview

This project integrates with **Slack** in two flexible ways:
1. 🔧 **Manual Tools** — Trigger custom logic with predefined Slack commands.
2. 🤖 **AI-powered** — Use **Claude (via Agno)** to process natural language commands.

Ideal for automating workflows, responding intelligently in threads, and enhancing Slack-based productivity.

---

## 🗃️ Project Structure

| File | Description |
|------|-------------|
| `main.py` | App entry point — routes messages to the appropriate handler |
| `slack.py` | Slack event handling and API communication |
| `slack_manual.py` | Manual command handlers (e.g., `/status`, `/report`) |
| `README.md` | You are here 📘 |
| `pyproject.toml` | Project dependencies and settings |
| `uv.lock` | Locked dependency versions |
| `.gitignore` | Files ignored by Git |
| `.python-version` | Python version used for virtual environment |

---

## 🚀 How It Works

### 🛠 Manual Slack Tools

- Uses Slack slash commands or message keywords.
- Routes messages to specific functions inside `slack_manual.py`.
- Example:
  ```bash
  /report today
  ```
  ➝ Generates a manual task report.

### 🧠 Claude (via Agno) Integration

- Connects to Claude using Agno as a middleware API.
- Accepts flexible natural language like:
  ```
  "Summarize this channel’s last 5 messages."
  "Create a ClickUp task from this message."
  ```
- Claude processes the intent and Slack_MCP executes the right logic.

---

## 🔧 Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/slack_mcp.git
cd slack_mcp
```

### 2. Install dependencies

```bash
pip install -r requirements.txt   # or use `uv` if preferred
```

---

## 🔐 Environment Variables

Set up a `.env` file with:

```env
# Slack
SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...

# Claude / Agno
AGNO_API_KEY=...
CLAUDE_MODEL_ID=claude-2

# Optional
LOG_LEVEL=info
```

---

## 🧪 Running Locally

```bash
python main.py
```

Or using uvicorn (if using FastAPI):
```bash
uvicorn main:app --reload
```

---

## 📎 Useful Commands

| Command | Description |
|--------|-------------|
| `/status` | Shows current server and AI status |
| `/mcp help` | Lists available manual and Claude commands |
| Natural messages | Routed through Claude via Agno |

---

## 📬 Future Improvements

- [ ] Slack thread-context memory
- [ ] Claude fallback when manual commands fail
- [ ] ClickUp/Jira integration

---

## 📝 License

MIT License

---

Built by **SukeshOfficial** ⚡
