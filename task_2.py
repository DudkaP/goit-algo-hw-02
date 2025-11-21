from collections import deque
import string

def is_palindrome(text: str) -> bool:
    text = text.lower()
    
    cleaned_text = "".join(ch for ch in text if ch.isalnum())
    
    dq = deque(cleaned_text)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("Never odd or even"))
print(is_palindrome("Python"))
print(is_palindrome("Я несу гусеня"))
