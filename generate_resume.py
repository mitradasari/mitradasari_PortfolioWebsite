from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
import shutil
import os

pdf_path = "c:/sunny/mitra_github_project/resume.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=44,
    rightMargin=44,
    topMargin=44,
    bottomMargin=44
)

styles = getSampleStyleSheet()

# Colors
PRIMARY = colors.HexColor("#0f172a")       # Slate 900
ACCENT = colors.HexColor("#334155")        # Slate 700
TEXT_DARK = colors.HexColor("#1e293b")     # Slate 800
TEXT_MUTED = colors.HexColor("#475569")    # Slate 600
LINE_COLOR = colors.HexColor("#94a3b8")    # Line

title_style = ParagraphStyle(
    'NameTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=PRIMARY,
    alignment=1, # Centered
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    leading=15,
    textColor=TEXT_DARK,
    alignment=1, # Centered
    spaceAfter=3
)

contact_style = ParagraphStyle(
    'Contact',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=TEXT_MUTED,
    alignment=1, # Centered
    spaceAfter=12
)

section_heading = ParagraphStyle(
    'SectionHeading',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=15,
    textColor=PRIMARY,
    spaceBefore=12,
    spaceAfter=4,
    textTransform='uppercase'
)

body_text = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=14,
    textColor=TEXT_DARK
)

bold_text = ParagraphStyle(
    'BoldText',
    parent=body_text,
    fontName='Helvetica-Bold'
)

bullet_text = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=14,
    textColor=TEXT_DARK,
    leftIndent=14,
    spaceAfter=3
)

story = []

# Header
story.append(Paragraph("MITRA DASARI", title_style))
story.append(Paragraph("B.Tech Student | Computer Science Engineering", subtitle_style))
story.append(Paragraph("mitradasari232@gmail.com | +91 9274569155", contact_style))
story.append(HRFlowable(width="100%", thickness=1, color=LINE_COLOR, spaceBefore=4, spaceAfter=10))

# Professional Summary
story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
story.append(Paragraph(
    "Motivated Computer Science Engineering student at UKA Tarsadia University with an interest in web development, web design, and programming. Familiar with HTML, CSS, Java, and SQL. Interested in applying technical knowledge to practical projects, developing problem-solving skills, and learning new technologies.",
    body_text
))
story.append(Spacer(1, 4))

# Education
story.append(Paragraph("EDUCATION", section_heading))
story.append(Paragraph("<b>Bachelor of Technology (B.Tech) – Computer Science Engineering</b>", bold_text))
story.append(Paragraph("UKA Tarsadia University | Currently pursuing – 3rd Semester", body_text))
story.append(Spacer(1, 4))

# Technical Skills
story.append(Paragraph("TECHNICAL SKILLS", section_heading))
story.append(Paragraph("<b>Web Technologies:</b> HTML, CSS", body_text))
story.append(Spacer(1, 2))
story.append(Paragraph("<b>Programming Language:</b> Java", body_text))
story.append(Spacer(1, 2))
story.append(Paragraph("<b>Database:</b> SQL", body_text))
story.append(Spacer(1, 2))
story.append(Paragraph("<b>Design:</b> Web Design", body_text))
story.append(Spacer(1, 4))

# Academic Project
story.append(Paragraph("ACADEMIC PROJECT", section_heading))
story.append(Paragraph("<b>Ethnic Hub – Wholesale Traditional Wear Website</b>", bold_text))
story.append(Spacer(1, 3))
story.append(Paragraph("• Developed a website concept for a traditional-wear wholesale business.", bullet_text))
story.append(Paragraph("• Designed web pages to present ethnic wear products and their details.", bullet_text))
story.append(Paragraph("• Worked on features such as product display, shopping cart, and contact form.", bullet_text))
story.append(Paragraph("• Explored database integration and website functionality.", bullet_text))
story.append(Spacer(1, 4))

# Core Strengths
story.append(Paragraph("CORE STRENGTHS", section_heading))
story.append(Paragraph("• Willingness to learn new technologies", bullet_text))
story.append(Paragraph("• Interest in web development and software projects", bullet_text))
story.append(Paragraph("• Practical approach to learning technical concepts", bullet_text))
story.append(Paragraph("• Interest in improving programming and problem-solving skills", bullet_text))

doc.build(story)
print("Mitra Dasari Resume PDF created at", pdf_path)

# Copy to assets/docs/Mitra_Dasari_Resume.pdf
backup_dest = "c:/sunny/mitra_github_project/assets/docs/Mitra_Dasari_Resume.pdf"
shutil.copyfile(pdf_path, backup_dest)
print("Copied to", backup_dest)
