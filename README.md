# 🤖 AI Resume Analyzer & Job Matcher

An AI-powered web application that compares a resume with a job description to identify matching skills, missing skills, and provide improvement suggestions.  
Built using **Python, Flask, and OpenAI**, with a clean modern UI and real-world input handling.

---

## 🚀 Features

- 📄 Accepts **resume as text or file upload** (`.txt`, `.pdf`)
- 🧠 Uses **AI** to compare resume and job description
- 📊 Generates:
  - Match score (percentage)
  - Matching skills
  - Missing skills
  - Improvement suggestions
- 🎨 Modern UI with **gradient design**
- ⚠️ Validation and user-friendly error handling
- 🌐 Deployed and accessible on web (mobile & desktop)

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **OpenAI API**
- **HTML & CSS**
- **PyPDF2** (for PDF reading)
- **Git & GitHub**
- **Render** (deployment)

---

## 🧠 How It Works

1. User pastes resume text **or** uploads a resume file
2. User pastes a job description
3. Flask backend processes the input
4. Resume text and job description are sent to OpenAI using a structured prompt
5. AI compares both texts and returns:
   - Match score
   - Matching skills
   - Missing skills
   - Suggestions
6. Results are displayed on a dedicated results page

---

## 📁 Project Structure

