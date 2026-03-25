"""
Suppose we're building a word-guessing game with a secret word and a player's guess.

Given two strings, secret and guess, which are guaranteed to be of the same length (5 letters), determine how many characters are correct and in the exact same position.

Note: You don't need to know how Wordle works to do this challenge!

Example 1

Input: secret = "CODEX", guess = "COINS"
Output: 2
This is because the characters C and O are in the same position in both strings.
"""

def count_matches(secret, guess):
    count = 0
    
    for i in range(5):  # since both strings are guaranteed to be length 5
        if secret[i] == guess[i]:
            count += 1
            
    return count