let checkbox = document.getElementById("agree-term")
 let submitbtn=document.getElementById("signup")
let input =document.getElementById("email")
let input2 =document.getElementById("name")

let input3 =document.getElementById("pass")

let input4 =document.getElementById("re_pass")

if(input3.value==input4.value){
  



checkbox.addEventListener("change",()=>
  {
    if (checkbox.checked) 
    {
   
     //submitbtn.classList.add("interaction")
     submitbtn.classList.remove("no-interaction")
    }
   else 
    {    
     //submitbtn.classList.remove("interaction")
   
     submitbtn.classList.add("no-interaction")
    }    
 }    
 )      
}
