const $$ =document


let animate=$$.querySelectorAll(".ftco-animate")
let userselectbtn=$$.querySelectorAll(".col-lg-3")
let userselectdiv=$$.querySelectorAll(".userp-book-prop")
let useractivbtn=$$.querySelectorAll("#nav")
let useractivediv=$$.querySelectorAll("#tab")
let profileusername=$$.querySelector(".profile-username")
let profileprop=$$.getElementById("prof-prop")
let rowbtn=$$.getElementById("row")
let profileuserimg=$$.querySelector(".profile-user-img")
let userimg=$$.getElementById("userimg")
let noactivetitle=$$.getElementById("no-active-title")
let ftcosection=$$.getElementById("ftcosection")
let bookactivitititle=$$.getElementById("bookactivitititle")
let rentbtn=$$.getElementById('rent-btn')
let commentbtn=$$.querySelectorAll('#comment-btn')
let commentsection=$$.getElementById('comment-section')

let editalertbtn1=$$.getElementById("edit-alert-btn1-2")
let editalertbtn2 =$$.getElementById("edit-alert-btn2-2")
let editalertdiv=$$.getElementById("edit-alertdiv-2")

let textarea=$$.getElementById('textarea')
 



ftcosection.classList.add("hide")
profileusername.innerText=profileprop.innerText 
profileuserimg.innerHTML=userimg.innerText
window.addEventListener("load",function(){
animate.forEach(element => {
    element.classList.remove("ftco-animate")
    element.style.transition='all 0.8s'
    
});

})


userselectbtn.forEach((button,index)=>{
    button.addEventListener("click",()=>{
          userselectdiv.forEach((div)=>{
            div.classList.add("hide")
          })
          userselectdiv[index].classList.remove('hide')

        })  
    })
    
useractivbtn.forEach((button1,index1)=>{
    button1.addEventListener("click",()=>{
          useractivediv.forEach((div1)=>{
            div1.classList.add("hide")
          })
          useractivediv[index1].classList.remove('hide')
          ftcosection.classList.remove("hide")
          
        })
    })


       
             
       