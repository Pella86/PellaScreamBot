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




strange_symbols = '''U+0068
U+0334
U+0350
U+035D
U+030F
U+033E
U+034A
U+0360
U+034B
U+033E
U+033F
U+0348
U+033B
U+0321
U+034E
U+0331
U+0355
U+0347
U+031E
U+031C
U+0065
U+0334
U+0310
U+0360
U+0332
U+0328
U+0327
U+006C
U+0334
U+035B
U+0341
U+033E
U+0308
U+0303
U+0308
U+0358
U+0309
U+0360
U+0303
U+0302
U+0351
U+030F
U+0306
U+033A
U+0330
U+0349
U+033A
U+032A
U+032D
U+0324
U+0320
U+031F
U+035C
U+031C
U+0332
U+031D
U+006C
U+0335
U+0344
U+031B
U+0343
U+0332
U+0332
U+034E
U+0348
U+0320
U+0329
U+0353
U+006F
U+0338
U+0357
U+0350
U+035B
U+0350
U+0360
U+0343
U+0303
U+030A
U+030D
U+0302
U+0328
U+0326
U+0348
U+033B
U+0319
U+0333
U+0324
U+0319
U+0020
U+0336
U+0306
U+0308
U+035D
U+031A
U+030F
U+0340
U+034C
U+0327
U+033B
U+0348
U+0322
U+0066
U+0334
U+033F
U+031F
U+0075
U+0335
U+0343
U+0301
U+0307
U+033D
U+0308
U+0344
U+0303
U+032E
U+0355
U+0324
U+033A
U+0324
U+0324
U+0324
U+031E
U+0345
U+035C
U+0063
U+0337
U+030F
U+030A
U+0317
U+0333
U+0345
U+032D
U+006B
U+0338
U+031A
U+033E
U+0305
U+0360
U+0341
U+033F
U+030D
U+0357
U+030A
U+0301
U+0344
U+035B
U+034C
U+0353
U+0331
U+0328
U+032C
U+0065
U+0337
U+0302
U+0344
U+0344
U+030B
U+0313
U+034B
U+0315
U+0344
U+034B
U+0307
U+034D
U+0347
U+0359
U+0356
U+0345
U+034D
U+032E
U+032E
U+0356
U+032C
U+032D
U+0327
U+0323
U+032E
U+0359
U+0072
U+0336
U+0343
U+0351
U+0357
U+0343
U+033E
U+030C
U+0351
U+0350
U+030F
U+030D
U+035D
U+030D
U+034C
U+031D
U+032C
U+0323
U+032F
U+0354
U+0324
U+031F
U+0326
U+035C
U+0328
U+033C
U+031D
U+0073
U+0336
U+0308
U+033D
U+030F
U+031A
U+0350
U+034C
U+0307
U+034B
U+0342
U+0343
U+0304
U+0350
U+0300
U+030A
U+031B
U+0325
U+033C
U+0333
U+033A
U+0326
U+0321
U+0348
'''

set_symbols = set(strange_symbols.split("\n"))

print(set_symbols)

unique_symbols = []
for c in set_symbols:
    if c and not (c in list("hello fuckers")):
        number = "0x" + c.replace("U+", "")

        #print(number)
        
        h = int(number, 0)
        
        #print(h)
        
        char = chr(h)
        
        if char in list("hello fuckers"):
            continue
        
        unique_symbols.append(char)
        
        # l = f"\\u{ord(char):0>4}"  
        # print(l)
        # unique_symbols.append(l)
        
# print(list(map(repr, unique_symbols)))

# print("[", end="")
# for s in unique_symbols[:-1]:
#     print("\"" + s  + "\"" + ", ", end="")

# print("\"" + unique_symbols[-1] + "\"" + "]")

# my_symbols = ["\u0845", "\u0775", "\u0774", "\u0857", "\u0817", "\u0831", "\u0830", "\u0853", "\u0852", "\u0805", "\u0856", "\u0794", "\u0816", "\u0832", "\u0828", "\u0840", "\u0841", "\u0813", "\u0797", "\u0795", "\u0855", "\u0837", "\u0806", "\u0833", "\u0854", "\u0834", "\u0823", "\u0796", "\u0807", "\u0826", "\u0810", "\u0814", "\u0849", "\u0770", "\u0769", "\u0781", "\u0839", "\u0803", "\u0861", "\u0799", "\u0777", "\u0779", "\u0835", "\u0783", "\u0820", "\u0798", "\u0800", "\u0819", "\u0809", "\u0824", "\u0827", "\u0812", "\u0780", "\u0842", "\u0829", "\u0804", "\u0815", "\u0801", "\u0768", "\u0851", "\u0844", "\u0864", "\u0789", "\u0787", "\u0778", "\u0836", "\u0793", "\u0784", "\u0773", "\u0776", "\u0821", "\u0860", "\u0772", "\u0843", "\u0808", "\u0818", "\u0846", "\u0791", "\u0771", "\u0802", "\u0822", "\u0859", "\u0848"]
# print(my_symbols)
        
        
print(unique_symbols)

my_symbols = ['͍', '̇', '̆', '͙', '̱', '̿', '̾', '͕', '͔', '̥', '͘', '̚', '̰', '̀', '̼', '͈', '͉', '̭', '̝', '̛', '͗', 'ͅ', '̦', '́', '͖', '͂', '̷', '̜', '̧', '̺', '̪', '̮', '͑', '̂', '́', '̍', '͇', '̣', '͝', '̟', '̉', '̋', '̓', '̏', '̴', '̞', '̠', '̳', '̩', '̸', '̻', '̬', '̌', '͊', '̽', '̤', '̯', '̡', '̀', '͓', '͌', '͠', '̕', '̓', '̊', '̈́', '̙', '̐', '̅', '̈', '̵', '͜', '̄', '͋', '̨', '̲', '͎', '̗', '̃', '̢', '̶', '͛', '͐']

print(my_symbols)

import random

def demonize(text):
    s = ""
    for l in text:
        n_symbols = random.randint(5, 10)
        # c = l + "".join([random.choice(my_symbols) for i in range(n_symbols)])
        c = l.encode("utf-8") + random.choice(my_symbols).encode("utf-8")
        c = c.decode("utf-8")
        print(c)
        s += c
    
    return(text)


print(demonize(text))