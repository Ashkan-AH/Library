const captionmember=document.getElementById("pills-manufacturer-tab")
const captionwriter=document.getElementById("pills-review-tab")
const divdiscription=document.getElementById("pills-description1")
const divmember=document.getElementById("pills-manufacturer1")

captionmember.addEventListener("click",()=>{
    divmember.classList.remove("hide")
    divdiscription.classList.add("hide")
})

captionwriter.addEventListener("click",()=>{
    divmember.classList.add("hide")
    divdiscription.classList.remove("hide")
})
