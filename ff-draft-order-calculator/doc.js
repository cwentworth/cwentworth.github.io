var teams = ['team12','team11',
'team10','team9',
'team8','team7',
'team6','team5',
'team4','team3',
'team2','team1'
];

var weights = [
120,11,
10,9,
8,7,
6,5,
4,3,
2,1
];

hat = []
for (w in weights){
   zero = 0
   while (zero < weights[w]){
      hat.push(teams[w])
      zero++
   }
}

function shuffle(array) {
  var currentIndex = array.length
  var temporaryValue
  var randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    // randomIndex equals round down of a random number * the current index length
    // make the currentIndex be one less number
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

function populate() {
order = []
while (order.length < teams.length) {
   selection = Math.floor(Math.random() * hat.length);
   if (!order.includes(hat[selection])) {
      order.push(hat[selection]);
   }
}
return order;
}

teamDict = {}
for (t in teams) {
    teamDict[teams[t]] = 0
}

summary = {}
for (t in teams) {
   summary[t] = teamDict
}
