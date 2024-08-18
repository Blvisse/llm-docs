import logging

import openai

try:
    import requests

    logging.debug("successfully installed libraries")
except ModuleNotFoundError as mnf:
    logging.error("Error importing module {} Library not found ".format(mnf.name))
    logging.error("Error log details: {}".format(mnf))


def fetch_data() -> dict:
    docs_url = 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json'

    response = requests.get(docs_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise requests.exceptions.HTTPError("Failed to fetch data")
