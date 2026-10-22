from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(BASE_DIR, "GitHub_EnrollmentNo_MitraDasari.pdf")

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=40,
    rightMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

PRIMARY = colors.HexColor("#0f172a")      # Slate 900
ACCENT = colors.HexColor("#4f46e5")       # Indigo
MUTED = colors.HexColor("#475569")        # Slate 600
BORDER_COLOR = colors.HexColor("#cbd5e1") # Slate 300
BG_HEADER = colors.HexColor("#f8fafc")

doc_title = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=PRIMARY,
    alignment=1,
    spaceAfter=4
)

doc_subtitle = ParagraphStyle(
    'DocSubtitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=ACCENT,
    alignment=1,
    spaceAfter=14
)

section_title = ParagraphStyle(
    'SectionTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=16,
    textColor=PRIMARY,
    spaceBefore=12,
    spaceAfter=6,
    textTransform='uppercase'
)

body = ParagraphStyle(
    'BodyText',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=14,
    textColor=PRIMARY
)

body_bold = ParagraphStyle(
    'BodyBold',
    parent=body,
    fontName='Helvetica-Bold'
)

bullet = ParagraphStyle(
    'Bullet',
    parent=body,
    leftIndent=14,
    spaceAfter=3
)

story = []

# Title & Subtitle
story.append(Paragraph("MINI PROJECT REPORT: PERSONAL PORTFOLIO WEBSITE", doc_title))
story.append(Paragraph("Subject Code: IT4048 — Version Control with Git and GitHub", doc_subtitle))
story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceBefore=2, spaceAfter=10))

# 1. Student & Submission Information Table
story.append(Paragraph("1. STUDENT & SUBMISSION METADATA", section_title))
metadata_data = [
    [Paragraph("<b>Student Name:</b>", body), Paragraph("Mitra Dasari", body), Paragraph("<b>Enrollment No:</b>", body), Paragraph("<i>[Insert Enrollment Number Here]</i>", body)],
    [Paragraph("<b>Course Code:</b>", body), Paragraph("IT4048", body), Paragraph("<b>Course Name:</b>", body), Paragraph("Version Control with Git & GitHub", body)],
    [Paragraph("<b>GitHub Username:</b>", body), Paragraph("mitradasari", body), Paragraph("<b>Email Address:</b>", body), Paragraph("mitradasari232@gmail.com", body)],
    [Paragraph("<b>Repository Link:</b>", body), Paragraph("https://github.com/mitradasari/MitraDasari_PortfolioWebsite", body), Paragraph("<b>Live Pages Link:</b>", body), Paragraph("https://mitradasari.github.io/MitraDasari_PortfolioWebsite/", body)],
    [Paragraph("<b>Submission Date:</b>", body), Paragraph("24th October 2026", body), Paragraph("<b>Format Standard:</b>", body), Paragraph("GitHub_EnrollmentNo_YourName", body)]
]

t_meta = Table(metadata_data, colWidths=[110, 160, 120, 142])
t_meta.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), BG_HEADER),
    ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
    ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(t_meta)
story.append(Spacer(1, 10))

# 2. Objective of the Project
story.append(Paragraph("2. OBJECTIVE OF THE PROJECT", section_title))
story.append(Paragraph(
    "The primary objective of this mini-project is to design, engineer, and deploy an ultra-responsive, professional personal portfolio website that comprehensively highlights the student's technical abilities, sample software projects, version control competencies, and contact information. The project strictly satisfies all pedagogical requirements for <b>IT4048 (Version Control with Git and GitHub)</b>, including repository creation, commit discipline, branch management, pull requests, automated GitHub Pages deployment, and responsive UI/UX across desktop, tablet, and mobile displays.",
    body
))
story.append(Spacer(1, 10))

# 3. Technologies Used
story.append(Paragraph("3. TECHNOLOGIES & TOOLS USED", section_title))
tech_data = [
    [Paragraph("<b>Layer / Domain</b>", body_bold), Paragraph("<b>Technology / Framework</b>", body_bold), Paragraph("<b>Application & Role</b>", body_bold)],
    [Paragraph("Markup & Structure", body), Paragraph("Semantic HTML5", body), Paragraph("Accessible DOM structure, SEO meta tags, OpenGraph cards, ARIA roles", body)],
    [Paragraph("Styling & Design System", body), Paragraph("Modern Vanilla CSS3", body), Paragraph("CSS Custom Properties, Glassmorphism, CSS Grid & Flexbox, clamp() typography", body)],
    [Paragraph("Interactivity & State", body), Paragraph("Vanilla JavaScript (ES6+)", body), Paragraph("Dynamic typing tagline, theme toggle (Dark/Light), modals, live form validation", body)],
    [Paragraph("Version Control", body), Paragraph("Git (CLI & GitHub Flow)", body), Paragraph("Feature branching, semantic commit messages, merge conflict resolution", body)],
    [Paragraph("Cloud Hosting / CI-CD", body), Paragraph("GitHub Pages", body), Paragraph("Continuous deployment pipeline delivering zero-build static hosting", body)],
    [Paragraph("Iconography & Fonts", body), Paragraph("Google Fonts & FontAwesome 6", body), Paragraph("Plus Jakarta Sans, Inter, JetBrains Mono, and FontAwesome vector icons", body)],
    [Paragraph("Documentation & CV", body), Paragraph("ReportLab & Headless PDF", body), Paragraph("Standardized A4 PDF resume and project submission documentation", body)]
]

t_tech = Table(tech_data, colWidths=[120, 140, 272])
t_tech.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), BG_HEADER),
    ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
    ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ('TOPPADDING', (0,0), (-1,-1), 3.5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
]))
story.append(t_tech)
story.append(Spacer(1, 10))

# 4. Mandatory Sections Implemented
story.append(Paragraph("4. MANDATORY SECTIONS IMPLEMENTATION CHECKLIST", section_title))
story.append(Paragraph("• <b>Home / About Page:</b> Professional portrait photo, dynamic typing tagline, comprehensive bio, academic context, and quick action CTAs.", bullet))
story.append(Paragraph("• <b>Skills Page:</b> Categorized technical and soft skills (Frontend, Backend, Git/DevOps, Soft Skills) with animated proficiency percentage bars and core IT4048 badges.", bullet))
story.append(Paragraph("• <b>Projects Page:</b> 2 featured academic projects (1. Ethnic Hub – Wholesale Traditional Wear Website [HTML, CSS, JS, PHP, MySQL, XAMPP], 2. Student Skill Swap – Student Skill Exchange Platform [HTML, CSS, PHP, MySQL, XAMPP, phpMyAdmin]) with tech tags, quick-view detail modals, and GitHub links.", bullet))
story.append(Paragraph("• <b>Contact Page:</b> Comprehensive contact channels (email, GitHub, LinkedIn), instant copy-to-clipboard button, and interactive contact form with real-time field validation.", bullet))
story.append(Paragraph("• <b>Resume Download & View:</b> Functional download button for <i>resume.pdf</i> as well as embedded modal preview.", bullet))
story.append(Paragraph("• <b>Responsive & Accessible:</b> Fully responsive down to 320px mobile screens with slide-out drawer menu, fluid typography, and dark/light mode toggle.", bullet))

# Page Break for Screenshots
story.append(PageBreak())

# 5. Screenshots of Website Pages
story.append(Paragraph("5. SCREENSHOTS OF WEBSITE PAGES & FEATURES", section_title))
story.append(Paragraph("The following high-resolution screenshots verify the visual fidelity and functionality of the live deployed website:", body))
story.append(Spacer(1, 8))

# Screenshot Table 1: Home & Light Mode
img_hero = Image(os.path.join(BASE_DIR, "assets", "images", "screenshots", "01_hero_home.png"), width=255, height=145)
img_light = Image(os.path.join(BASE_DIR, "assets", "images", "screenshots", "02_light_theme.png"), width=255, height=145)

t_img1 = Table([
    [img_hero, img_light],
    [Paragraph("<b>Figure 1:</b> Home / Hero Section (Dark Theme)", body), Paragraph("<b>Figure 2:</b> Instant Theme Switch (Light Theme)", body)]
], colWidths=[266, 266])
t_img1.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 2),
]))
story.append(t_img1)
story.append(Spacer(1, 8))

# Screenshot Table 2: About & Skills
img_about = Image(os.path.join(BASE_DIR, "assets", "images", "screenshots", "03_about_section.png"), width=255, height=125)
img_skills = Image(os.path.join(BASE_DIR, "assets", "images", "screenshots", "04_skills_section.png"), width=255, height=125)

t_img2 = Table([
    [img_about, img_skills],
    [Paragraph("<b>Figure 3:</b> About Me & IT4048 Course Section", body), Paragraph("<b>Figure 4:</b> Skills with Animated Progress Bars", body)]
], colWidths=[266, 266])
t_img2.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 2),
]))
story.append(t_img2)
story.append(Spacer(1, 8))

# Screenshot Table 3: Projects & Modal
img_projects = Image(os.path.join(BASE_DIR, "assets", "images", "screenshots", "05_projects_section.png"), width=255, height=135)
img_modal = Image(os.path.join(BASE_DIR, "assets", "images", "screenshots", "06_project_modal.png"), width=255, height=135)

t_img3 = Table([
    [img_projects, img_modal],
    [Paragraph("<b>Figure 5:</b> Featured Projects Grid & Tags", body), Paragraph("<b>Figure 6:</b> Interactive Project Quick View Modal", body)]
], colWidths=[266, 266])
t_img3.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 2),
]))
story.append(t_img3)
story.append(Spacer(1, 8))

# Screenshot Table 4: Contact Form
img_contact = Image(os.path.join(BASE_DIR, "assets", "images", "screenshots", "07_contact_section.png"), width=255, height=115)
t_img4 = Table([
    [img_contact, Paragraph("<br/><br/><b>Figure 7 (Left):</b> Contact Form with live validation, instant response alert, and clickable contact links.<br/><br/><b>Deployment:</b> Configured with standard GitHub Pages workflow from main branch.<br/><br/><b>Status:</b> 100% Tested & Verified across viewport widths.", body)]
], colWidths=[266, 266])
t_img4.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 2),
]))
story.append(t_img4)

doc.build(story)
print("Report generated successfully at", pdf_path)
