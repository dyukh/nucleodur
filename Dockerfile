FROM python:3.13-bookworm
LABEL maintainer="Andrey Sobolev <SobolevAY@ipgg.sbras.ru>"

WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY .streamlit/config.toml .streamlit/config.toml
COPY nucl.py .
COPY stream.py .
COPY template.xlsx .

EXPOSE 8501
ENTRYPOINT [ "streamlit", "run"]
CMD [ "stream.py" ]
