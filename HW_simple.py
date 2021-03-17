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
            'keyboard':[[{'text':'A'},{'text':'B'}],
            [{'text':'C'},{'text':'D'}]]
        }
      
        
    }
    r=requests.post(url,json=payload)
    return r.json()

    
ids=1051394478
print(sendKeyboard(ids))


#1051394478
     
        
        

        
   

    

