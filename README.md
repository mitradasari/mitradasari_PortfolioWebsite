# Personal Portfolio Website — IT4048 Mini Project
**Subject Code:** IT4048 Version Control with Git and GitHub  
**Student Name:** Sohan Enjamuri (Sunny)  
**Live GitHub Pages Demo:** [https://sohanenjamuri.github.io/SohanEnjamuri_PortfolioWebsite/](https://sohanenjamuri.github.io/SohanEnjamuri_PortfolioWebsite/)  
**GitHub Repository:** [https://github.com/sohanenjamuri/SohanEnjamuri_PortfolioWebsite](https://github.com/sohanenjamuri/SohanEnjamuri_PortfolioWebsite)  

---

## 📌 Project Overview
This repository contains the complete source code for a modern, responsive personal portfolio website designed and developed for the **IT4048 Version Control with Git and GitHub** course mini-project. 

The website highlights the student's background, technical and soft skills, featured software projects, contact information, and downloadable résumé. It is built using semantic **HTML5**, modern **Vanilla CSS3** (with glassmorphism and dark/light mode), and **JavaScript (ES6+)**, completely optimized for zero-build static hosting on **GitHub Pages**.

---

## 🎯 Verification of Project Requirements

| Requirement Item from Guidelines | Implementation Details | Status |
| :--- | :--- | :---: |
| **1. Home / About Section** | Student's name (Sohan Enjamuri), high-resolution portrait photograph, professional dynamic typing tagline, concise biography, and academic highlights for IT4048. | ✅ Completed |
| **2. Skills Section** | Categorized list of technical skills (Frontend, Backend, Git/DevOps) and soft skills (Problem Solving, Collaboration, PR Reviews), complete with icons, badges, and animated progress bars. | ✅ Completed |
| **3. Projects Section** | 4 full sample projects (`DevPulse`, `CloudVault`, `AlgoArena`, `ShopWave`) with descriptions, tech stack tags, GitHub repository links, live preview buttons, and interactive Quick View modal dialogs. | ✅ Completed |
| **4. Contact Section** | Direct clickable links for LinkedIn, GitHub, and Email (`sunnyenjamuri4456@gmail.com`), instant copy email button, plus an interactive contact form with client-side field validation and animated feedback. | ✅ Completed |
| **5. Résumé Download Button** | Working button to download the PDF résumé (`resume.pdf`), along with an in-browser modal viewer. | ✅ Completed |
| **Design: Responsive Layout** | 100% responsive across desktop (1920px, 1200px), tablet (768px-1024px), and mobile (down to 320px) with slide-out drawer menu. | ✅ Completed |
| **Design: Consistent Color Theme** | Modern obsidian/indigo dark theme with cyan highlights, plus an instant Dark / Light mode toggle saved in `localStorage`. | ✅ Completed |
| **Design: Smooth Navigation** | Fixed glassmorphism navbar with scrollspy active link indicator and smooth scroll to sections. | ✅ Completed |
| **Design: Interactivity & Animations** | Animated typing hero tagline, floating badge cards, hover lift/glow effects, animated progress bars, modal popups, and toast notifications. | ✅ Completed |
| **Design: Footer Links** | Social media channels (GitHub, LinkedIn, Email, Twitter/X), course disclaimer, navigation links, and back-to-top button. | ✅ Completed |

---

## 🗂️ File & Directory Structure

```text
mitra_github_project/
├── index.html                           # Main portfolio single-page application
├── style.css                            # Modern Vanilla CSS design system & tokens
├── script.js                            # Client-side interactivity (typing, theme, modals, validation)
├── resume.html                          # Accessible HTML résumé template
├── resume.pdf                           # Official downloadable A4 PDF résumé
├── generate_resume.py                   # Python ReportLab generator for resume.pdf
├── generate_report.py                   # Python ReportLab generator for submission PDF report
├── GitHub_EnrollmentNo_SohanEnjamuri.pdf# Complete mini-project report with screenshots
├── README.md                            # Project documentation & deployment guide
└── assets/
    ├── docs/
    │   └── Sohan_Enjamuri_Resume.pdf    # Backup copy of PDF resume
    └── images/
        ├── favicon.svg                  # Vector browser favicon
        ├── profile.jpg                  # Professional portrait headshot
        ├── project-devpulse.jpg         # DevPulse project preview
        ├── project-cloudvault.jpg       # CloudVault project preview
        ├── project-algoarena.jpg        # AlgoArena project preview
        ├── project-shopwave.jpg         # ShopWave project preview
        └── screenshots/                 # High-resolution screenshots of live website
            ├── 01_hero_home.png
            ├── 02_light_theme.png
            ├── 03_about_section.png
            ├── 04_skills_section.png
            ├── 05_projects_section.png
            ├── 06_project_modal.png
            └── 07_contact_section.png
```

---

## 🚀 Git & GitHub Deployment Instructions

Follow these exact steps to push this project to GitHub and deploy it on **GitHub Pages**:

### Step 1: Initialize Git and Commit All Files
Open terminal or PowerShell in this project folder:
```bash
# 1. Initialize local Git repository (if not already done)
git init

# 2. Add all project files
git add .

# 3. Create initial commit
git commit -m "feat: complete personal portfolio website for IT4048 mini-project submission"
```

### Step 2: Create a New GitHub Repository
1. Log in to [GitHub](https://github.com/).
2. Click **New Repository** (or visit `https://github.com/new`).
3. Repository Name: `YourName_PortfolioWebsite` (e.g. `SohanEnjamuri_PortfolioWebsite`).
4. Set visibility to **Public** (required for grading).
5. Do **not** initialize with a README, .gitignore, or license (we already have them).
6. Click **Create repository**.

### Step 3: Link and Push to GitHub
```bash
# Set branch to main
git branch -M main

# Add your GitHub remote repository (replace with your repository URL)
git remote add origin https://github.com/sohanenjamuri/SohanEnjamuri_PortfolioWebsite.git

# Push files to GitHub
git push -u origin main
```

### Step 4: Deploy Live using GitHub Pages
1. On GitHub, go to your repository: `https://github.com/sohanenjamuri/SohanEnjamuri_PortfolioWebsite`
2. Click **Settings** (top navigation tab).
3. In the left sidebar, click **Pages** (under the "Code and automation" section).
4. Under **Build and deployment**:
   - **Source:** Select `Deploy from a branch`.
   - **Branch:** Select `main` from the dropdown, and `/ (root)` folder.
   - Click **Save**.
5. Wait 1–2 minutes for the GitHub Actions deployment to finish.
6. Refresh the page; your live link will be generated:
   ```text
   https://sohanenjamuri.github.io/SohanEnjamuri_PortfolioWebsite/
   ```
7. Open the live link in your browser to verify all links, buttons, and sections.

---

## 📋 Course Submission Checklist (Deadline: 24th October 2026)

Prepare the following 3 items for submission as specified in the assignment PDF:

1. **GitHub Repository Link:**  
   `https://github.com/sohanenjamuri/SohanEnjamuri_PortfolioWebsite`
2. **Live GitHub Pages Link:**  
   `https://sohanenjamuri.github.io/SohanEnjamuri_PortfolioWebsite/`
3. **Short Project Report (PDF):**  
   - Generated file: `GitHub_EnrollmentNo_SohanEnjamuri.pdf` (rename `EnrollmentNo` to your student enrollment number).
   - Contains: Student Name, Enrollment Number, Project Objective, Technologies Used, Website Page Screenshots, Repository Link, and Live Pages Link.
4. **Google Drive Submission Folder:**  
   Upload the PDF report and links to the course Google Drive link:  
   `https://drive.google.com/drive/folders/122W5B3tNqc7r6aJS-tIkOIpjNgjHJ_dj?usp=sharing`

---
© 2026 Sohan Enjamuri. Built for IT4048: Version Control with Git and GitHub.
