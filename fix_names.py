#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path("webcomics")
DIGITS = 3

def extract_season_episode(name):
    """Extract season and episode numbers from folder name."""
    season_match = re.search(r'\(S(\d+)\)', name)
    season = int(season_match.group(1)) if season_match else 1

    ep_match = re.search(r'Episode\s*(\d+)', name, re.IGNORECASE)
    episode = int(ep_match.group(1)) if ep_match else 0

    return season, episode

def rename_images(chapter_dir):
    images = sorted(
        [f for f in chapter_dir.iterdir() if f.is_file() and f.suffix.lower() == ".png"],
        key=lambda f: f.name
    )
    for i, img in enumerate(images, start=1):
        new_name = f"{i:03d}.png"
        new_path = chapter_dir / new_name
        if new_path != img:
           # print(f"  Renaming image: {img.name} -> {new_name}")
            img.rename(new_path)

def rename_chapters(series_path):
    chapters = [d for d in series_path.iterdir() if d.is_dir()]
    
    # Sort by season then episode
    chapters.sort(key=lambda d: extract_season_episode(d.name))

    for i, chapter_dir in enumerate(chapters, start=1):
        new_name = f"Episode_{i:03d}"
        new_path = series_path / new_name
        if new_path != chapter_dir:
            print(f"Renaming chapter: {chapter_dir.name} -> {new_name}")
            chapter_dir.rename(new_path)
        rename_images(new_path)

def main():
    if not ROOT.exists():
        print(f"Error: {ROOT} folder not found.")
        return

    for series in ROOT.iterdir():
        if not series.is_dir():
            continue
        print(f"Processing series: {series.name}")
        rename_chapters(series)

if __name__ == "__main__":
    main()
