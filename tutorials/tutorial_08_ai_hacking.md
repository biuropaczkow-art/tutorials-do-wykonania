# Tutorial #8: Budowa AI aplikacji do Hackingu (i jak to zrobić legalnie)

## Film: I Built an UNCENSORED AI app For Hacking (and YOU can too)
**ID filmu:** bwzK1FuSp1Q  
**Data:** 2026-07-02

---

## TL;DR - Szybka instrukcja:
1. Zrozum etyczne hacking
2. Zbuduj narzędzie AI
3. Przetestuj legalnie
4. Zabezpiecz przed nadużyciami

---

## ⚠️ UWAGA - ETYKA I PRAWO

**To, co tworzysz, MUSI być:**
- Używane tylko do celów legalnych
- Testowane na własnym sprzęcie/sieć
- Przeznaczone dla certyfikowanych specjalistów
- Zabezpieczone przed nadużyciem

---

## KROK 1: Etyczny hacking

### Co to znaczy?
- **White Hat** - legalny pentest
- **Gray Hat** - szarolegalne testy
- **Black Hat** - nielegalne ataki (NIGDY!)

### Narzędzia do nauki:
- HackTheBox
- TryHackMe
- OverTheWire
- GoogleCTF

---

## KROK 2: Budowa AI App - Przykład "Phishing Detector"

### Funkcjonalności:
1. Analiza URL pod kątem phishingu
2. Wykrywanie podejrzanych treści
3. Ocena zaufania strony
4. Raportowanie

### KROK 2a: Przygotowanie projektu
```bash
mkdir phishing-detector
cd phishing-detector
npm init -y
npm install express axios dom-parser
```

### KROK 2b: Backend (app.js)
```javascript
const express = require('express');
const axios = require('axios');
const app = express();

app.use(express.json());

// Prosty detector phishingu
app.post('/check', async (req, res) => {
    const { url } = req.body;
    
    // Analiza URL
    const analysis = {
        url: url,
        suspicious: checkSuspicious(url),
        domainAge: await getDomainAge(url),
        ssl: checkSSL(url),
        score: calculateScore(url)
    };
    
    res.json(analysis);
});

function checkSuspicious(url) {
    const suspiciousPatterns = [
        /login\./,
        /secure\./,
        /verify\./,
        /-\d{5,}\./,  // liczby w nazwie
        /bit\.ly/,
        /tinyurl/
    ];
    
    return suspiciousPatterns.some(pattern => pattern.test(url));
}

async function getDomainAge(url) {
    // Implementacja sprawdzania daty domeny
    return "Nieznane";
}

function checkSSL(url) {
    return url.startsWith('https://');
}

function calculateScore(url) {
    let score = 100;
    if (checkSuspicious(url)) score -= 30;
    if (!checkSSL(url)) score -= 40;
    return Math.max(0, score);
}

app.listen(3000, () => {
    console.log('Phishing Detector running on port 3000');
});
```

### KROK 2c: Frontend (index.html)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Phishing Detector AI</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
        .result { padding: 15px; border-radius: 10px; margin-top: 20px; }
        .safe { background: #d4edda; color: #155724; }
        .unsafe { background: #f8d7da; color: #721c24; }
        input, button { padding: 10px; margin: 5px; }
        button { background: #007bff; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>🔍 Phishing Detector AI</h1>
    <p>Wpisz URL, aby sprawdzić zaufanie strony:</p>
    
    <input type="text" id="url" placeholder="https://example.com" size="40">
    <button onclick="check()">Sprawdź</button>
    
    <div id="result"></div>
    
    <script>
        async function check() {
            const url = document.getElementById('url').value;
            const resultDiv = document.getElementById('result');
            
            const response = await fetch('/check', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({url})
            });
            
            const result = await response.json();
            const isSafe = result.score > 70;
            
            resultDiv.innerHTML = `
                <div class="result ${isSafe ? 'safe' : 'unsafe'}">
                    <h3>${isSafe ? '✅ Strona jest bezpieczna' : '⚠️ UWAGA! Strona może być niebezpieczna'}</h3>
                    <p>Score: ${result.score}/100</p>
                    <p>SSL: ${result.ssl ? 'Tak' : 'Nie'}</p>
                    <p>Suspicious: ${result.suspicious ? 'Tak' : 'Nie'}</p>
                </div>
            `;
        }
    </script>
</body>
</html>
```

---

## KROK 3: Testowanie

### Test 1: Legalne testy
```bash
# Uruchom serwer
node app.js

# Testuj na znanych stronach
# https://google.com
# https://facebook.com
# https://example.com
```

### Test 2: Symulacja ataku
Użyj lokalnych plików HTML do testowania:
- Stwórz fałszywą stronę logowania
- Przetestuj detekcję
- Zweryfikuj, że system działa

---

## KROK 4: Bezpieczeństwo

### Jak zapobiec nadużyciom?
1. **Rate limiting** - ogranicz liczbę zapytań
2. **Logowanie** - rejestruj wszystkie zapytania
3. **API Key** - wymagaj klucza dostępu
4. **Warunki użycia** - jasno określ ograniczenia

### Przykład zabezpieczeń:
```javascript
const rateLimit = new Map();

app.use('/check', (req, res, next) => {
    const ip = req.ip;
    const now = Date.now();
    
    if (!rateLimit.has(ip)) {
        rateLimit.set(ip, []);
    }
    
    const times = rateLimit.get(ip);
    const recent = times.filter(t => now - t < 60000); // 1 minuta
    
    if (recent.length > 10) {
        return res.status(429).json({error: 'Za dużo zapytań'});
    }
    
    recent.push(now);
    rateLimit.set(ip, recent);
    next();
});
```

---

## KROK 5: Rozwój projektu

### Co dodać:
1. **Machine Learning** - ucz model na danych phishingu
2. **API integracji** - połącz z VirusTotal, Google Safe Browsing
3. **Dashboard admina** - monitoruj użycie
4. **Mobile app** - aplikacja na telefon

---

## Przykładowe polecenia AI

> "Stwórz detektor phishingu w Node.js z Expressem. Powinien sprawdzać URL pod kątem podejrzanych wzorców i dawać ocenę bezpieczeństwa."

> "Dodaj do detektora phishingu analizę treści strony - czy zawiera podobne treści do znanych phishingów."

> "Stwórz prosty interfejs webowy dla detektora z przyjaznym UI."