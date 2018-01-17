//Page 16 

// Setting and Swapping
var myNumber = 42;
var myName = "Laurence";
var temp = myName;
myNumber = myName;
myName = temp;

// Print -52 to 1066
for(var num = -52; num<= 1066; num++){
	console.log(num);
}

// Don't Worry, Be Happy
function beCheerful(){
	for(num = 0; num<98; num++){
		console.log("good morning!")
	}
}

// Multiples of Three - but Not All
for(num=-300; num<=0; num+=3){
	if(num == -6 || num == -3){
		continue;
	}
	console.log(num);
}

// Print Integers with While
var num = 2000;
while(num<=5280){
	console.log(num);
	num++;
}

// You Say It's Your Birthday
function birthday(input){
	if (input == "1101" || input == "0111"){
		console.log("How did you know?");
	}
	else{
		console.log("Just another day...");
	}
}

// Leap Year
function leapYear(year){
	if((year%4===0 && year%100!==0) ||year%400===0)
		console.log(true);
	else
		console.log(false);
}

// Print and Count
var count = 0;
for(var num = 512; num<=4096; num++){
	if(num%5 ==0){
		console.log(num);
		count+=1;
	}
}
console.log("There are "+count+" multples of 5 between 512 and 4096.")


// Multiples of Six
var num = 0;
while(num<=60000){
	if(num%6==0){
		console.log(num);
	}
	num++;
}

// Counting, the Dojo Way
for(var num = 1; num<=100; num++){
	if(num%5 == 0){
		console.log("Coding");
		if(num%10 == 0)
		console.log("Coding Dojo");
	}
}

// What Do You Know?
function whatDoYouKknow(incoming){
	console.log(incoming);
}

// Whoa, That Sucker's Huge...
var sum = 0;
for(var num = -300000; num<=300000; num+=1){
	sum += num;
}
console.log(sum);

// Countdown By Fours
var num = 2016;
while(num>4){
	num-=4;
	console.log(num)
}

// Flexible Countdown
function flexibleCountdown(lowNum, highNum, mul){
	for(var num = highNum; lowNum<highNum; num -= mul){
		console.log(num);
		highNum-=mul;
	}
}

// THe Final Countdown
function theFinalCountdown(param1, param2, param3, param4){
	var num = param2;
	while(num<=param3){
		if (num%param1 == 0 && num !== param4) {
			console.log(num);
		}
		num++;
	}
}

//page 20

//Countdown
function countDown(num) {
    var arr = [];
    for (var num; num >= 0; num--){
        arr.push(num);
    }
    console.log(arr)
    console.log(arr.length)
}

//Print and return
function printAndReturn(arr){
    console.log(arr[0])
    return arr[1]
}

//First Plus Length
function firstPlusLength(arr) {
    return arr[0]+arr.length
}

//Values Greater than Second
function greaterThanSecond(arr) {
    var count = 0;
    for (var i = 0; i <= arr.length; i++){
        if (arr[i]>arr[1]){
            count++
        }
    }
    return count;
}

//Values Graeter than Second, Generalized
function greaterThanSecondGeneralized(arr) {
    var count = 0;
    var newArr = [];
    if (arr.length > 0) {
        for (var i = 0; i <= arr.length; i++) {
            if (arr[i] > arr[1]) {
                newArr.push(arr[i]);
                count++;
            }
        }
    }
    else {
        console.log("There is only one value in the arrary")
    }
    return "New arrary is "+ newArr+ " and there are "+count+" values in the new array";
}


//This Length, That Value



//Fit the First IDBCursorWithValueFahrenheit to Celcius



//Celsius to Fahrenheit