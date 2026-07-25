# Tutorial #6: Wdrożenie stron internetowych z Google AI Studio - Krok po Kroku

## Film: Jak Poprawnie Wdrożyć Strony Internetowe Google AI Studio - Krok po Kroku
**ID filmu:** LJlzeOA_GpA  
**Data:** 2026-06-17

---

## TL;DR - Szybka instrukcja:
1. Stwórz projekt w Google AI Studio
2. Zaprojektuj stronę
3. Skonfiguruj domenę
4. Wdróż na hosting

---

## Szczegółowy przewodnik

### KROK 1: Dostęp do Google AI Studio
1. Wejdź na https://aistudio.google.com/
2. Zaloguj się kontem Google
3. Utwórz nowy projekt

### KROK 2: Tworzenie strony
1. Kliknij "Create new app"
2. Wybierz szablon lub zacznij od czystego
3. Skorzystaj z AI do generowania treści

### KROK 3: Generowanie treści przez AI
```javascript
// Przykładowe zapytanie do AI:
"Stwórz stronę portfolio dla developera z opisem umiejętności w JavaScript, Python, AI"
```

### KROK 4: Eksportowanie kodu
1. Kliknij "Export"
2. Pobierz gotowy kod HTML/CSS/JS
3. Lub skonfiguruj CI/CD

### KROK 5: Hosting na Firebase
```bash
# Zainstaluj Firebase CLI
npm install -g firebase-tools
firebase login

# Inicjalizacja
firebase init hosting

# Konfiguracja
# public: ./dist (lub katalog z Twoją stroną)
# configure as single-page app? Yes
```

### KROK 6: Deploy
```bash
firebase deploy
```

### KROK 7: Niestandardowa domena
1. Wejdź w Firebase Console > Hosting
2. Kliknij "Add custom domain"
3. Dodaj swoją domenę
4. Skonfiguruj rekordy DNS:
   - A: 126.0.0.1
   - AAAA: 2001:4888::1

---

## Przykładowa struktura projektu
```
moja-strona/
├── index.html
├── styles.css
├── app.js
├── assets/
│   ├── logo.png
│   └── favicon.ico
└── firebase.json
```

**firebase.json:**
```json
{
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```