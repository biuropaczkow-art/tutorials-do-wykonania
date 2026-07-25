# 🎓 Tutorialy - Playlista "Do wykonania"

Strona z 7 tutoriali z YouTube (playlisty "Do wykonania") oraz narzędzia do śledzenia postępu.

## 📁 Struktura projektu

```
├── README.md                  # Ten plik
├── app.py                     # Serwis Flask
├── requirements.txt           # Zależności Python
├── templates/
│   ├── index.html            # Strona główna
│   ├── view.html             # Podgląd tutoriala
│   └── edit.html             # Edycja notatek
├── tutorials/                  # Tutoriale w formacie Markdown
│   ├── tutorial_01_windows11_android.md
│   ├── tutorial_02_samsung_windows11.md
│   ├── tutorial_03_sim_card_hack.md
│   ├── tutorial_04_hermes_hostinger.md
│   ├── tutorial_05_web_apps_ai_firebase.md
│   ├── tutorial_06_google_ai_studio.md
│   ├── tutorial_07_vibe_coding.md
│   └── tutorial_08_ai_hacking.md
├── progress_tracker.py        # System śledzenia postępu
├── progress_db.json           # Baza danych postępu
└── static/
    └── style.css              # Style CSS
```

## 🚀 Uruchomienie

```bash
# 1. Instalacja zależności
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# lub venv\Scripts\activate  # Windows
pip install -r requirements.txt

# 2. Uruchomienie serwisu
python app.py

# 3. Otwórz w przeglądarce
http://localhost:5000
```

## 📊 System śledzenia postępu

```bash
# Sprawdź status
python progress_tracker.py --status

# Pobierz raport
python progress_tracker.py --report

# Zaktualizuj postęp
python progress_tracker.py --update <video_id> --watched --notes --tasks
```

## 📺 Playlista "Do wykonania"

| # | Tytuł | Filmy |
|---|-------|-------|
| 1 | Windows 11 na Androidzie | 1 |
| 2 | Windows 11 na Samsungu | 1 |
| 3 | SIM Card Hack | 1 |
| 4 | Hermes Agent na Hostingerze | 1 |
| 5 | Aplikacje Webowe z Google AI + Firebase | 1 |
| 6 | Google AI Studio | 1 |
| 7 | Vibe Coding | 1 |
| 8 | AI App do Hackingu | 1 |

## 🛠️ Technologie

- **Backend:** Python + Flask
- **Frontend:** HTML5 + CSS3
- **Markdown:** Konwersja do HTML
- **Baza danych:** JSON

## 📝 Licensa

MIT License