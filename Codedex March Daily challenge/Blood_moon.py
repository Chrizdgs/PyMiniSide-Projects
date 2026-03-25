"""
In The Legend of Zelda: Breath of the Wild, a Blood Moon occurs every 2 hours and 48 minutes. The fallen enemies respawn and the moon casts an eerie glow over the world.
You are given a timestamp in the format "HH:MM" (24-hour time). Your task is to predict the next 3 times the blood moon will occur.

Example 1

Input: "01:00"
Output: ["03:48", "06:36", "09:24"]
Each of these are 2 hours and 48 minutes apart.
"""

def next_blood_moons(time):
    # Convert input time to total minutes
    hours, minutes = map(int, time.split(":"))
    total_minutes = hours * 60 + minutes
    
    result = []
    
    for _ in range(3):
        total_minutes = (total_minutes + 168) % 1440  # 168 = 2h 48m
        
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        
        result.append(f"{new_hours:02d}:{new_minutes:02d}")
    
    return result