from flask import Flask, render_template, request
from openai import OpenAI
from PyPDF2 import PdfReader
import os

app = Flask(__name__)

# Initialize OpenAI client using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.route("/", methods=["GET", "POST"])
def home():
    error = None

    if request.method == "POST":
        # Get inputs
        resume_text = request.form.get("resume_text", "").strip()
        resume_file = request.files.get("resume_file")
        job_text = request.form.get("job", "").strip()

        # ---------------- VALIDATION ----------------
        if not job_text:
            error = "Job description is required."

        if not resume_text and not resume_file:
            error = "Please paste your resume text or upload a resume file."

        if error:
            return render_template("index.html", error=error)

        # ---------------- READ RESUME FILE IF NEEDED ----------------
        if not resume_text and resume_file:
            try:
                if resume_file.filename.lower().endswith(".txt"):
                    resume_text = resume_file.read().decode("utf-8")

                elif resume_file.filename.lower().endswith(".pdf"):
                    reader = PdfReader(resume_file)
                    resume_text = ""
                    for page in reader.pages:
                        resume_text += page.extract_text() or ""

                else:
                    error = "Unsupported file type. Please upload a .txt or .pdf file."
                    return render_template("index.html", error=error)

            except Exception:
                error = "Unable to read the resume file. Please try another file."
                return render_template("index.html", error=error)

        # ---------------- AI PROMPT (SHORT & CONTROLLED) ----------------
        prompt = f"""
You are an AI resume analyzer.

Compare the resume and job description.

Provide:
- Match score (percentage)
- Top 5 matching skills
- Top 5 missing skills
- 2 short improvement suggestions

Rules:
- Use bullet points only
- Keep the response under 120 words
- Do not add explanations

Resume:
{resume_text}

Job Description:
{job_text}
"""

        # ---------------- AI CALL ----------------
        try:
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )
            analysis = response.output_text

        except Exception:
            error = "AI service is temporarily unavailable. Please try again later."
            return render_template("index.html", error=error)

        # ---------------- SUCCESS ----------------
        return render_template("result.html", analysis=analysis)

    # GET request
    return render_template("index.html")


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

