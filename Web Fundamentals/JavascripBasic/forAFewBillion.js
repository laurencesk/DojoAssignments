var sum =0;
var current = 1

for(var i =1; i<=30; i++){
  if (i==1) {
    sum = 1
  }
  else {
    current*=2
    sum += current
    console.log(sum)
  }
}
console.log(sum/100)


Bonus

var payment = 0
var current = 1
for(var i =1;payment<=10000;i++){
    if (i==1) {
      sum = 1
    }
    else {
      current*=2
      payment += current
    }
}
console.log("i="+(i-1))
