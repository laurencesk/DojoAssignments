for(var daysUntilMyBirthday = 60; daysUntilMyBirthday>=0; daysUntilMyBirthday--){
    if(daysUntilMyBirthday>=30){
      console.log(daysUntilMyBirthday+" until my birthday. Such a long time...")
    }
    else if(daysUntilMyBirthday<30 && daysUntilMyBirthday >5){
      console.log(daysUntilMyBirthday+" until my birthday. My birthday is within a month!")
    }
    else if(daysUntilMyBirthday<5 && daysUntilMyBirthday !=0){
      console.log(daysUntilMyBirthday+" DAYS UNTIL MY BIRTHDAY!")
    }
    else if(daysUntilMyBirthday==0){
      console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*")
      console.log(";♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪")
      console.log("*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«")
    }
}
