import os, json
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

transcriptions = {}
for video in Path("videos").glob("*/*.mp4"):
    creator = video.parent.name
    print(f"Transcrevendo {creator}/{video.name}...")
    with open(video, "rb") as f:
        text = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=(video.name, f.read()),
            response_format="text",
        )
    transcriptions.setdefault(creator, []).append(
        {"video": video.name, "transcription": str(text).strip()}
    )

Path("transcriptions.json").write_text(
    json.dumps(transcriptions, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("Pronto! Salvo em transcriptions.json")
