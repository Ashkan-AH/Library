let checkbox = document.getElementById("agree-term")
 let submitbtn=document.getElementById("signup")
let input =document.getElementById("id_email")
let input2 =document.getElementById("id_username")

let input3 =document.getElementById("id_password1")

let input4 =document.getElementById("id_password2")

  



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
