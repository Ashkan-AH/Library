let commentbtn=document.querySelector("#comment-btn")
let commentsection=document.querySelector("#comment-section")
let value=document.querySelector(".value")
let cancelbtn=document.querySelector("#cancel-ratebtn")
let stars =document.querySelectorAll('.fa-star')


  
  
  cancelbtn.addEventListener("click",()=>{
    commentsection.classList.add("hide")
   document.body.classList.remove("no-interaction")
   commentsection.classList.remove("interaction")
       
  })
  commentbtn.addEventListener("click",()=>{
    commentsection.classList.remove("hide")
    document.body.classList.add("no-interaction")
    commentsection.classList.add("interaction")
    console.log("درست");
    
  })



/*
editalertbtn2.addEventListener("click",()=>{
  editalertdiv.classList.add("hide")
commentsection.classList.remove("no-interaction")
commentsection.classList.add("interaction")


})
*/
stars.forEach((star,index)=>{
  
    star.addEventListener("click",()=>{
        const st=index
        if (st.classList!="checked")
        {
            
          for (let i = 0; i <=st; i++)
             {
               stars[i].classList.add("checked")

               for (let t = stars.length-1; t >st; t--) 
                {
                 stars[t].classList.remove("checked")
                
                }
             }  
        }
        
    })
})

