//Page 16 

// Setting and Swapping
var myNumber = 42;
var myName = "Laurence";
var temp = myName;
myNumber = myName;
myName = temp;

// Print -52 to 1066
for (var num = -52; num <= 1066; num++) {
    console.log(num);
}

// Don't Worry, Be Happy
function beCheerful() {
    for (num = 0; num < 98; num++) {
        console.log("good morning!")
    }
}

// Multiples of Three - but Not All
for (num = -300; num <= 0; num += 3) {
    if (num == -6 || num == -3) {
        continue;
    }
    console.log(num);
}

// Print Integers with While
var num = 2000;
while (num <= 5280) {
    console.log(num);
    num++;
}

// You Say It's Your Birthday
function birthday(input) {
    if (input == "1101" || input == "0111") {
        console.log("How did you know?");
    }
    else {
        console.log("Just another day...");
    }
}

// Leap Year
function leapYear(year) {
    if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0)
        console.log(true);
    else
        console.log(false);
}

// Print and Count
var count = 0;
for (var num = 512; num <= 4096; num++) {
    if (num % 5 == 0) {
        console.log(num);
        count += 1;
    }
}
console.log("There are " + count + " multples of 5 between 512 and 4096.")


// Multiples of Six
var num = 0;
while (num <= 60000) {
    if (num % 6 == 0) {
        console.log(num);
    }
    num++;
}

// Counting, the Dojo Way
for (var num = 1; num <= 100; num++) {
    if (num % 5 == 0) {
        console.log("Coding");
        if (num % 10 == 0)
            console.log("Coding Dojo");
    }
}

// What Do You Know?
function whatDoYouKknow(incoming) {
    console.log(incoming);
}

// Whoa, That Sucker's Huge...
var sum = 0;
for (var num = -300000; num <= 300000; num += 1) {
    sum += num;
}
console.log(sum);

// Countdown By Fours
var num = 2016;
while (num > 4) {
    num -= 4;
    console.log(num)
}

// Flexible Countdown
function flexibleCountdown(lowNum, highNum, mul) {
    for (var num = highNum; lowNum < highNum; num -= mul) {
        console.log(num);
        highNum -= mul;
    }
}

// THe Final Countdown
function theFinalCountdown(param1, param2, param3, param4) {
    var num = param2;
    while (num <= param3) {
        if (num % param1 == 0 && num !== param4) {
            console.log(num);
        }
        num++;
    }
}

//page 20

//Countdown
function countDown(num) {
    var arr = [];
    for (var num; num >= 0; num--) {
        arr.push(num);
    }
    console.log(arr)
    console.log(arr.length)
}

//Print and return
function printAndReturn(arr) {
    console.log(arr[0])
    return arr[1]
}

//First Plus Length
function firstPlusLength(arr) {
    return arr[0] + arr.length
}

//Values Greater than Second
function greaterThanSecond(arr) {
    var count = 0;
    for (var i = 0; i <= arr.length; i++) {
        if (arr[i] > arr[1]) {
            count++
        }
    }
    return count;
}

//Values Graeter than Second, Generalized
function greaterThanSecondGeneralized(arr) {
    var count = 0;
    var newArr = [];
    if (arr.length > 1) {
        for (var i = 0; i <= arr.length; i++) {
            if (arr[i] > arr[1]) {
                newArr.push(arr[i]);
                count++;
            }
        }
        return ("New arrary is " + newArr + " and there are " + count + " values in the new array")
    }
    else {
        return ("There is only one or no value in the arrary")
    }
}
//This Length, That Value
function thisLengthThatValue(num1, num2) {
    var arr = [num1, num2]
    if (num1 == num2) {
        console.log("Jinx")
    }
    console.log(arr.length)
}

//Fit the First Value
function fitTheFirstValue(arr) {
    if (arr[0] > arr.length) {
        console.log("Too Big")
    }
    else if (arr[0] < arr.length) {
        console.log("Too small")
    }
    else {
        console.log("Just right!")
    }
}

//Fahrenheit to Celcius
function fahrenheitToCelsius(fDegrees) {
    celsius = (fDegrees - 32) * 5 / 9
    return celsius
}

//Celsius to Fahrenheit
function celsiusToFahrenheit(cDegrees) {
    fahrenheit = (cDegrees * 9 / 5) + 32
    return fahrenheit
}

//Page 22
//Biggie Size
function makeItBig(arr) {
     for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            arr[i] = 'big'
        }
        else {
            arr[i] = arr[i]
        }  
    }
    return arr;
}

//Print Low, Return High
function printLowReturnHigh(arr) {
    var max = arr[0];
    var min = arr[0];
    for (var i = 0; i < arr.length; i++){
        if (arr[i] > max) {
            max = arr[i]
        }
        if (arr[i] < min) {
            min = arr[i]
        }
    }
    console.log(min);
    return max;
}

//Print One, Return Another
function printonereturnanother(arr) {
    for (var i = 0; i < arr.length; i++){
        if (arr[i] % 2 === 1) {
            var odd = arr[i];
            break;
        }
    }
    console.log(arr[arr.length - 2]);
    return odd;
}

//Double Visiion
function double(arr) {
    newArr = [];
    for (var i = 0; i < arr.length; i++) {
        newArr.push(arr[i]*2)
        }
    return newArr
}

//Count Positives
function countPositives(arr) {
//I don't follow the question.'
}

//Evens and Odds
function evensAndOdss(arr) {
    var even = 0
    var odd = 0
    for (var i = 0; i < arr.length; i++) {

        if (arr[i] % 2 == 0) {
            even++
            if (even == 3) {
                return 'even more so'
            }
        }
        if (arr[i] % 2 != 0) {
            odd++
            if (odd == 3) {
                return "that's odd"
            }
        }
    }
}

//Increment the Seconds
function incrementTheSeconds(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 !==0) {
            arr[i]+=1
        }
    }
    console.log(arr)
}

//Previous Lengths
function previousLengths(arr) {
   for (var i = 0; i < arr.length; i++) {
       if (typeof arr[i] == 'string') {
            arr[i] = i
        }
    }
    return arr
}

//Add Seven to Most
function addSevenToMost(arr) {
    var newArr = []
    for (var i = 1; i < arr.length; i++) {
        newArr[i-1] = arr[i]+7
    }
    return newArr
}

//Reverse Arrary
function reverse(arr) {
    var newArr = [];
    for (var i = arr.length; i >= 0; i--) {
        newArr.push(arr[i])
    }
    return newArr;
}

//Outlook: Negative
function negative(arr) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i]>0){
            newArr.push(arr[i] * -1)
        }
        else {
           newArr.push(arr[i])
        }
    }
    return newArr;
}

//Always HUngry
function alwaysHungry(arr) {
    var food = 0
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] == 'food') {
            food ++
        }
    }
    if (food > 0) {
        return 'yummy'
    }
    else {
        return "I'm hungry"
    }
}

//Swap Toward the Center
function swapTowardTheCenter(arr) {
    var temp1 = arr[0]
    arr[0] = arr[arr.length-1]
    arr[arr.length-1] = temp1

    var temp2 = arr[2]
    arr[2] = arr[arr.length - 3]
    arr[arr.length - 3] = temp2

    return arr
}

//Scale the Arary
function scaleTheArray(arr,num) {
    for (var i = 0; i < arr.length; i++){
        arr[i]=arr[i]*num
    }
    return arr
}

