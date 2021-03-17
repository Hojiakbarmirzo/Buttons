import requests
import json
from pprint import pprint


    
token='1696683157:AAHLgLkeTG-m7VbWVp-x_dxjdORPWJKFBmw'

def sendKeyboard(idx):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    payload={
        'chat_id':idx,
        'text':'Button',
        'reply_markup':{
            'keyboard':[
            [{'text':'7'},{'text':'8'},{'text':'9'},{'text':'*'}],
            [{'text':'4'},{'text':'5'},{'text':'6'},{'text':'/'}],
            [{'text':'1'},{'text':'2'},{'text':'3'},{'text':'-'}],
            [{'text':'0'},{'text':'.'},{'text':'='},{'text':'+'}]
            ]
        }
      
        
    }
    r=requests.post(url,json=payload)
    return r.json()

    
ids=1051394478
print(sendKeyboard(ids))


#1051394478
     
        
        

        
   

    

