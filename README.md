# AGI Copywriter

An AI copywriting agent that generates Instagram Reels scripts by mimicking the style of reference content creators.

## How it works

1. **Transcription** — `transcripter.py` downloads MP4 reels from reference creators and transcribes them using Groq's Whisper model, saving results to `transcriptions.json`.
2. **Agent** — `agent.py` spins up an [agno](https://github.com/agno-agi/agno) agent (GPT-4.1-mini) that:
   - Searches the web via Tavily to gather facts about the requested topic.
   - Reads transcriptions of the selected creator to learn their style.
   - Proposes 10+ hook options and writes a 150–250 word reel script in English, faithfully mimicking the chosen creator's tone and sentence structure.

## Stack

| Component | Technology |
|---|---|
| Agent framework | [agno](https://github.com/agno-agi/agno) |
| LLM | OpenAI GPT-4.1-mini |
| Transcription | Groq Whisper large-v3 |
| Web search | Tavily |
| Session storage | SQLite |

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/Renanes/agi-copywriter.git
cd agi-copywriter

# 2. Install dependencies (requires Python 3.12+)
pip install -e .

# 3. Configure environment
cp .env.example .env
# Edit .env and fill in your API keys

# 4. Add reference videos
# Place MP4 files under videos/<creator_name>/*.mp4
# Example: videos/jeffnippard/my_reel.mp4

# 5. Transcribe videos
python transcripter.py

# 6. Start the agent
python agent.py
```

## Environment variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | OpenAI API key (GPT-4.1-mini) |
| `GROQ_API_KEY` | Groq API key (Whisper transcription) |
| `TAVILY_API_KEY` | Tavily API key (web search) |

Copy `.env.example` to `.env` and fill in your keys. **Never commit `.env`.**
