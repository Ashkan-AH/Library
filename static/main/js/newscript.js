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
let timeread=$$.getElementById("time-read-label")
let pie=$$.getElementById("pie")
let pieinnervalue=$$.getElementById("pie-inner-value")
let rentbtnstyle=$$.getElementById("rent-btn-style")
let againbtn=$$.createElement('button')
let rentbtn=$$.getElementById('rent-btn')
let commentbtn=$$.querySelectorAll('#comment-btn')
let commentsection=$$.getElementById('comment-section')

let editalertbtn1=$$.getElementById("edit-alert-btn1-2")
let editalertbtn2 =$$.getElementById("edit-alert-btn2-2")
let editalertdiv=$$.getElementById("edit-alertdiv-2")

let timegive=$$.getElementById("time-give-label")

let pieinnervalue2=$$.getElementById("pie-inner-value2")
let cancelratebtn=$$.getElementById('cancel-ratebtn')
let textarea=$$.getElementById('textarea')

let timereadnumber=Number(timeread.innerText)
let pievalue=100/14

let timegetreadnumber=Number(timegive.innerText)
let pie2value=100/7

againbtn.innerText="درخواست تمدید"
pie.style.background="conic-gradient(#01d28e 0"+timereadnumber*pievalue+"%"+", #eaeaea 0)"

pie2.style.background="conic-gradient(#01d28e 0"+timegetreadnumber*pie2value+"%"+", #eaeaea 0)"
pieinnervalue.innerText=timeread.innerText

pieinnervalue2.innerText=timegive.innerText
if(timereadnumber<=2){
  
pie.style.background="conic-gradient(red 0"+timereadnumber*pievalue+"%"+", #eaeaea 0)"
pieinnervalue.style.color="red"

againbtn.classList.add("again-btn")
rentbtnstyle.appendChild(againbtn)
rentbtn.style.display="none"

}

if(timegetreadnumber<=2){
  
  pie2.style.background="conic-gradient(red 0"+timegetreadnumber*pie2value+"%"+", #eaeaea 0)"
  pieinnervalue2.style.color="red"
  
  
  }

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
          bookactivitititle.classList.add('hide')

        })  
    })
    
useractivbtn.forEach((button1,index1)=>{
    button1.addEventListener("click",()=>{
          useractivediv.forEach((div1)=>{
            div1.classList.add("hide")
          })
          useractivediv[index1].classList.remove('hide')
          noactivetitle.classList.add("hide")
          ftcosection.classList.remove("hide")
          
        })
    })


    commentbtn.forEach(elment =>{
      elment.addEventListener("click",()=>{
        commentsection.classList.remove("hide")
       $$.body.classList.add("no-interaction")
       commentsection.classList.add("interaction")
           

       
      })

    })

       cancelratebtn.addEventListener("click",(event)=>{
    event.preventDefault()
        commentsection.classList.remove("interaction")
        commentsection.classList.add("no-interaction")

        editalertdiv.classList.remove("hide")
        editalertdiv.classList.add("interaction")

        editalertbtn1.addEventListener("click",()=>{

        commentsection.classList.add("hide")
        $$.body.classList.remove("no-interaction")
        commentsection.classList.remove("interaction")
        editalertdiv.classList.add("hide")
        textarea.value=""

        })

        editalertbtn2.addEventListener("click",()=>{
          editalertdiv.classList.add("hide")
        commentsection.classList.remove("no-interaction")
        commentsection.classList.add("interaction")


        })
        
       })
             
       