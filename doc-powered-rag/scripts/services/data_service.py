import logging
import json
import os.path

DATA_JSON_PATH = '../../data/documents.json'
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

def fetch_documents(response: dict) -> list:
    documents = []

    for document in response:
        course_name = document['course']

        for doc in document['documents']:
            doc['course'] = course_name
            documents.append(doc)

    return documents


def save_documents_json_file(documents: dict) -> None:
    #check if document already exists

    if os.path.isfile(DATA_JSON_PATH):
        print("File already exists, skipping saving")
    else:
        with open(DATA_JSON_PATH, 'w') as outfile:
            print("Writing to file {}".format(DATA_JSON_PATH))
            json.dump(documents, outfile)
            print("Successfully written to file {}".format(DATA_JSON_PATH))


