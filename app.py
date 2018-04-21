from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
#from linebot.models import (
#    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
#)
from linebot.models import *

from bs4 import BeautifulSoup
import time
from requests import get

target_url = 'https://www.mtggoldfish.com/spoilers/Dominaria'
web='https://www.mtggoldfish.com'
def get_web(url):
    time.sleep(0.5)
    resp=get(url=url)
    return resp.text


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('line access token')
# Channel Secret
handler = WebhookHandler('channel secret')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def get_cards(divs):
    content=''
    for div in divs:
        if(div.find('a')):
            name=div.find('a').string
            link=div.find('a')['href']
            link=web+link
            link+='#paper'
            if(link):
                soup2=BeautifulSoup(get_web(link),'html.parser')
                price=soup2.find('div','price-box-price').string
                content+='{}${}\n{}\n'.format(name,price,link)
    return content


###Black
def MythicB():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','B Mythic mix spoiler-card')
    content=get_cards(divs)
    return content
def RareB():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','B Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonB():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','B Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonB():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','B Common mix spoiler-card')
    content=get_cards(divs)
    return content
###White
def MythicW():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Mythic W mix spoiler-card')
    content=get_cards(divs)
    return content
def RareW():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Rare W mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonW():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Uncommon W mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonW():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Common W mix spoiler-card')
    content=get_cards(divs)
    return content
###Red
def MythicR():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Mythic R mix spoiler-card')
    content=get_cards(divs)
    return content
def RareR():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','R Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonR():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','R Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonR():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Common R mix spoiler-card')
    content=get_cards(divs)
    return content
###Blue
def MythicU():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Mythic U mix spoiler-card')
    content=get_cards(divs)
    return content
def RareU():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Rare U mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonU():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','U Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonU():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Common U mix spoiler-card')
    content=get_cards(divs)
    return content
###Green
def MythicG():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','G Mythic mix spoiler-card')
    content=get_cards(divs)
    return content
def RareG():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','G Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonG():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','G Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonG():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Common G mix spoiler-card')
    content=get_cards(divs)
    return content
###Colorless
def MythicC():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','C Mythic mix spoiler-card')
    content=get_cards(divs)
    return content
def RareC():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','C Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonC():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','C Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonC():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','C Common mix spoiler-card')
    content=get_cards(divs)
    return content
###MultiColor
def MythicM():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','M Mythic mix spoiler-card')
    content=get_cards(divs)
    return content
def RareM():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','M Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonM():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','M Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
###Land
def RareL():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','L Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonL():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','L Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonL():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Common L mix spoiler-card')
    content=get_cards(divs)
    return content
def BasicL():
    soup=BeautifulSoup(get_web(target_url),'html.parser')
    divs=soup.find_all('div','Basic L Land mix spoiler-card')
    content=get_cards(divs)
    return content
###



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if event.message.text.upper() == "MTG":
        buttons_template = TemplateSendMessage(
            alt_text='MTG template',
            template=ButtonsTemplate(
                title='選擇環境',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/3NYvZzG.jpg',
                actions=[
                    MessageTemplateAction(
                        label='多明納里亞',
                        text='多明納里亞'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "多明納里亞":
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(text='選擇顏色', title='請選擇', actions=[
                MessageTemplateAction(
                    label='黑色', text='DOM黑色'),
                MessageTemplateAction(
                    label='白色', text='DOM白色'),
                MessageTemplateAction(
                    label='綠色', text='DOM綠色')
            ]),
            CarouselColumn(text='選擇顏色', title='請選擇', actions=[
                MessageTemplateAction(
                    label='紅色', text='DOM紅色'),
                MessageTemplateAction(
                    label='藍色', text='DOM藍色'),
                MessageTemplateAction(
                    label='多色', text='DOM多色')
            ]),
            CarouselColumn(text='選擇顏色', title='請選擇', actions=[
                MessageTemplateAction(
                    label='無色', text='DOM無色'),
                MessageTemplateAction(
                    label='地', text='DOM地'),
                MessageTemplateAction(
                    label='--', text='--')
            ]),
        ])
        template_message = TemplateSendMessage(
            alt_text='多明納里亞 template', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    if event.message.text == "DOM黑色":
        buttons_template = TemplateSendMessage(
            alt_text='多明納里亞黑色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/IxX566X.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text='Black Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text='Black Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text='Black Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text='Black Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "DOM白色":
        buttons_template = TemplateSendMessage(
            alt_text='多明納里亞白色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/p07TnJp.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text='White Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text='White Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text='White Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text='White Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "DOM紅色":
        buttons_template = TemplateSendMessage(
            alt_text='多明納里亞紅色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/qYEgZOM.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text='Red Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text='Red Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text='Red Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text='Red Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "DOM藍色":
        buttons_template = TemplateSendMessage(
            alt_text='多明納里亞藍色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/IiRxrAD.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text='Blue Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text='Blue Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text='Blue Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text='Blue Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "DOM綠色":
        buttons_template = TemplateSendMessage(
            alt_text='多明納里亞綠色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/qVhRL6W.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text='Green Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text='Green Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text='Green Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text='Green Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "DOM無色":
        buttons_template = TemplateSendMessage(
            alt_text='多明納里亞無色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/FMF4E8Z.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text='Colorless Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text='Colorless Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text='Colorless Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text='Colorless Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "DOM多色":
        buttons_template = TemplateSendMessage(
            alt_text='多明納里亞多色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/gnYu0Wk.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text='MultiColor Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text='MultiColor Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text='MultiColor Uncommon'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "DOM地":
        buttons_template = TemplateSendMessage(
            alt_text='多明納里亞地 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/BrXXT6o.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Rare',
                        text='Land Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text='Land Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text='Land Common'
                    ),
                    MessageTemplateAction(
                        label='Basic',
                        text='Basic Land'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Black Mythic":
        content = MythicB()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Black Rare":
        content = RareB()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Black Uncommon":
        content = UncommonB()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Black Common":
        content = CommonB()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "White Mythic":
        content = MythicW()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "White Rare":
        content = RareW()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "White Uncommon":
        content = UncommonW()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "White Common":
        content = CommonW()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Red Mythic":
        content = MythicR()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Red Rare":
        content = RareR()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Red Uncommon":
        content = UncommonR()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Red Common":
        content = CommonR()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Blue Mythic":
        content = MythicU()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Blue Rare":
        content = RareU()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Blue Uncommon":
        content = UncommonU()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Blue Common":
        content = CommonU()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Green Mythic":
        content = MythicG()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Green Rare":
        content = RareG()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Green Uncommon":
        content = UncommonG()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Green Common":
        content = CommonG()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Colorless Mythic":
        content = MythicC()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Colorless Rare":
        content = RareC()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Colorless Uncommon":
        content = UncommonC()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Colorless Common":
        content = CommonC()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "MultiColor Mythic":
        content = MythicM()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "MultiColor Rare":
        content = RareM()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "MultiColor Uncommon":
        content = UncommonM()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Land Rare":
        content = RareL()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Land Uncommon":
        content = UncommonL()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Land Common":
        content = CommonL()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "Basic Land":
        content = BasicL()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
