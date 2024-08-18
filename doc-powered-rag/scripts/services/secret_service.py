from dotenv import load_dotenv
import os


def _get_gpt_secret() -> str:
    return os.getenv("OPEN_API_KEY")
