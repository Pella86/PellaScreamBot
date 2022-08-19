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

import Requests
import Updater


# =============================================================================
# Bot class
# =============================================================================

class Bot:
    
    telegram_api = Requests.tg_requests
    
    
    def __init__(self):
        
        r = self.telegram_api.getMe()
        rjson = r.json()
    
        print("Bot:", rjson["result"]["first_name"], "@" + rjson["result"]["username"])
    
    
    def sendMessage(self, chat_id, text, parse_mode="HTML"):
        params= {"chat_id":chat_id, "text":text, "parse_mode":parse_mode}
                
        self.telegram_api.sendMessage(params)  
        
    def sendHelpMessage(self, chat_id):
        
        text = "Hello, I'm Pella Scream Bot\nUse me inline with <code>@pellascreambot ...text...</code>, then chose any option."
        
        self.sendMessage(chat_id, text)


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


# =============================================================================
# Query option generation
# =============================================================================

class ResultArticle:
    
    def __init__(self, shape, text, org_text):
        
        message = dict({"message_text": text,
                    "parse_mode":"HTML"}) 
        
        text_id = hashlib.md5(text.encode()).hexdigest()
        
        self.result = dict({"type":"article",
                               "id": text_id,
                               "title": shape + ": " + org_text[:15],
                               "input_message_content": message})

if __name__ == "__main__":
    
    bot = Bot()

    update = Updater.Update()
    

    while True:
        time.sleep(0.1)
        
        
        new_messages = update.getUpdates()

        try:
            
            for message in new_messages:
                
                if "message" in message:
                    chat_id = message["message"]["chat"]["id"]
                    
                    bot.sendHelpMessage(chat_id)
                    

                                        
                
                if "inline_query" in message:
                    inline_query = message["inline_query"]
                    
                    text = inline_query["query"]
                    
                    if text:
                        
                        # limit text to 100 characters
                        text = text[:100]
                        
                        
                        # uppercase
                        text = text.upper()
                        
                        
                        
                        l_shape_text = l_shape(text)
                        diamond_shape_text = diamond_shape(text)
                        cross_sahpe_text = cross_shape(text)
                        
                        result_l_shape = ResultArticle("L shape", l_shape_text, text)
                        result_diamond = ResultArticle("Diamond", diamond_shape_text, text)
                        result_cross = ResultArticle("Cross", cross_sahpe_text, text)
                        

                        
                        query_result_array = [result_l_shape.result,
                                              result_diamond.result,
                                              result_cross.result]
                        
                        resp = Requests.tg_requests.answerInlineQuery(inline_query["id"], json.dumps(query_result_array))
                        

                
                    
                
        except KeyError as e:
            print("key:", e)
            print(traceback.format_exc())
            
            print("message parsing error")
            print(json.dumps(message, indent=4))
