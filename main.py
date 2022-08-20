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
        
        text = "Hello, I'm Pella Scream Bot\nUse me inline with\n<code>@pellascreambot ...text...</code>\n, then chose any option."
        
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
    
    def __init__(self, shape, text):
        
        # limit text to 100 characters
        text = text[:100]
                
        # uppercase
        text = text.upper()
        
        # strip lose stuff
        text = text.strip()
        
        if shape == "L shape":
            mod_text = l_shape(text)
        elif shape == "Diamond":
            mod_text = diamond_shape(text)
        elif shape == "Cross":
            mod_text = cross_shape(text)
        else:
            mod_text = text
            print("shape not found")
            
        if len(mod_text) < 4096:

            message = dict({"message_text": mod_text,
                        "parse_mode":"HTML"}) 
            text_id = hashlib.md5(mod_text.encode()).hexdigest()
            
            
            
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


    
            

if __name__ == "__main__":
    
    # start the bot
    bot = Bot()
    
    # start the messsage updater
    update = Updater.Update()
    
    # main loop
    while True:
        # dont spam requests
        time.sleep(0.1)

        # get the messages updates
        new_messages = update.getUpdates()
        
        # do the thingy
        try:
            
            for message in new_messages:
                
                # if is a private message 
                if "message" in message:
                    chat_id = message["message"]["chat"]["id"]
                    bot.sendHelpMessage(chat_id)
                
                # answer the query
                if "inline_query" in message:
                    inline_query = message["inline_query"]
                    
                    text = inline_query["query"]
                    
                    if text:
                        
                        # available shapes
                        shapes = ["L shape" , "Diamond", "Cross"]
                        
                        # array to be visualized as options
                        query_results_array = []
                        
                        # options
                        for shape in shapes:
                            result = ResultArticle(shape, text)
                            query_results_array.append(result.result)
                         
                        # show the stuff
                        resp = Requests.tg_requests.answerInlineQuery(inline_query["id"], json.dumps(query_results_array))
                        
                        
                        if resp.status_code == 200:
                            print(message["inline_query"]["from"]["first_name"], "@" + str(message["inline_query"]["from"].get("username")), text)
                        
                        if resp.status_code == 400:
                            print("ERROR: inline_query", text)
                            respj = resp.json()
                            if respj["description"] == "Bad Request: MESSAGE_TOO_LONG":
                                res_article = ResultArticle("Bad request", "message too long")
                                query_array = [res_article.result]
                                resp = Requests.tg_requests.answerInlineQuery(inline_query["id"], json.dumps(query_array))
                                
                            
        # in case the message is not a query       
        except KeyError as e:
            # print where the error is
            print("Error key:", e)
            print(traceback.format_exc())
            
            # print where the message
            print("------ message parsing error --------")
            print(json.dumps(message, indent=4))
            
            
