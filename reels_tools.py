import json
from pathlib import Path

TRANSCRIPTIONS_FILE = Path(__file__).parent / "transcriptions.json"


def get_creator_transcriptions(creator: str) -> str:
    """Retorna todas as transcrições dos vídeos de um criador em uma única string markdown.

    Use esta ferramenta para obter os roteiros/transcrições de referência de um criador
    antes de escrever um novo conteúdo no estilo dele.

    Args:
        creator (str): Nome do criador (ex.: "jeffnippard", "kallaway", "rourkeheath").

    Returns:
        str: Transcrições no formato:
            Transcript 1
            <transcrição do primeiro vídeo>

            Transcript 2
            <transcrição do segundo vídeo>
    """
    data = json.loads(TRANSCRIPTIONS_FILE.read_text(encoding="utf-8"))
    videos = data.get(creator)
    if not videos:
        return f"Criador '{creator}' não encontrado. Disponíveis: {', '.join(data)}."

    return "\n\n".join(
        f"Transcript {i}\n{item['transcription']}"
        for i, item in enumerate(videos, 1)
    )


def list_available_creators() -> str:
    """Lista todos os criadores disponíveis no arquivo de transcrições.

    Use esta ferramenta para descobrir quais criadores existem antes de pedir
    as transcrições de um deles com `get_creator_transcriptions`.

    Returns:
        str: Nomes dos criadores separados por vírgula (ex.: "jeffnippard, kallaway, rourkeheath").
    """
    data = json.loads(TRANSCRIPTIONS_FILE.read_text(encoding="utf-8"))
    if not data:
        return "Nenhum criador disponível."
    return ", ".join(data)
