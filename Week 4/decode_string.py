class Solution:
    def decodeString(s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_str, current_num = "", 0
            elif char == ']':
                last_str, num = stack.pop()
                current_str = last_str + num * current_str
            else:
                current_str += char
        
        return current_str