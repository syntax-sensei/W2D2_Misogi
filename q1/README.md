# NLP Assignment: Tokenisation & Fill-in-the-Blank

This project explores how different tokenisation methods break down a sentence and how a masked language model predicts missing tokens.

## Tasks Completed
- Tokenised a sentence using:
  - BPE (GPT-2)
  - WordPiece (BERT)
  - SentencePiece (Unigram)
- Replaced 2 tokens with `[MASK]` and predicted them using BERT (`bert-base-uncased`)
- Recorded and saved predictions

## Files
- `tokenise.py`: Python script for tokenisation and prediction
- `predictions.json`: JSON file containing model predictions
- `compare.md`: Comparison of tokenisation methods
- `README.md`: This description
