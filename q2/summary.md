# Hallucination Detection Summary

## 🧠 Objective
This project implements a simple hallucination detection system for language model outputs using a fixed knowledge base (KB). The system identifies when a model gives incorrect or out-of-domain answers and attempts a retry.

---

## 📊 Results

**Total Questions Asked:** 15  
- **From Knowledge Base:** 10  
- **Out-of-Domain (Extra):** 5  

**Initial Pass (Correct First Try):** 9  
- All 9 were KB questions.

**Detected Hallucinations:** 6  
- 2 KB answers were wrong initially → retried → corrected
- 4 OOD answers were flagged as "RETRY: out-of-domain" → retried → still OOD

**Retries Attempted:** 6  
- **Retries Successful (Corrected):** 2 (both KB)
- **Retries Failed (Still OOD or wrong):** 4 (all out-of-domain)

---

## ✅ Insights

- The system correctly identifies whether a question is in the KB.
- It successfully catches hallucinated answers and retries them.
- Retry mechanism works well for in-KB errors.
- OOD detection and retry handling is functional but limited (no ground truth to compare to).

---

## 🔧 Files Submitted

- `kb.json`: Knowledge base with 10 Q&A pairs
- `ask_model.py`: Simulates model answers (some with errors)
- `validator.py`: Checks for hallucinations and retries
- `run.log`: Full log of Q&A, validations, and retries
- `summary.md`: This report

---

## 🚀 What I Learned

- How to use JSON to store structured data
- Basic data validation with Python
- Simulating model outputs and building simple AI guardrails
- Detecting hallucinations using rule-based logic
