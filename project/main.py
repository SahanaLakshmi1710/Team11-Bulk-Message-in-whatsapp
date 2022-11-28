
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import pyperclip3 as pc
document_path = r"C:\Users\N Sahana Lakshmi\OneDrive\Documents\pspp-assignment.docx"
data = pd.read_csv("numbersinp.csv")        
data_dict = data.to_dict('list')
leads = data_dict['MobileNumber']
messages = data_dict['Message']
combo = zip(leads,messages)
first = True


for lead,message in combo:
    time.sleep(8)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
    if first:
        time.sleep(10)
        first=False 

    width,height = pg.size()
    pg.click(width/2,height/2)
    
    time.sleep(10)
    _send_button_=pg.locateOnScreen('send.png')
    pg.click(pg.center(_send_button_))
    time.sleep(10)
    _attachment_btn_=pg.locateOnScreen('Capture.png')
    pg.click(pg.center(_attachment_btn_))
    
    time.sleep(10)
    _document_btn_=pg.locateOnScreen('document.png')
    pg.click(pg.center(_document_btn_))
    
    time.sleep(10)
    pg.click(pg.center(_document_btn_))
    pc.copy(document_path)
    pg.hotkey('ctrl', 'v')
    
    time.sleep(10)
    _send_document_btn_=pg.locateOnScreen('send_document_btn.png')
    pg.click(pg.center(_send_document_btn_))

    time.sleep(10)
    _send_document_btn_wha_=pg.locateOnScreen('send_attachment_btn_whatsapp.png')
    pg.click(pg.center(_send_document_btn_wha_))
    time.sleep(10)
    pg.hotkey('ctrl', 'w') 

