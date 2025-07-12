import streamlit as st
import tempfile
import os
import sys
from pathlib import Path
from PyPDF2 import PdfReader
from contract.crew import ContractReviewTeam

# Allow import from local contract directory
sys.path.append(str(Path(__file__).resolve().parent / "contract"))

def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Page setup
st.set_page_config(page_title="Contract Review Team", layout="wide")
st.title("📄 AI-Powered Contract Review")
st.markdown("""
Upload your contract and let our multi-agent AI team review it from legal, financial, and negotiation perspectives. 

The output includes:
- 📌 Highlighted issues and missing clauses
- 💡 Suggestions for improvement
- ⚠️ Risk severity tagging
- ✍️ Clause drafting tips (coming soon)
""")

# File uploader
uploaded_file = st.file_uploader("📎 Upload a contract (PDF or TXT)", type=["pdf", "txt"])

contract_text = ""

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        contract_text = extract_text_from_pdf(tmp_path)
        os.unlink(tmp_path)

    elif uploaded_file.type == "text/plain":
        contract_text = uploaded_file.read().decode("utf-8")

    if contract_text:
        with st.expander("📄 Contract Preview", expanded=False):
            st.text_area("Raw Text", value=contract_text, height=300)

        if st.button("🚀 Run Contract Review"):
            with st.spinner("Running the AI review agents..."):
                try:
                    crew = ContractReviewTeam()
                    result = crew.crew().kickoff(inputs={"input": contract_text})

                    # Display result with formatting and feedback tools
                    st.subheader("✅ Contract Review Output")
                    review_lines = result.raw.strip().split("\n")

                    for line in review_lines:
                        line = line.strip()
                        if line.startswith("- ") or line.startswith("• "):
                            st.markdown(f"🟡 {line}")
                        elif line.lower().startswith("without") or "liability" in line.lower():
                            st.markdown(f"🔴 {line}")
                        elif "recommend" in line.lower():
                            st.markdown(f"🟢 {line}")
                        else:
                            st.markdown(line)

                    st.success("✅ Review Complete")
                    st.download_button("📥 Download Full Review", result.raw, file_name="contract_review.txt")

                except Exception as e:
                    st.error(f"❌ An error occurred: {e}")
else:
    st.info("📂 Please upload a PDF or TXT file to begin.")
