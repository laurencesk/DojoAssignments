//define function
function fancyArrary(arr,reverse,mark){
    //if user wants it in order
    if (reverse = false) {
      //loop for iterate array
        for(var i=0; i< arr.length; i++){
            console.log(i+" "+mark+" "+arr[i]);
        }
    }
    else{
        for(var i=arr.length-1; i>=0 ; i--){
            console.log(i+" "+mark+" "+arr[i]);
        }
    }
}
