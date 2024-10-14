
let val=$$.querySelectorAll("#bookday")

 /////////////////////////
val.forEach((element,index)=>{
    let timeread=element.querySelector("#time-read-label")
    let pie=element.querySelector("#pie")
    let pieinnervalue=element.querySelector("#pie-inner-value")

   
    let timereadnumber=Number(timeread.innerText) 
    let pievalue=100/14
    console.log(timereadnumber);
    
pie.style.background="conic-gradient(#01d28e 0"+timereadnumber*pievalue+"%"+", #eaeaea 0)"
pieinnervalue.innerText=timeread.innerText

  
if(timereadnumber<=3){
  
    pie.style.background="conic-gradient(red 0"+timereadnumber*pievalue+"%"+", #eaeaea 0)"
    pieinnervalue.style.color="red"
}  
}
)



/////////////////////////












