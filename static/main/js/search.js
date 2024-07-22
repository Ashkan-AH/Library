
let alertion=document.getElementById("alertion")
let alertiontext=document.getElementById("alertion-text")
let searchinput=document.getElementById("search-input")

let searchbtn=document.getElementById("search-btn")
let navsrarch=document.getElementById("nav-search")

let resultcontainer=document.getElementById("result-container")

searchbtn.addEventListener("click",(event)=>{
event.preventDefault()

 
if(searchinput1.value!="")
{  
    const searchterm=searchinput1.value
    const xhr=new XMLHttpRequest();
    xhr.open('get','/search-results?q='+searchterm);
    xhr.onload=()=>{
         if(xhr.status===200){
          resultcontainer.innerHTML=xhr.responseText;
         }
         else{
            

alertion.classList.remove("hide")
alertiontext.innerText="   خطایی در جست جو رخ داد    "
setTimeout(
    ()=>{
        alertion.classList.add("hide")
      alertiontext.innerText=""   
    }
,3000  )
         }


    }
xhr.send();
}
else{
    
alertion.classList.remove("hide")
alertiontext.innerText="لطفا قسمت جست و جو را پر کنید"
setTimeout(
    ()=>{
        alertion.classList.add("hide")
      alertiontext.innerText=""   
    }
,3000  )
         
}
 
  
})



window.addEventListener("scroll",(event)=>{
if(scrollY<=300){
navsrarch.classList.add("hide")
}
else{navsrarch.classList.remove("hide")}
  
  }
  )




  searchinput.addEventListener("input",()=>{
    if(searchinput.value.length>0){
  
  
  
      resultcontainer.classList.remove("hide")
    }
    else{
      
      resultcontainer.classList.add("hide")
      
  
    }
    })
    
    