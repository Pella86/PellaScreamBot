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


import src.Requests
import src.Updater
import src.Bot
import src.UnicodeFonts
import src.TelegramObjects as tg_obj
import src.StringManipulation
   


# # =============================================================================
# # Query option generation
# # =============================================================================

# class ResultArticle:
    
#     def __init__(self, shape, text):
        
#         # # limit text to 100 characters
#         # text = text[:100]
                

        
#         # strip lose stuff
#         text = text.strip()
        
    
#         if shape == "L shape":
#             text = text.upper()
#             mod_text = l_shape(text)
            
#         elif shape == "Diamond":
#             text = text.upper()
#             mod_text = diamond_shape(text)
            
#         elif shape == "Cross":
#             text = text.upper()
#             mod_text = cross_shape(text)
            
#         elif shape == "Upside Down":
#             mod_text = upside_down(text)

#         elif shape == "Fraktur":
#             mod_text = fraktur(text)
        
#         elif shape == "Double Struck":
#             mod_text = double_struck(text)
        
#         elif shape == "Echo":
#             mod_text = echo(text)
        
#         elif shape == "Zalgo":
#             mod_text = zalgo(text)
        
#         elif shape == "Sauwastika":
#             mod_text = sauwastika(text)
            
#         else:
#             mod_text = text
#             print("shape not found")
            
#         if len(mod_text) < 4096:

#             message = dict({"message_text": mod_text,
#                         "parse_mode":"HTML",
#                         "disable_web_page_preview":True}) 
#             text_id = hashlib.md5((shape + mod_text).encode()).hexdigest()
            
            
            
#             self.result = dict({"type":"article",
#                                    "id": text_id,
#                                    "title": shape + ": " + text[:15],
#                                    "input_message_content": message}) 
#         else:
            
#             message = dict({"message_text": "ERROR: message too long",
#                         "parse_mode":"HTML"}) 
#             text_id = hashlib.md5(mod_text.encode()).hexdigest()
            
            
            
#             self.result = dict({"type":"article",
#                                    "id": text_id,
#                                    "title": shape + ": " + "message too long",
#                                    "input_message_content": message}) 


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
    
    string_manipulation = src.StringManipulation.ResultArticleGenerator()
    
    
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
                        shapes = list(string_manipulation.convert_text.keys())
                        
                        # array to be visualized as options
                        query_results_array = []
                        
                        # options
                        for shape in shapes:
                            result = string_manipulation.generate(text, shape)
                            query_results_array.append(result)
                         
                        # show the stuff
                        resp = bot.answerInlineQuery(inline_query.id, json.dumps(query_results_array))
                   
                        if resp:
                        
                            if resp.status_code == 200:
                                print(inline_query.user, text)
                            
                            if resp.status_code == 400:
                                print("ERROR: inline_query", text)
                                respj = resp.json()
                                if respj["description"] == "Bad Request: MESSAGE_TOO_LONG":
                                    res_article = string_manipulation.generate("message too long", "Bad request")
                                    query_array = [res_article]
                                    resp = bot.answerInlineQuery(inline_query.id, json.dumps(query_array))
                                    
                            
        # in case the message is not a query       
        except KeyError as e:
            # print where the error is
            print("Error key:", e)
            print(traceback.format_exc())
            
            # print where the message
            print("------ message parsing error --------")
            print(json.dumps(update, indent=4))
            
            
