# 📄 Resume Keyword Matcher (NLP with Streamlit)

This app helps job seekers compare their resumes to job descriptions using **Natural Language Processing (NLP)**. It identifies **matched** and **missing keywords**, calculates a **match score**, and visually displays the results — making it easier to tailor your resume to specific roles.
---
## 🚀 Features

- ✅ Upload a **TXT file** of your resume
- ✅ Paste a **job description**
- ✅ Extract **keywords** using spaCy (NLP)
- ✅ See **matched vs. missing** keywords
- ✅ Display **match score** (%)
- ✅ View results in a clean, horizontal layout

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-keyword-matcher.git
cd resume-keyword-matcher
Download the spaCy English Language Model
python -m spacy download en_core_web_sm
pip install streamlit
pip install spacy
Run the App
streamlit run app.py
```

⚙️ How It Works
Upload Resume: Accepts plain .txt format.

Paste Job Description: Paste the job posting or requirements.

NLP Processing: Uses spaCy to extract relevant nouns/proper nouns as keywords.

Matching & Scoring: Compares the resume to the job description and calculates a match percentage.

Output: Clearly shows:

✅ Matched Keywords

❌ Missing Keywords

📊 Match Score

💡 Why Use This?
Many companies use Applicant Tracking Systems (ATS) to scan resumes. This app helps you optimize your resume so you pass through initial filters and stand out to hiring managers.

🛠️ Roadmap
 Add support for PDF/DOCX files

 Keyword importance weighting

 Export results to PDF/CSV

 AI-powered resume rewrite suggestions







