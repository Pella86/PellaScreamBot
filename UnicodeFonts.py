# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:32:54 2022

@author: maurop
"""


import string


char_to_unicode = {}

char_to_unicode["a"] = "\u0250"
char_to_unicode["b"] = "q"
char_to_unicode["c"] = "\u0254"
char_to_unicode["d"] = "p"
char_to_unicode["e"] = "\u01DD"
char_to_unicode["f"] = "\u025F"
char_to_unicode["g"] = "\u0183"
char_to_unicode["h"] = "\u0265"
char_to_unicode["i"] = "\u1D09"
char_to_unicode["j"] = "\u027E"
char_to_unicode["k"] = "\u029E"
char_to_unicode["l"] = "l"
char_to_unicode["m"] = "\u026F"
char_to_unicode["n"] = "u"
char_to_unicode["o"] = "o"
char_to_unicode["p"] = "q"
char_to_unicode["q"] = "p"
char_to_unicode["r"] = "\u0279"
char_to_unicode["s"] = "s"
char_to_unicode["t"] = "\u0287"
char_to_unicode["u"] = "n"
char_to_unicode["v"] = "\u028C"
char_to_unicode["w"] = "\u028D"
char_to_unicode["x"] = "x"
char_to_unicode["y"] = "\u028E"
char_to_unicode["z"] = "z"
char_to_unicode["A"] = "\u2200"
char_to_unicode["B"] = "B"
char_to_unicode["C"] = "\u0186"
char_to_unicode["D"] = "D"
char_to_unicode["E"] = "\u018E"
char_to_unicode["F"] = "\u2132"
char_to_unicode["G"] = "\u200E\u05E4"
char_to_unicode["H"] = "H"
char_to_unicode["I"] = "I"
char_to_unicode["J"] = "\u017F"
char_to_unicode["K"] = "K"
char_to_unicode["L"] = "\u02E5"
char_to_unicode["M"] = "W"
char_to_unicode["N"] = "N"
char_to_unicode["O"] = "O"
char_to_unicode["P"] = "\u0500"
char_to_unicode["Q"] = "Q"
char_to_unicode["R"] = "\u1D1A"
char_to_unicode["S"] = "S"
char_to_unicode["T"] = "\u2534"
char_to_unicode["U"] = "\u2229"
char_to_unicode["V"] = "\u039B"
char_to_unicode["W"] = "M"
char_to_unicode["X"] = "X"
char_to_unicode["Y"] = "\u2144"
char_to_unicode["Z"] = "Z"
char_to_unicode["1"] = "\u0196"
char_to_unicode["2"] = "\u1105"
char_to_unicode["3"] = "\u0190"
char_to_unicode["4"] = "\u3123"
char_to_unicode["5"] = "\u03DB"
char_to_unicode["6"] = "9"
char_to_unicode["7"] = "\u3125"
char_to_unicode["8"] = "8"
char_to_unicode["9"] = "6"
char_to_unicode["0"] = "0"
char_to_unicode[","] = "'"
char_to_unicode["."] = "\u02D9"
char_to_unicode["?"] = "\u00BF"
char_to_unicode["!"] = "\u00A1"
char_to_unicode["\""] = ",,"
char_to_unicode["'"] = ","
char_to_unicode["`"] = ","
char_to_unicode["("] = ")"
char_to_unicode[")"] = "("
char_to_unicode["["] = "]"
char_to_unicode["]"] = "["
char_to_unicode["{"] = "}"
char_to_unicode["}"] = "{"
char_to_unicode["<"] = ">"
char_to_unicode[">"] = "<"
char_to_unicode["&"] = "\u214B"
char_to_unicode["_"] = "\u203E"

def upside_down(text):
    s = ""
    for l in text[::-1]:

        try:
            s += char_to_unicode[l]
        except KeyError:
            s += l
    return s


def fraktur(text):
    start = 0x1D56C
    #end = 0x1D537
    
    capitals = string.ascii_uppercase
    lowers = string.ascii_lowercase
    
    alphabet = capitals + lowers
    
    ascii_to_fraktur = {}
    
    for l in alphabet:
        ascii_to_fraktur[l] = chr(start)
        start += 1
    
    s = ""
    for l in text:
        try:
            s += ascii_to_fraktur[l]
        except KeyError:
            s += l
    
    return s

def double_struck(text):
    
    # alphabet
    start = 0x1D538
    
    capitals = string.ascii_uppercase
    lowers = string.ascii_lowercase
    alphabet = capitals + lowers
    
    
    exceptions = "CHNPQRZ"
    symbols = "\u2102\u210D\u2115\u2119\u211A\u211D\u2124"
    
    exp_sym = dict(zip(list(exceptions), list(symbols)))

    ascii_to_doublestruck = {}
    
    for l in alphabet:
        if l in exp_sym:
            ascii_to_doublestruck[l] = exp_sym[l]
        else:
            ascii_to_doublestruck[l] = chr(start)
        start += 1
    
    # digits
    start = 0x1D7D8    
    for l in string.digits:
        ascii_to_doublestruck[l] = chr(start)
        start += 1
        
    # string building
    s = ""
    for l in text:
        try:
            s += ascii_to_doublestruck[l]
        except KeyError:
            s += l
    
    return s    


def subsup_unicode_map():
    #https://stackoverflow.com/questions/17908593/how-to-find-the-unicode-of-the-subscript-alphabet
    unicode_map = {
         #           superscript     subscript
        '0'        : ('\u2070',   '\u2080'      ),
        '1'        : ('\u00B9',   '\u2081'      ),
        '2'        : ('\u00B2',   '\u2082'      ),
        '3'        : ('\u00B3',   '\u2083'      ),
        '4'        : ('\u2074',   '\u2084'      ),
        '5'        : ('\u2075',   '\u2085'      ),
        '6'        : ('\u2076',   '\u2086'      ),
        '7'        : ('\u2077',   '\u2087'      ),
        '8'        : ('\u2078',   '\u2088'      ),
        '9'        : ('\u2079',   '\u2089'      ),
        'a'        : ('\u1d43',   '\u2090'      ),
        'b'        : ('\u1d47',   '\u1D66'           ),
        'c'        : ('\u1d9c',   '\uA700'           ),
        'd'        : ('\u1d48',   '\u2094'           ),
        'e'        : ('\u1d49',   '\u2091'      ),
        'f'        : ('\u1da0',   '\u0562'           ),
        'g'        : ('\u1d4d',   '\u2089'           ),
        'h'        : ('\u02b0',   '\u2095'      ),
        'i'        : ('\u2071',   '\u1d62'      ),
        'j'        : ('\u02b2',   '\u2c7c'      ),
        'k'        : ('\u1d4f',   '\u2096'      ),
        'l'        : ('\u02e1',   '\u2097'      ),
        'm'        : ('\u1d50',   '\u2098'      ),
        'n'        : ('\u207f',   '\u2099'      ),
        'o'        : ('\u1d52',   '\u2092'      ),
        'p'        : ('\u1d56',   '\u209a'      ),
        'q'        : ('\u1D60',        '\u1D69'           ),
        'r'        : ('\u02b3',   '\u1d63'      ),
        's'        : ('\u02e2',   '\u209b'      ),
        't'        : ('\u1d57',   '\u209c'      ),
        'u'        : ('\u1d58',   '\u1d64'      ),
        'v'        : ('\u1d5b',   '\u1d65'      ),
        'w'        : ('\u02b7',   '\u1D65\u1D65'           ),
        'x'        : ('\u02e3',   '\u2093'      ),
        'y'        : ('\u02b8',   '\u1D67'           ),
        'z'        : ('\u1DBB',        '\u2082'           ),
        'A'        : ('\u1d2c',   '?'           ),
        'B'        : ('\u1d2e',   '?'           ),
        'C'        : ('?',        '?'           ),
        'D'        : ('\u1d30',   '?'           ),
        'E'        : ('\u1d31',   '?'           ),
        'F'        : ('?',        '?'           ),
        'G'        : ('\u1d33',   '?'           ),
        'H'        : ('\u1d34',   '?'           ),
        'I'        : ('\u1d35',   '?'           ),
        'J'        : ('\u1d36',   '?'           ),
        'K'        : ('\u1d37',   '?'           ),
        'L'        : ('\u1d38',   '?'           ),
        'M'        : ('\u1d39',   '?'           ),
        'N'        : ('\u1d3a',   '?'           ),
        'O'        : ('\u1d3c',   '?'           ),
        'P'        : ('\u1d3e',   '?'           ),
        'Q'        : ('?',        '?'           ),
        'R'        : ('\u1d3f',   '?'           ),
        'S'        : ('?',        '?'           ),
        'T'        : ('\u1d40',   '?'           ),
        'U'        : ('\u1d41',   '?'           ),
        'V'        : ('\u2c7d',   '?'           ),
        'W'        : ('\u1d42',   '?'           ),
        'X'        : ('?',        '?'           ),
        'Y'        : ('?',        '?'           ),
        'Z'        : ('?',        '?'           ),         
        '+'        : ('\u207A',   '\u208A'      ),
        '-'        : ('\u207B',   '\u208B'      ),
        '='        : ('\u207C',   '\u208C'      ),
        '('        : ('\u207D',   '\u208D'      ),
        ')'        : ('\u207E',   '\u208E'      ),        
        ':alpha'   : ('\u1d45',   '?'           ), 
        ':beta'    : ('\u1d5d',   '\u1d66'      ), 
        ':gamma'   : ('\u1d5e',   '\u1d67'      ), 
        ':delta'   : ('\u1d5f',   '?'           ), 
        ':epsilon' : ('\u1d4b',   '?'           ), 
        ':theta'   : ('\u1dbf',   '?'           ),
        ':iota'    : ('\u1da5',   '?'           ),
        ':pho'     : ('?',        '\u1d68'      ),
        ':phi'     : ('\u1db2',   '?'           ),
        ':psi'     : ('\u1d60',   '\u1d69'      ),
        ':chi'     : ('\u1d61',   '\u1d6a'      ),
        ':coffee'  : ('\u2615',   '\u2615'      )
    }
    
    return unicode_map   


subsup_map = subsup_unicode_map()

def subscript_letter(letter):
    
    if letter in subsup_map:
        return subsup_map[letter][1]
    else:
        return letter


def superscript_letter(letter):
    if letter in subsup_map:
        return subsup_map[letter][0]
    else:
        return letter


def echo_text(text):
    
    s = ""
    
    
    # subscript
    s += "".join(map(subscript_letter, text.lower()))
    
    s += text
    
    #superscript
    s += "".join(map(superscript_letter, text.lower()))
    
    return s


if __name__ == "__main__":

    sentence = "the quick brown fox jumps over the lazy dog\n"
    sentence += "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG\n"
    sentence += "1234567890"
    sentence += ",.?!'\"`()[]{}<>&_"
            
    print(upside_down(sentence))
    
    print()
    
    print(fraktur(sentence))
    
    print()
    
    print(double_struck(sentence))
    
    print("echo")
    
    print(echo_text(sentence))