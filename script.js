/**
 * ==============================================================================
 * PORTFOLIO CLIENT-SIDE INTERACTIVITY SCRIPT
 * Student: Mitra Dasari
 * Course: IT4048 - Version Control with Git and GitHub
 * ==============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  /* --------------------------------------------------------------------------
     1. Project Data Store for Quick View Modal
     -------------------------------------------------------------------------- */
  const projectsData = {
    ethnichub: {
      title: 'Ethnic Hub — Wholesale Traditional Wear Website',
      category: 'Academic Project & Web Design',
      badge: 'Academic Project',
      image: 'assets/images/project-ethnichub.jpg',
      tags: ['HTML5', 'CSS3', 'Web Design', 'Java', 'SQL'],
      description: 'A dedicated website concept engineered for a traditional-wear wholesale business, featuring categorized catalog displays, interactive shopping cart capabilities, and database-driven product inventory.',
      features: [
        'Developed a comprehensive website concept tailored for traditional-wear wholesale businesses.',
        'Designed responsive web pages to present ethnic wear collections with detailed product views.',
        'Implemented core customer workflows: catalog filtering, dynamic shopping cart, and contact inquiry form.',
        'Explored SQL database schema integration and web functionality for inventory management.'
      ],
      githubUrl: 'https://github.com/mitradasari/ethnic-hub-website',
      liveUrl: 'https://mitradasari.github.io/ethnic-hub-website'
    },
    devpulse: {
      title: 'DevPulse — Developer Activity & GitHub Analytics',
      category: 'Full Stack & GitHub API',
      badge: 'IT4048 Project Highlight',
      image: 'assets/images/project-devpulse.jpg',
      tags: ['JavaScript', 'GitHub REST API', 'Chart.js', 'CSS3', 'Git CI/CD'],
      description: 'DevPulse is a high-performance developer metrics web dashboard that interfaces with the GitHub REST API to track commit cadences, code changes, and team pull request velocity in real-time.',
      features: [
        'Real-time visualization of commit frequencies and pull request timelines with Chart.js.',
        'Client-side cache strategy reducing GitHub REST API rate-limiting penalties by 40%.',
        'Configurable repository selector supporting both public and personal developer profiles.',
        'Zero-dependency build pipeline configured for instant GitHub Pages continuous deployment.'
      ],
      githubUrl: 'https://github.com/mitradasari/devpulse-analytics',
      liveUrl: 'https://mitradasari.github.io/devpulse-analytics'
    },
    cloudvault: {
      title: 'CloudVault — Secure Cloud File Platform',
      category: 'Frontend & Glassmorphism',
      badge: 'Modern Web App',
      image: 'assets/images/project-cloudvault.jpg',
      tags: ['HTML5', 'CSS Glassmorphism', 'JavaScript (ES6+)', 'LocalStorage API'],
      description: 'A modern, responsive cloud storage portal featuring intuitive drag-and-drop file uploads, progress monitoring, simulated end-to-end client-side encryption, and file categorization.',
      features: [
        'Drag-and-drop file upload with real-time size validation and visual progress indicators.',
        'Category breakdown filters for Documents, Images, Code, and Archives.',
        'Client-side persistence using LocalStorage with rapid multi-criteria search filtering.',
        'Polished dark-mode glassmorphic interface with accessible keyboard navigation.'
      ],
      githubUrl: 'https://github.com/mitradasari/cloudvault-storage',
      liveUrl: 'https://mitradasari.github.io/cloudvault-storage'
    },
    algoarena: {
      title: 'AlgoArena — Interactive Algorithm Visualizer',
      category: 'Interactive Tools & CS Education',
      badge: 'Algorithms & Data Structures',
      image: 'assets/images/project-algoarena.jpg',
      tags: ['JavaScript ES6', 'HTML5 Canvas', 'Sorting Algorithms', 'CSS Animations'],
      description: 'An interactive pedagogical tool designed to demystify classic computer science algorithms (QuickSort, MergeSort, BubbleSort, and Binary Search) through step-by-step canvas rendering.',
      features: [
        'Real-time color-coded bar rendering highlighting comparisons, pivots, and sorted partitions.',
        'Adjustable array sizes (10 to 100 elements) and granular playback speed slider.',
        'Live comparison counters, swap counters, and Big-O space-time complexity analysis tables.',
        'Step-by-step manual step forward/backward debugging controls.'
      ],
      githubUrl: 'https://github.com/mitradasari/algo-arena-visualizer',
      liveUrl: 'https://mitradasari.github.io/algo-arena-visualizer'
    },
    shopwave: {
      title: 'ShopWave — Next-Gen E-Commerce Web App',
      category: 'Frontend & State Management',
      badge: 'E-Commerce Solution',
      image: 'assets/images/project-shopwave.jpg',
      tags: ['Modern JavaScript', 'CSS Grid', 'Shopping Cart Logic', 'Toast Feedback'],
      description: 'A high-performance modern web storefront interface featuring instant category and price filtering, slide-out cart drawer, dynamic discount calculations, and toast alerts.',
      features: [
        'Instant multi-filter product catalog by category, price range, and in-stock availability.',
        'Slide-out shopping cart drawer with quantity adjustment and persistent state.',
        'Interactive coupon code verification engine with dynamic subtotal recalculation.',
        'Responsive layout optimized for smartphones, tablets, and wide desktop displays.'
      ],
      githubUrl: 'https://github.com/mitradasari/shopwave-ecommerce',
      liveUrl: 'https://mitradasari.github.io/shopwave-ecommerce'
    }
  };

  /* --------------------------------------------------------------------------
     2. Hero Section Typing Effect
     -------------------------------------------------------------------------- */
  const typingElement = document.getElementById('typing-text');
  if (typingElement) {
    const roles = [
      'responsive web applications.',
      'modern full-stack software.',
      'collaborative Git workflows.',
      'scalable cloud interfaces.',
      'clean & accessible code.'
    ];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 90;

    function typeEffect() {
      const currentRole = roles[roleIndex];

      if (isDeleting) {
        typingElement.textContent = currentRole.substring(0, charIndex - 1);
        charIndex--;
        typingSpeed = 45;
      } else {
        typingElement.textContent = currentRole.substring(0, charIndex + 1);
        charIndex++;
        typingSpeed = 90;
      }

      if (!isDeleting && charIndex === currentRole.length) {
        isDeleting = true;
        typingSpeed = 1600; // Pause at end of word
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        roleIndex = (roleIndex + 1) % roles.length;
        typingSpeed = 400; // Pause before new word
      }

      setTimeout(typeEffect, typingSpeed);
    }

    typeEffect();
  }

  /* --------------------------------------------------------------------------
     3. Theme Toggle (Dark & Light Mode) with LocalStorage
     -------------------------------------------------------------------------- */
  const themeToggleBtn = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  const htmlRoot = document.documentElement;

  // Retrieve saved preference or default to dark
  const savedTheme = localStorage.getItem('portfolio-theme') || 'dark';
  applyTheme(savedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = htmlRoot.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      applyTheme(newTheme);
      showToast(`Switched to ${newTheme === 'dark' ? 'Dark' : 'Light'} theme`, 'info');
    });
  }

  function applyTheme(theme) {
    htmlRoot.setAttribute('data-theme', theme);
    localStorage.setItem('portfolio-theme', theme);

    if (themeIcon) {
      if (theme === 'light') {
        themeIcon.className = 'fa-solid fa-sun';
        themeToggleBtn.setAttribute('title', 'Switch to Dark Mode');
      } else {
        themeIcon.className = 'fa-solid fa-moon';
        themeToggleBtn.setAttribute('title', 'Switch to Light Mode');
      }
    }
  }

  /* --------------------------------------------------------------------------
     4. Sticky Header & Scrollspy (Active Navigation Indicator)
     -------------------------------------------------------------------------- */
  const header = document.getElementById('header');
  const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', () => {
    // Header shadow and padding change
    if (window.scrollY > 30) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }

    // Back to top button visibility
    const backToTopBtn = document.getElementById('back-to-top');
    if (backToTopBtn) {
      if (window.scrollY > 400) {
        backToTopBtn.style.opacity = '1';
        backToTopBtn.style.pointerEvents = 'auto';
      } else {
        backToTopBtn.style.opacity = '0';
        backToTopBtn.style.pointerEvents = 'none';
      }
    }

    // Scrollspy active section
    let currentSectionId = '';
    const scrollPosition = window.scrollY + 120;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        currentSectionId = section.getAttribute('id');
      }
    });

    if (currentSectionId) {
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSectionId}`) {
          link.classList.add('active');
        }
      });
    }
  }, { passive: true });

  /* --------------------------------------------------------------------------
     5. Mobile Drawer Navigation
     -------------------------------------------------------------------------- */
  const hamburgerBtn = document.getElementById('hamburger-btn');
  const mobileDrawer = document.getElementById('mobile-drawer');
  const drawerOverlay = document.getElementById('mobile-drawer-overlay');
  const mobileCloseBtn = document.getElementById('mobile-close-btn');
  const mobileLinks = document.querySelectorAll('.mobile-nav-link');

  function openDrawer() {
    mobileDrawer?.classList.add('active');
    drawerOverlay?.classList.add('active');
    hamburgerBtn?.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    mobileDrawer?.classList.remove('active');
    drawerOverlay?.classList.remove('active');
    hamburgerBtn?.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  hamburgerBtn?.addEventListener('click', openDrawer);
  mobileCloseBtn?.addEventListener('click', closeDrawer);
  drawerOverlay?.addEventListener('click', closeDrawer);
  mobileLinks.forEach(link => link.addEventListener('click', closeDrawer));

  /* --------------------------------------------------------------------------
     6. Animated Progress Bars on Scroll
     -------------------------------------------------------------------------- */
  const progressBars = document.querySelectorAll('.progress-bar-fill');
  if ('IntersectionObserver' in window && progressBars.length > 0) {
    const progressObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const fill = entry.target;
          const targetWidth = fill.getAttribute('data-progress') || '0%';
          fill.style.width = targetWidth;
          observer.unobserve(fill);
        }
      });
    }, { threshold: 0.25 });

    progressBars.forEach(bar => progressObserver.observe(bar));
  } else {
    // Fallback for older browsers
    progressBars.forEach(bar => {
      bar.style.width = bar.getAttribute('data-progress') || '85%';
    });
  }

  /* --------------------------------------------------------------------------
     7. Skills Category Filter
     -------------------------------------------------------------------------- */
  const skillTabs = document.querySelectorAll('.filter-tab');
  const skillCards = document.querySelectorAll('.skill-card');

  skillTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      skillTabs.forEach(t => {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');

      const filterValue = tab.getAttribute('data-filter');

      skillCards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        if (filterValue === 'all' || cardCategory === filterValue) {
          card.style.display = 'flex';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 20);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 200);
        }
      });
    });
  });

  /* --------------------------------------------------------------------------
     8. Projects Category Filter
     -------------------------------------------------------------------------- */
  const projectFilterBtns = document.querySelectorAll('.project-filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  projectFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      projectFilterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filterValue === 'all' || category === filterValue) {
          card.style.display = 'flex';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 30);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(12px)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 220);
        }
      });
    });
  });

  /* --------------------------------------------------------------------------
     9. Project Quick View Modal
     -------------------------------------------------------------------------- */
  const projectModal = document.getElementById('project-modal');
  const projectModalBackdrop = document.getElementById('project-modal-backdrop');
  const projectModalClose = document.getElementById('project-modal-close');
  const projectModalTitle = document.getElementById('project-modal-title');
  const projectModalContent = document.getElementById('project-modal-content');
  const projectModalFooter = document.getElementById('project-modal-footer');
  const openModalButtons = document.querySelectorAll('.open-modal-btn');

  function openProjectModal(projectId) {
    const data = projectsData[projectId];
    if (!data || !projectModal) return;

    projectModalTitle.innerHTML = `<i class="fa-solid fa-laptop-code text-accent"></i> ${data.title}`;

    const tagsHtml = data.tags.map(tag => `<span class="tech-tag">${tag}</span>`).join(' ');
    const bulletsHtml = data.features.map(f => `<li>${f}</li>`).join('');

    projectModalContent.innerHTML = `
      <img src="${data.image}" alt="${data.title}" class="modal-project-img">
      <div class="project-tags" style="margin-bottom: 14px;">${tagsHtml}</div>
      <p style="font-size: 0.95rem; color: var(--text-primary); margin-bottom: 12px; line-height: 1.6;">${data.description}</p>
      <h4 style="font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; color: var(--text-primary); margin-top: 16px;">Key Architectural Features:</h4>
      <ul class="modal-project-bullets">${bulletsHtml}</ul>
    `;

    projectModalFooter.innerHTML = `
      <a href="${data.githubUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">
        <i class="fa-brands fa-github"></i> Repository
      </a>
      <a href="${data.liveUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">
        <i class="fa-solid fa-arrow-up-right-from-square"></i> Live Demo
      </a>
      <button class="btn btn-secondary btn-sm" id="close-modal-inline">Dismiss</button>
    `;

    document.getElementById('close-modal-inline')?.addEventListener('click', closeProjectModal);

    projectModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeProjectModal() {
    projectModal?.classList.remove('active');
    document.body.style.overflow = '';
  }

  openModalButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const projectId = btn.getAttribute('data-project');
      if (projectId) openProjectModal(projectId);
    });
  });

  projectModalClose?.addEventListener('click', closeProjectModal);
  projectModalBackdrop?.addEventListener('click', closeProjectModal);

  /* --------------------------------------------------------------------------
     10. Resume View Modal
     -------------------------------------------------------------------------- */
  const resumeModal = document.getElementById('resume-modal');
  const viewResumeBtn = document.getElementById('view-resume-modal-btn');
  const resumeModalClose = document.getElementById('resume-modal-close');
  const resumeModalBackdrop = document.getElementById('resume-modal-backdrop');
  const modalResumeDismiss = document.getElementById('modal-resume-dismiss');

  function openResumeModal() {
    if (resumeModal) {
      resumeModal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeResumeModal() {
    if (resumeModal) {
      resumeModal.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  viewResumeBtn?.addEventListener('click', openResumeModal);
  resumeModalClose?.addEventListener('click', closeResumeModal);
  resumeModalBackdrop?.addEventListener('click', closeResumeModal);
  modalResumeDismiss?.addEventListener('click', closeResumeModal);

  // Close modals on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeProjectModal();
      closeResumeModal();
      closeDrawer();
    }
  });

  /* --------------------------------------------------------------------------
     11. Contact Form Live Validation & Interactive Submission
     -------------------------------------------------------------------------- */
  const contactForm = document.getElementById('contact-form');
  const nameInput = document.getElementById('contact-name');
  const emailInput = document.getElementById('contact-email');
  const subjectInput = document.getElementById('contact-subject');
  const messageInput = document.getElementById('contact-message');
  const charCounter = document.getElementById('char-counter');
  const formAlert = document.getElementById('form-alert');
  const submitBtn = document.getElementById('contact-submit-btn');

  // Character counter for textarea
  if (messageInput && charCounter) {
    messageInput.addEventListener('input', () => {
      const len = messageInput.value.length;
      charCounter.textContent = `${len} / 500`;
      if (len >= 480) {
        charCounter.style.color = 'var(--accent-amber)';
      } else {
        charCounter.style.color = 'var(--text-muted)';
      }
    });
  }

  // Live input error cleanup
  [nameInput, emailInput, subjectInput, messageInput].forEach(input => {
    if (input) {
      input.addEventListener('input', () => {
        input.classList.remove('is-invalid');
        const errorEl = document.getElementById(`${input.name}-error`);
        if (errorEl) errorEl.textContent = '';
      });
    }
  });

  function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
  }

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      let isValid = true;

      // Validate Name
      if (!nameInput.value.trim() || nameInput.value.trim().length < 2) {
        nameInput.classList.add('is-invalid');
        document.getElementById('name-error').textContent = 'Please enter your name (at least 2 characters).';
        isValid = false;
      }

      // Validate Email
      if (!emailInput.value.trim() || !validateEmail(emailInput.value.trim())) {
        emailInput.classList.add('is-invalid');
        document.getElementById('email-error').textContent = 'Please provide a valid email address.';
        isValid = false;
      }

      // Validate Subject
      if (!subjectInput.value.trim() || subjectInput.value.trim().length < 3) {
        subjectInput.classList.add('is-invalid');
        document.getElementById('subject-error').textContent = 'Please enter a subject.';
        isValid = false;
      }

      // Validate Message
      if (!messageInput.value.trim() || messageInput.value.trim().length < 10) {
        messageInput.classList.add('is-invalid');
        document.getElementById('message-error').textContent = 'Message should be at least 10 characters long.';
        isValid = false;
      }

      if (!isValid) {
        showToast('Please fix the errors in the form before submitting.', 'error');
        return;
      }

      // Simulate asynchronous form submission
      const btnText = submitBtn.querySelector('.btn-text');
      const btnLoader = submitBtn.querySelector('.btn-loader');
      submitBtn.disabled = true;
      if (btnText) btnText.style.display = 'none';
      if (btnLoader) btnLoader.style.display = 'inline-flex';

      setTimeout(() => {
        submitBtn.disabled = false;
        if (btnText) btnText.style.display = 'inline-flex';
        if (btnLoader) btnLoader.style.display = 'none';

        // Show success alert
        if (formAlert) {
          formAlert.className = 'form-alert success';
          formAlert.innerHTML = `
            <i class="fa-solid fa-circle-check"></i>
            <strong>Thank you, ${nameInput.value.trim()}!</strong> Your message has been sent successfully. I will get back to you shortly at <em>${emailInput.value.trim()}</em>.
          `;
          formAlert.style.display = 'block';
        }

        showToast('Message sent successfully!', 'success');

        // Reset form
        contactForm.reset();
        if (charCounter) charCounter.textContent = '0 / 500';

        // Auto-hide alert after 8 seconds
        setTimeout(() => {
          if (formAlert) formAlert.style.display = 'none';
        }, 8000);

      }, 1200);
    });
  }

  /* --------------------------------------------------------------------------
     12. Copy Email to Clipboard
     -------------------------------------------------------------------------- */
  const copyEmailBtn = document.getElementById('copy-email-btn');
  if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', () => {
      const email = 'mitradasari232@gmail.com';
      navigator.clipboard.writeText(email).then(() => {
        const originalHtml = copyEmailBtn.innerHTML;
        copyEmailBtn.innerHTML = `<i class="fa-solid fa-check"></i> <span>Copied!</span>`;
        copyEmailBtn.style.color = 'var(--accent-emerald)';
        showToast('Email address copied to clipboard!', 'success');

        setTimeout(() => {
          copyEmailBtn.innerHTML = originalHtml;
          copyEmailBtn.style.color = '';
        }, 2500);
      }).catch(() => {
        showToast('Failed to copy. Please manually copy mitradasari232@gmail.com', 'error');
      });
    });
  }

  /* --------------------------------------------------------------------------
     13. Back to Top Smooth Scroll
     -------------------------------------------------------------------------- */
  const backToTopBtn = document.getElementById('back-to-top');
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  /* --------------------------------------------------------------------------
     14. Toast Notification Utility
     -------------------------------------------------------------------------- */
  function showToast(message, type = 'info') {
    const toastContainer = document.getElementById('toast-container');
    if (!toastContainer) return;

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;

    let iconHtml = '<i class="fa-solid fa-info-circle toast-icon"></i>';
    if (type === 'success') iconHtml = '<i class="fa-solid fa-circle-check toast-icon"></i>';
    if (type === 'error') iconHtml = '<i class="fa-solid fa-triangle-exclamation toast-icon"></i>';

    toast.innerHTML = `
      ${iconHtml}
      <div class="toast-message">${message}</div>
    `;

    toastContainer.appendChild(toast);

    // Trigger animation
    setTimeout(() => toast.classList.add('show'), 10);

    // Remove after 3.5 seconds
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  }

  // Smooth scroll offset adjustment for all anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        const headerOffset = 70;
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  console.log('Portfolio initialized successfully for Mitra Dasari (Course: IT4048).');
});
