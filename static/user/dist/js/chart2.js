
let val2=$$.querySelectorAll("#bookday-2")

 /////////////////////////
val2.forEach((element,index)=>{
    let timeread=element.querySelector("#time-read-label-2")
    let pie=element.querySelector("#pie-2")
    let pieinnervalue=element.querySelector("#pie-inner-value-2")

   
    let timereadnumber=Number(timeread.innerText) 
    let pievalue=100/7
    console.log(timereadnumber);
    
pie.style.background="conic-gradient(#01d28e 0"+timereadnumber*pievalue+"%"+", #eaeaea 0)"
pieinnervalue.innerText=timeread.innerText

  
if(timereadnumber<=2){
  
    pie.style.background="conic-gradient(red 0"+timereadnumber*pievalue+"%"+", #eaeaea 0)"
    pieinnervalue.style.color="red"
}  
}
)



/////////////////////////










