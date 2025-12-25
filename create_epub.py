#!/usr/bin/env python3
"""Create EPUB for Inadequate Equilibria by Eliezer Yudkowsky"""

import os
import zipfile
from datetime import datetime

# Book metadata
BOOK_TITLE = "Inadequate Equilibria"
BOOK_SUBTITLE = "Where and How Civilizations Get Stuck"
AUTHOR = "Eliezer Yudkowsky"
PUBLISHER = "Machine Intelligence Research Institute"
LANGUAGE = "en"
IDENTIFIER = "inadequate-equilibria-2017"
PUBLICATION_DATE = "2017"

# Chapter data
chapters = [
    {
        "number": 1,
        "title": "Inadequacy and Modesty",
        "content": """
<h1>Chapter 1: Inadequacy and Modesty</h1>

<h2>Core Thesis</h2>

<p>This chapter introduces two incompatible epistemological frameworks for evaluating whether one might perform unusually well in some domain:</p>

<ol>
<li><strong>Inadequacy Analysis</strong>: Examines whether systemic incentive structures create exploitable gaps in civilization's competence</li>
<li><strong>Modesty</strong>: Argues that disagreement with experts or institutions shouldn't generate confidence in one's own judgment</li>
</ol>

<h2>The Modesty Perspective</h2>

<p>The modest view emphasizes epistemic humility through several arguments:</p>

<ul>
<li>Base rates suggest you're likely below average at roughly half of things</li>
<li>The Dunning-Kruger effect shows systematic overconfidence in unskilled individuals</li>
<li>Disagreement alone provides no evidence about whose epistemic standards are superior</li>
<li>When experts disagree with you, you shouldn't assume your judgment beats theirs</li>
</ul>

<p>As the text notes, "You see that someone says X, which seems wrong, so you conclude their epistemic standards are bad. But they could just see that you say Y, which sounds wrong to them."</p>

<h2>The Inadequacy Analysis Framework</h2>

<p>The counterargument focuses on <strong>incentive structures</strong>. Using financial markets as the exemplar of civilizational adequacy, the author argues that:</p>

<ul>
<li>Markets efficiently aggregate information through profit motives</li>
<li>When no profit opportunity exists to correct errors, mistakes can persist indefinitely</li>
<li>The Bank of Japan case exemplifies this: no individual could profit from correcting monetary policy</li>
</ul>

<h2>Empirical Example: Bank of Japan</h2>

<p>The author originally criticized Japan's monetary policy despite lacking formal economics credentials. After the Bank of Japan later adopted similar policies under new leadership, Japan's real GDP growth improved from negative trends to 2.3% annually—apparently validating the earlier analysis.</p>

<p>This suggests expertise can be identified and exercised even outside one's formal credentials when incentive structures create systematic blind spots.</p>
"""
    },
    {
        "number": 2,
        "title": "An Equilibrium of No Free Energy",
        "content": """
<h1>Chapter 2: An Equilibrium of No Free Energy</h1>

<h2>Core Concepts</h2>

<p>The chapter introduces three distinct economic concepts:</p>

<p><strong>Efficiency</strong>: "Microsoft's stock price is neither too low nor too high, relative to anything <em>you</em> can possibly know." A market where average price movements cannot be predicted by individual actors.</p>

<p><strong>Inexploitability</strong>: Markets may be inefficient yet still resist exploitation. Housing markets can be overpriced without offering profitable shorting opportunities. The author notes that "frothy housing market[s] may see many overpriced houses, but few underpriced ones."</p>

<p><strong>Adequacy</strong>: Whether societies have harvested obvious, high-value opportunities. The author defines it as whether "low-hanging fruit that save <em>more</em> than ten thousand lives for less than a hundred thousand dollars total have, in fact, been picked up."</p>

<h2>Key Insights</h2>

<p>The author uses academia as a case study. Researchers pursue citations and prestige, grantmakers seek prestige-per-dollar, yet genuinely important work offering massive health improvements per dollar remains unfunded. This isn't because individuals are malicious—it's a Nash equilibrium where competing incentives prevent anyone from deviating.</p>

<p>A critical distinction emerges: "usually, when things suck, it's because they suck in a way that's a Nash equilibrium." Single altruists cannot overcome systemic inadequacy when multiple barriers exist simultaneously.</p>

<p>The author illustrates this through personal experience treating seasonal affective disorder with high-intensity lighting—an intervention producing real benefits despite no formal research literature supporting it, suggesting systemic inadequacy rather than ineffectiveness.</p>
"""
    },
    {
        "number": 3,
        "title": "Moloch's Toolbox",
        "content": """
<h1>Chapter 3: Moloch's Toolbox</h1>

<p>This chapter presents a dialogue examining why civilizations fail to address obvious problems, using dead babies from improper parenteral nutrition as a central case study.</p>

<h2>Core Framework</h2>

<p>Yudkowsky organizes systemic failures into three categories:</p>

<ol>
<li><strong>Misaligned incentives</strong>: Decision-makers don't personally benefit from fixing problems</li>
<li><strong>Asymmetric information</strong>: Knowledge exists but can't reliably reach those who need it</li>
<li><strong>Bad Nash equilibria</strong>: Systems trap themselves in stable but suboptimal states</li>
</ol>

<h2>Key Examples</h2>

<p><strong>The parenteral nutrition tragedy</strong>: For decades, hospitals fed premature infants soybean oil-based nutrition lacking proper omega-3 fatty acids (docosahexaenoic acid), causing preventable liver damage and death. The Boston Children's Hospital eventually developed a working alternative, but regulatory barriers prevented wider adoption for years.</p>

<h2>Mechanisms of Failure</h2>

<p><strong>Multi-factor markets and signaling equilibria</strong>: Using the metaphor of competing magical towers that drain four years of lifespan, the chapter explains how institutions become locked in place through circular incentives—employers prefer graduates from prestigious institutions because smart people attend them; smart people attend them because employers value the credential.</p>

<p><strong>Regulatory capture</strong>: Occupational licensing and similar rules entrench existing systems. Doctors must train as generalists despite specialization being superior because the profession protects its status.</p>

<p><strong>Absence of competition</strong>: No government allows experimental hospital designs, preventing innovation testing at any scale.</p>

<p><strong>Venture capital lock-in</strong>: Seed investors must anticipate what Series A investors believe about viable companies, creating self-reinforcing stereotypes about entrepreneur profiles that persist even when recognized as unfounded.</p>

<p><strong>First-past-the-post voting</strong>: This electoral system creates "wasted votes," mathematically locking voters into supporting one of two major parties even when they prefer alternatives. This generates the Red-vs.-Blue polarization where citizens vote based on hating the opposing faction rather than supporting positive vision.</p>

<h2>The Moloch Problem</h2>

<p>The chapter concludes that coordination failures trap entire civilizations in inadequate equilibria. Individual actors rationally respond to existing incentives, yet the aggregate system produces catastrophic outcomes. Unlike a tyrant imposing rules explicitly, these failures emerge from distributed decision-making with no single villain—making them nearly impossible to reform unilaterally.</p>

<p>The dead babies represent the ultimate inadequacy: a fixable problem that persists through layered systemic dysfunction rather than malice or ignorance.</p>
"""
    },
    {
        "number": 4,
        "title": "Living in an Inadequate World",
        "content": """
<h1>Chapter 4: Living in an Inadequate World</h1>

<h2>Main Themes</h2>

<p>This chapter explores how to navigate a civilization with systemic failures without falling into either blind trust or excessive cynicism. Eliezer Yudkowsky argues that understanding inadequate equilibria helps calibrate when to trust experts versus when to think independently.</p>

<h2>Key Arguments</h2>

<p><strong>On False Cynicism:</strong></p>
<p>Yudkowsky warns against dismissing entire systems as broken without evidence. He uses the example of parents caring for sick infants—parents who drive hours monthly to obtain lifesaving medications demonstrate genuine concern that contradicts cynical explanations of systemic failure.</p>

<p><strong>On Competence Assessment:</strong></p>
<p>Rather than ranking yourself against experts hierarchically, Yudkowsky advocates examining specific domains. His medical anecdotes illustrate how doctors can be simultaneously knowledgeable (correctly diagnosing migraines) and limited (missing fungal causes of dandruff). "Medical competence—not absolute performance, but competence relative to what I can figure out by Googling—is high-variance."</p>

<p><strong>On Status Versus Systems:</strong></p>
<p>Modest epistemology conflates performance differences with status hierarchies. The alternative isn't claiming superiority but recognizing that organizations have different incentive structures. A nonprofit research institute organized differently than academia doesn't claim higher status—just different alignment with certain research goals.</p>

<p><strong>On Practical Improvement:</strong></p>

<p>The realistic distribution of meaningful contributions includes:</p>
<ul>
<li>0-2 lifetime instances of advancing civilization's knowledge substantially</li>
<li>Annual opportunities to synthesize existing expert disagreements for personal benefit</li>
<li>Frequent chances to identify correct contrarians in existing disputes</li>
</ul>

<p><strong>On Concrete Action:</strong></p>
<p>Yudkowsky emphasizes updating hard on direct experience, placing actual bets, and accepting failure as learning. His Higgs boson wager at unfavorable odds taught him more than abstract reasoning alone could convey.</p>

<h2>Core Message</h2>

<p>Becoming effective in an inadequate world means abandoning both naive deference and grandiose self-assessment, instead building skill through empirical observation and measured experimentation.</p>
"""
    },
    {
        "number": 5,
        "title": "Blind Empiricism",
        "content": """
<h1>Chapter 5: Blind Empiricism</h1>

<h2>Core Argument</h2>

<p>This chapter critiques excessive deference to empiricism and the "outside view" in reasoning. The author argues that "it's okay to reason about the particulars of where civilization might be inadequate" and act on detailed models while remaining open to evidence.</p>

<h2>Three Illustrative Conversations</h2>

<p><strong>Conversation 1 (AI Testing):</strong> The author wanted advance predictions before experiments to test understanding, but faced pushback from someone who seemed to view theorizing as inherently risky. Yudkowsky argues you must "master saying oops" to have theories and make experimental predictions without losing empirical rigor.</p>

<p><strong>Conversation 2 (Startup MVP):</strong> A founder wanted to release an unpolished product immediately. Yudkowsky countered that a "minimum viable product" requires detailed user modeling—understanding specific workflows and tasks—not just shipping compilable code. Without this causal thinking, you learn nothing meaningful.</p>

<p><strong>Conversation 3 (Business Planning):</strong> Another founder used the outside view to avoid ambitious goals, assuming his Snowshoes company shouldn't exceed average Flippers industry size. The author pushed back: success requires backward-chaining from desired outcomes and understanding why market premiums exist.</p>

<h2>Key Insight</h2>

<p>The chapter warns against conflating "avoid overconfidence" with "avoid having theories." Blind empiricism—collecting observations without causal models—produces shallow generalizations. Effective reasoning requires both detailed modeling and willingness to update based on evidence.</p>
"""
    },
    {
        "number": 6,
        "title": "Against Modest Epistemology",
        "content": """
<h1>Chapter 6: Against Modest Epistemology</h1>

<h2>Core Argument</h2>

<p>This chapter challenges "modest epistemology"—the view that we should defer to others' judgments rather than trust our own reasoning, especially when facing disagreement or novel situations.</p>

<h2>Key Premises</h2>

<p>The author references Aumann's theorem: two ideal Bayesian reasoners with identical priors cannot maintain disagreement if fully rational. However, the author argues this doesn't justify blanket deference to others.</p>

<h2>Main Points</h2>

<p><strong>The Anecdotal Case:</strong></p>
<p>The author describes disagreeing with colleague Anna Salamon about teaching methodology. Despite having what seemed like superior reasoning, he was wrong. This taught him that his "meta-rationality"—ability to judge whose thinking is clearer—wasn't necessarily better than hers.</p>

<p><strong>Against Rule M (Modesty):</strong></p>
<p>The author constructs a formal rule capturing modest epistemology, then demonstrates its absurdity through reductios:</p>
<ul>
<li>It would require believing God exists (averaging with religious believers)</li>
<li>It would make superintelligent AIs think they're psychiatric patients</li>
<li>It would suggest you're likely asleep (averaging with dreamers)</li>
</ul>

<p><strong>Proper Bayesian Reasoning:</strong></p>
<p>True Bayesian epistemology requires conditioning on available evidence—including knowledge of one's own reasoning capabilities—rather than abstracting away to generic self-descriptions that apply equally to crackpots and thoughtful reasoners.</p>

<h2>Conclusion</h2>

<p>Rather than rejecting detailed self-observation, effective epistemology should distinguish between good and bad reasoning while remaining open to discovering one's errors.</p>
"""
    },
    {
        "number": 7,
        "title": "Status Regulation and Anxious Underconfidence",
        "content": """
<h1>Chapter 7: Status Regulation and Anxious Underconfidence</h1>

<h2>Overview</h2>

<p>This chapter examines emotional and social factors underlying modesty as an epistemological stance, arguing that anxious underconfidence and status regulation—rather than pure epistemic reasoning—drive much of modesty's appeal.</p>

<h2>Main Arguments</h2>

<p><strong>Anxious Underconfidence</strong></p>

<p>The author describes a pervasive pattern where people avoid attempting valuable goals due to fear of failure disproportionate to actual consequences. A person might pursue nursing instead of physics because they're certain they'll succeed at nursing, avoiding anything uncertain. The author illustrates: "If you never fail, you're only trying things that are too easy and playing far below your level."</p>

<p>This emotional pattern causes people to filter opportunities excessively, crossing off uncertain projects before seriously considering them.</p>

<p><strong>Status Regulation</strong></p>

<p>The author argues that many people experience status as a fundamental emotional entity—a reified social thing distinct from respect, goods, or deliberative reasoning. Attempting to claim status beyond one's current level triggers a slapdown response that protects the social hierarchy.</p>

<p>Modest epistemology can function as "cheater-resistant" social enforcement: preventing lower-status individuals from challenging established authorities, particularly in respected fields.</p>

<p><strong>Key Distinctions</strong></p>

<p>The author emphasizes that modest epistemology often mimics efficient market reasoning but operates in domains lacking sufficient mechanisms for efficiency. What works for liquid asset markets shouldn't automatically transfer to housing markets, medicine, or scientific fields.</p>

<h2>Conclusion</h2>

<p>Rather than accepting modesty as pure epistemology, the author suggests recognizing when social anxiety and status concerns masquerade as rational caution. Better reasoning requires addressing underlying emotional drivers, not merely adopting skeptical verbal formulas.</p>
"""
    },
    {
        "number": 8,
        "title": "Against Shooting Yourself in the Foot",
        "content": """
<h1>Conclusion: Against Shooting Yourself in the Foot</h1>

<p>This chapter serves as the conclusion to "Inadequate Equilibria." The author addresses potential misuses of the advice contained within the work.</p>

<h2>Main Themes</h2>

<p><strong>Warnings and Practical Guidance</strong></p>

<p>Yudkowsky emphasizes the importance of common sense and empirical observation. He advises readers to "pay more attention to observation than to theory" when evidence conflicts, and to test oneself whenever possible to receive rapid feedback.</p>

<p><strong>Different Audiences, Different Risks</strong></p>

<p>The author expresses concern that overconfident individuals might misappropriate the terminology as excuses rather than tools for improvement. However, he suggests the book may benefit underconfident readers more substantially. He notes he's "not aware of cases where modest epistemology actually rescued previously overconfident people."</p>

<p><strong>Calibration Through Betting</strong></p>

<p>A practical recommendation involves making predictions on testable matters to develop accurate confidence levels. This practice serves dual purposes: reducing both overconfidence and underconfidence while building emotional resilience for reasoning about systems.</p>

<p><strong>The Balance for Ambitious Work</strong></p>

<p>For those attempting unusually difficult goals—scientists, entrepreneurs, effective altruists—modesty can prove counterproductive. Breakthrough work requires "acting on private information" and "breaking new ground," necessitating confidence despite uncertainty.</p>

<h2>Central Message</h2>

<p>Rather than focusing on self-assessment, readers should concentrate on understanding specific capabilities and matching them to actual challenges. The conclusion advocates examining "details of what you can do, what there is to be done, and how one might do it."</p>

<p>The world isn't mysteriously doomed to its current level of inadequacy—incentive structures have parts and can be reengineered in some cases, worked around in others. Better to not worry quite so much about how lowly or impressive you are, and better to meditate on the details of what you can do, what there is to be done, and how one might do it.</p>
"""
    }
]

def create_epub():
    """Create EPUB file structure"""

    # Create directories
    os.makedirs("epub/META-INF", exist_ok=True)
    os.makedirs("epub/OEBPS", exist_ok=True)

    # Create mimetype file (must be first and uncompressed)
    with open("epub/mimetype", "w") as f:
        f.write("application/epub+zip")

    # Create container.xml
    container_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''

    with open("epub/META-INF/container.xml", "w") as f:
        f.write(container_xml)

    # Create stylesheet
    css = '''body {
    font-family: Georgia, serif;
    line-height: 1.6;
    margin: 1em;
}

h1 {
    font-size: 2em;
    margin-top: 1em;
    margin-bottom: 0.5em;
    text-align: left;
}

h2 {
    font-size: 1.5em;
    margin-top: 1em;
    margin-bottom: 0.5em;
}

p {
    margin: 0.5em 0;
    text-indent: 0;
}

ul, ol {
    margin: 0.5em 0;
    padding-left: 2em;
}

strong {
    font-weight: bold;
}

em {
    font-style: italic;
}'''

    with open("epub/OEBPS/stylesheet.css", "w") as f:
        f.write(css)

    # Create title page
    title_html = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{BOOK_TITLE}</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
</head>
<body>
    <div style="text-align: center; margin-top: 3em;">
        <h1>{BOOK_TITLE}</h1>
        <h2>{BOOK_SUBTITLE}</h2>
        <p style="margin-top: 2em; font-size: 1.2em;">by {AUTHOR}</p>
        <p style="margin-top: 3em;">{PUBLISHER}</p>
        <p>{PUBLICATION_DATE}</p>
    </div>
</body>
</html>'''

    with open("epub/OEBPS/title.xhtml", "w") as f:
        f.write(title_html)

    # Create chapter files
    for chapter in chapters:
        chapter_html = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Chapter {chapter['number']}: {chapter['title']}</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
</head>
<body>
{chapter['content']}
</body>
</html>'''

        with open(f"epub/OEBPS/chapter{chapter['number']}.xhtml", "w") as f:
            f.write(chapter_html)

    # Create content.opf
    manifest_items = ['<item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>']
    manifest_items.append('<item id="css" href="stylesheet.css" media-type="text/css"/>')

    spine_items = ['<itemref idref="title"/>']

    for chapter in chapters:
        manifest_items.append(f'<item id="chapter{chapter["number"]}" href="chapter{chapter["number"]}.xhtml" media-type="application/xhtml+xml"/>')
        spine_items.append(f'<itemref idref="chapter{chapter["number"]}"/>')

    content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:title>{BOOK_TITLE}: {BOOK_SUBTITLE}</dc:title>
        <dc:creator>{AUTHOR}</dc:creator>
        <dc:language>{LANGUAGE}</dc:language>
        <dc:identifier id="bookid">{IDENTIFIER}</dc:identifier>
        <dc:publisher>{PUBLISHER}</dc:publisher>
        <dc:date>{PUBLICATION_DATE}</dc:date>
        <dc:rights>CC NC-BY-SA 4.0</dc:rights>
        <meta property="dcterms:modified">{datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")}</meta>
    </metadata>
    <manifest>
        {chr(10).join('        ' + item for item in manifest_items)}
        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    </manifest>
    <spine toc="ncx">
        {chr(10).join('        ' + item for item in spine_items)}
    </spine>
</package>'''

    with open("epub/OEBPS/content.opf", "w") as f:
        f.write(content_opf)

    # Create toc.ncx
    nav_points = []
    for i, chapter in enumerate(chapters, 1):
        nav_points.append(f'''        <navPoint id="navPoint-{i+1}" playOrder="{i+1}">
            <navLabel>
                <text>Chapter {chapter['number']}: {chapter['title']}</text>
            </navLabel>
            <content src="chapter{chapter['number']}.xhtml"/>
        </navPoint>''')

    toc_ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="{IDENTIFIER}"/>
        <meta name="dtb:depth" content="1"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle>
        <text>{BOOK_TITLE}</text>
    </docTitle>
    <navMap>
        <navPoint id="navPoint-1" playOrder="1">
            <navLabel>
                <text>Title Page</text>
            </navLabel>
            <content src="title.xhtml"/>
        </navPoint>
{chr(10).join(nav_points)}
    </navMap>
</ncx>'''

    with open("epub/OEBPS/toc.ncx", "w") as f:
        f.write(toc_ncx)

    # Create EPUB zip file
    epub_filename = "Inadequate_Equilibria_Eliezer_Yudkowsky.epub"

    with zipfile.ZipFile(epub_filename, 'w', zipfile.ZIP_DEFLATED) as epub:
        # mimetype must be first and uncompressed
        epub.write("epub/mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)

        # Add all other files
        for root, dirs, files in os.walk("epub"):
            for file in files:
                if file != "mimetype":
                    file_path = os.path.join(root, file)
                    arc_path = file_path[5:]  # Remove "epub/" prefix
                    epub.write(file_path, arc_path)

    print(f"✓ EPUB created successfully: {epub_filename}")
    return epub_filename

if __name__ == "__main__":
    create_epub()
