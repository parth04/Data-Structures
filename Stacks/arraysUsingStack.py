
"""
iven an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.

 

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]

"""




class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_len = len(target)
        output = []
        temp = []
        for i in range(target[target_len-1],-1,-1):
            temp.append(i+1)

        while len(temp)-1!=0:
            if temp.pop() not in target:
                output.append("Push")
                output.append("Pop")
            else:
                output.append("Push")
                
        return output
                
            
            
    
            

"""
Explanation:
1) Take temporary list where length will be equal to the last element of target array and elements would be sequential numbers upto last target element.
2) Store it in a reverse manner(This is the catch) because we are gonna pop the element.
3) Check every popped element from temp with target and correspondingly append the output list.

"""
    
      
            
      
