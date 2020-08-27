# Day III Notes

## CodeSignal Unit Assessment Results: 
https://app.codesignal.com/test-result/FdHrFzyEfEGTGmQ46?accessToken=riSN79DwWmRmwFk5H-goHrwG7aJDrrNxbjKvvG4Ezv

---

## Interview Prep notes with Lindsay Gilson
- ### Feedback from hiring managers
    - **Mistakes Noticed**
        1. Candidate not having researched company, hiring manager, etc prior to interview
        2. Not being detail oriented (typos, misspelled words, tardniess, etc)
        3. Lack of engagement (no questions, seeming disinterested)
        4. Not being able to explain "why" (why they want to work there, why they should be hired, why they're a culture fit, etc.)

---

## LeetCode - `Pascal's Triangle`
Link: https://leetcode.com/problems/pascals-triangle/

- **Iterative:**
    ```py
    class Solution:
        def generate(self, numRows: int) -> List[List[int]]:
            rows = []
            for i in range(numRows):
                # First row
                if i == 0:
                    rows.append([1])
                
                # Second row
                elif i == 1:
                    rows.append([1,1])
                    
                # General case rows
                else:
                    # Start with 1
                    new_row = [1]
                    
                    # Fill in the middle numbers
                    middle_number_count = i - 1
                    
                    for j in range(middle_number_count):
                        col_index = j + 1
                        prev_row = rows[-1]
                        value = prev_row[col_index] + prev_row[col_index - 1]
                        
                        new_row.append(value)
                        
                    # Add a one on the end
                    new_row.append(1)
                    
                    rows.append(new_row)
                
            return rows
    ```
- **Recursive:**
    ```py
    class Solution:
        def generate(self, numRows: int) -> List[List[int]]:
            rows = []
            
            cache = {}
            
            def get_row(n):
                
                if n <= 1:
                    return [1] * (n+1)
                
                if n not in cache:
                    prev_row = get_row(n-1)
    ​
                    # Start with 1
                    new_row = [1]
    ​
                    # Fill in the middle numbers
                    middle_number_count = n - 1
    ​
                    for j in range(middle_number_count):
                        col_index = j + 1
                        value = prev_row[col_index] + prev_row[col_index - 1]
    ​
                        new_row.append(value)
    ​
                    new_row.append(1)
                    
                    cache[n] = new_row
                
                return cache[n]
                
            for r in range(numRows):
                rows.append(get_row(r))
                
            return rows
    ```
