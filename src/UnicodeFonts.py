# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:32:54 2022

@author: maurop
"""


import string


class BaseConverter:
    
    '''Base class to convert the strings, it skips characters that are not known
    could be a decorator but is here in case more stuff happens'''
    
    def convert(self, text):
        resulting_string = ""
        for l in text:
            
            try:
                resulting_string += self.convert_dict[l]
            except KeyError:
                resulting_string += l
        return resulting_string
                


# =============================================================================
# Upside Down
# =============================================================================

class UpsideDown(BaseConverter):
    
    def __init__(self):
        self.convert_dict = {}
        
        self.convert_dict["a"] = "\u0250"
        self.convert_dict["b"] = "q"
        self.convert_dict["c"] = "\u0254"
        self.convert_dict["d"] = "p"
        self.convert_dict["e"] = "\u01DD"
        self.convert_dict["f"] = "\u025F"
        self.convert_dict["g"] = "\u0183"
        self.convert_dict["h"] = "\u0265"
        self.convert_dict["i"] = "\u1D09"
        self.convert_dict["j"] = "\u027E"
        self.convert_dict["k"] = "\u029E"
        self.convert_dict["l"] = "l"
        self.convert_dict["m"] = "\u026F"
        self.convert_dict["n"] = "u"
        self.convert_dict["o"] = "o"
        self.convert_dict["p"] = "q"
        self.convert_dict["q"] = "b"
        self.convert_dict["r"] = "\u0279"
        self.convert_dict["s"] = "s"
        self.convert_dict["t"] = "\u0287"
        self.convert_dict["u"] = "n"
        self.convert_dict["v"] = "\u028C"
        self.convert_dict["w"] = "\u028D"
        self.convert_dict["x"] = "x"
        self.convert_dict["y"] = "\u028E"
        self.convert_dict["z"] = "z"
        self.convert_dict["A"] = "\u2200"
        self.convert_dict["B"] = "B"
        self.convert_dict["C"] = "\u0186"
        self.convert_dict["D"] = "D"
        self.convert_dict["E"] = "\u018E"
        self.convert_dict["F"] = "\u2132"
        self.convert_dict["G"] = "\u200E\u05E4"
        self.convert_dict["H"] = "H"
        self.convert_dict["I"] = "I"
        self.convert_dict["J"] = "\u017F"
        self.convert_dict["K"] = "K"
        self.convert_dict["L"] = "\u02E5"
        self.convert_dict["M"] = "W"
        self.convert_dict["N"] = "N"
        self.convert_dict["O"] = "O"
        self.convert_dict["P"] = "\u0500"
        self.convert_dict["Q"] = "Q"
        self.convert_dict["R"] = "\u1D1A"
        self.convert_dict["S"] = "S"
        self.convert_dict["T"] = "\u2534"
        self.convert_dict["U"] = "\u2229"
        self.convert_dict["V"] = "\u039B"
        self.convert_dict["W"] = "M"
        self.convert_dict["X"] = "X"
        self.convert_dict["Y"] = "\u2144"
        self.convert_dict["Z"] = "Z"
        self.convert_dict["1"] = "\u0196"
        self.convert_dict["2"] = "\u1105"
        self.convert_dict["3"] = "\u0190"
        self.convert_dict["4"] = "\u3123"
        self.convert_dict["5"] = "\u03DB"
        self.convert_dict["6"] = "9"
        self.convert_dict["7"] = "\u3125"
        self.convert_dict["8"] = "8"
        self.convert_dict["9"] = "6"
        self.convert_dict["0"] = "0"
        self.convert_dict[","] = "'"
        self.convert_dict["."] = "\u02D9"
        self.convert_dict["?"] = "\u00BF"
        self.convert_dict["!"] = "\u00A1"
        self.convert_dict["\""] = ",,"
        self.convert_dict["'"] = ","
        self.convert_dict["`"] = ","
        self.convert_dict["("] = ")"
        self.convert_dict[")"] = "("
        self.convert_dict["["] = "]"
        self.convert_dict["]"] = "["
        self.convert_dict["{"] = "}"
        self.convert_dict["}"] = "{"
        self.convert_dict["<"] = ">"
        self.convert_dict[">"] = "<"
        self.convert_dict["&"] = "\u214B"
        self.convert_dict["_"] = "\u203E"     
        

# =============================================================================
# Fraktur
# =============================================================================

class Fraktur(BaseConverter):
    
    def __init__(self):
        start = 0x1D56C
        #end = 0x1D537
        
        capitals = string.ascii_uppercase
        lowers = string.ascii_lowercase
        
        alphabet = capitals + lowers
        
        self.convert_dict = {}
        
        for l in alphabet:
            self.convert_dict[l] = chr(start)
            start += 1


# =============================================================================
# Double struck
# =============================================================================

class DoubleStruck(BaseConverter):
    
    def __init__(self):
        # alphabet
        start = 0x1D538
        
        capitals = string.ascii_uppercase
        lowers = string.ascii_lowercase
        alphabet = capitals + lowers
        
        
        exceptions = "CHNPQRZ"
        symbols = "\u2102\u210D\u2115\u2119\u211A\u211D\u2124"
        
        exp_sym = dict(zip(list(exceptions), list(symbols)))
    
        self.convert_dict = {}
        
        for l in alphabet:
            if l in exp_sym:
                self.convert_dict[l] = exp_sym[l]
            else:
                self.convert_dict[l] = chr(start)
            start += 1
        
        # digits
        start = 0x1D7D8    
        for l in string.digits:
            self.convert_dict[l] = chr(start)
            start += 1          

# =============================================================================
# Echo
# =============================================================================

class Echo(BaseConverter):
    
    def __init__(self):
        
        #https://stackoverflow.com/questions/17908593/how-to-find-the-unicode-of-the-subscript-alphabet
        self.unicode_map = {
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
           


    def subscript_letter(self, letter):
        if letter in self.unicode_map:
            return self.unicode_map[letter][1]
        else:
            return letter
    
    
    def superscript_letter(self, letter):
        if letter in self.unicode_map:
            return self.unicode_map[letter][0]
        else:
            return letter
        
    def convert(self, text):
        s = ""
        
        # subscript
        s += "".join(map(self.subscript_letter, text.lower()))
        
        s += text
        
        #superscript
        s += "".join(map(self.superscript_letter, text.lower()))
        
        return s        


# =============================================================================
# Encase
# =============================================================================

class Encase(BaseConverter):
    
    def __init__(self):
        self.convert_dict = {}
        
        # encased letters
        ascii_upper = string.ascii_uppercase
        alpha_code_start = 0x1f150
        for l in ascii_upper:
            self.convert_dict[l] = chr(alpha_code_start)
            alpha_code_start += 1
        
        # encased numbers
        numbers = "123456789"
        number_code_start = 0x2776
        for i, n in enumerate(numbers):
            self.convert_dict[n] = chr(number_code_start)
            number_code_start += 1
        
        self.convert_dict["0"] = chr(0x24FF)     

# =============================================================================
# Cursive
# =============================================================================
    
class Cursive(BaseConverter):
    
    def __init__(self):

        code_start = 0x1D4D0
        
        self.convert_dict = {}
        
        letters = string.ascii_uppercase + string.ascii_lowercase
        
        for l in letters:
            self.convert_dict[l] = chr(code_start)
            code_start += 1
        

if __name__ == "__main__":

    sentence = "the quick brown fox jumps over the lazy dog\n"
    sentence += "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG\n"
    sentence += "1234567890"
    sentence += ",.?!'\"`()[]{}<>&_"
    
    upside_down = UpsideDown()
    fraktur = Fraktur()
    double_struck = DoubleStruck()
    echo_text = Echo()
    encase = Encase()
    cursive = Cursive()
            
    print("Upside down")
    print(upside_down.convert(sentence))
    
    print("Fraktur")
    
    print(fraktur.convert(sentence))
    
    print("Double struck")
    
    print(double_struck.convert(sentence))
    
    print("Echo")
    
    print(echo_text.convert(sentence))

    print("Encase")
    
    print(encase.convert(sentence))
    
    print("Cursive")
    
    print(cursive.convert(sentence))