#!/usr/bin/env python3
"""Download EPUBs from Project Gutenberg and other sources."""

import os
import time
import urllib.request
import urllib.error
from pathlib import Path

# Create library structure
LIBRARY_ROOT = "epub_library"
CATEGORIES = {
    "ancient_philosophy": "Ancient Philosophy & Stoicism",
    "enlightenment": "Enlightenment Philosophy & Epistemology",
    "modern_philosophy": "Modern Philosophy",
    "political_economy": "Political Philosophy & Economics",
    "mathematics_logic": "Mathematics & Logic",
    "science_evolution": "Science & Evolution",
    "cybernetics_systems": "Cybernetics & Systems Thinking",
    "rationality_ai": "Rationality & AI Safety",
    "probability_risk": "Probability, Risk & Complexity",
    "appropriate_tech": "Appropriate Technology & Resilience"
}

# Project Gutenberg EPUB downloads
# Format: (gutenberg_id, filename, category, author, title, related_to)
GUTENBERG_BOOKS = [
    # Ancient Philosophy & Stoicism
    (2680, "marcus_aurelius_meditations.epub", "ancient_philosophy", "Marcus Aurelius", "Meditations", "Taleb, Vassar"),
    (45109, "epictetus_enchiridion.epub", "ancient_philosophy", "Epictetus", "The Enchiridion", "Taleb"),
    (10661, "epictetus_discourses.epub", "ancient_philosophy", "Epictetus", "Discourses", "Taleb"),
    (1497, "plato_republic.epub", "ancient_philosophy", "Plato", "The Republic", "All"),
    (8438, "aristotle_nicomachean_ethics.epub", "ancient_philosophy", "Aristotle", "Nicomachean Ethics", "All"),

    # Enlightenment Philosophy & Epistemology
    (9662, "hume_enquiry_concerning_human_understanding.epub", "enlightenment", "David Hume", "An Enquiry Concerning Human Understanding", "Taleb, Vassar"),
    (4705, "hume_treatise_human_nature.epub", "enlightenment", "David Hume", "A Treatise of Human Nature", "Taleb, Vassar"),
    (59, "descartes_discourse_on_method.epub", "enlightenment", "René Descartes", "Discourse on Method", "Vassar"),
    (23306, "descartes_meditations.epub", "enlightenment", "René Descartes", "Meditations on First Philosophy", "Vassar"),
    (3800, "spinoza_ethics.epub", "enlightenment", "Baruch Spinoza", "Ethics", "Taleb, Vassar"),
    (4280, "kant_critique_pure_reason.epub", "enlightenment", "Immanuel Kant", "Critique of Pure Reason", "Vassar"),
    (5683, "kant_critique_practical_reason.epub", "enlightenment", "Immanuel Kant", "Critique of Practical Reason", "Vassar"),
    (3600, "montaigne_essays.epub", "enlightenment", "Michel de Montaigne", "Essays", "Taleb"),
    (45988, "bacon_novum_organum.epub", "enlightenment", "Francis Bacon", "Novum Organum", "Vassar, Taleb"),
    (56463, "bacon_essays.epub", "enlightenment", "Francis Bacon", "Essays", "Taleb"),

    # Modern Philosophy
    (4363, "nietzsche_beyond_good_evil.epub", "modern_philosophy", "Friedrich Nietzsche", "Beyond Good and Evil", "Taleb"),
    (1998, "nietzsche_zarathustra.epub", "modern_philosophy", "Friedrich Nietzsche", "Thus Spoke Zarathustra", "Taleb"),
    (52319, "nietzsche_genealogy_morals.epub", "modern_philosophy", "Friedrich Nietzsche", "On the Genealogy of Morals", "Taleb"),
    (41654, "russell_mathematical_philosophy.epub", "modern_philosophy", "Bertrand Russell", "Introduction to Mathematical Philosophy", "Vassar"),
    (5827, "russell_problems_philosophy.epub", "modern_philosophy", "Bertrand Russell", "The Problems of Philosophy", "Vassar"),
    (25447, "russell_mysticism_logic.epub", "modern_philosophy", "Bertrand Russell", "Mysticism and Logic", "Vassar"),
    (57628, "james_principles_psychology_vol1.epub", "modern_philosophy", "William James", "The Principles of Psychology Vol 1", "Vassar"),
    (57634, "james_principles_psychology_vol2.epub", "modern_philosophy", "William James", "The Principles of Psychology Vol 2", "Vassar"),
    (5116, "james_pragmatism.epub", "modern_philosophy", "William James", "Pragmatism", "Vassar, Taleb"),

    # Political Philosophy & Economics
    (3207, "hobbes_leviathan.epub", "political_economy", "Thomas Hobbes", "Leviathan", "All"),
    (7370, "locke_second_treatise.epub", "political_economy", "John Locke", "Second Treatise of Government", "Taleb, Gupta"),
    (3300, "smith_wealth_nations.epub", "political_economy", "Adam Smith", "The Wealth of Nations", "Taleb"),
    (30107, "mill_political_economy.epub", "political_economy", "John Stuart Mill", "Principles of Political Economy", "Taleb"),
    (147, "paine_common_sense.epub", "political_economy", "Thomas Paine", "Common Sense", "Gupta, Taleb"),
    (3742, "paine_rights_of_man.epub", "political_economy", "Thomas Paine", "The Rights of Man", "Gupta, Taleb"),
    (57037, "machiavelli_prince.epub", "political_economy", "Niccolò Machiavelli", "The Prince", "Taleb"),
    (10827, "machiavelli_discourses.epub", "political_economy", "Niccolò Machiavelli", "Discourses on Livy", "Taleb"),

    # Mathematics & Logic
    (21076, "euclid_elements.epub", "mathematics_logic", "Euclid", "Elements (First Six Books)", "Vassar"),
    (76404, "newton_principia.epub", "mathematics_logic", "Isaac Newton", "Principia Mathematica", "Vassar, Gupta"),

    # Science & Evolution
    (2009, "darwin_origin_species.epub", "science_evolution", "Charles Darwin", "On the Origin of Species", "All"),
    (2300, "darwin_descent_man.epub", "science_evolution", "Charles Darwin", "The Descent of Man", "All"),
]

def create_library_structure():
    """Create the directory structure for the EPUB library."""
    print(f"Creating library structure in {LIBRARY_ROOT}/")
    Path(LIBRARY_ROOT).mkdir(exist_ok=True)

    for category_key, category_name in CATEGORIES.items():
        category_path = Path(LIBRARY_ROOT) / category_key
        category_path.mkdir(exist_ok=True)
        print(f"  Created: {category_key}/")

    print()

def download_gutenberg_epub(book_id, filename, category):
    """Download an EPUB from Project Gutenberg."""
    # Try multiple URL formats
    urls = [
        f"https://www.gutenberg.org/ebooks/{book_id}.epub3.images",
        f"https://www.gutenberg.org/ebooks/{book_id}.epub.images",
        f"https://www.gutenberg.org/ebooks/{book_id}.epub.noimages",
        f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}-images.epub",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.epub",
    ]

    output_path = Path(LIBRARY_ROOT) / category / filename

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

                # Verify it's actually an EPUB (should be a zip file)
                if content[:2] == b'PK':  # ZIP magic number
                    with open(output_path, 'wb') as f:
                        f.write(content)
                    print(f"  ✓ Downloaded: {filename}")
                    return True

        except urllib.error.HTTPError as e:
            if e.code == 404:
                continue  # Try next URL
            else:
                print(f"  ! HTTP Error {e.code}: {url}")
        except Exception as e:
            print(f"  ! Error: {e}")
            continue

    print(f"  ✗ Failed to download: {filename} (ID: {book_id})")
    return False

def download_all_books():
    """Download all books from the list."""
    print(f"Downloading {len(GUTENBERG_BOOKS)} books from Project Gutenberg...")
    print("This may take a while. Be patient and respectful of Project Gutenberg's servers.\n")

    success_count = 0
    fail_count = 0

    for i, (book_id, filename, category, author, title, related) in enumerate(GUTENBERG_BOOKS, 1):
        print(f"[{i}/{len(GUTENBERG_BOOKS)}] {author} - {title}")
        print(f"  Related to: {related}")

        if download_gutenberg_epub(book_id, filename, category):
            success_count += 1
        else:
            fail_count += 1

        # Be polite to Project Gutenberg servers
        if i < len(GUTENBERG_BOOKS):
            time.sleep(2)  # 2 second delay between downloads

        print()

    print("=" * 70)
    print(f"Download complete!")
    print(f"  ✓ Success: {success_count}")
    print(f"  ✗ Failed: {fail_count}")
    print(f"  Total: {len(GUTENBERG_BOOKS)}")
    print("=" * 70)

def create_catalog():
    """Create a catalog of downloaded books."""
    catalog_path = Path(LIBRARY_ROOT) / "CATALOG.md"

    with open(catalog_path, 'w', encoding='utf-8') as f:
        f.write("# EPUB Library Catalog\n\n")
        f.write("**Collection Focus:** Books referenced by or influential to:\n")
        f.write("- **Michael Vassar** (Transhumanist, Rationalist, Former Singularity Institute President)\n")
        f.write("- **Nassim Taleb** (Author of The Black Swan, Antifragile, expert on probability and risk)\n")
        f.write("- **Vinay Gupta** (Ethereum Project Manager, Resilience Expert, Hexayurt Inventor)\n\n")
        f.write(f"**Total Books:** {len(GUTENBERG_BOOKS)}\n\n")
        f.write("---\n\n")

        for category_key, category_name in CATEGORIES.items():
            # Get books in this category
            books_in_category = [b for b in GUTENBERG_BOOKS if b[2] == category_key]

            if not books_in_category:
                continue

            f.write(f"## {category_name}\n\n")

            for book_id, filename, _, author, title, related in books_in_category:
                f.write(f"### {author} - {title}\n")
                f.write(f"- **File:** `{category_key}/{filename}`\n")
                f.write(f"- **Related to:** {related}\n")
                f.write(f"- **Project Gutenberg ID:** {book_id}\n")
                f.write(f"- **URL:** https://www.gutenberg.org/ebooks/{book_id}\n\n")

        f.write("---\n\n")
        f.write("## Notes\n\n")
        f.write("All books in this collection are from Project Gutenberg and are in the public domain.\n\n")
        f.write("### Additional Resources (Not Yet Downloaded)\n\n")
        f.write("These works are also highly relevant but may require manual download:\n\n")
        f.write("- **Eliezer Yudkowsky** - Rationality: From AI to Zombies (Free from MIRI: https://intelligence.org/rationality-ai-zombies/)\n")
        f.write("- **Buckminster Fuller** - Operating Manual for Spaceship Earth (Internet Archive)\n")
        f.write("- **Seneca** - Letters from a Stoic (Free PDF from Tim Ferriss: https://tim.blog/2017/07/06/tao-of-seneca/)\n")
        f.write("- Works from Internet Archive on cybernetics, systems thinking, and complexity theory\n")

    print(f"Created catalog: {catalog_path}")

if __name__ == '__main__':
    print("EPUB Library Downloader")
    print("=" * 70)
    print("Downloading books related to:")
    print("  - Michael Vassar (Rationalist, Transhumanist)")
    print("  - Nassim Taleb (Risk, Probability, Antifragility)")
    print("  - Vinay Gupta (Resilience, Systems Thinking)")
    print("=" * 70)
    print()

    create_library_structure()
    download_all_books()
    create_catalog()

    print("\nLibrary created successfully!")
    print(f"Browse the collection in: {LIBRARY_ROOT}/")
    print(f"See full catalog: {LIBRARY_ROOT}/CATALOG.md")
