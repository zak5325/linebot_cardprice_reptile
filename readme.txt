MTG卡價機器人
	設計為查詢即時卡價,其依據為金魚網上paper價
	機器人id:@wxg8107f
	OB測試中,歡迎各路測試找bug


部署步驟:
1.heroku login
	{heroku email}
	{heroku password}
2.git config --global user.name '{uesrname}'
3.git config --global user.email {email}
4.git init
5.heroku git:remote -a {heroku appname}
6.git add .
7.git commit -m "Init"
8.git push heroku master

if modified or add something, repeat step 6, 7, 8


log:
heroku logs --tail --app {heroku appname}


參考教學:
http://www.oxxostudio.tw/articles/201701/line-bot.html
https://yaoandy107.github.io/line-bot-tutorial/#%E4%BD%BF%E7%94%A8-Heroku-CLI


後記:
目前只有多明納里亞環境,未來有時間會想辦法將其他環境做進去XD
如有其他建議或是有bug可以在主頁下面留言給我,會盡快做修復



#20181212
新增UMA終極大師,為保留原本標準環境範圍,預計此功能將可使用3~4個月後會移除,並移除地類別部分基本地分類,新增密稀地分類
#20180922
新增GRN環境,再選色&地的template增加其他選項,用於因應雙面牌,連體牌,再請各路測試找bug,感謝!
#20180811
新增M19環境
#20180423
已經將目前標準內所有環境的爬蟲設計完成
測試階段中還請大家多多找bugXD
#20180425
發現依夏蘭選項會回傳成決勝依夏蘭,目前已經修復
另外鵬洛客卡包中的限定鵬洛客閃卡無普卡價格,之前會回傳同篩選下閃卡的上一張卡價格,現在修正抓不到則為'----'
因此,預計測試增加閃卡選項,可以選擇查詢普卡或是閃卡價格