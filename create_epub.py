#!/usr/bin/env python3
"""Create an EPUB from markdown content."""

import zipfile
import os
import re
from datetime import datetime

def create_epub(md_file, epub_file):
    """Create EPUB from markdown file."""

    # Read the markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Extract headers for TOC
    toc_entries = extract_toc(md_content)

    # Convert markdown to HTML (simple conversion)
    html_content = markdown_to_html(md_content, toc_entries)

    # Create temporary directory structure
    os.makedirs('epub_temp/META-INF', exist_ok=True)
    os.makedirs('epub_temp/OEBPS', exist_ok=True)

    # Create mimetype file
    with open('epub_temp/mimetype', 'w') as f:
        f.write('application/epub+zip')

    # Create container.xml
    container_xml = '''<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>'''

    with open('epub_temp/META-INF/container.xml', 'w') as f:
        f.write(container_xml)

    # Create content.opf
    content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="BookID">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:title>The Covert Dismantling of Reason</dc:title>
    <dc:creator>Conversation Analysis</dc:creator>
    <dc:language>en</dc:language>
    <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
    <dc:identifier id="BookID">urn:uuid:covert-dismantling-reason-2025</dc:identifier>
  </metadata>
  <manifest>
    <item id="toc" href="toc.html" media-type="application/xhtml+xml"/>
    <item id="content" href="content.html" media-type="application/xhtml+xml"/>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
  </manifest>
  <spine toc="ncx">
    <itemref idref="toc"/>
    <itemref idref="content"/>
  </spine>
  <guide>
    <reference type="toc" title="Table of Contents" href="toc.html"/>
  </guide>
</package>'''

    with open('epub_temp/OEBPS/content.opf', 'w') as f:
        f.write(content_opf)

    # Create toc.ncx with all sections
    max_depth = max([entry['level'] for entry in toc_entries], default=1)

    navpoints = []
    for i, entry in enumerate(toc_entries):
        navpoints.append(f'''    <navPoint id="navPoint-{i+1}" playOrder="{i+1}">
      <navLabel><text>{escape_xml(entry['text'])}</text></navLabel>
      <content src="content.html#{entry['id']}"/>
    </navPoint>''')

    toc_ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:covert-dismantling-reason-2025"/>
    <meta name="dtb:depth" content="{max_depth}"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>The Covert Dismantling of Reason</text>
  </docTitle>
  <navMap>
{chr(10).join(navpoints)}
  </navMap>
</ncx>'''

    with open('epub_temp/OEBPS/toc.ncx', 'w', encoding='utf-8') as f:
        f.write(toc_ncx)

    # Create visible HTML table of contents page
    toc_html_entries = []
    for entry in toc_entries:
        indent = '  ' * (entry['level'] - 1)
        toc_html_entries.append(f'{indent}<li><a href="content.html#{entry["id"]}">{entry["text"]}</a></li>')

    toc_html = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Table of Contents</title>
  <style type="text/css">
    body {{
      font-family: Georgia, serif;
      line-height: 1.8;
      margin: 2em;
      max-width: 800px;
    }}
    h1 {{
      color: #2c3e50;
      border-bottom: 3px solid #3498db;
      padding-bottom: 0.5em;
      margin-bottom: 1em;
    }}
    ul {{
      list-style-type: none;
      padding-left: 0;
    }}
    li {{
      margin: 0.5em 0;
      padding-left: 0;
    }}
    li li {{
      padding-left: 2em;
      margin: 0.3em 0;
    }}
    li li li {{
      padding-left: 4em;
      font-size: 0.95em;
    }}
    a {{
      color: #2980b9;
      text-decoration: none;
      display: block;
      padding: 0.3em 0;
    }}
    a:hover {{
      color: #3498db;
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <h1>Table of Contents</h1>
  <ul>
{chr(10).join(toc_html_entries)}
  </ul>
</body>
</html>'''

    with open('epub_temp/OEBPS/toc.html', 'w', encoding='utf-8') as f:
        f.write(toc_html)

    # Create content.html
    html_doc = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>The Covert Dismantling of Reason</title>
  <style type="text/css">
    body {{ font-family: Georgia, serif; line-height: 1.6; margin: 2em; }}
    h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; }}
    h2 {{ color: #34495e; margin-top: 1.5em; }}
    h3 {{ color: #7f8c8d; }}
    blockquote {{
      border-left: 4px solid #3498db;
      padding-left: 1em;
      margin: 1em 0;
      font-style: italic;
      color: #555;
    }}
    code {{
      background-color: #f4f4f4;
      padding: 2px 6px;
      border-radius: 3px;
      font-family: monospace;
    }}
    strong {{ color: #2c3e50; }}
  </style>
</head>
<body>
{html_content}
</body>
</html>'''

    with open('epub_temp/OEBPS/content.html', 'w', encoding='utf-8') as f:
        f.write(html_doc)

    # Create EPUB (zip file) with maximum compression
    with zipfile.ZipFile(epub_file, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as epub:
        # mimetype must be first and uncompressed per EPUB spec
        epub.write('epub_temp/mimetype', 'mimetype', compress_type=zipfile.ZIP_STORED)
        # Add other files with maximum compression
        epub.write('epub_temp/META-INF/container.xml', 'META-INF/container.xml')
        epub.write('epub_temp/OEBPS/content.opf', 'OEBPS/content.opf')
        epub.write('epub_temp/OEBPS/toc.ncx', 'OEBPS/toc.ncx')
        epub.write('epub_temp/OEBPS/toc.html', 'OEBPS/toc.html')
        epub.write('epub_temp/OEBPS/content.html', 'OEBPS/content.html')

    # Cleanup
    import shutil
    shutil.rmtree('epub_temp')

    print(f"EPUB created successfully: {epub_file}")


def extract_toc(md_text):
    """Extract table of contents from markdown headers."""
    toc_entries = []
    header_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)

    for match in header_pattern.finditer(md_text):
        level = len(match.group(1))
        text = match.group(2).strip()
        # Create ID from text
        header_id = re.sub(r'[^\w\s-]', '', text.lower())
        header_id = re.sub(r'[-\s]+', '-', header_id)

        toc_entries.append({
            'level': level,
            'text': text,
            'id': header_id
        })

    return toc_entries


def escape_xml(text):
    """Escape XML special characters."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')


def markdown_to_html(md_text, toc_entries):
    """Simple markdown to HTML conversion with anchored headers."""
    html = md_text

    # Escape HTML entities
    html = html.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # Headers with IDs for navigation
    header_index = 0
    def replace_header(match):
        nonlocal header_index
        level = len(match.group(1))
        text = match.group(2)
        if header_index < len(toc_entries):
            header_id = toc_entries[header_index]['id']
            header_index += 1
            return f'<h{level} id="{header_id}">{text}</h{level}>'
        return f'<h{level}>{text}</h{level}>'

    html = re.sub(r'^(#{1,6})\s+(.+)$', replace_header, html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # Code blocks
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)

    # Blockquotes
    html = re.sub(r'^&gt; (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

    # Horizontal rules
    html = re.sub(r'^---$', r'<hr/>', html, flags=re.MULTILINE)

    # Paragraphs (simple approach)
    lines = html.split('\n')
    processed_lines = []
    in_paragraph = False

    for line in lines:
        stripped = line.strip()

        # Check if line is a tag
        if stripped.startswith('<'):
            if in_paragraph:
                processed_lines.append('</p>')
                in_paragraph = False
            processed_lines.append(line)
        elif stripped == '':
            if in_paragraph:
                processed_lines.append('</p>')
                in_paragraph = False
            processed_lines.append(line)
        else:
            if not in_paragraph:
                processed_lines.append('<p>')
                in_paragraph = True
            processed_lines.append(line)

    if in_paragraph:
        processed_lines.append('</p>')

    return '\n'.join(processed_lines)


if __name__ == '__main__':
    create_epub(
        'the-covert-dismantling-of-reason.md',
        'the-covert-dismantling-of-reason.epub'
    )
