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