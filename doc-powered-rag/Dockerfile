FROM python:3.12.3-slim-bullseye

RUN mkdir doc-powered-rag
WORKDIR doc-powered-rag
COPY . .


RUN python3 -m pip install -r requirements.txt

RUN chmod +x cli.sh
RUN chmod +x start.sh


CMD ["/doc-powered-rag/start.sh"]