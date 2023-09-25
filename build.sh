#!/usr/bin/env bash
# exit on error
set -o errexit

apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
