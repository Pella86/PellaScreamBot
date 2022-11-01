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

import src.telegram.Updater as Updater
import src.telegram.Bot as Bot
import src.telegram.TelegramObjects as tg_obj

import src.UnicodeFonts
import src.StringManipulation

from src.telegram.Requests import TelegramRequestError
   
# =============================================================================
# Pella scream bot
# =============================================================================
    
class PellaScreamBot(Bot.Bot):
    
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
    updater = Updater.Update()
    
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
                        
                        if resp.status_code == 200:
                            print(inline_query.user, text)
   
                            
        # in case the message is not a query       
        except KeyError as e:
            # print where the error is
            print("Error key:", e)
            print(traceback.format_exc())
            
            # print where the message
            print("------ message parsing error --------")
            print(json.dumps(update, indent=4))
            
        except TelegramRequestError as e:
            print(e)
            
            
