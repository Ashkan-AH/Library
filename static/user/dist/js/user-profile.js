let useractivbtn=document.querySelectorAll("#nav")

let useractivediv=document.querySelectorAll("#tab")
let ftcosection=document.getElementById("ftcosection")


    
useractivbtn.forEach((button1,index1)=>{
    button1.addEventListener("click",()=>{
          useractivediv.forEach((div1)=>{
            div1.classList.add("hide")
          })
          useractivediv[index1].classList.remove('hide')
          ftcosection.classList.remove("hide")
          
        })
    })

