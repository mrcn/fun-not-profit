#!/usr/bin/env python3
"""Download Seneca's works from Project Gutenberg."""

import os
import time
import urllib.request
import urllib.error
from pathlib import Path

LIBRARY_ROOT = "epub_library"

# Seneca's works on Project Gutenberg
SENECA_WORKS = [
    # Seneca has multiple works available
    (2607, "seneca_on_benefits.epub", "Seneca", "On Benefits"),
    (8178, "seneca_on_the_shortness_of_life.epub", "Seneca", "On the Shortness of Life"),
    (46965, "seneca_moral_letters_to_lucilius_vol1.epub", "Seneca", "Moral Letters to Lucilius Vol 1"),
    (59242, "seneca_moral_letters_to_lucilius_vol2.epub", "Seneca", "Moral Letters to Lucilius Vol 2"),
    (10001, "seneca_moral_epistles.epub", "Seneca", "Moral Epistles"),
]

def download_gutenberg_epub(book_id, filename, author, title):
    """Download an EPUB from Project Gutenberg."""
    urls = [
        f"https://www.gutenberg.org/ebooks/{book_id}.epub3.images",
        f"https://www.gutenberg.org/ebooks/{book_id}.epub.images",
        f"https://www.gutenberg.org/ebooks/{book_id}.epub.noimages",
        f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}-images.epub",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.epub",
    ]

    output_path = Path(LIBRARY_ROOT) / "ancient_philosophy" / filename

    if output_path.exists():
        print(f"  ✓ Already exists: {filename}")
        return True

    for url in urls:
        try:
            print(f"  Trying: {url}")
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; EpubDownloader/1.0)'}
            req = urllib.request.Request(url, headers=headers)

            with urllib.request.urlopen(req, timeout=30) as response:
                content = response.read()

                if content[:2] == b'PK':  # ZIP magic number
                    with open(output_path, 'wb') as f:
                        f.write(content)
                    print(f"  ✓ Downloaded: {filename}")
                    return True

        except urllib.error.HTTPError as e:
            if e.code == 404:
                continue
            else:
                print(f"  ! HTTP Error {e.code}: {url}")
        except Exception as e:
            print(f"  ! Error: {e}")
            continue

    print(f"  ✗ Failed to download: {filename} (ID: {book_id})")
    return False

if __name__ == '__main__':
    print("Downloading Seneca's works (crucial for Taleb)...")
    print("=" * 70)

    success = 0
    for i, (book_id, filename, author, title) in enumerate(SENECA_WORKS, 1):
        print(f"[{i}/{len(SENECA_WORKS)}] {author} - {title}")
        if download_gutenberg_epub(book_id, filename, author, title):
            success += 1
        if i < len(SENECA_WORKS):
            time.sleep(2)
        print()

    print("=" * 70)
    print(f"Downloaded {success}/{len(SENECA_WORKS)} Seneca works")
