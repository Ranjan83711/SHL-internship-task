import streamlit as st

from preprocessing.text_builder import build_documents
from preprocessing.chunker import chunk_documents
from retrieval.retriever import retrieve_chunks
from retrieval.ranker import rank_results
from utils.parser import parse_assessment_text


# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Assessment Recommendation Engine",
    layout="centered"
)


# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("🧠 Assessment Recommender")
st.caption("AI-powered semantic recommendations based on job descriptions")


# -------------------------------------------------
# Input Section
# -------------------------------------------------
query = st.text_area(
    "Job Description / Skills",
    placeholder="e.g. Data Analyst with strong numerical, analytical, and problem-solving skills"
)

top_k = st.slider(
    "Number of recommendations",
    min_value=3,
    max_value=10,
    value=5
)


# -------------------------------------------------
# Recommendation Pipeline
# -------------------------------------------------
if st.button("Recommend"):
    if not query.strip():
        st.warning("Please enter a job description or skills.")
    else:
        with st.spinner("Finding the most relevant assessments..."):
            documents = build_documents()
            chunks = chunk_documents(documents)

            results = retrieve_chunks(query, chunks, top_k=top_k)
            ranked_results = rank_results(results)

        st.subheader("✅ Recommended Assessments")

        for result in ranked_results:
            parsed = parse_assessment_text(result)
            if not parsed:
                continue

            with st.container():
                st.markdown(f"### ✅ {parsed['name']}")
                st.markdown(f"**Type:** {parsed['type']}")
                st.markdown(f"**Skills Measured:** {parsed['skills']}")
                st.markdown(f"**Job Roles:** {parsed['roles']}")
                st.markdown(f"**Duration:** {parsed['duration']} minutes")
                st.markdown(f"**Description:** {parsed['description']}")
                st.divider()
