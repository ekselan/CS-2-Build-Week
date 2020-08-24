# Day I Notes


## ***Describing Your Code in an Interview***

Pretend you already have the job and the interviewer is a coworker who came to you
for help on a difficult problem.
* If you already had the job, there's no stress
* Reframes the situation from an interview to just problem-solving
* Puts you in a cooperative mindset
* It forces you to *teach* the problem and solution

---

## ***UPER is the key to it all***

### **Understand**
* Ask questions about the problem
* Dialog
* Rephrase the problem back to the interviewer in your own words
* Teaching the "what" of the problem to the interviewer

### **Plan**
* Come up with multiple plans, if possible
* Don't ignore the naive plan
* Teach the plan to the interviewer
* Think in big concepts, not code

### **Execute**
* If you're describing existing code:
  * Interviewer will look for where the concepts match the blocks of code
  * Point out interesting things in it
  * Make sure it's well commented and looks good
* If you're writing new code:
  * Interviewer will look for where the concepts match the blocks of code
  * Actually code it up at this point

### **Reflect**
* What could we have done better?
* Future directions and features
* If you made any mistakes, point them out with solutions.



---



# LeetCode Palindromes Challenge

Link to challenge prompt: https://leetcode.com/problems/valid-palindrome/ 

```py
#from re import sub
​
class Solution:
    #def isPalindrome(self, s: str) -> bool:
    def isPalindrome(self, s):
        s = "".join(c for c in s if c.isalnum()).lower()
        
        def ispal(s):
            if len(s) < 2:
                return True
​
            return s[0] == s[-1] and ispal(s[1:-1])
        
        return ispal(s)
​
        """
        s = sub(r'[\W_]', '', s).lower() 
        return s == s[::-1]
        """
        
        """
        s = "".join(c for c in s if c.isalnum()).lower()
        
        i0 = 0
        i1 = len(s) - 1 
        
        while i1 > i0:
            if s[i0] != s[i1]:
                return False
            
            i0 += 1
            i1 -= 1
            
        return True
        """
        
        """
        if s == "":
            return True
        
        i0 = 0
        i1 = len(s) - 1 
        
        while i1 > i0:
            if not s[i0].isalnum():
                i0 += 1
                continue
                
            if not s[i1].isalnum():
                i1 -= 1
                continue
                
            if s[i0].lower() != s[i1].lower():
                return False
            
            i0 += 1
            i1 -= 1
            
        return True
        """
```