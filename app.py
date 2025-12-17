import streamlit as st
import json

from preprocessing.text_builder import build_documents
from preprocessing.chunker import chunk_documents
from retrieval.retriever import retrieve_chunks
from retrieval.ranker import rank_results
from utils.parser import parse_assessment_text

from evaluation.evaluation import precision_at_k, hit_rate_at_k


# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Assessment Recommendation Engine",
    layout="centered"
)


# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.title("Mode")
mode = st.sidebar.radio(
    "Choose action",
    ["Recommend Assessments", "System Evaluation"]
)


# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("🧠 Assessment Recommender")
st.caption("AI-powered semantic recommendations based on job descriptions")


# -------------------------------------------------
# Input Section (for Recommendation Mode)
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
if mode == "Recommend Assessments":

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


# -------------------------------------------------
# System Evaluation Section
# -------------------------------------------------
if mode == "System Evaluation":

    st.header("📊 System Evaluation")
    st.caption("Evaluation using retrieval-based metrics on a curated query set")

    # Load evaluation queries
    with open("evaluation/evaluation_queries.json") as f:
        eval_data = json.load(f)

    # Build documents and chunks once
    documents = build_documents()
    chunks = chunk_documents(documents)

    k = 5
    precision_scores = []
    hit_scores = []

    for item in eval_data:
        eval_query = item["query"]
        relevant = item["relevant_assessments"]

        results = retrieve_chunks(eval_query, chunks, top_k=k)
        ranked = rank_results(results)

        retrieved = []
        for r in ranked:
            parsed = parse_assessment_text(r)
            if parsed:
                retrieved.append(parsed["name"])

        precision_scores.append(precision_at_k(retrieved, relevant, k))
        hit_scores.append(hit_rate_at_k(retrieved, relevant, k))

    avg_precision = round(sum(precision_scores) / len(precision_scores), 2)
    avg_hit_rate = round(sum(hit_scores) / len(hit_scores), 2)

    st.metric("Average Precision@5", avg_precision)
    st.metric("Hit Rate@5", avg_hit_rate)

    st.info(
        "Precision@K measures the relevance of retrieved assessments, "
        "while Hit Rate@K checks whether at least one relevant assessment "
        "appears in the top-K recommendations."
    )
