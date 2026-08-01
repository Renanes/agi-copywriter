# AGI Copywriter

<p>
  <a href="#english-version">English</a> •
  <a href="#versão-em-português">Português</a>
</p>

---

## English Version

An AI copywriting agent that generates Instagram Reels scripts by mimicking the style of reference content creators.

### How it works

1. **Transcription** — `transcripter.py` processes MP4 reels from reference creators and transcribes them using Groq's Whisper model, saving results to `transcriptions.json`.
2. **Agent** — `agent.py` spins up an [agno](https://github.com/agno-agi/agno) agent (GPT-4.1-mini) that:
   - Searches the web via Tavily to gather facts about the requested topic.
   - Reads transcriptions of the selected creator to learn their style.
   - Proposes 10+ hook options and writes a 150–250 word reel script in English, faithfully mimicking the chosen creator's tone and sentence structure.

### Stack

| Component | Technology |
|---|---|
| Agent framework | [agno](https://github.com/agno-agi/agno) |
| LLM | OpenAI GPT-4.1-mini |
| Transcription | Groq Whisper large-v3 |
| Web search | Tavily |
| Session storage | SQLite |

### Setup

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

### Environment variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | OpenAI API key (GPT-4.1-mini) |
| `GROQ_API_KEY` | Groq API key (Whisper transcription) |
| `TAVILY_API_KEY` | Tavily API key (web search) |

Copy `.env.example` to `.env` and fill in your keys. **Never commit `.env`.**

---

## Versão em Português

Um agente de IA para copywriting que gera roteiros de Reels para Instagram imitando o estilo de criadores de conteúdo de referência.

### Como funciona

1. **Transcrição** — `transcripter.py` processa os arquivos MP4 dos criadores de referência e os transcreve usando o modelo Whisper da Groq, salvando os resultados em `transcriptions.json`.
2. **Agente** — `agent.py` inicializa um agente [agno](https://github.com/agno-agi/agno) (GPT-4.1-mini) que:
   - Pesquisa na web via Tavily para coletar fatos sobre o tema solicitado.
   - Lê as transcrições do criador selecionado para aprender seu estilo.
   - Sugere 10+ opções de hook e escreve um roteiro de 150–250 palavras em inglês, imitando fielmente o tom e a estrutura de frases do criador escolhido.

### Tecnologias

| Componente | Tecnologia |
|---|---|
| Framework de agentes | [agno](https://github.com/agno-agi/agno) |
| LLM | OpenAI GPT-4.1-mini |
| Transcrição | Groq Whisper large-v3 |
| Busca na web | Tavily |
| Armazenamento de sessão | SQLite |

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/Renanes/agi-copywriter.git
cd agi-copywriter

# 2. Instale as dependências (requer Python 3.12+)
pip install -e .

# 3. Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env e preencha suas chaves de API

# 4. Adicione os vídeos de referência
# Coloque os arquivos MP4 em videos/<nome_do_criador>/*.mp4
# Exemplo: videos/jeffnippard/meu_reel.mp4

# 5. Transcreva os vídeos
python transcripter.py

# 6. Inicie o agente
python agent.py
```

### Variáveis de ambiente

| Variável | Descrição |
|---|---|
| `OPENAI_API_KEY` | Chave da API da OpenAI (GPT-4.1-mini) |
| `GROQ_API_KEY` | Chave da API da Groq (transcrição Whisper) |
| `TAVILY_API_KEY` | Chave da API da Tavily (busca na web) |

Copie `.env.example` para `.env` e preencha suas chaves. **Nunca faça commit do `.env`.**
