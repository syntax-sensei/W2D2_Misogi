import json
import random

# Load KB questions
with open("kb.json") as f:
    kb = json.load(f)

kb_questions = [item["question"] for item in kb]

# Add 5 unseen questions (outside the KB)
extra_questions = [
    "What is the square root of 144?",                         # should be 12
    "Who painted the Mona Lisa?",                              # Leonardo da Vinci
    "How many moons does Mars have?",                          # 2
    "What is the speed of light?",                             # 299,792 km/s
    "Which element has the atomic number 1?"                   # Hydrogen
]

# Combine all questions
all_questions = kb_questions + extra_questions

# Simulate model answering (some intentionally incorrect)
def simulate_model_response(question):
    # Simple logic: get real answer from KB if question is in KB
    for item in kb:
        if item["question"] == question:
            # 80% chance to be correct
            return item["answer"] if random.random() > 0.2 else "Incorrect Answer"

    # For out-of-KB questions, return either a correct or wrong guess
    mock_answers = {
        "What is the square root of 144?": ["12", "14", "Incorrect Answer"],
        "Who painted the Mona Lisa?": ["Leonardo da Vinci", "Vincent van Gogh"],
        "How many moons does Mars have?": ["2", "1"],
        "What is the speed of light?": ["299,792 km/s", "300,000 km/h"],
        "Which element has the atomic number 1?": ["Hydrogen", "Helium"]
    }

    options = mock_answers.get(question, ["Unknown"])
    return random.choice(options)

# Ask model all questions
results = []
for q in all_questions:
    a = simulate_model_response(q)
    results.append({"question": q, "model_answer": a})

# Save answers to file
with open("model_answers.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ All questions asked and saved to model_answers.json")
