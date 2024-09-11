let $=document
const stars =$.querySelectorAll('.star-rate')

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
                console.log(st+1);
             }  
        }
        
    })
})