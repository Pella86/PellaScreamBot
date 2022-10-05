# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:56:35 2022

@author: maurop
"""
# =============================================================================
# Imports
# =============================================================================

import hashlib
import random

import src.UnicodeFonts

# =============================================================================
# base class
# =============================================================================

class StringManipulationBase:
    ''' Also this class is here in case more repetive functionalities gets added
    for now it just packs the text between the code tags'''
    
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
        text = text[::-1]
        return self.upside_down.convert(text)
    

class Fraktur(StringManipulationBase):
    
    def __init__(self):
        self.fraktur = src.UnicodeFonts.Fraktur()
    
    def convert_fn(self, text):
        return self.fraktur.convert(text)
    

class DoubleStruck(StringManipulationBase):
    
    def __init__(self):
        self.double_struck = src.UnicodeFonts.DoubleStruck()
    
    def convert_fn(self, text):
        return self.double_struck.convert(text)
    
class Echo(StringManipulationBase):
    
    def __init__(self):
        self.echo = src.UnicodeFonts.Echo()
        
    def convert_fn(self, text):
        return self.echo.convert(text)


class Zalgo(StringManipulationBase):
    
    def __init__(self):
        zalgo_symbols = ['̖',' ̗',' ̘',' ̙',' ̜',' ̝',' ̞',' ̟',' ̠',' ̤',' ̥',' ̦',' ̩',' ̪',' ̫',' ̬',' ̭',' ̮',' ̯',' ̰',' ̱',' ̲',' ̳',' ̹',' ̺',' ̻',' ̼',' ͅ',' ͇',' ͈',' ͉',' ͍',' ͎',' ͓',' ͔',' ͕',' ͖',' ͙',' ͚',' ', ' ̍',' ̎',' ̄',' ̅',' ̿',' ̑',' ̆',' ̐',' ͒',' ͗',' ͑',' ̇',' ̈',' ̊',' ͂',' ̓',' ̈́',' ͊',' ͋',' ͌',' ̃',' ̂',' ̌',' ͐',' ́',' ̋',' ̏',' ̽',' ̉',' ͣ',' ͤ',' ͥ',' ͦ',' ͧ',' ͨ',' ͩ',' ͪ',' ͫ',' ͬ',' ͭ',' ͮ',' ͯ',' ̾',' ͛',' ͆',' ̚', ' ̕',' ̛',' ̀',' ́',' ͘',' ̡',' ̢',' ̧',' ̨',' ̴',' ̵',' ̶',' ͜',' ͝',' ͞',' ͟',' ͠',' ͢',' ̸',' ̷',' ͡']
        self.zalgo_symbols = list(map(lambda x : x.strip(), zalgo_symbols))
    
    def pack_text(self, text):
        mod_text = ""
        for letter in text:

            if letter.isalpha():
                n_symbols = random.randint(5, 10)
                
                accents = "".join([random.choice(self.zalgo_symbols) for i in range(n_symbols)])
                
                new_character = letter + accents
                
                mod_text += new_character
            else:
                mod_text += letter 
        return mod_text


class Sauwastika(StringManipulationBase):
    
    def pack_text(self, text):
        
        l_text = len(text)
        
        mod_text = ""
        
        rev_text = text[::-1]
        
        # first line
        line = rev_text + " "*(l_text-2) + rev_text[0] + "\n"
        mod_text += " ".join(list(line))
        
        # arm above
        part = text[1:-1]
        for i, l in enumerate(part):
            mod_text += " "* (l_text*2-2) + part[i] + " "*(l_text*2-3) + rev_text[i+1] + "\n"
        
        # central line
        line = text + rev_text[1:] + "\n"
        mod_text += " ".join(list(line))
        
        # arm below
        for i, l in enumerate(part):
            mod_text +=part[i] + " "*(l_text*2-3) + rev_text[i+1] + "\n"
        
        # last line
        line = text[-1] + " "*(l_text-2) + text
        mod_text += " ".join(list(line)) + "\n"
        
        mod_text = "<code>" + mod_text + "</code>"        
        
        wiki_link = "https://en.m.wikipedia.org/wiki/Swastika"
        linked_text = "<a href=\"{}\">info</a>".format(wiki_link)
        mod_text +="<span class=\"tg-spoiler\">{}</span>".format(linked_text)
           
        return mod_text 
        

class Encase(StringManipulationBase):
    
    def __init__(self):
        self.encase = src.UnicodeFonts.Encase()
    
    def convert_fn(self, text):
        text = text.upper()
        return self.encase.convert(text)

class Cursive(StringManipulationBase):
    
    def __init__(self):
        self.cursive = src.UnicodeFonts.Cursive()
        
    def convert_fn(self, text):
        return self.cursive.convert(text)


class Spongebob(StringManipulationBase):
    
    def convert_fn(self, text):
        s = ""
        text = text.lower()
        
        for l in text:
            r = random.randrange(2)
            
            if r == 1:
                s += l.upper()
    
            else:
                s += l
    
        return s
    

# =============================================================================
# Result Article
# =============================================================================
    
class ResultArticleGenerator:
    ''' This class initializes all the possible types and generates the article
    needed to be displayed on telegram'''
    
    def __init__(self):
        
        self.convert_text = {}
        
        self.convert_text["L shape"] = LShape()
        self.convert_text["Diamond"] = Diamond()
        self.convert_text["Cross"] = Cross()
        self.convert_text["Upside Down"] = UpsideDown()
        self.convert_text["Fraktur"] = Fraktur()
        self.convert_text["Double Struck"] = DoubleStruck()
        self.convert_text["Echo"] = Echo()
        self.convert_text["Zalgo"] = Zalgo()
        self.convert_text["Sauwastika"] = Sauwastika()
        self.convert_text["Encase"] = Encase()
        self.convert_text["Cursive"] = Cursive()
        self.convert_text["Spongebob"] = Spongebob()
 
    def generate(self, text, shape):

        # strip lose stuff
        text = text.strip()
        
        # try to use a known shape else return the unmodified text
        mod_text = ""
        if shape in self.convert_text:
            mod_text = self.convert_text[shape].pack_text(text)
        else:
            print("Shape not found")
            mod_text = mod_text
        
        # create the result articles
        if len(mod_text) < 4096:

            message = dict({"message_text": mod_text,
                            "parse_mode":"HTML",
                            "disable_web_page_preview":True}) 
            
            text_id = hashlib.md5((shape + mod_text).encode()).hexdigest()

            result = dict({"type":"article",
                            "id": text_id,
                            "title": shape + ": " + text[:15],
                            "input_message_content": message}) 
        else:
            
            message = dict({"message_text": "ERROR: message too long",
                            "parse_mode":"HTML"}) 
            
            text_id = hashlib.md5(mod_text.encode()).hexdigest()

            result = dict({"type":"article",
                           "id": text_id,
                           "title": shape + ": " + "message too long",
                           "input_message_content": message}) 
            
        return result