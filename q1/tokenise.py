from transformers import AutoTokenizer
from transformers import pipeline
import json

# Sentence to tokenize
sentence = "The cat sat on the mat because it was tired."

# List of tokenizer models (all open-source)
tokenizer_models = {
    "BPE": "gpt2",  # Uses BPE
    "WordPiece": "bert-base-uncased",  # Uses WordPiece
    "SentencePiece": "google/pegasus-xsum"  # Uses SentencePiece
}

results = {}

for name, model_name in tokenizer_models.items():
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer.tokenize(sentence)
    ids = tokenizer.convert_tokens_to_ids(tokens)

    results[name] = {
        "tokens": tokens,
        "token_ids": ids,
        "token_count": len(tokens)
    }

# Print results (optional)
for model, data in results.items():
    print(f"\n--- {model} ---")
    print("Tokens:", data["tokens"])
    print("IDs:", data["token_ids"])
    print("Count:", data["token_count"])


# Load fill-mask pipeline using a masked language model
fill = pipeline("fill-mask", model="bert-base-uncased")

# Use proper [MASK] tokens for BERT
masked_sentence = "The cat sat on the [MASK] because it was [MASK]."

# Predict
predictions = fill(masked_sentence, top_k=3)

# Print results
for i, prediction in enumerate(predictions):
    print(f"\nTop predictions for mask {i + 1}:")
    for option in prediction:
        print(f" - {option['token_str']} (Score: {option['score']:.4f})")

# Save to file
with open("predictions.json", "w") as f:
    json.dump(predictions, f, indent=2)
