#!/usr/bin/env python3
"""Create an EPUB from markdown content."""

import zipfile
import os
from datetime import datetime

def create_epub(md_file, epub_file):
    """Create EPUB from markdown file."""

    # Read the markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML (simple conversion)
    html_content = markdown_to_html(md_content)

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
    <item id="content" href="content.html" media-type="application/xhtml+xml"/>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
  </manifest>
  <spine toc="ncx">
    <itemref idref="content"/>
  </spine>
</package>'''

    with open('epub_temp/OEBPS/content.opf', 'w') as f:
        f.write(content_opf)

    # Create toc.ncx
    toc_ncx = '''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:covert-dismantling-reason-2025"/>
    <meta name="dtb:depth" content="1"/>
  </head>
  <docTitle>
    <text>The Covert Dismantling of Reason</text>
  </docTitle>
  <navMap>
    <navPoint id="content">
      <navLabel><text>Main Content</text></navLabel>
      <content src="content.html"/>
    </navPoint>
  </navMap>
</ncx>'''

    with open('epub_temp/OEBPS/toc.ncx', 'w') as f:
        f.write(toc_ncx)

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

    # Create EPUB (zip file)
    with zipfile.ZipFile(epub_file, 'w', zipfile.ZIP_DEFLATED) as epub:
        # mimetype must be first and uncompressed
        epub.write('epub_temp/mimetype', 'mimetype', compress_type=zipfile.ZIP_STORED)
        # Add other files
        epub.write('epub_temp/META-INF/container.xml', 'META-INF/container.xml')
        epub.write('epub_temp/OEBPS/content.opf', 'OEBPS/content.opf')
        epub.write('epub_temp/OEBPS/toc.ncx', 'OEBPS/toc.ncx')
        epub.write('epub_temp/OEBPS/content.html', 'OEBPS/content.html')

    # Cleanup
    import shutil
    shutil.rmtree('epub_temp')

    print(f"EPUB created successfully: {epub_file}")


def markdown_to_html(md_text):
    """Simple markdown to HTML conversion."""
    import re

    html = md_text

    # Escape HTML entities
    html = html.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

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
