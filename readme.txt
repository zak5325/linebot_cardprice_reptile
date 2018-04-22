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
目前使用的機器人id:@wxg8107f
目前只有多明納里亞環境,未來有時間會想辦法將其他環境做進去XD
如有其他建議或是有bug可以在主頁下面留言給我,會盡快做修復

#20180423
已經將目前標準內所有環境的爬蟲設計完成
測試階段中還請大家多多找bugXD