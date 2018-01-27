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
    for(var i=0; i<arr.length; i++){
        if(typeof(arr[i]) !=="number"){
            for(var j = i; j<arr.length; j++){
              if(typeof(arr[j+1]) ==="number"){
                var temp = arr[j+1]
                arr[j+1] = arr[i]
                arr[i] = temp
                break
              }

            }
        }
    }
    for(var k = arr.length-1; k>=0; k--){
        if(typeof(arr[k]) !=="number"){
          arr.pop()
        }
    }
    return arr;
}
