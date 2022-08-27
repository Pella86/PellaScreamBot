# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 09:49:21 2022

@author: maurop
"""


text = "Hello.World!"
text2 = "Hello..World!"

quick_text = "The quick brown fox jumps over the lazy dog"

def diamond_shape(text):
    
    print("input text:", text)
    
    length = len(text)
    half_length= int(length / 2)
    
    
    print("lenght, half", length, half_length)
    
    mod_text = ""
    
    for i, l in enumerate(text):
        if i == 0:
            mod_text += " "*(half_length - i) + l + "\n"
            continue
        
        

        if i < half_length:
            mod_text += " "*(half_length - i) + l + " "*(i*2 - 1) + l + "\n"
        else:
            mod_text += " "*(i - half_length) + l
            
            if length % 2 == 0:
                mod_text += " "*( (length-i)*2 - 1) + l + "\n"
            else:
                if i == length-1:
                    continue
                    
                mod_text += " "*( (length-i)*2 - 3) + l + "\n"
           
    return mod_text


# print(diamond_shape(text))
# print(diamond_shape(text2))


text = "Hello"
text2 = "Helloo"

def cross_shape(text):
    
    length = len(text)
    
       
    half_lenght = int(length / 2)
    
    if length % 2 == 0:
        half_lenght -= 1
    
    mod_text = ""
        
    for i, c in enumerate(text):
        
        if i == half_lenght:
            spaced_text = "".join(l + " " for l in text)
            mod_text += spaced_text + "\n"
        else:
            mod_text += " "*(half_lenght*2) + c + "\n"
    return mod_text

# print(cross_shape(text), len(text))
# print(cross_shape(text2), len(text2))

def sub_sup_map():
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


def echo(text):
    s = ""
    
    char_map = sub_sup_map()
    for letter in text.lower():
        if letter in char_map:
            s += char_map[letter][1]
        else:
            s += letter
    
    s += text
    
    for letter in text.lower():
        if letter in char_map:
            s += char_map[letter][0]
        else:
            s += letter
    
    
    
    return s


print(echo(text))
