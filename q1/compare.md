# Tokenisation Comparison

## Sentence:
`The cat sat on the mat because it was tired.`

### BPE (GPT-2):
- Tokens: ['The', 'Ġcat', 'Ġsat', 'Ġon', 'Ġthe', 'Ġmat', 'Ġbecause', 'Ġit', 'Ġwas', 'Ġtired', '.']
- Token Count: 11

### WordPiece (BERT):
- Tokens: ['the', 'cat', 'sat', 'on', 'the', 'mat', 'because', 'it', 'was', 'tired', '.']
- Token Count: 11

### SentencePiece (Unigram):
- Tokens: ['▁The', '▁cat', '▁sat', '▁on', '▁the', '▁mat', '▁because', '▁it', '▁was', '▁tired', '.']
- Token Count: 11

## Explanation

Different tokenization methods split words based on different rules.  
- **BPE** (Byte Pair Encoding) merges frequent character pairs and uses special spacing characters like `Ġ`.  
- **WordPiece**, used in BERT, breaks words into subwords for handling rare or unseen terms.  
- **SentencePiece** (Unigram model) adds boundaries like `▁` and is trained on raw text (no whitespace needed).  

Though all three produced the same token count here, their internal token splits differ, especially for whitespace and subword boundaries.
