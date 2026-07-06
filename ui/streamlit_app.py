import streamlit as st
import requests
import json
import tempfile
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.pdf_parser import extract_text

st.set_page_config(page_title="TalentMatch AI V2", layout="wide")
st.title("TalentMatch AI V2")
st.caption("AI-powered CV analysis and tailoring")

API_URL = "http://127.0.0.1:8000/api/analyze"

uploaded_file = st.file_uploader("Upload your CV", type=["pdf", "docx"], key="cv_uploader")
job_description = st.text_area("Paste the job description", height=200, key="job_description")

if st.button("Analyze", type="primary"):
    if not uploaded_file or not job_description.strip():
        st.warning("Please upload a CV and enter a job description.")
    else:
        # Sistemin geçici dosya alanına yazıyoruz, proje klasörüne değil
        suffix = os.path.splitext(uploaded_file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.getbuffer())
            temp_path = tmp.name

        cv_text = extract_text(temp_path)
        os.remove(temp_path)  # işimiz bitince temizle

        status_placeholder = st.empty()
        result_placeholder = st.container()

        payload = {"cv_text": cv_text, "job_description": job_description}

        with requests.post(API_URL, json=payload, stream=True) as response:
            for line in response.iter_lines():
                if not line:
                    continue
                decoded = line.decode("utf-8")
                if decoded.startswith("data: "):
                    event = json.loads(decoded[len("data: "):])

                    if event["event_type"] != "done":
                        status_placeholder.info(event["data"]["status"])
                    else:
                        status_placeholder.success("Analysis complete!")
                        final = event["data"]

                        with result_placeholder:
                            st.subheader(f"Match Score: {final['match_analysis']['score']}/100")

                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown("**Matched Skills**")
                                for skill in final["match_analysis"]["matched_skills"]:
                                    st.markdown(f"- {skill}")
                            with col2:
                                st.markdown("**Missing Skills**")
                                for skill in final["match_analysis"]["missing_skills"]:
                                    st.markdown(f"- {skill}")

                            st.markdown("**Reasoning**")
                            st.write(final["match_analysis"]["reason"])

                            st.markdown("---")
                            st.markdown("**Tailored Experience**")
                            for exp in final["tailored_experiences"]:
                                st.write(exp["tailored_text"])