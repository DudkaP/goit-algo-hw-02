def check_delimiters(expr: str) -> str:
    stack = []
    
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    opening = set(pairs.values())
    closing = set(pairs.keys())
    
    for char in expr:
        if char in opening:
            stack.append(char)
        
        elif char in closing:
            if not stack:
                return "Несиметрично"
            if stack.pop() != pairs[char]:
                return "Несиметрично"

    if stack:
        return "Несиметрично"
    return "Симетрично"


examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for ex in examples:
    print(f"{ex}: {check_delimiters(ex)}")
