"""
morse is a small library providing utility functions converting between
text to morse, and vice versa.
"""

DEFAULT_SHORT_CHAR = "."
DEFAULT_LONG_CHAR = "-"

morse_map = \
{ \
"A":".-", "B":"-...", "C":"-.-.", \
"D":"-..", "E":".", "F":"..-.", \
"G":"--.", "H":"....", "I":"..", \
"J":".---", "K":"-.-", "L":".-..", \
"M":"--", "N":"-.", "O":"---", \
"P":".--.", "Q":"--.-", "R":".-.", \
"S":"...", "T":"-", "U":"..-", \
"V":"...-", "W":".--", "X":"-..-", \
"Y":"-.--", "Z":"--..", "0":"-----", \
"1":".----", "2":"..---", "3":"...--", \
"4":"....-", "5":".....", "6":"-....", \
"7":"--...", "8":"---..", "9":"----." \
}

reversed_morse_map = { value:key for key,value in morse_map.items() }

def reformat(string,newcharset,charset=(DEFAULT_SHORT_CHAR,DEFAULT_LONG_CHAR)):
    """
    reformats the string, replacing old charset with new charset
    charset format is (short_char,long_char)
    """
    if newcharset[0] == newcharset[1]:
        raise ValueError("short character and long character must be distinct.")

    return string.replace(charset[0],newcharset[0]).replace(charset[1],newcharset[1])

def encode(string, seperator = " "):
    "returns the string converted into morse code, US format, with default charset"
    return seperator.join([morse_map.get(i) for i in string.upper()])

def decode(morse, charset = None, seperator = " "):
    "converts morse(with or without charset) into string"
    if charset != None:
        morse = morse.reformat((DEFAULT_SHORT_CHAR,DEFAULT_LONG_CHAR),charset)

    return "".join([reversed_morse_map.get(i) for i in morse.split(seperator)])
