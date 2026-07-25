# Tutorial #4: Instalacja Hermes Agent na Hostingerze (VPS)

## Film: Poradnik Hermes Agent na Hostinger: Zainstaluj i Skonfiguruj Hermes na VPS-ie
**ID filmu:** Ivkf5F3wFGk  
**Data:** 2026-06-17

---

## TL;DR - Szybka instrukcja:
1. Zarejestruj się na Hostingerze
2. Uruchom VPS z Debian/Ubuntu
3. Zainstaluj Hermes Agenta
4. Skonfiguruj dostęp

---

## Szczegółowy przewodnik

### KROK 1: Przygotowanie VPS
```bash
# Po zalogowaniu się na VPS
ssh root@twoj-vps-ip
```

### KROK 2: Instalacja zależności
```bash
# Ubuntu/Debian
apt update
apt install -y curl wget git python3 python3-pip

# Alternatywnie użyj uv (szybszy)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### KROK 3: Pobranie Hermes Agenta
```bash
# Utwórz katalog
mkdir /opt/hermes
cd /opt/hermes

# Pobierz najnowszą wersję
# (sprawdź na https://hermes-agent.com najnowszy link)
wget https://github.com/nousresearch/hermes-agent/releases/latest/download/hermes-linux-amd64.tar.gz
tar -xzf hermes-linux-amd64.tar.gz
```

### KROK 4: Konfiguracja
```bash
# Utwórz katalog profilu
mkdir -p /opt/data/profiles/websytes

# Skopiuj token/secret jeśli masz
# Skonfiguruj środowisko
export HERES_TOKEN="twój-token"
```

### KROK 5: Uruchomienie
```bash
# Uruchom jako serwis
./hermes --profile websytes --port 3000
```

### KROK 6: Docker (alternatywa)
```bash
# Jeśli masz docker
docker run -d \
  -p 3000:3000 \
  -v /opt/data/profiles:/opt/data/profiles \
  --name hermes \
  ghcr.io/nousresearch/hermes-agent:latest
```

---

## Konfiguracja jako usługa (systemd)

Utwórz plik `/etc/systemd/system/hermes.service`:
```ini
[Unit]
Description=Hermes Agent
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/hermes
ExecStart=/opt/hermes/hermes --profile websytes
Restart=always

[Install]
WantedBy=multi-user.target
```

Aktywuj:
```bash
systemctl daemon-reload
systemctl enable hermes
systemctl start hermes
```