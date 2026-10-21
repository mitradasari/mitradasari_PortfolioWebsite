from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
import os

pdf_path = "c:/sunny/mitra_github_project/resume.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=36,
    rightMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# Colors
PRIMARY = colors.HexColor("#1e1b4b")       # Deep indigo
ACCENT = colors.HexColor("#4f46e5")        # Electric Indigo
TEXT_DARK = colors.HexColor("#0f172a")     # Slate 900
TEXT_MUTED = colors.HexColor("#475569")    # Slate 600
LINE_COLOR = colors.HexColor("#cbd5e1")    # Slate 300
BG_BADGE = colors.HexColor("#eef2ff")      # Soft indigo

title_style = ParagraphStyle(
    'NameTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=PRIMARY,
    spaceAfter=2
)

tagline_style = ParagraphStyle(
    'Tagline',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=ACCENT,
    spaceAfter=4
)

contact_style = ParagraphStyle(
    'Contact',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=TEXT_MUTED,
    alignment=2 # Right aligned
)

section_heading = ParagraphStyle(
    'SectionHeading',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=PRIMARY,
    spaceBefore=8,
    spaceAfter=3,
    textTransform='uppercase'
)

body_text = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=12.5,
    textColor=TEXT_DARK
)

bullet_text = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11.5,
    textColor=TEXT_DARK,
    leftIndent=12,
    spaceAfter=2
)

item_title = ParagraphStyle(
    'ItemTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=12,
    textColor=PRIMARY
)

item_sub = ParagraphStyle(
    'ItemSub',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=11,
    textColor=ACCENT
)

date_style = ParagraphStyle(
    'Date',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=11,
    textColor=TEXT_MUTED,
    alignment=2
)

story = []

# Header Table (Name on left, contacts on right)
header_left = [
    Paragraph("SOHAN ENJAMURI", title_style),
    Paragraph("Full-Stack Developer & Software Engineering Student", tagline_style),
    Paragraph("Focus: Modern Web Apps • Git Version Control • Cloud Systems", ParagraphStyle('SubSub', parent=body_text, fontSize=8.5, textColor=TEXT_MUTED))
]

header_right = [
    Paragraph("Email: sunnyenjamuri4456@gmail.com", contact_style),
    Paragraph("GitHub: github.com/sohanenjamuri", contact_style),
    Paragraph("Portfolio: sohanenjamuri.github.io/portfolio", contact_style),
    Paragraph("LinkedIn: linkedin.com/in/sohan-enjamuri", contact_style),
    Paragraph("Location: India • Open to Internships", contact_style)
]

header_table = Table([[header_left, header_right]], colWidths=[330, 210])
header_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
]))
story.append(header_table)
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceBefore=4, spaceAfter=8))

# Professional Summary
story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
story.append(HRFlowable(width="100%", thickness=0.75, color=LINE_COLOR, spaceBefore=1, spaceAfter=4))
story.append(Paragraph(
    "Detail-driven Computer Science undergraduate specializing in full-stack web engineering, modern JavaScript architecture, and version control workflows. Demonstrated proficiency in building responsive web applications with semantic HTML5, modern CSS3, and JavaScript/React. Hands-on experience with collaborative Git branching models, merge conflict resolution, CI/CD automation, and live deployment on GitHub Pages as part of Course IT4048 (Version Control with Git and GitHub).",
    body_text
))
story.append(Spacer(1, 4))

# Technical Skills
story.append(Paragraph("TECHNICAL & SOFT SKILLS", section_heading))
story.append(HRFlowable(width="100%", thickness=0.75, color=LINE_COLOR, spaceBefore=1, spaceAfter=4))

skills_data = [
    [
        Paragraph("<b>Frontend:</b>", ParagraphStyle('SkL', parent=body_text, fontName='Helvetica-Bold')),
        Paragraph("HTML5, CSS3, JavaScript (ES6+), React.js, Responsive UI/UX, Flexbox, Grid", body_text)
    ],
    [
        Paragraph("<b>Backend & DB:</b>", ParagraphStyle('SkL', parent=body_text, fontName='Helvetica-Bold')),
        Paragraph("Node.js, Express.js, RESTful APIs, JSON, MongoDB, PostgreSQL, SQL Basics", body_text)
    ],
    [
        Paragraph("<b>Version Control & Tools:</b>", ParagraphStyle('SkL', parent=body_text, fontName='Helvetica-Bold')),
        Paragraph("Git (Branching, Merging, Rebasing, Stashing), GitHub, GitHub Pages, VS Code, Bash/CLI", body_text)
    ],
    [
        Paragraph("<b>Soft Skills:</b>", ParagraphStyle('SkL', parent=body_text, fontName='Helvetica-Bold')),
        Paragraph("Problem Solving, Team Collaboration, Agile Sprint Workflow, Documentation, Adaptability", body_text)
    ]
]

skills_table = Table(skills_data, colWidths=[140, 400])
skills_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 1.5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
]))
story.append(skills_table)
story.append(Spacer(1, 4))

# Featured Projects
story.append(Paragraph("FEATURED PROJECTS", section_heading))
story.append(HRFlowable(width="100%", thickness=0.75, color=LINE_COLOR, spaceBefore=1, spaceAfter=4))

# Project 1
p1_row = [[Paragraph("DevPulse — Developer Activity & GitHub Analytics", item_title), Paragraph("2026 | Live Demo & GitHub", date_style)]]
t_p1 = Table(p1_row, colWidths=[380, 160])
t_p1.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 1)]))
story.append(t_p1)
story.append(Paragraph("Tech Stack: JavaScript, GitHub REST API, Chart.js, HTML5/CSS3", item_sub))
story.append(Paragraph("• Architected a high-performance developer metrics dashboard that visualizes commit trends, code frequencies, and active pull requests.", bullet_text))
story.append(Paragraph("• Integrated client-side caching to reduce GitHub REST API rate-limit usage by 40% while preserving sub-second load times.", bullet_text))
story.append(Spacer(1, 3))

# Project 2
p2_row = [[Paragraph("CloudVault — Modern Secure Cloud Storage Platform", item_title), Paragraph("2026 | Live Demo & GitHub", date_style)]]
t_p2 = Table(p2_row, colWidths=[380, 160])
t_p2.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 1)]))
story.append(t_p2)
story.append(Paragraph("Tech Stack: HTML5, CSS3 Glassmorphism, JavaScript (ES6+), LocalStorage API", item_sub))
story.append(Paragraph("• Implemented drag-and-drop file upload interface with visual progress bar, file-type filtering, and encryption badge indicators.", bullet_text))
story.append(Paragraph("• Built dynamic category filtering (Documents, Images, Media) with responsive grid and list views.", bullet_text))
story.append(Spacer(1, 3))

# Project 3
p3_row = [[Paragraph("AlgoArena — Interactive Algorithm & Sorting Visualizer", item_title), Paragraph("2025 – 2026 | Live Demo & GitHub", date_style)]]
t_p3 = Table(p3_row, colWidths=[380, 160])
t_p3.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 1)]))
story.append(t_p3)
story.append(Paragraph("Tech Stack: JavaScript, HTML5 Canvas, Modern CSS Transitions", item_sub))
story.append(Paragraph("• Designed an intuitive visualizer for QuickSort, MergeSort, and Binary Search with customizable array sizes and playback speeds.", bullet_text))
story.append(Paragraph("• Added real-time comparison counters and big-O notation complexity breakdowns for educational clarity.", bullet_text))
story.append(Spacer(1, 3))

# Project 4
p4_row = [[Paragraph("Personal Portfolio Website (Mini Project IT4048)", item_title), Paragraph("2026 | GitHub Pages", date_style)]]
t_p4 = Table(p4_row, colWidths=[380, 160])
t_p4.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 1)]))
story.append(t_p4)
story.append(Paragraph("Tech Stack: HTML5, CSS3, JavaScript, Git, GitHub Pages", item_sub))
story.append(Paragraph("• Built a responsive, multi-section personal portfolio satisfying all criteria for IT4048 Version Control with Git and GitHub.", bullet_text))
story.append(Paragraph("• Features dark/light themes, interactive contact form with instant validation, animated skill bars, and live GitHub Pages hosting.", bullet_text))
story.append(Spacer(1, 4))

# Education
story.append(Paragraph("EDUCATION", section_heading))
story.append(HRFlowable(width="100%", thickness=0.75, color=LINE_COLOR, spaceBefore=1, spaceAfter=4))
edu_row = [[Paragraph("Bachelor of Technology (B.Tech) — Computer Science & Engineering", item_title), Paragraph("2023 – 2027", date_style)]]
t_edu = Table(edu_row, colWidths=[380, 160])
t_edu.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 1)]))
story.append(t_edu)
story.append(Paragraph("Coursework Highlights: IT4048 Version Control with Git & GitHub, Data Structures, Web Technologies, Database Systems", body_text))
story.append(Spacer(1, 4))

# Key Achievements & Git Proficiency
story.append(Paragraph("VERSION CONTROL (IT4048) & ACHIEVEMENTS", section_heading))
story.append(HRFlowable(width="100%", thickness=0.75, color=LINE_COLOR, spaceBefore=1, spaceAfter=4))
story.append(Paragraph("• <b>Git & GitHub Mastery:</b> Experienced in repository setup, branching workflows (feature branches, main), semantic commits, rebasing, pull requests, code reviews, and resolving merge conflicts.", bullet_text))
story.append(Paragraph("• <b>Automated Deployment:</b> Configured GitHub Pages deployment for zero-downtime, continuous static hosting from the main branch.", bullet_text))
story.append(Paragraph("• <b>Open-Source Engagement:</b> Regular contributor to student open-source repositories and collaborative coding projects.", bullet_text))

doc.build(story)
print("Resume generated successfully at", pdf_path)
