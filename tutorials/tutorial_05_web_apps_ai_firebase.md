# Tutorial #5: Tworzenie prawdziwych aplikacji webowych z Google AI + Firebase

## Film: Jak Tworzyć i Publikować PRAWDZIWE Aplikacje Webowe (Google AI + Firebase)
**ID filmu:** FapvBoyMh5o  
**Data:** 2026-06-17

---

## TL;DR - Szybka instrukcja:
1. Skonfiguruj projekt w Google Cloud
2. Włącz Firebase i Google AI API
3. Zbuduj aplikację
4. Wdróż na Firebase Hosting

---

## Szczegółowy przewodnik

### KROK 1: Przygotowanie środowiska
```bash
# Zainstaluj Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install -y nodejs

# Zainstaluj Firebase CLI
npm install -g firebase-tools

# Zaloguj się
firebase login
```

### KROK 2: Tworzenie projektu w Google Cloud
1. Wejdź na https://console.cloud.google.com/
2. Utwórz nowy projekt
3. Włącz API:
   - Firebase
   - Google AI (Vertex AI)
   - Cloud Functions

### KROK 3: Inicjalizacja projektu
```bash
mkdir moja-aplikacja
cd moja-aplikacja
firebase init
```

Wybierz:
- Hosting: Firebase Hosting
- Functions: Cloud Functions (Node.js)
- AI: Vertex AI

### KROK 4: Przykładowa aplikacja

**public/index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Moja Aplikacja AI</title>
</head>
<body>
    <h1>Aplikacja z Google AI</h1>
    <input type="text" id="prompt" placeholder="Wpisz zapytanie...">
    <button onclick="zapytanie()">Zapytaj AI</button>
    <div id="wynik"></div>
    
    <script>
        async function zapytanie() {
            const prompt = document.getElementById('prompt').value;
            const response = await fetch('/api/zapytanie', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({prompt})
            });
            const data = await response.json();
            document.getElementById('wynik').innerText = data.wynik;
        }
    </script>
</body>
</html>
```

### KROK 5: Backend (Cloud Functions)

**functions/index.js:**
```javascript
const functions = require('firebase-functions');
const {LanguageServiceClient} = require('@google-cloud/language');

exports.zapytanie = functions.https.onRequest(async (req, res) => {
    const prompt = req.body.prompt;
    
    // Tutaj użyj AI Google (np. Gemini)
    // Przykład:
    const response = await callGeminiAPI(prompt);
    
    res.json({wynik: response});
});
```

### KROK 6: Deploy
```bash
firebase deploy
```

---

## Przydatne linki:
- Firebase: https://firebase.google.com/
- Google AI: https://ai.google/
- Dokumentacja: https://firebase.google.com/docs