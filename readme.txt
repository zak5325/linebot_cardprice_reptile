step:
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


reference:
http://www.oxxostudio.tw/articles/201701/line-bot.html
https://yaoandy107.github.io/line-bot-tutorial/#%E4%BD%BF%E7%94%A8-Heroku-CLI