let commentbtn=document.querySelector("#comment-btn")
let commentsection=document.querySelector("#comment-section")
let value=document.querySelector(".value")
let cancelbtn=document.querySelector("#cancel-ratebtn")


  
  
  cancelbtn.addEventListener("click",()=>{
    commentsection.classList.add("hide")
   document.body.classList.remove("no-interaction")
   commentsection.classList.remove("interaction")
       
  })
  commentbtn.addEventListener("click",()=>{
    commentsection.classList.remove("hide")
    document.body.classList.add("no-interaction")
    commentsection.classList.add("interaction")
    
  })



/*
editalertbtn2.addEventListener("click",()=>{
  editalertdiv.classList.add("hide")
commentsection.classList.remove("no-interaction")
commentsection.classList.add("interaction")


})
*/