function numbersOnly(arr){
    var newArr = [];
    for(var i=0; i<arr.length; i++){
        if(typeof(arr[i]) ==="number"){
            newArr.push(arr[i])
        }
    }
    return newArr;
}


function numbersOnlyInline(arr){
    var count = 0;
    for(var i=0; i < arr.length; i++){
        if(typeof(arr[i]) !=="number"){
            for(var j = i+1; j < arr.length; j++ ){
                if(typeof(arr[j]) =='number'){
                  temp = arr[j]
                  arr[j] = arr[i]
                  arr[i] = temp
                  count++
                  break
                }
            }
        }
    }
    for(var i = 1; i<count; i++){
      arr.pop()
    }
      return arr;
}
