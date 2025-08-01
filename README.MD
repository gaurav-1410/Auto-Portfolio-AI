<h1 align="center">AutoPortfolio-AI 🚀</h1>

<div align="center">
    <a href="https://github.com/gaurav-1410/Auto-Portfolio-AI">
        <img src="https://img.shields.io/github/stars/gaurav-1410/Auto-Portfolio-AI?style=for-the-badge" alt="Stars"/>
    </a>
    <a href="https://github.com/gaurav-1410/Auto-Portfolio-AI/network/members">
        <img src="https://img.shields.io/github/forks/gaurav-1410/Auto-Portfolio-AI?style=for-the-badge" alt="Forks"/>
    </a>
    <a href="https://github.com/gaurav-1410/Auto-Portfolio-AI/issues">
        <img src="https://img.shields.io/github/issues/gaurav-1410/Auto-Portfolio-AI?style=for-the-badge" alt="Issues"/>
    </a>
    <a href="https://github.com/gaurav-1410/Auto-Portfolio-AI/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/gaurav-1410/Auto-Portfolio-AI?style=for-the-badge" alt="License"/>
    </a>
</div>

<div align="center">
    <i>
        A Flask web app to parse PDF resumes, match skills to job descriptions, analyze skill gaps, and generate LLM-powered AI cover letters with project suggestions.
    </i>
    <br>
    <br>
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white"/>
    <img src="https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white&style=flat"/>
    <img src="https://img.shields.io/badge/LLM-LLaMA--3-blueviolet"/>
    <img src="https://img.shields.io/badge/OpenRouter-API-green"/>
</div>

---

## 🗂️ Table of Contents
- [Features](#features-)
- [Getting Started](#getting-started)
- [Docker](#docker)
- [Usage](#usage-)
- [Tech Stack](#tech-stack-)
- [Roadmap](#roadmap-)
- [Contributing](#contributing-)
- [License](#license-)
- [Acknowledgements](#acknowledgements-)

---

## Features ✨

- **PDF Resume Parsing:** Extract skills from uploaded resumes in PDF format.
- **AI-Powered Job Matching:** Match user skills against job descriptions with LLaMA 3 via OpenRouter.
- **Skill Gap Analysis:** Identify and highlight missing skills for your targeted role.
- **Cover Letter Generation:** Instantly generate tailored cover letters using AI.
- **Project Suggestions:** Receive project ideas to bridge your skill gaps.
- **Smooth Multi-Step Forms** and session handling.

## Getting Started

```bash
git clone https://github.com/gaurav-1410/Auto-Portfolio-AI.git
cd Auto-Portfolio-AI
pip install -r requirements.txt
python app.py
```

> Go to `http://localhost:5000` in your browser.

---

## Docker 

You can also run AutoPortfolio-AI using Docker:

### Pull from Docker Hub

```bash
docker pull gp1410/autoportfolio_ai
```

### Run the container

```bash
docker run -p 8888:5000 gp1410/autoportfolio_ai
```
Visit `http://localhost:8888` in your browser.

### Or Build Locally

```bash
docker build -t autoportfolio_ai .
docker run -p 8888:5000 autoportfolio_ai
```

View the image on [Docker Hub](https://hub.docker.com/r/gp1410/autoportfolio_ai).

## Usage 👨‍💻

1. **Upload your PDF resume.**
2. **Paste the target job description.**
3. **Review matched skills, gaps, and suggested projects.**
4. **Download your tailored, AI-generated cover letter.**

---

## Tech Stack 🧰

- **Flask** - Web framework
- **pdfplumber** - PDF parsing
- **LLaMA 3 via OpenRouter** - LLM-based intelligence
- **Python-dotenv** - Configuration
- **Requests, Werkzeug** - Utilities
- **Docker** - Containerization

---

## Roadmap 🗺️

- Add persistent user sessions
- Expand project suggestion logic
- Enhance PDF processing accuracy
- Frontend UI/UX improvements

---

## Contributing 🤝

Contributions are welcome!  
- Open an issue or submit a pull request for enhancements and bug fixes.

---

## License 🏷️

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements 🙏

- Thanks to LLaMA 3 and the OpenRouter ecosystem.

---

> _If you like this project, please leave a ⭐!_
