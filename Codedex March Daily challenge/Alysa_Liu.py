"""
For this Daily Challenge, let's focus on the first one...

🎯 Technical Element Score (TES)

Each skating element (jump, spin, or step sequence) has a base value.
Nine judges assign a Grade of Execution (GOE) for each element (-5 to 5).
To reduce bias, the highest and lowest GOE are dropped.
The remaining 7 are averaged.
The element score is calculated as:

Element Score = Base Value + (Average GOE X 0.1 X Base Value)
The TES is the sum of all element scores.

Given these rules, complete the function to calculate the TES (round it to one decimal place).

Input: elements
elements = [
  ("Triple Flip",            9.7,  [3, 2, 3, 3, 2, 4, 3, 2, 3]),
  ("Triple Lutz+Toe Combo", 12.5,  [4, 5, 4, 5, 5, 4, 4, 3, 4]),
  ("Triple Salchow",         7.0,  [2, 3, 2, 2, 3, 2, 2, 3, 2]),
  ("Triple Loop",            6.0,  [3, 3, 2, 4, 3, 3, 2, 3, 2]),
  ("Step Sequence",          3.3,  [4, 4, 4, 4, 3, 3, 4, 3, 4])
]
Output: 50.9
"""

def calculate_tes(elements):
    total = 0
    
    for name, base, goes in elements:
        sorted_goes = sorted(goes)
        
        # Remove lowest and highest
        trimmed = sorted_goes[1:-1]
        
        avg_goe = sum(trimmed) / len(trimmed)
        
        element_score = base + (avg_goe * 0.1 * base)
        
        total += element_score
    
    return round(total, 1)