import json
import requests
import pandas
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt


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
]

season = {}
winsAll = []

for wk in wks:
  u = str("https://www.pro-football-reference.com/years/2020/" + wk + ".htm")
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
'Kansas City Chiefs',
'New England Patriots',
'Baltimore Ravens',
'Buffalo Bills',
'Las Vegas Raiders',
'Seattle Seahawks',
'Philadelphia Eagles',
'Detroit Lions',
'Indianapolis Colts',
'Green Bay Packers',
'Cincinnati Bengals',
'San Francisco 49ers',
'New Orleans Saints',
'Dallas Cowboys',
'Pittsburgh Steelers',
'Denver Broncos'
],
"week_2":[
''
],
"week_3":[
''
],
"week_4":[
''
],
"week_5":[
''
],
"week_6":[
''
],
"week_7":[
''
],
"week_8":[
''
],
"week_9":[
''
],
"week_10":[
''
],
"week_11":[
''
],
"week_12":[
''
],
"week_13":[
''
],
"week_14":[
''
],
"week_15":[
''
],
"week_16":[
''
],
"week_17":[
''
]
}

meechPoolSummary = {}
for wk in wks:
    if wk in meechPoolPicks.keys():
        personalPicks = meechPoolPicks[wk]
        wwins = 0
        for index, item in enumerate(personalPicks):
            if wk in season.keys():
                if personalPicks[index] in season[wk]:
                    wwins = wwins + 1
                    meechPoolSummary[wk]=wwins






chris = [
'San Francisco 49ers',
'Buffalo Bills',
'Dallas Cowboys',
'Indianapolis Colts',
'Cleveland Browns',
'Houston Texans',
'Las Vegas Raiders',
'Detroit Lions',
'Cincinnati Bengals',
'Washington Football Team'
]

matt = [
'Baltimore Ravens',
'New Orleans Saints',
'Seattle Seahawks',
'Tampa Bay Buccaneers',
'New England Patriots',
'Chicago Bears',
'Los Angeles Rams',
'Atlanta Falcons',
'New York Giants',
'Carolina Panthers'
]

dennis = [
'Kansas City Chiefs',
'Green Bay Packers',
'Philadelphia Eagles',
'Pittsburgh Steelers',
'Minnesota Vikings',
'Tennessee Titans',
'Denver Broncos',
'Miami Dolphins',
'Arizona Cardinals',
'Los Angeles Chargers'
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



f = open('index.html','r')
html_content = f.read()
hc = BeautifulSoup(html_content)
standingsTable = hc.find('table',attrs={'id':'standings'})
standingsTable.decompose()

picksTable = hc.find('table',attrs={'id':'teamPicks'})
picksTable.decompose()

teamPickSummaryDf.style.set_properties(**{'text-align': 'center'})
picksTableHtml = teamPickSummaryDf.to_html(table_id='teamPicks',classes=['compact', 'hover', 'stripe'],justify='center',index=False)
picksTableHtmls = BeautifulSoup(picksTableHtml)


finalOutput.style.set_properties(**{'text-align': 'center'})
standingsHtml = finalOutput.to_html(table_id='standings',classes=['compact', 'hover', 'stripe'],justify='center')
standingsHtmls = BeautifulSoup(standingsHtml)

body = hc.find('body')

body.append(standingsHtmls)

secondth = "<h2><br></br>Pick Summary</h2>"
secondTableHeader = BeautifulSoup(secondth)

body.append(secondTableHeader)

body.append(picksTableHtmls)
f.close()

htmlFinal = hc.prettify("utf-8")
with open("index.html", "wb") as file:
    file.write(htmlFinal)

print(meechPoolSummary)
