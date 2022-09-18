# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 08:36:02 2022

@author: maurop
"""

# =============================================================================
# imports
# =============================================================================

import time
import hashlib
import json
import traceback
import random


import src.Requests
import src.Updater
import src.Bot
import src.UnicodeFonts
import src.TelegramObjects as tg_obj


# =============================================================================
# string manipulations
# =============================================================================

def l_shape(text):
    
    mod_text = ""
    for l in text:
        mod_text += l + " "
    
    for i, l in enumerate(text[1:]):
        mod_text += "\n" + l + " "*(i*2 + 1) + l
        
    mod_text = "<code>" + mod_text + "</code>"
    
    return mod_text

def diamond_shape(text):
   
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
   
    mod_text = "<code>" + mod_text + "</code>"
    
    return mod_text

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
    
    mod_text = "<code>" + mod_text + "</code>"
    
    return mod_text

def upside_down(text):
    mod_text = "<code>" + src.UnicodeFonts.upside_down(text) + "</code>"
    return mod_text

def fraktur(text):
    mod_text = "<code>" + src.UnicodeFonts.fraktur(text) + "</code>"
    return mod_text

def double_struck(text):
    mod_text = "<code>" + src.UnicodeFonts.double_struck(text) + "</code>"
    return mod_text    

def echo(text):
    mod_text = "<code>" + src.UnicodeFonts.echo_text(text) + "</code>"
    return mod_text


zalgo_symbols = ['̖',' ̗',' ̘',' ̙',' ̜',' ̝',' ̞',' ̟',' ̠',' ̤',' ̥',' ̦',' ̩',' ̪',' ̫',' ̬',' ̭',' ̮',' ̯',' ̰',' ̱',' ̲',' ̳',' ̹',' ̺',' ̻',' ̼',' ͅ',' ͇',' ͈',' ͉',' ͍',' ͎',' ͓',' ͔',' ͕',' ͖',' ͙',' ͚',' ', ' ̍',' ̎',' ̄',' ̅',' ̿',' ̑',' ̆',' ̐',' ͒',' ͗',' ͑',' ̇',' ̈',' ̊',' ͂',' ̓',' ̈́',' ͊',' ͋',' ͌',' ̃',' ̂',' ̌',' ͐',' ́',' ̋',' ̏',' ̽',' ̉',' ͣ',' ͤ',' ͥ',' ͦ',' ͧ',' ͨ',' ͩ',' ͪ',' ͫ',' ͬ',' ͭ',' ͮ',' ͯ',' ̾',' ͛',' ͆',' ̚', ' ̕',' ̛',' ̀',' ́',' ͘',' ̡',' ̢',' ̧',' ̨',' ̴',' ̵',' ̶',' ͜',' ͝',' ͞',' ͟',' ͠',' ͢',' ̸',' ̷',' ͡']

zalgo_symbols = list(map(lambda x : x.strip(), zalgo_symbols))

def zalgo(text):
    
    mod_text = ""
    for letter in text:
         
        
        if letter.isalpha():
            n_symbols = random.randint(5, 10)
            
            accents = "".join([random.choice(zalgo_symbols) for i in range(n_symbols)])
            
            new_character = letter + accents
            
            mod_text += new_character
        else:
            mod_text += letter

    #mod_text = "<code>" + mod_text + "</code>"        

    return mod_text

def sauwastika(text):
    
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


# =============================================================================
# Query option generation
# =============================================================================

class ResultArticle:
    
    def __init__(self, shape, text):
        
        # # limit text to 100 characters
        # text = text[:100]
                

        
        # strip lose stuff
        text = text.strip()
        
    
        if shape == "L shape":
            text = text.upper()
            mod_text = l_shape(text)
            
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


# =============================================================================
# Pella scream bot
# =============================================================================
    
class PellaScreamBot(src.Bot.Bot):
    
    def __init__(self):
        super().__init__()
        
    def sendHelpMessage(self, chat_id):
        text = "Hello, I'm Pella Scream Bot\nUse me inline with\n<code>@pellascreambot ...text...</code>\nthen chose any option."
        self.sendMessage(chat_id, text)

if __name__ == "__main__":
    
    # start the bot
    bot = PellaScreamBot()
    
    # start the messsage updater
    updater = src.Updater.Update()
    
    
    # main loop
    while True:
        # dont spam requests
        time.sleep(0.1)

        # get the messages updates
        new_updates = updater.getUpdates()
        
        # do the thingy
        try:
            
            for update in new_updates:
                
                # if is a private update 
                if "message" in update:
                    message = tg_obj.Message(update["message"])
                    bot.sendHelpMessage(message.chat.id)
                
                # answer the query
                if "inline_query" in update:
                    inline_query = tg_obj.InlineQuery(update["inline_query"])
                    
                    text = inline_query.text
                    
                    if text:
                        
                        # available shapes
                        shapes = ["L shape" , "Diamond", "Cross",
                                  "Upside Down", "Fraktur", "Double Struck",
                                  "Echo", "Zalgo", "Sauwastika"]
                        
                        # array to be visualized as options
                        query_results_array = []
                        
                        # options
                        for shape in shapes:
                            result = ResultArticle(shape, text)
                            query_results_array.append(result.result)
                         
                        # show the stuff
                        resp = bot.answerInlineQuery(inline_query.id, json.dumps(query_results_array))
                   
                        if resp:
                        
                            if resp.status_code == 200:
                                print(inline_query.user, text)
                            
                            if resp.status_code == 400:
                                print("ERROR: inline_query", text)
                                respj = resp.json()
                                if respj["description"] == "Bad Request: MESSAGE_TOO_LONG":
                                    res_article = ResultArticle("Bad request", "message too long")
                                    query_array = [res_article.result]
                                    resp = bot.answerInlineQuery(inline_query.id, json.dumps(query_array))
                                    
                            
        # in case the message is not a query       
        except KeyError as e:
            # print where the error is
            print("Error key:", e)
            print(traceback.format_exc())
            
            # print where the message
            print("------ message parsing error --------")
            print(json.dumps(update, indent=4))
            
            
