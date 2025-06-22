import json
import random

# Load KB and model answers
with open("kb.json") as f:
    kb = json.load(f)

with open("model_answers.json") as f:
    answers = json.load(f)

# Create helper KB dict
kb_dict = {item["question"]: item["answer"] for item in kb}

log_lines = []

# Retry function (simulates a better model retrying)
def retry_answer(question):
    # Simulate getting it right on retry if in KB
    if question in kb_dict:
        return kb_dict[question]
    # For OOD (out-of-domain), return a new guess (simulate improvement)
    return "Improved guess"

# Validate each answer
for item in answers:
    q = item["question"]
    a = item["model_answer"]
    retry_flag = False

    if q in kb_dict:
        if a.strip().lower() != kb_dict[q].strip().lower():
            result = "RETRY: answer differs from KB"
            retry_flag = True
        else:
            result = "OK"
    else:
        result = "RETRY: out-of-domain"
        retry_flag = True

    log_lines.append(f"Q: {q}\nA: {a}\nResult: {result}")

    if retry_flag:
        retry_a = retry_answer(q)
        log_lines.append(f"RETRYING...\nRetry Answer: {retry_a}")
        if q in kb_dict:
            if retry_a.strip().lower() == kb_dict[q].strip().lower():
                log_lines.append("Retry Result: OK")
            else:
                log_lines.append("Retry Result: FAIL")
        else:
            log_lines.append("Retry Result: OUT-OF-DOMAIN")

    log_lines.append("-" * 50)

# Write log file
with open("run.log", "w") as f:
    f.write("\n".join(log_lines))

print("✅ Validation complete. See run.log")
