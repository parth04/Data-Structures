"""


"""

class Solution:
    def decodeString(self, s: str) -> str:
        n = []
        char = []
        digit = ""
        for i in s:
            if i.isnumeric():
                digit = digit + i
                continue
            if i.isalpha():
                char.append(i)
                continue
            if i == "[":
                n.append(int(digit))
                digit = ""
                char.append(i)
                continue
            if i == "]":
                temp = ''
                while True:
                    c = char.pop()
                    if c != '[':
                        temp =  c + temp
                    else:
                        break
                char.append(n.pop() * temp)

        return "".join(char)


"""
Explanation:
1)Catch here is when 2 digit or 3 digit integer occurse then how you gonna append complete integer in int stack. So solution to this is, first append the digit  
to temporary variable until opening bracket doesn't appear. 
2)When opening bracket appears append the integer stored in temporary variable to integer stack and again initialize temp var to empty string.
3)Also order of string appending in char stack.
  temp = c + temp and temp = temp + c makes a huge difference.
"""
