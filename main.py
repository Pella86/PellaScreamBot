# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 08:36:02 2022

@author: maurop
"""

# =============================================================================
# imports
# =============================================================================

import time
import json
import traceback

import src.Requests
import src.Updater
import src.Bot
import src.UnicodeFonts
import src.TelegramObjects as tg_obj
import src.StringManipulation
   
# =============================================================================
# Pella scream bot
# =============================================================================
    
class PellaScreamBot(src.Bot.Bot):
    
    def __init__(self):
        super().__init__()
        
    def sendHelpMessage(self, chat_id):
        text  = f"Hello, I'm {self.info.first_name}\nUse me inline with\n"
        text += f"<code>@{self.info.username} ...text...</code>\n"
        text += "then chose any option."
        self.sendMessage(chat_id, text)

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    
    # start the bot
    bot = PellaScreamBot()
    
    # start the messsage updater
    updater = src.Updater.Update()
    
    # start the various dictionaries for converting unicode text
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
                    if message.chat.type == "private":
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
            
            
