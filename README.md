
# 📄 AI-Powered Contract Review App

This is a **Streamlit-based web app** that allows users to upload contract files (PDF or TXT) and receive a detailed AI-generated review using a multi-agent CrewAI system. The system provides feedback on legal clarity, financial risk, and negotiation readiness.

---

## 🚀 Features

- ✅ Review contracts using AI agents for legal, financial, and negotiation insights
- 📌 Flag missing or ambiguous clauses (e.g., indemnity, confidentiality, force majeure)
- 💡 Recommend specific improvements and additions
- ⚠️ Tag risks by severity (🔴 High, 🟡 Medium, 🟢 Low/Suggestion)
- 📄 Preview raw contract text
- 📥 Download full review report

---

## 📁 Project Structure

```
project/
├── app.py                       # Main Streamlit app
├── contract/
│   ├── crew.py                 # CrewAI setup (agents + tasks)
│   ├── __init__.py
├── config/
│   ├── agents.yaml             # Agent definitions
│   └── tasks.yaml              # Task instructions
├── requirements.txt or pyproject.toml
```

---

## 🛠️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/contract-review-app.git
cd contract-review-app
```

2. **Set up virtual environment**:
```bash
uv venv .venv
source .venv/bin/activate
```

3. **Install dependencies**:
```bash
uv pip install streamlit crewai langchain-openai PyPDF2
```

> Or use `pip install -r requirements.txt` if provided.

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Navigate to [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📂 Example Contract
To test the system, upload any `.txt` or `.pdf` contract document. A sample file is available in the repo or you can generate one using:

```bash
python generate_sample_contract.py
```

---

## ✨ Future Enhancements
- Drafting clause suggestions
- Tabbed view for agent-specific outputs
- Export report as PDF or Markdown
- Clause extraction & section-by-section feedback

---

## 🤖 Built With
- [Streamlit](https://streamlit.io/) - Web UI
- [CrewAI](https://docs.crewai.com/) - Multi-agent framework
- [LangChain](https://www.langchain.com/) - LLM Orchestration
- [OpenAI GPT](https://openai.com/) - Natural Language Understanding

---

## 📬 Contact
For feature requests or contributions, please open an issue or PR.
