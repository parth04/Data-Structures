"""
8. String to Integer (atoi)
Medium

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, 231 − 1 or −231 is returned.
 

Example 1:

Input: str = "42"
Output: 42
Example 2:

Input: str = "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: str = "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: str = "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.

"""


class Solution:
    def myAtoi(self, s: str) -> int:
        # s = "".join(i for i in s if i.isnumeric() or i== '-')
        t = ''
        s = s.strip() #Removing all the leading or trailing white spaces
        # print("After striping:",s)
        
        for key, val in enumerate(s):
            #Checking if first char is alphabet. If it is directly return 0
            if key ==0 and val != "+" and val !="-" and not val.isnumeric():
                return 0
            if key > 0:
                #If we started with =ve or -ve sign in t and then comes any alphabet then directly return zero.
                if not val.isnumeric() and (t == '-' or t == '+'): 
                    return 0
                
                #Checking if there is char in between digit. e.g. "420abc520" then we want 420 only and discard rest of it. So braking the loop and coming out of it.
                if not val.isnumeric(): 
                    break
            t+="".join(val)
                
            
        
        # print(t)
        
        if not t or t=="+" or t=="-": #Checking if t is empty or only contains +ve or -ve sign
            return 0
        
        t = int(t)
        if t > 2**31 -1:
            return 2**31 -1
        elif t < -2**31:
            return -2**31
        else:
            return t


"""
Explanation:
1) I wrote the comments which are self explanatory. In such verbose problems focus on terminating conditions.  
"""
        
        
        

