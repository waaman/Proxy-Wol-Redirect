FROM python:3.12.0a1-slim-bullseye
ENV DEBIAN_FRONTEND=noninteractive

ENV SERVER_PORT=8565
ENV TIMEOUT=120
ENV MAC="52:54:00:42:35:5C"
ENV REDIRECT="https://google.fr"

RUN \
    # Timezone
    echo "${TZ}" > /etc/timezone \
    # Mise à jour des dépôts
    && apt-get update \
    # Paquets nécessaires
    && apt-get -y install nano \
    # Ménage
    && apt-get clean && apt-get --purge autoremove && rm -R /var/cache/apt/archives/*


WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY root /

CMD [ "python", "./wol-serveur.py" ]