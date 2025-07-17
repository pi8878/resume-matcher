import streamlit as st
import spacy

# Set Streamlit page config
st.set_page_config(page_title="Resume Keyword Matcher", layout="centered")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# ---------- Keyword Extraction ----------
def extract_keywords(text):
    """
    Extracts lowercase nouns and proper nouns from text using spaCy.
    """
    doc = nlp(text)
    keywords = set()
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop:
            keywords.add(token.lemma_.lower())
    return sorted(keywords)

# ---------- Keyword Comparison ----------
def compare_keywords(resume_kw, jd_kw):
    """
    Compares resume and job description keyword lists.
    Returns matched and missing keywords.
    """
    resume_set = set(resume_kw)
    jd_set = set(jd_kw)
    matched = sorted(resume_set & jd_set)
    missing = sorted(jd_set - resume_set)
    return matched, missing

# ---------- Match Score ----------
def calculate_match_score(matched, total_required):
    """
    Calculates a match percentage based on job description keywords.
    """
    if total_required == 0:
        return 0.0
    return round((len(matched) / total_required) * 100, 2)

# ---------- Display Tags ----------
def render_keywords_as_tags(keywords, color):
    for kw in keywords:
        st.markdown(
            f"<span style='background-color:{color}; "
            f"padding:5px 10px; margin:3px; border-radius:15px; "
            f"display:inline-block; color:white;'>{kw}</span>",
            unsafe_allow_html=True
        )

# ---------- UI ----------
st.title("📄 Resume Keyword Matcher")
st.markdown("Upload your **resume** (TXT) and paste your **job description** below:")

resume_file = st.file_uploader("Upload your resume (.txt)", type=["txt"])
job_description = st.text_area("Paste the job description here")

if resume_file is not None:
    resume_text = resume_file.read().decode("utf-8")
    st.subheader("📄 Resume Preview")
    st.text(resume_text)
else:
    resume_text = ""

if job_description:
    st.subheader("📝 Job Description Preview")
    st.text(job_description)

if resume_text and job_description:
    st.success("Inputs received! Processing… ✅")

    # Extract & compare
    resume_keywords = extract_keywords(resume_text)
    jd_keywords     = extract_keywords(job_description)
    matched, missing = compare_keywords(resume_keywords, jd_keywords)

    # Score
    score = calculate_match_score(matched, len(jd_keywords))
    st.subheader(f"📊 Resume Match Score: {score}%")
    if score >= 80:
        st.success("✅ Strong match!")
    elif score >= 50:
        st.warning("⚠️ Moderate match.")
    else:
        st.error("❌ Low match.")

    # Two‑column layout for tags
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matched Keywords")
        if matched:
            render_keywords_as_tags(matched, "#28a745")
        else:
            st.warning("None")

    with col2:
        st.subheader("❌ Missing Keywords")
        if missing:
            render_keywords_as_tags(missing, "#dc3545")
        else:
            st.info("None")
