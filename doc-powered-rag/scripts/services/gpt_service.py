import logging

import openai

try:
    from openai import OpenAI
    import os
    from dotenv import load_dotenv
    from scripts.services import secret_service

    load_dotenv()

    logging.debug("successfully installed libraries")
except ModuleNotFoundError as mnf:
    logging.error("Error importing module {} Library not found ".format(mnf.name))
    logging.error("Error log details: {}".format(mnf))


def chat_completion(message: dict,model_name: str = "gpt-3.5-turbo-0125"):
    client_secret = secret_service._get_gpt_secret()
    if secret_service is not None:
        openai_client = OpenAI(api_key=client_secret)
        response = openai_client.chat.completions.create(
            model=model_name,
            messages=[message]
        )
        return response
    else:
        logging.error("Open API key missing")
