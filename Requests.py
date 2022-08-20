# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 08:44:46 2022

@author: maurop
"""

import datetime
import requests


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
        
        print("Requests: limit reached")
    
    
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
            
            if response.status_code != 200:
               print(response.status_code, response.text)
               return response
            
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
    
    def banChatMemeber(self, params):
        url = self.api_url + "banChatMember"
        return self.request.post(url, params)
    
    def answerInlineQuery(self, query_id, query_list):
        url = self.api_url + "answerInlineQuery"
        params = {"inline_query_id" : query_id,
                  "results": query_list}
        return self.request.post(url, params)

    def read_token(self):
        with open("./bot_token/bot_token.txt") as f:
            lines = f.readlines()
            
        
        for line in lines:
            
            if line:
                parts = line.split("=")
                
                token = parts[1].strip()
    
        return token
    

tg_requests = TelegramRequests()