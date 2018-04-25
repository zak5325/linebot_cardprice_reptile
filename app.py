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

#environment
DOM = 'https://www.mtggoldfish.com/spoilers/Dominaria'
RIX = 'https://www.mtggoldfish.com/spoilers/Rivals+of+Ixalan'
IXA = 'https://www.mtggoldfish.com/spoilers/Ixalan'
HOU = 'https://www.mtggoldfish.com/spoilers/Hour+of+Devastation'
AKH = 'https://www.mtggoldfish.com/spoilers/Amonkhet'
AER = 'https://www.mtggoldfish.com/spoilers/Aether+Revolt'
KLD = 'https://www.mtggoldfish.com/spoilers/Kaladesh'

web = 'https://www.mtggoldfish.com'
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


def CarouselColor(env):
    carousel_template = CarouselTemplate(columns=[
            CarouselColumn(text='選擇顏色', title='請選擇', actions=[
                MessageTemplateAction(
                    label='黑色', text=env+'黑色'),
                MessageTemplateAction(
                    label='白色', text=env+'白色'),
                MessageTemplateAction(
                    label='綠色', text=env+'綠色')
            ]),
            CarouselColumn(text='選擇顏色', title='請選擇', actions=[
                MessageTemplateAction(
                    label='紅色', text=env+'紅色'),
                MessageTemplateAction(
                    label='藍色', text=env+'藍色'),
                MessageTemplateAction(
                    label='多色', text=env+'多色')
            ]),
            CarouselColumn(text='選擇顏色', title='請選擇', actions=[
                MessageTemplateAction(
                    label='無色', text=env+'無色'),
                MessageTemplateAction(
                    label='地', text=env+'地'),
                MessageTemplateAction(
                    label='--', text='--')
            ]),
        ])
    return carousel_template

def checkenv(env):
    if env=='DOM':
        env=DOM
    if env=='RIX':
        env=RIX
    if env=='IXA':
        env=IXA
    if env=='HOU':
        env=HOU
    if env=='AKH':
        env=AKH
    if env=='AER':
        env=AER
    if env=='KLD':
        env=KLD
    return env

#測試:增加閃卡選擇
# def foilask():
#     message = TemplateSendMessage(
#     alt_text='是否查詢閃卡',
#     template=ConfirmTemplate(
#         text='請選擇?',
#         actions=[
#             MessageTemplateAction(label='普卡', text='普卡'),
#             MessageTemplateAction(label='閃卡', text='閃卡')
#             ]
#         )
#     )
#     line_bot_api.reply_message(event.reply_token, message)

def get_cards(divs):
    content=''
    for div in divs:
        if(div.find('a')):
            name=div.find('a').string
            link=div.find('a')['href']
            link=web+link
            link+='#paper'
            if(link):
                paperprice=''
                soup=BeautifulSoup(get_web(link),'html.parser')
                paper=soup.find_all('div','price-box paper')
                for price in paper:
                    paperprice=price.find('div','price-box-price').string
                    if paperprice=='':
                        papereprice='--'
                content+='{}${}\n{}\n'.format(name,paperprice,link)
    print(content)
    return content


###Black
def MythicB(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','B Mythic mix spoiler-card')
    content=get_cards(divs)
    return content
def RareB(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','B Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonB(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','B Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonB(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','B Common mix spoiler-card')
    content=get_cards(divs)
    return content
###White
def MythicW(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Mythic W mix spoiler-card')
    content=get_cards(divs)
    return content
def RareW(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Rare W mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonW(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Uncommon W mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonW(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Common W mix spoiler-card')
    content=get_cards(divs)
    return content
###Red
def MythicR(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Mythic R mix spoiler-card')
    content=get_cards(divs)
    return content
def RareR(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','R Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonR(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','R Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonR(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Common R mix spoiler-card')
    content=get_cards(divs)
    return content
###Blue
def MythicU(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Mythic U mix spoiler-card')
    content=get_cards(divs)
    return content
def RareU(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Rare U mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonU(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','U Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonU(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Common U mix spoiler-card')
    content=get_cards(divs)
    return content
###Green
def MythicG(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','G Mythic mix spoiler-card')
    content=get_cards(divs)
    return content
def RareG(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','G Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonG(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','G Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonG(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Common G mix spoiler-card')
    content=get_cards(divs)
    return content
###Colorless
def MythicC(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','C Mythic mix spoiler-card')
    content=get_cards(divs)
    return content
def RareC(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','C Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonC(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','C Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonC(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','C Common mix spoiler-card')
    content=get_cards(divs)
    return content
###MultiColor
def MythicM(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','M Mythic mix spoiler-card')
    content=get_cards(divs)
    return content
def RareM(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','M Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonM(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','M Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
###Land
def RareL(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','L Rare mix spoiler-card')
    content=get_cards(divs)
    return content
def UncommonL(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','L Uncommon mix spoiler-card')
    content=get_cards(divs)
    return content
def CommonL(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Common L mix spoiler-card')
    content=get_cards(divs)
    return content
def BasicL(env):
    env=checkenv(env)
    soup=BeautifulSoup(get_web(env),'html.parser')
    divs=soup.find_all('div','Basic L Land mix spoiler-card')
    content=get_cards(divs)
    return content
###



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    envionment=''
    print(event.message.text)
    if event.message.text.upper() == "MTG":
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(text='選擇環境', title='請選擇', actions=[
                MessageTemplateAction(
                    label='多明納里亞', text='多明納里亞'),
                MessageTemplateAction(
                    label='決勝依夏蘭', text='決勝依夏蘭'),
                MessageTemplateAction(
                    label='依夏蘭', text='依夏蘭')
            ]),
            CarouselColumn(text='選擇環境', title='請選擇', actions=[
                MessageTemplateAction(
                    label='幻滅時刻', text='幻滅時刻'),
                MessageTemplateAction(
                    label='阿芒凱', text='阿芒凱'),
                MessageTemplateAction(
                    label='乙太之亂', text='乙太之亂')
            ]),
            CarouselColumn(text='選擇環境', title='請選擇', actions=[
                MessageTemplateAction(
                    label='卡拉德許', text='卡拉德許'),
                MessageTemplateAction(
                    label='--', text='--'),
                MessageTemplateAction(
                    label='--', text='--')
            ])
        ])
        template_message = TemplateSendMessage(
            alt_text='envionment template', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    if event.message.text == "多明納里亞":
        envionment='DOM'
        carousel_template =CarouselColor(envionment)
        template_message = TemplateSendMessage(
            alt_text='envionment template', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    if event.message.text == "決勝依夏蘭":
        envionment='RIX'
        carousel_template =CarouselColor(envionment)
        template_message = TemplateSendMessage(
            alt_text='envionment template', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    if event.message.text == "依夏蘭":
        envionment='IXA'
        carousel_template =CarouselColor(envionment)
        template_message = TemplateSendMessage(
            alt_text='envionment template', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    if event.message.text == "幻滅時刻":
        envionment='HOU'
        carousel_template =CarouselColor(envionment)
        template_message = TemplateSendMessage(
            alt_text='envionment template', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    if event.message.text == "阿芒凱":
        envionment='AKH'
        carousel_template =CarouselColor(envionment)
        template_message = TemplateSendMessage(
            alt_text='envionment template', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    if event.message.text == "乙太之亂":
        envionment='AER'
        carousel_template =CarouselColor(envionment)
        template_message = TemplateSendMessage(
            alt_text='envionment template', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    if event.message.text == "卡拉德許":
        envionment='KLD'
        carousel_template =CarouselColor(envionment)
        template_message = TemplateSendMessage(
            alt_text='envionment template', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0
    if event.message.text.find('黑色')!=-1:
        envionment = event.message.text[0:3]
        buttons_template = TemplateSendMessage(
            alt_text='黑色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/IxX566X.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text=envionment+' Black Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text=envionment+' Black Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text=envionment+' Black Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text=envionment+' Black Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text.find('白色')!=-1:
        envionment = event.message.text[0:3]
        buttons_template = TemplateSendMessage(
            alt_text='白色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/p07TnJp.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text=envionment+' White Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text=envionment+' White Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text=envionment+' White Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text=envionment+' White Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text.find('紅色')!=-1:
        envionment = event.message.text[0:3]
        buttons_template = TemplateSendMessage(
            alt_text='紅色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/qYEgZOM.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text=envionment+' Red Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text=envionment+' Red Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text=envionment+' Red Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text=envionment+' Red Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text.find('藍色')!=-1:
        envionment = event.message.text[0:3]
        buttons_template = TemplateSendMessage(
            alt_text='藍色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/IiRxrAD.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text=envionment+' Blue Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text=envionment+' Blue Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text=envionment+' Blue Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text=envionment+' Blue Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text.find('綠色')!=-1:
        envionment = event.message.text[0:3]
        buttons_template = TemplateSendMessage(
            alt_text='綠色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/qVhRL6W.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text=envionment+' Green Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text=envionment+' Green Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text=envionment+' Green Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text=envionment+' Green Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text.find('無色')!=-1:
        envionment = event.message.text[0:3]
        buttons_template = TemplateSendMessage(
            alt_text='無色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/FMF4E8Z.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text=envionment+' Colorless Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text=envionment+' Colorless Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text=envionment+' Colorless Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text=envionment+' Colorless Common'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text.find('多色')!=-1:
        envionment = event.message.text[0:3]
        buttons_template = TemplateSendMessage(
            alt_text='多色 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/gnYu0Wk.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Mythic',
                        text=envionment+' MultiColor Mythic'
                    ),
                    MessageTemplateAction(
                        label='Rare',
                        text=envionment+' MultiColor Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text=envionment+' MultiColor Uncommon'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text.find('地')!=-1:
        envionment = event.message.text[0:3]
        buttons_template = TemplateSendMessage(
            alt_text='地 template',
            template=ButtonsTemplate(
                title='選擇稀有度',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/BrXXT6o.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Rare',
                        text=envionment+' Land Rare'
                    ),
                    MessageTemplateAction(
                        label='Uncommon',
                        text=envionment+' Land Uncommon'
                    ),
                    MessageTemplateAction(
                        label='Common',
                        text=envionment+' Land Common'
                    ),
                    MessageTemplateAction(
                        label='Basic',
                        text=envionment+' Basic Land'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text.find('Black Mythic')!=-1:
        envionment = event.message.text[0:3]
        content = MythicB(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Black Rare')!=-1:
        envionment = event.message.text[0:3]
        content = RareB(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Black Uncommon')!=-1:
        envionment = event.message.text[0:3]
        content = UncommonB(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Black Common')!=-1:
        envionment = event.message.text[0:3]
        content = CommonB(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('White Mythic')!=-1:
        envionment = event.message.text[0:3]
        content = MythicW(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('White Rare')!=-1:
        envionment = event.message.text[0:3]
        content = RareW(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('White Uncommon')!=-1:
        envionment = event.message.text[0:3]
        content = UncommonW(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('White Common')!=-1:
        envionment = event.message.text[0:3]
        content = CommonW(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Red Mythic')!=-1:
        envionment = event.message.text[0:3]
        content = MythicR(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Red Rare')!=-1:
        envionment = event.message.text[0:3]
        content = RareR(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Red Uncommon')!=-1:
        envionment = event.message.text[0:3]
        content = UncommonR(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Red Common')!=-1:
        envionment = event.message.text[0:3]
        content = CommonR(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Blue Mythic')!=-1:
        envionment = event.message.text[0:3]
        content = MythicU(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Blue Rare')!=-1:
        envionment = event.message.text[0:3]
        content = RareU(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Blue Uncommon')!=-1:
        envionment = event.message.text[0:3]
        content = UncommonU(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Blue Common')!=-1:
        envionment = event.message.text[0:3]
        content = CommonU(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Green Mythic')!=-1:
        envionment = event.message.text[0:3]
        content = MythicG(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Green Rare')!=-1:
        envionment = event.message.text[0:3]
        content = RareG(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Green Uncommon')!=-1:
        envionment = event.message.text[0:3]
        content = UncommonG(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Green Common')!=-1:
        envionment = event.message.text[0:3]
        content = CommonG(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Colorless Mythic')!=-1:
        envionment = event.message.text[0:3]
        content = MythicC(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Colorless Rare')!=-1:
        envionment = event.message.text[0:3]
        content = RareC(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Colorless Uncommon')!=-1:
        envionment = event.message.text[0:3]
        content = UncommonC(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Colorless Common')!=-1:
        envionment = event.message.text[0:3]
        content = CommonC(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('MultiColor Mythic')!=-1:
        envionment = event.message.text[0:3]
        content = MythicM(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('MultiColor Rare')!=-1:
        envionment = event.message.text[0:3]
        content = RareM(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('MultiColor Uncommon')!=-1:
        envionment = event.message.text[0:3]
        content = UncommonM(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Land Rare')!=-1:
        envionment = event.message.text[0:3]
        content = RareL(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Land Uncommon')!=-1:
        envionment = event.message.text[0:3]
        content = UncommonL(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Land Common')!=-1:
        envionment = event.message.text[0:3]
        content = CommonL(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text.find('Basic Land')!=-1:
        envionment = event.message.text[0:3]
        content = BasicL(envionment)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
