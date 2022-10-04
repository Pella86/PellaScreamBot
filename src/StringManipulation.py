# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:56:35 2022

@author: maurop
"""

import hashlib

import src.UnicodeFonts

class StringManipulationBase:
    
    def pack_text(self, text):
        return  "<code>" + self.convert_fn(text) + "</code>"


class LShape(StringManipulationBase):
    
    def convert_fn(self, text):
        text = text.upper()
        
        mod_text = ""
        for l in text:
            mod_text += l + " "
        
        for i, l in enumerate(text[1:]):
            mod_text += "\n" + l + " "*(i*2 + 1) + l

        return mod_text
    
class Diamond(StringManipulationBase):
    
    def convert_fn(self, text):
        
        text = text.upper()

        length = len(text)
        half_length= int(length / 2)
    
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
    
class Cross(StringManipulationBase):
    
    def convert_fn(self, text):
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


class UpsideDown(StringManipulationBase):
    
    def __init__(self):
        self.upside_down = src.UnicodeFonts.UpsideDown()
    
    def convert_fn(self, text):
        return self.upside_down.convert(text)
    

class Fraktur(StringManipulationBase):
    
    def __init__(self):
        
    

# =============================================================================
# Result Article
# =============================================================================
    
class ResultArticleGenerator:
    
    def __init__(self):
        
        self.convert_text = {}
        
        self.convert_text["L shape"] = LShape()
        self.convert_text["Diamond"] = Diamond()
        self.convert_text["Cross"] = Cross()
        self.convert_text["Upside Down"] = UpsideDown()
        
        
    
    
    def generate(self, text, shape):
        
        # strip lose stuff
        text = text.strip()
        
        mod_text = ""
        if shape in self.convert_text:
            mod_text = self.convert_text[shape].pack_text(text)
        else:
            print("Shape not found")
            mod_text = mod_text
            
        
    
        if shape == "L shape":
            mod_text = lshape.pack_text(text)
            
        elif shape == "Diamond":
            text = text.upper()
            mod_text = diamond_shape(text)
            
        elif shape == "Cross":
            text = text.upper()
            mod_text = cross_shape(text)
            
        elif shape == "Upside Down":
            mod_text = upside_down(text)

        elif shape == "Fraktur":
            mod_text = fraktur(text)
        
        elif shape == "Double Struck":
            mod_text = double_struck(text)
        
        elif shape == "Echo":
            mod_text = echo(text)
        
        elif shape == "Zalgo":
            mod_text = zalgo(text)
        
        elif shape == "Sauwastika":
            mod_text = sauwastika(text)
            
        else:
            mod_text = text
            print("shape not found")
            
        if len(mod_text) < 4096:

            message = dict({"message_text": mod_text,
                            "parse_mode":"HTML",
                            "disable_web_page_preview":True}) 
            text_id = hashlib.md5((shape + mod_text).encode()).hexdigest()
            
            
            
            self.result = dict({"type":"article",
                                   "id": text_id,
                                   "title": shape + ": " + text[:15],
                                   "input_message_content": message}) 
        else:
            
            message = dict({"message_text": "ERROR: message too long",
                        "parse_mode":"HTML"}) 
            text_id = hashlib.md5(mod_text.encode()).hexdigest()
            
            
            
            self.result = dict({"type":"article",
                                   "id": text_id,
                                   "title": shape + ": " + "message too long",
                                   "input_message_content": message}) 