"""
In today's Daily Challenge, your task is to recreate that demo! 📻🎶🎵

The Altair had no keyboard or screen. Programs were entered using toggle switches. To enter a value into memory, you flipped switches up (1) or down (0). For example, 0100000101 is a binary number representing 261, the frequency of a C note.

Given a list/array of text strings representing the front-panel switches on the Altair, convert them from binary numbers to decimal numbers, and return the corresponding music notes.

So "0100000101" to 261 to "C4".

Frequency (Hz)	Note
261	"C4"
294	"D4"
329	"E4"
349	"F4"
392	"G4"
440	"A4"
494	"B4"
523	"C5"
0	"REST"

Example 1

Input: ["0100000101", "0100000101", "0110001000", "0110001000", "0110111000", "0110111000", "0110001000", "0000000000"]
Output: ["C4", "C4", "G4", "G4", "A4", "A4", "G4", "REST"]
"""

def altair_music(switches):
    freq_to_note = {
        261: "C4",
        294: "D4",
        329: "E4",
        349: "F4",
        392: "G4",
        440: "A4",
        494: "B4",
        523: "C5",
        0: "REST"
    }
    
    result = []
    
    for binary in switches:
        decimal = int(binary, 2)   # convert binary → decimal
        note = freq_to_note.get(decimal)
        result.append(note)
    
    return result