class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        sentence = sentence.split()
        for word in dictionary:
            
            for i, cand in enumerate(sentence):
                if cand.startswith(word):
                    sentence[i] = word
                    
        return ' '.join(sentence)
