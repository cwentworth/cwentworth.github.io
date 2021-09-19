import json
import requests
import pandas
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from subprocess import call
import os


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
  soup = BeautifulSoup(data)
  winners = soup.findAll("tr", {"class": "winner"})
  wins = []
  for row in winners:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    wins.append(cols[0])
    winsAll.append(cols[0])
    season[wk]=wins

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
]
}

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
teamPickSummaryDf.columns = ['Player','Team']
teamPickSummaryDf = teamPickSummaryDf[[
'Team','Player'
]]
teamPickSummaryDf.sort_values(['Player', 'Team'])


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
    weekPicksSummary.append([target,pickCt,successPct])


f = open('index.html','r')
html_content = f.read()
hc = BeautifulSoup(html_content)
standingsTable = hc.find('table',attrs={'id':'standings'})
standingsTable.decompose()

picksTable = hc.find('table',attrs={'id':'teamPicks'})
picksTable.decompose()

updateField = hc.find('p',attrs={'id':'updates'})
updateField.decompose()

updateField = hc.find('p',attrs={'id':'winpct'})
updateField.decompose()

headTwo = hc.find('h2',attrs={'id':'secondH'})
headTwo.decompose()

teamPickSummaryDf.style.set_properties(**{'text-align': 'center'})
picksTableHtml = teamPickSummaryDf.to_html(table_id='teamPicks',classes=['compact', 'hover', 'stripe'],justify='center',index=False)
picksTableHtmls = BeautifulSoup(picksTableHtml)


finalOutput.style.set_properties(**{'text-align': 'center'})
standingsHtml = finalOutput.to_html(table_id='standings',classes=['compact', 'hover', 'stripe'],justify='center')
standingsHtmls = BeautifulSoup(standingsHtml)

body = hc.find('body')

body.append(standingsHtmls)

updatedField = "<p id='updates'>" + "updated: " + str(datetime.now().strftime('%Y-%m-%d')) + "</p>"
updatedFields = BeautifulSoup(updatedField)

personalWinPct = "<p id='winpct'>" + "personal weekly picks win percentage in 2021: " + str(round((sum(mpTotal)/len(winsAll)),4)) + "</p>"
personalWinPcts = BeautifulSoup(personalWinPct)

secondHead = "<h2 id='secondH'><br></br>Pick Summary</h2>"
secondHeads = BeautifulSoup(secondHead)


body.append(secondHeads)
body.append(picksTableHtmls)
body.append(updatedFields)
body.append(personalWinPcts)

for index, item in enumerate(weekPicksSummary):
    body.append(BeautifulSoup("<p id=winpct>" + str(item) + "</p>"))

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

for index,item in enumerate(meechPoolPicks["week_2"]):
    if index + 1 == len(meechPoolPicks["week_2"]):
        print(item[0],"-",item[1])
    else:
        print(item[0])