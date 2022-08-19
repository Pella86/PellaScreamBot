# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 09:49:21 2022

@author: maurop
"""


text = "Hello.World!"
text2 = "Hello..World!"

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

print(cross_shape(text), len(text))
print(cross_shape(text2), len(text2))
