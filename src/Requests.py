# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 08:44:46 2022

@author: maurop
"""

import datetime
import requests
import time


# =============================================================================
# Requests
# =============================================================================

class Requests:
    ''' The class Requests ensures that the limit of 30 requests per second is
    not surpassed. '''
    
    messages_second = 30
    
    def __init__(self):
        # stores the time when a request was done
        self.requests_stack = []
        
        print("Requests instance number", id(self))
 
    
    def clean_stack(self):
        # remove the requests times that are past 1 second ago
        delete_indexes = []
        for i, date in enumerate(self.requests_stack):
            if datetime.datetime.now() - date > datetime.timedelta(seconds=1):
                delete_indexes.append(i)

        delete_indexes.reverse()

        for i in delete_indexes:
            del self.requests_stack[i]        
    
    
    def request(self, reqfunc, url, params):

        self.clean_stack()
        
        if len(self.requests_stack) < self.messages_second:
            self.requests_stack.append(datetime.datetime.now())
            
            response = reqfunc(url, params)
            
            return response
        
        else:
        
            print("Requests: limit reached")
            print("waiting...")
            time.sleep(1)

    
    
    def get(self, url, params = {}):
        
        response = None
            
        
        while response is None:
            
            response = self.request(requests.get, url, params)
            
            if response:
                return response

    
    def post(self, url, params={}):
        
        response = None
            
        
        while response is None:
            
            response = self.request(requests.post, url, params)
            
            if response and response.status_code != 200:
               print("ERROR: Requests: post: ", response.status_code, response.text)
               print(url, params)
           
            
            if response:
                return response            


# =============================================================================
# Telegram Requests
# =============================================================================


class TelegramRequests:
    ''' Main class that manages the queries to the API'''
    
    def __init__(self):
        token = self.read_token()
        
        self.api_url = 'https://api.telegram.org/bot' + token + '/'   
        self.request = Requests()            
    
    
    def getMe(self):
        url = self.api_url + "getMe"
        return self.request.get(url)
    
    
    def getUpdates(self, params):
        url = self.api_url + "getUpdates"
        return self.request.get(url, params)
    
    def sendMessage(self, params):
        url = self.api_url + "sendMessage"
        return self.request.post(url, params)
    
    def editMessageText(self, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode="HTML", entities=None, disable_web_page_preview=None, reply_markup=None):
        url = self.api_url + "editMessageText"
        params = {"text":text}
        
        if chat_id:
            params["chat_id"] = chat_id
        
        if message_id:
            params["message_id"] = message_id
        
        if inline_message_id:
            params["inline_message_id"] = inline_message_id
            
        params["parse_mode"] = parse_mode
            
        if entities:
            params["entities"] = entities
            
        if disable_web_page_preview:
            params["disable_web_page_preview"] = disable_web_page_preview
            
        if reply_markup:
            params["reply_markup"] = reply_markup
        
        
        return self.request.post(url, params)

    
    def answerInlineQuery(self, query_id, query_list):
        url = self.api_url + "answerInlineQuery"
        params = {"inline_query_id" : query_id,
                  "results": query_list}
        return self.request.post(url, params)
    
    def getChatMemeber(self, chat_id, user_id):
        url = self.api_url + "getChatMember"
        params = {"chat_id" : chat_id,
                  "user_id": user_id}
        return self.request.get(url, params)        

    def banChatMemeber(self, chat_id, user_id, until_date=None, revoke_messages=None):
        url = self.api_url + "banChatMember"
        params = {"chat_id" : chat_id,
                  "user_id": user_id
            }
        
        if until_date:
            params["until_date"] = until_date  
            
        
        if revoke_messages:
            params["revoke_messages"] = revoke_messages
        
        
        return self.request.post(url, params)
    
    def unbanChatMember(self, chat_id, user_id, only_if_banned=None):
        url = self.api_url + "unbanChatMember"
        params = {"chat_id" : chat_id,
                  "user_id": user_id
            }
        
        if only_if_banned:
            params["only_if_banned"] = only_if_banned
            
        return self.request.post(url, params)
    
    def getChatMember(self, chat_id, user_id):
        url = self.api_url + "getChatMember"
        params = {"chat_id" : chat_id,
                  "user_id": user_id
            }
    
        return self.request.get(url, params)  

    def answerCallbackQuery(self, callback_query_id, text=None, show_alert=None, url=None):
        api_url = self.api_url + "answerCallbackQuery"
        
        
        params = {"callback_query_id" : callback_query_id
            }
        
        if text:
            params["text"] = text
        
        if show_alert:
            params["show_alert"] = show_alert
            
        if url:
            params["url"] = url
    
        return self.request.post(api_url, params)          
        
        
    
    def read_token(self):
        with open("./bot_token/bot_token.txt") as f:
            lines = f.readlines()
            
        
        for line in lines:
            
            if line:
                parts = line.split("=")
                
                token = parts[1].strip()
    
        return token
    

tg_requests = TelegramRequests()



'''
answerCallbackQuery
Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.

Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via @BotFather and accept the terms. Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.

Parameter	Type	Required	Description
callback_query_id	String	Yes	Unique identifier for the query to be answered
text	String	Optional	Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
show_alert	Boolean	Optional	If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.
url	String	Optional	URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @BotFather, specify the URL that opens your game - note that this will only work if the query comes from a callback_game button.

Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.
cache_time	Integer	Optional	The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.
'''