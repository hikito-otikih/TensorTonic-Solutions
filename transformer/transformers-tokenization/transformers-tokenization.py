import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        special_tokens = [self.pad_token, self.unk_token, self.bos_token, self.eos_token]
    
        unique_words = set()
        for text in texts:
            for word in text.split(): 
                unique_words.add(word.lower())
            
        vocab = special_tokens + sorted(list(unique_words - set(special_tokens)))

        self.word_to_id = {word: i for i, word in enumerate(vocab)}
        self.id_to_word = {i: word for i, word in enumerate(vocab)}
        self.vocab_size = len(vocab)
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        enc = []
        for st in text.split() :
            if not (st.lower() in self.word_to_id) :
                enc.append(self.word_to_id[self.unk_token])
            else :
                enc.append(self.word_to_id[st.lower()])
        return enc
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        words = [self.id_to_word.get(token_id, self.unk_token) for token_id in ids]
        return " ".join(words)
