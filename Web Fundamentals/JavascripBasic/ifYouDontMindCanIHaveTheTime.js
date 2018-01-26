
var HOUR = 8;
var MINUTE = 50;
var PERIOD = "AM";

if(HOUR ==8 && PERIOD == "AM"){
  if(MINUTE<30)
    console.log("It's just 8 in the morning")
  else
    console.log("It's almost 9 in the morning")

}
else if(HOUR ==7 && PERIOD == "PM"){
  if(MINUTE<30)
    console.log("It's just 8 in the evening")
  else
    console.log("It's almost 9 in the evening")
}
