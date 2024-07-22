let $=document
const captionmember=$.getElementById("pills-manufacturer-tab")
const captionwriter=$.getElementById("pills-review-tab")
const divdiscription=$.getElementById("pills-description1")
const divmember=$.getElementById("pills-manufacturer1")

captionmember.addEventListener("click",()=>{
    divmember.classList.remove("hide")
    divdiscription.classList.add("hide")
})

captionwriter.addEventListener("click",()=>{
    divmember.classList.add("hide")
    divdiscription.classList.remove("hide")
})

alert("maksfcndsiososiovbdsfou")