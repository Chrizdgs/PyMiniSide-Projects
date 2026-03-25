"""
You're given the hours each team member planned to sleep vs. actually slept over a week. 🛌💤

        Sleep Debt = max(0, Planned Sleep - Actual Sleep)

    Planned Sleep: Hours someone intended to sleep
    Actual Sleep: Hours they actually got
    max(0, x): Returns the larger of 0 or x.

Complete the function and return:
    The total sleep debt for the week (including +1 Daylight Savings hour)
    The longest streak of consecutive days with sleep debt

Python: Return two numbers.

Example 1: Sonny

Input:
planned = [7.5, 8, 7.5, 8, 8.5, 8, 7.5]
actual = [5, 12, 6, 6, 9, 8, 6.5]
Output:
8.0
2
Sleep debt: 2.5 + 0 + 1.5 + 2 + 0 + 0 + 1 = 7.0 hours (+1 Daylight Savings hour)
Longest streak: 2 days (day 3 and day 4)
"""

def sleep_debt(planned, actual):
    debts = [max(0, p - a) for p, a in zip(planned, actual)]
    total = sum(debts) + 1  # Daylight Savings hour
    
    longest = curr = 0
    for d in debts:
        curr = curr + 1 if d > 0 else 0
        longest = max(longest, curr)
        
    return total, longest