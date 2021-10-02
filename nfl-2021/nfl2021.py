import json
import requests
import pandas
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from subprocess import call
import os
import random
import string


wks = [
"week_1",
"week_2",
"week_3",
"week_4",
"week_5",
"week_6",
"week_7",
"week_8",
"week_9",
"week_10",
"week_11",
"week_12",
"week_13",
"week_14",
"week_15",
"week_16",
"week_17",
"week_18"
]

season = {}
winsAll = []

for wk in wks:
  u = str("https://www.pro-football-reference.com/years/2021/" + wk + ".htm")
  r  = requests.get(u)
  data = r.text
  soup = BeautifulSoup(data,features="lxml")
  winners = soup.findAll("tr", {"class": "winner"})
  wins = []
  for row in winners:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    wins.append(cols[0])
    winsAll.append(cols[0])
    season[wk]=wins

meechPoolPicks = {
"week_1":[
['Tampa Bay Buccaneers'],
['Buffalo Bills'],
['Philadelphia Eagles'],
['Washington Football Team'],
['Tennessee Titans'],
['Jacksonville Jaguars'],
['San Francisco 49ers'],
['Seattle Seahawks'],
['Minnesota Vikings'],
['Carolina Panthers'],
['Denver Broncos'],
['New England Patriots'],
['Green Bay Packers'],
['Kansas City Chiefs'],
['Los Angeles Rams'],
['Baltimore Ravens','51 total points']
],
"week_2":[
['Washington Football Team'],
['New Orleans Saints'],
['Cleveland Browns'],
['Cincinnati Bengals'],
['Pittsburgh Steelers'],
['Buffalo Bills'],
['Indianapolis Colts'],
['San Francisco 49ers'],
['Denver Broncos'],
['New England Patriots'],
['Arizona Cardinals'],
['Tampa Bay Buccaneers'],
['Tennessee Titans'],
['Los Angeles Chargers'],
['Kansas City Chiefs'],
['Green Bay Packers','47 total points']
],
"week_3":[
['Carolina Panthers'],
['Arizona Cardinals'],
['Tennessee Titans'],
['Baltimore Ravens'],
['Buffalo Bills'],
['New Orleans Saints'],
['Kansas City Chiefs'],
['Atlanta Falcons'],
['Cleveland Browns'],
['Pittsburgh Steelers'],
['Las Vegas Raiders'],
['Denver Broncos'],
['Tampa Bay Buccaneers'],
['Seattle Seahawks'],
['San Francisco 49ers'],
['Philadelphia Eagles','49 total points']
],
"week_4":[
['Cincinnati Bengals'],
['Atlanta Falcons'],
['Detroit Lions'],
['Tennessee Titans'],
['Cleveland Browns'],
['Miami Dolphins'],
['Carolina Panthers'],
['New Orleans Saints'],
['Kansas City Chiefs'],
['Buffalo Bills'],
['Arizona Cardinals'],
['San Francisco 49ers'],
['Baltimore Ravens'],
['Green Bay Packers'],
['Tampa Bay Buccaneers'],
['Los Angeles Chargers','48 total points']
]
}

teamsReference = [
'Arizona Cardinals','Atlanta Falcons',
'Baltimore Ravens','Buffalo Bills',
'Carolina Panthers','Chicago Bears','Cincinnati Bengals','Cleveland Browns',
'Dallas Cowboys','Denver Broncos','Detroit Lions',
'Green Bay Packers',
'Houston Texans',
'Indianapolis Colts',
'Jacksonville Jaguars',
'Kansas City Chiefs',
'Los Angeles Chargers','Los Angeles Rams','Las Vegas Raiders',
'Miami Dolphins','Minnesota Vikings',
'New England Patriots','New Orleans Saints','New York Giants','New York Jets',
'Philadelphia Eagles','Pittsburgh Steelers',
'San Francisco 49ers','Seattle Seahawks',
'Tampa Bay Buccaneers','Tennessee Titans',
'Washington Football Team'
]

teamLogos = [
['Arizona Cardinals','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/ari.png" width="40"></img>'],
['Atlanta Falcons','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/atl.png" width="40"></img>'],
['Baltimore Ravens','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/bal.png" width="40"></img>'],
['Buffalo Bills','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/buf.png" width="40"></img>'],
['Carolina Panthers','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/car.png" width="40"></img>'],
['Chicago Bears','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/chi.png" width="40"></img>'],
['Cincinnati Bengals','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/cin.png" width="40"></img>'],
['Cleveland Browns','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/cle.png" width="40"></img>'],
['Dallas Cowboys','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/dal.png" width="40"></img>'],
['Denver Broncos','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/den.png" width="40"></img>'],
['Detroit Lions''<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/det.png" width="40"></img>'],
['Green Bay Packers','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/gb.png" width="40"></img>'],
['Houston Texans','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/hou.png" width="40"></img>'],
['Indianapolis Colts','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/ind.png" width="40"></img>'],
['Jacksonville Jaguars','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/jax.png" width="40"></img>'],
['Kansas City Chiefs','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/kc.png" width="40"></img>'],
['Los Angeles Chargers','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/lac.png" width="40"></img>'],
['Los Angeles Rams','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/lar.png" width="40"></img>'],
['Las Vegas Raiders','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/lvr.png" width="40"></img>'],
['Miami Dolphins','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/mia.png" width="40"></img>'],
['Minnesota Vikings','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/min.png" width="40"></img>'],
['New England Patriots','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/ne.png" width="40"></img>'],
['New Orleans Saints','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/no.png" width="40"></img>'],
['New York Giants','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/nyg.png" width="40"></img>'],
['New York Jets','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/nyj.png" width="40"></img>'],
['Philadelphia Eagles','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/phi.png" width="40"></img>'],
['Pittsburgh Steelers','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/pit.png" width="40"></img>'],
['San Francisco 49ers','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/sf.png" width="40"></img>'],
['Seattle Seahawks','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/sea.png" width="40"></img>'],
['Tampa Bay Buccaneers','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/tb.png" width="40"></img>'],
['Tennessee Titans','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/ten.png" width="40"></img>'],
['Washington Football Team','<img src="https://cwentworth.github.io/nfl-2021/imgs/teams/was.png" width="40"></img>']
]

teamLogosDf = pandas.DataFrame(teamLogos)
teamLogosDf.columns = ['Team Name','Team']
teamLogosDf = teamLogosDf[[
'Team Name','Team'
]]


personalPicksFlat = []
meechPoolSummary = {}
for wk in wks:
    if wk in meechPoolPicks.keys():
        personalPicks = meechPoolPicks[wk]
        wwins = 0
        for index, item in enumerate(personalPicks):
            personalPicksFlat.append(personalPicks[index][0])
            if wk in season.keys():
                if personalPicks[index][0] in season[wk]:
                    wwins = wwins + 1
                    meechPoolSummary[wk]=wwins

mpTotal = []
for wk in wks:
    if wk in meechPoolSummary.keys():
        mpTotal.append(meechPoolSummary[wk])


chris = [
'San Francisco 49ers',
'Baltimore Ravens',
'Los Angeles Chargers',
'Miami Dolphins',
'New England Patriots',
'New Orleans Saints',
'Pittsburgh Steelers',
'Atlanta Falcons',
'Philadelphia Eagles',
'New York Jets'
]

matt = [
'Tampa Bay Buccaneers',
'Buffalo Bills',
'Los Angeles Rams',
'Seattle Seahawks',
'Dallas Cowboys',
'Minnesota Vikings',
'Arizona Cardinals',
'Carolina Panthers',
'Denver Broncos',
'Jacksonville Jaguars'
]

dennis = [
'Kansas City Chiefs',
'Green Bay Packers',
'Cleveland Browns',
'Tennessee Titans',
'Washington Football Team',
'Indianapolis Colts',
'Chicago Bears',
'Las Vegas Raiders',
'Cincinnati Bengals',
'New York Giants'
]

teamPickSummary = []

for i in dennis:
    teamPickSummary.append(["Dennis",i])

for i in chris:
    teamPickSummary.append(["Chris",i])

for i in matt:
    teamPickSummary.append(["Matt",i])

teamPickSummaryDf = pandas.DataFrame(teamPickSummary)
teamPickSummaryDf.columns = ['Player','Team Name']
teamPickSummaryDf = teamPickSummaryDf[[
'Team Name','Player'
]]
teamPickSummaryDf.sort_values(['Player', 'Team Name'])
teamPickSummaryDf = pandas.merge(teamPickSummaryDf,teamLogosDf,on='Team Name',how='left')
teamPickSummaryDf = teamPickSummaryDf[[
'Team','Player'
]]

summary ={}
sus = []

for wk in wks:
    cw = 0
    mw = 0
    dw = 0
    if wk in season.keys():
        for t in chris:
            if t in season[wk]:
                cw = cw + 1
        sus.append([str(wk),"Chris",cw])
        for t in matt:
            if t in season[wk]:
                mw = mw + 1
        sus.append([str(wk),"Matt",mw])
        for t in dennis:
            if t in season[wk]:
                dw = dw + 1
        sus.append([str(wk),"Dennis",dw])

sus2 = pandas.DataFrame(sus)
sus2.columns = ['Week','Player','Wins']
sus2['weekNumber'] = sus2['Week'].str.replace('week_', '', regex=False)
sus2['weekNumber'] = pandas.to_numeric(sus2['weekNumber'])

susChris = sus2[sus2['Player']=='Chris']
susChris = susChris[[
'weekNumber',
'Wins'
]]
susChris.columns = ['Week','Wins - Chris']
susChris.sort_values(['Week'])
susChris = susChris.set_index('Week')
susChris.loc['Total']= susChris.sum()

susDennis = sus2[sus2['Player']=='Dennis']
susDennis = susDennis[[
'weekNumber',
'Wins'
]]
susDennis.columns = ['Week','Wins - Dennis']
susDennis.sort_values(['Week'])
susDennis = susDennis.set_index('Week')
susDennis.loc['Total']= susDennis.sum()

susMatt = sus2[sus2['Player']=='Matt']
susMatt = susMatt[[
'weekNumber',
'Wins'
]]
susMatt.columns = ['Week','Wins - Matt']
susMatt.sort_values(['Week'])
susMatt = susMatt.set_index('Week')
susMatt.loc['Total']= susMatt.sum()

finalOutput = pandas.merge(susChris,susDennis,on='Week',how='left')
finalOutput = pandas.merge(finalOutput,susMatt,on='Week',how='left')

weekPicksSummary = []
for index, item in enumerate(teamsReference):
    target = item
    pickCt = 0
    successCt = 0
    for index, item in enumerate(personalPicksFlat):
        if item == target:
            pickCt = pickCt+1
    for index, item in enumerate(winsAll):
        if item == target:
            successCt = successCt+1
    if pickCt == 0:
        successPct = 0
    else :
        successPct = successCt/pickCt
    weekPicksSummary.append([target,pickCt,successCt])


f = open('index.html','r')
html_content = f.read()
hc = BeautifulSoup(html_content,features="lxml")
standingsTable = hc.find('table',attrs={'id':'standings'})
standingsTable.decompose()

picksTable = hc.find('table',attrs={'id':'teamPicks'})
picksTable.decompose()

updateField = hc.find('p',attrs={'id':'updates'})
updateField.decompose()

headTwo = hc.find('h2',attrs={'id':'secondH'})
headTwo.decompose()

teamPickSummaryDf.style.set_properties(**{'text-align': 'center'})
picksTableHtml = teamPickSummaryDf.to_html(table_id='teamPicks',classes=['compact', 'hover', 'stripe'],justify='center',index=False,escape=False)
picksTableHtmls = BeautifulSoup(picksTableHtml,features="lxml")


finalOutput.style.set_properties(**{'text-align': 'center'})
standingsHtml = finalOutput.to_html(table_id='standings',classes=['compact', 'hover', 'stripe'],justify='center')
standingsHtmls = BeautifulSoup(standingsHtml,features="lxml")

body = hc.find('body')

body.append(standingsHtmls)

randVcode = str(random.choice(string.ascii_letters) +  random.choice(string.digits) + random.choice(string.digits) + "_" + random.choice(string.ascii_letters))

updatedField = "<p id='updates'>" + "updated: " + str(datetime.now().strftime('%Y-%m-%d')) + " ...version: " + str(randVcode) + "</p>"
updatedFields = BeautifulSoup(updatedField,features="lxml")

secondHead = "<h2 id='secondH'><br></br>Pick Summary</h2>"
secondHeads = BeautifulSoup(secondHead,features="lxml")

body.append(secondHeads)
body.append(picksTableHtmls)
body.append(updatedFields)
f.close()

htmlFinal = hc.prettify("utf-8")
with open("index.html", "wb") as file:
    file.write(htmlFinal)


patLoc = open("/Users/kennylofton/Documents/projects/ghpat.txt","r")
pat = patLoc.read()
print(pat)

os.chdir('/Users/kennylofton/Documents/GitHub/cwentworth.github.io/nfl-2021/')

#Commit Message
commit_message = "update" + str(datetime.now().strftime('%Y-%m-%d'))

#Stage the file
call('git add .', shell = True)

# Add your commit
call('git commit -m "'+ commit_message +'"', shell = True)

callCmd = 'git push https://' + pat + '@github.com/cwentworth/cwentworth.github.io.git'

call(callCmd, shell = True)

print('*****************************')
print('*****************************')
print('*****************************')
print('meech pool summary:')
for key in meechPoolSummary:
    print(key + ': ' + str(meechPoolSummary[key]) + ' / ' + str(len(meechPoolPicks[key])))
print('*****************************')
print("total wins: " + str(sum(mpTotal)) + " / " + str(len(winsAll)) + " total potential wins: ")
print("winning percentage: " + str(round((sum(mpTotal)/len(winsAll)),4)))

for i in weekPicksSummary:
    print(i)

for index,item in enumerate(meechPoolPicks["week_4"]):
    if index + 1 == len(meechPoolPicks["week_4"]):
        print(item[0],"-",item[1])
    else:
        print(item[0])