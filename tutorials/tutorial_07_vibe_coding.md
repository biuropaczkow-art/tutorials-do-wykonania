# Tutorial #7: Kompletny Przewodnik dla Początkujących po Vibe Coding

## Film: Kompletny Przewodnik dla Początkujących po Vibe Coding
**ID filmu:** DGZFr6dInnc  
**Data:** 2026-06-17

---

## TL;DR - Szybka instrukcja:
1. Zrozum koncepcję Vibe Coding
2. Zainstaluj narzędzia
3. Zacznij od prostych projektów
4. Rozwijaj umiejętności

---

## Co to jest Vibe Coding?

**Vibe Coding** to nowatorskie podejście do programowania, które:
- Skupia się na "czuciu" kodu
- Używa AI jako partnera
- Redukuje potrzebę pisania wszystkiego ręcznie
- Skraca ścieżkę od pomysłu do działającej aplikacji

---

## KROK 1: Zrozumienie koncepcji

### Filozofia Vibe Coding:
1. **Opisz** co chcesz zrobić
2. **AI generuje** prototyp
3. **Ty poprawiasz** i rozwijasz
4. **Iterujesz** z AI

### Narzędzia Vibe Coding:
- **Hermes Agent** - główny asystent
- **Claude Code** - do refaktora
- **OpenCode** - interaktywny coding
- **Cursor** - IDE z AI

---

## KROK 2: Instalacja narzędzi

### Metoda 1: Hermes Agent (rekomendowane)
```bash
# Na Linuxie/VPS
curl -fsSL https://hermes-agent.com/install.sh | sh

# Uruchom
hermes --profile websytes
```

### Metoda 2: Claude Code
```bash
# Instalacja
curl -fsSL https://claude.ai/code/install.sh | sh

# Logowanie
claude auth login
```

### Metoda 3: Cursor IDE
```bash
# Pobierz ze strony: cursor.sh
# Zainstaluj jak zwykłe IDE
```

---

## KROK 3: Pierwszy projekt - "Todo App"

### KROK 3a: Opisz wymagania
> "Chcę prostą aplikację todo z możliwością dodawania, usuwania i oznaczania zadań jako zrobione. Musi działać w przeglądarce."

### KROK 3b: AI generuje kod
```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 500px; margin: 50px auto; }
        .todo { padding: 10px; border: 1px solid #ddd; margin: 5px 0; border-radius: 5px; }
        .completed { text-decoration: line-through; color: #888; }
        button { margin-left: 10px; }
    </style>
</head>
<body>
    <h1>Moja Lista Zadań</h1>
    <input type="text" id="new-todo" placeholder="Co zrobić?">
    <ul id="todo-list"></ul>
    
    <script>
        const input = document.getElementById('new-todo');
        const list = document.getElementById('todo-list');
        
        input.addEventListener('keyup', e => {
            if (e.key === 'Enter' && input.value.trim()) {
                const li = document.createElement('li');
                li.className = 'todo';
                li.innerHTML = `
                    <span>${input.value}</span>
                    <button onclick="this.parentElement.style.textDecoration='line-through'">✓</button>
                    <button onclick="this.parentElement.remove()">✗</button>
                `;
                list.appendChild(li);
                input.value = '';
            }
        });
    </script>
</body>
</html>
```

### KROK 4: Rozwój aplikacji
1. Dodaj lokalną przechowywkę (localStorage)
2. Dodaj filtrowanie (all/active/completed)
3. Dodaj animacje CSS
4. Stwórz prosty backend z Firebase

---

## KROK 5: Praktyka - 10 wyzwań

1. **Calculator** - kalkulator prosty
2. **Weather App** - pogoda z API
3. **Quiz** - quiz z pytań
4. **Timer** - licznik odliczający
5. **Notes** - notatnik z zapisem
6. **Gallery** - galeria zdjęć
7. **Chat** - prosty czat w czasie rzeczywistym
8. **Game** - prosta gra (np. memory)
9. **Blog** - blog z CMS
10. **Portfolio** - portfolio osobiste

---

## Najlepsze praktyki Vibe Coding

✅ **Działaj tak:**
- Zaczynij od prostego MVP
- Używaj AI jako pomocnika, nie jako zastępstwa
- Zadawaj konkretne pytania
- Iteruj szybko

❌ **Nie rób tak:**
- Nie polegaj całkowicie na AI
- Nie kopiuj bez rozumienia
- Nie przeładowuj kontekstu

---

## Przydatne polecenia dla AI

**Generowanie kodu:**
> "Stwórz prostą aplikację [opis] w [język] z [funkcjonalności]"

**Poprawa kodu:**
> "Zoptymalizuj ten kod pod względem [wydajność/czytelność/bezpieczeństwa]"

**Debugowanie:**
> "Dlaczego ten kod nie działa? [kod błędu]"

**Refaktoryzacja:**
> "Przepisz to na czystszy kod w stylu [czysty kod/Funkcyjny/OOP]"