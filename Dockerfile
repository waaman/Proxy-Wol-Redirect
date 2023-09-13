FROM python:3.12.0a1-slim-bullseye

ENV SERVER_PORT=8565
ENV TIMEOUT=120
ENV MAC="52:54:00:42:35:5C"
ENV REDIRECT="https://google.fr"
ENV SSL_VERIFY=true

WORKDIR /usr/src/app
COPY root /
RUN \
    # Timezone
    echo "${TZ}" > /etc/timezone \
    # Dépendances python nécessaires
    && pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./wol-serveur.py" ]