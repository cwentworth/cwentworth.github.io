function randomDraw(mn,mx) {
    mn = Math.ceil(mn);
    mx = Math.floor(mx);
    return Math.floor(Math.random() * (mx-mn) + mn)
}

outputSingleNumber = document.createTextNode('number one to one-hundred: ' + randomDraw(0,100))

function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}
outputTxtCode = document.createTextNode('code: ' + makeid(4) + '-' + makeid(4) + '-' + makeid(4))

animals = ['cat',
'dog',
'bird',
'monkey',
'bear',
'penguin',
'giraffe',
'frog',
'fish',
'mouse',
'tiger',
'pig',
'sheep',
'otter',
'wolf',
'puffin'
]

outputAnimals = document.createTextNode('animal: ' + animals[randomDraw(0,animals.length)])

foods = [
'american',
'bbq',
'chinese',
'cajun',
'thai',
'fast food',
'pizza',
'italian',
'steak',
'seafood',
'mexican',
'soup',
'salad',
'cold sandwiches',
'hot sandwiches',
'chicken wings',
'apps'
]
outputFoods = document.createTextNode('food: ' + foods[randomDraw(0,foods.length)])

nflTeams = [
    'Arizona Cardinals',
    'Atlanta Falcons',
    'Baltimore Ravens',
    'Buffalo Bills',
    'Carolina Panthers',
    'Chicago Bears',
    'Cincinnati Bengals',
    'Cleveland Browns',
    'Dallas Cowboys',
    'Denver Broncos',
    'Detroit Lions',
    'Green Bay Packers',
    'Houston Texans',
    'Indianapolis Colts',
    'Jacksonville Jaguars',
    'Kansas City Chiefs',
    'Los Angeles Chargers',
    'Los Angeles Rams',
    'Las Vegas Raiders',
    'Miami Dolphins',
    'Minnesota Vikings',
    'New England Patriots',
    'New Orleans Saints',
    'New York Giants',
    'New York Jets',
    'Philadelphia Eagles',
    'Pittsburgh Steelers',
    'San Francisco 49ers',
    'Seattle Seahawks',
    'Tampa Bay Buccaneers',
    'Tennessee Titans',
    'Washington Football Team'
    ]
outputNFLTeam = document.createTextNode('nfl team: ' + nflTeams[randomDraw(0,nflTeams.length)])

coinFlip = ['heads','tails']
outputCoinFlip = document.createTextNode('coin flip: ' + outputCoinFlip[randomDraw(0,outputCoinFlip.length)])


window.onload = function(){
    document.querySelector('#disp').appendChild(outputAnimals);
    document.querySelector('#disp').appendChild(document.createElement("br"));
    document.querySelector('#disp').appendChild(outputFoods);
    document.querySelector('#disp').appendChild(document.createElement("br"));
    document.querySelector('#disp').appendChild(outputTxtCode);
    document.querySelector('#disp').appendChild(document.createElement("br"));
    document.querySelector('#disp').appendChild(outputSingleNumber);
    document.querySelector('#disp').appendChild(document.createElement("br"));
    document.querySelector('#disp').appendChild(outputNFLTeam);
    document.querySelector('#disp').appendChild(document.createElement("br"));
    document.querySelector('#disp').appendChild(outputCoinFlip);
}