#!/bin/sh

# db
if grep -qF "172.20.2.11 localhost" /etc/hosts; then
    echo "Entry already exists in /etc/hosts"
else
    echo -e "172.20.2.11 localhost_db" | sudo tee -a /etc/hosts >/dev/null
    echo "Entry added to /etc/hosts"
fi
# adminer
if grep -qF "172.20.2.12 localhost_adminer" /etc/hosts; then
    echo "Entry already exists in /etc/hosts"
else
    echo -e "172.20.2.12 localhost_adminer" | sudo tee -a /etc/hosts >/dev/null
    echo "Entry added to /etc/hosts"
fi
# django
if grep -qF "172.20.2.13 localhost_django" /etc/hosts; then
    echo "Entry already exists in /etc/hosts"
else
    echo -e "172.20.2.13 localhost_django" | sudo tee -a /etc/hosts >/dev/null
    echo "Entry added to /etc/hosts"
fi

docker compose up --build