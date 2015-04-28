from flask import Flask, url_for, render_template
from datetime import datetime as t
nats = Flask(__name__)

def getGameNumber():
	for i in xrange(162):
		date = datelist[i]
		print date
		if t.today().day<=date.day:
			return i
f = open('natsschedule.txt') #file containing information
listofgames = []
for line in f:
	listofgames.append(line)
splitlist = []
for game in listofgames: 
	splitlist.append(game.split('|'))
datelist = []
for game in splitlist:
	datelist.append(t.strptime(game[0],"%m/%d/%y"))

@nats.route('/')
def index():
	gamenum=getGameNumber()
	gameToday = (datelist[gamenum].day==t.today().day)
	if gameToday:
		return render_template('gameday.html', gameNumber=gamenum+1, opponent=(splitlist[gamenum][2]), gametime=(splitlist[gamenum][1]))
	else:
		timetilgame = datelist[gamenum]-t.today()
		if timetilgame.days==0:
			return render_template('gametomorrow.html', gameNumber=gamenum, opponent=(splitlist[gamenum][2]), gametime=(splitlist[gamenum][1]))
		return render_template('nogame.html', days=timetilgame.days)	
		#, hours=timetilgame.hours, minutes=timetilgame.minutes
		
if __name__=='__main__':
	nats.debug=True
	nats.run()




