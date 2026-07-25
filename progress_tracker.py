#!/usr/bin/env python3
"""
Automatyczny system śledzenia postępu dla tutoriali
Dla playlisty "Do wykonania" (9 filmów)
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Konfiguracja
PLAYLIST_ID = "PLfs618e2-dmkp55zZtbC11Ny473UGPXgD"  # "Do wykonania"
PLAYLISTS_DATA_PATH = Path("/opt/data/profiles/websytes/playlists_data.json")
TUTORIALS_DIR = Path("/opt/data/profiles/websytes")
PROGRESS_DB_PATH = TUTORIALS_DIR / "progress_db.json"


def load_playlist_data() -> dict:
    """Załaduj dane z playlists_data.json"""
    with open(PLAYLISTS_DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Znajdź playlistę "Do wykonania"
    for playlist in data.get('playlists', []):
        if playlist.get('title') == 'Do wykonania':
            return playlist
    
    raise ValueError(f"Playlist '{PLAYLIST_ID}' not found in {PLAYLISTS_DATA_PATH}")


def get_tutorial_files() -> Dict[str, Path]:
    """Znajdź wszystkie pliki tutoriali w katalogu"""
    tutorials = {}
    for f in TUTORIALS_DIR.glob("tutorial_*.md"):
        # Wyodrębnij numer i ID z nazwy pliku
        match = re.match(r'tutorial_(\d+)_(.+)\.md', f.name)
        if match:
            num, rest = match.groups()
            tutorials[f"tutorial_{num}"] = f
    return tutorials


def load_progress_db() -> dict:
    """Załaduj bazę postępu lub utwórz nową"""
    if PROGRESS_DB_PATH.exists():
        with open(PROGRESS_DB_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_progress_db(progress: dict) -> None:
    """Zapisz bazę postępu"""
    with open(PROGRESS_DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)


def check_video_status(video_id: str, progress_db: dict, tutorial_files: Dict[str, Path]) -> dict:
    """Sprawdź status jednego filmu"""
    
    if video_id in progress_db:
        return progress_db[video_id]
    
    # Automatyczne wykrywanie statusu
    status = {
        "watched": False,
        "notes_made": False,
        "tasks_done": False,
        "watched_date": None,
        "notes_file": None,
        "progress_percent": 0
    }
    
    # Sprawdź, czy istnieje plik notatek dla tego filmu
    for tutorial_key, file_path in tutorial_files.items():
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if video_id in content:
                    status["watched"] = True
                    status["notes_made"] = True
                    status["notes_file"] = file_path.name
                    status["watched_date"] = datetime.now().strftime("%Y-%m-%d")
                    break
        except Exception:
            continue
    
    # Oblicz procent postępu
    status["progress_percent"] = calculate_progress(status)
    
    return status


def calculate_progress(status: dict) -> int:
    """Oblicz procent postępu"""
    total = 0
    if status.get("watched"):
        total += 33
    if status.get("notes_made"):
        total += 33
    if status.get("tasks_done"):
        total += 34  # 33+33+34 = 100
    return total


def update_video_status(video_id: str, watched: bool = None, notes_made: bool = None, 
                        tasks_done: bool = None, notes_file: str = None) -> None:
    """Zaktualizuj status filmu w bazie"""
    progress_db = load_progress_db()
    
    if video_id not in progress_db:
        progress_db[video_id] = {
            "watched": False,
            "notes_made": False,
            "tasks_done": False,
            "watched_date": None,
            "notes_file": None,
            "progress_percent": 0
        }
    
    if watched is not None:
        progress_db[video_id]["watched"] = watched
        if watched and not progress_db[video_id]["watched_date"]:
            progress_db[video_id]["watched_date"] = datetime.now().strftime("%Y-%m-%d")
    
    if notes_made is not None:
        progress_db[video_id]["notes_made"] = notes_made
        if notes_made and notes_file:
            progress_db[video_id]["notes_file"] = notes_file
    
    if tasks_done is not None:
        progress_db[video_id]["tasks_done"] = tasks_done
    
    progress_db[video_id]["progress_percent"] = calculate_progress(progress_db[video_id])
    
    save_progress_db(progress_db)
    print(f"✓ Zaktualizowano status dla filmu {video_id}")


def generate_report() -> str:
    """Wygeneruj raport postępu w formie tabeli"""
    playlist = load_playlist_data()
    videos = playlist.get('videos', [])
    tutorial_files = get_tutorial_files()
    progress_db = load_progress_db()
    
    # Usuń duplikaty (film o tym samym ID)
    seen_ids = set()
    unique_videos = []
    for v in videos:
        if v['id'] not in seen_ids:
            seen_ids.add(v['id'])
            unique_videos.append(v)
    
    # Automatycznie wykryj status dla wszystkich filmów
    for video in unique_videos:
        video_id = video['id']
        if video_id not in progress_db:
            progress_db[video_id] = check_video_status(video_id, progress_db, tutorial_files)
    
    # Zapisz zaktualizowaną bazę danych
    save_progress_db(progress_db)
    
    report = []
    report.append("# Status Postępu — Playlista \"Do wykonania\"\n")
    report.append(f"**Data generacji:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    report.append(f"**Łączna liczba filmów:** {len(unique_videos)}\n")
    report.append(f"**Playlista:** {playlist.get('title', 'N/A')}\n")
    report.append("")
    
    # Tabela postępu
    report.append("## Podsumowanie postępu\n")
    report.append("| # | Film | Obejrzany | Notatki | Zadania | % | Status |\n")
    report.append("|---|------|-----------|---------|---------|---|--------|\n")
    
    overall_progress = 0
    for i, video in enumerate(unique_videos, 1):
        video_id = video['id']
        title = video['title'][:50] + "..." if len(video['title']) > 50 else video['title']
        
        status = check_video_status(video_id, progress_db, tutorial_files)
        
        watched_icon = "✓" if status.get("watched") else "○"
        notes_icon = "✓" if status.get("notes_made") else "○"
        tasks_icon = "✓" if status.get("tasks_done") else "○"
        percent = status.get("progress_percent", 0)
        overall_progress += percent
        
        # Określ status ogólny
        if percent == 100:
            status_text = "✓ Gotowe"
        elif percent >= 66:
            status_text = "🟡 W trakcie"
        elif percent > 0:
            status_text = "🔵 Rozpoczęte"
        else:
            status_text = "⏳ Do zrobienia"
        
        report.append(f"| {i} | {title} | {watched_icon} | {notes_icon} | {tasks_icon} | {percent}% | {status_text} |\n")
    
    # Średni postęp
    avg_progress = overall_progress / len(unique_videos) if unique_videos else 0
    report.append(f"\n**Średni postęp całkowity:** {avg_progress:.1f}%\n")
    
    # Szczegółowe informacje
    report.append("\n## Szczegóły filmów\n")
    for i, video in enumerate(unique_videos, 1):
        video_id = video['id']
        status = check_video_status(video_id, progress_db, tutorial_files)
        
        report.append(f"### {i}. {video['title']}\n")
        report.append(f"- **ID:** {video_id}\n")
        report.append(f"- **Data publikacji:** {video.get('published_at', 'N/A')[:10]}\n")
        report.append(f"- **Status:** Obejrzany: {'✓' if status.get('watched') else '○'}, Notatki: {'✓' if status.get('notes_made') else '○'}, Zadania: {'✓' if status.get('tasks_done') else '○'}\n")
        if status.get('notes_file'):
            report.append(f"- **Plik notatek:** {status['notes_file']}\n")
        report.append("\n")
    
    return "".join(report)


def print_status() -> None:
    """Wydrukuj skrócony status"""
    playlist = load_playlist_data()
    videos = playlist.get('videos', [])
    tutorial_files = get_tutorial_files()
    progress_db = load_progress_db()
    
    # Usuń duplikaty
    seen_ids = set()
    unique_videos = []
    for v in videos:
        if v['id'] not in seen_ids:
            seen_ids.add(v['id'])
            unique_videos.append(v)
    
    print(f"\nStatus postępu dla playlisty \"{playlist.get('title', 'N/A')}\":\n")
    
    for i, video in enumerate(unique_videos, 1):
        status = check_video_status(video['id'], progress_db, tutorial_files)
        
        watched = "✓" if status.get("watched") else "○"
        notes = "✓" if status.get("notes_made") else "○"
        tasks = "✓" if status.get("tasks_done") else "○"
        
        print(f"  {i}. {video['title'][:60]:<60} [{watched}] [{notes}] [{tasks}] {status.get('progress_percent')}%")
    
    # Podsumowanie
    total = len(unique_videos)
    completed = sum(1 for v in unique_videos 
                    if check_video_status(v['id'], progress_db, tutorial_files).get('progress_percent') == 100)
    print(f"\n  📊 {completed}/{total} filmów ukończonych ({completed*100//total if total else 0}%)\n")


def main():
    """Główna funkcja"""
    import sys
    
    args = sys.argv[1:]
    
    if '--status' in args:
        print_status()
    elif '--report' in args:
        report = generate_report()
        output_path = TUTORIALS_DIR / "tutorial_progress_report.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✓ Raport zapisano do: {output_path}")
    elif '--update' in args:
        # Przykład: python tutorial_progress_tracker.py --update CtNY3C-tuTM --watched --notes --tasks
        video_id = None
        watched = False
        notes = False
        tasks = False
        
        i = 0
        while i < len(args):
            if args[i] == '--update' and i + 1 < len(args):
                video_id = args[i + 1]
                i += 2
            elif args[i] == '--watched':
                watched = True
                i += 1
            elif args[i] == '--notes':
                notes = True
                i += 1
            elif args[i] == '--tasks':
                tasks = True
                i += 1
            else:
                i += 1
        
        if video_id:
            update_video_status(video_id, watched, notes, tasks)
        else:
            print("Użycie: python tutorial_progress_tracker.py --update <video_id> [--watched] [--notes] [--tasks]")
    else:
        # Domyślnie pokaż status
        print_status()


if __name__ == "__main__":
    main()