import sys

#mapping of letters, spaces, and numbers to braille
brailleMap = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", "1": "O.....", "2": "O.O...", "3": "OO....", 
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", 
    "9": ".OO...", "0": ".OOO..",
}

#convert braille to english
inverseBrailleMap = {}
for k, v in brailleMap.items():
    inverseBrailleMap[v] = k

#double check everythings in braille
def isBraille(input_string):
    return all(char in "O." for char in input_string)

#convert english to braille
def englishToBraille(text):
    braille = ""
    for char in text:
        if char.isupper():
            braille += ".....O"  
            braille += brailleMap[char.lower()]
        elif char.isdigit():
            braille += ".O.OOO"  
            braille += brailleMap[char]
        else:
            braille += brailleMap.get(char, "......")
    return braille

#convert braille to english
def brailleToEnglish(brailleText):
    english = ""
    isCapital = False
    isNumber = False
    brailleChars = []

#split braille into 6 chunk charactes
    for i in range(0, len(brailleText), 6):
        brailleChars.append(brailleText[i:i+6])

    
    for symbol in brailleChars:
        if symbol == ".....O":
            isCapital = True
        elif symbol == ".O.OOO":
            isNumber = True
        else:
            if isCapital:
                english += inverseBrailleMap[symbol].upper()
                isCapital = False
            elif isNumber:
                english += inverseBrailleMap[symbol]
                isNumber = False
            else:
                english += inverseBrailleMap[symbol]
    return english

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <string_to_translate>")
        sys.exit(1)
    
    input_string = sys.argv[1]
    
    if isBraille(input_string):
        result = brailleToEnglish(input_string)
    else:
        result = englishToBraille(input_string)
    
    print(result)

if __name__ == "__main__":
    main()
