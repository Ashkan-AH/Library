
const tabselect=document.querySelectorAll("#tab-select")
const tabdiv=document.querySelectorAll("#tab-div")

tabselect.forEach((Element,index)=>{
    Element.addEventListener("click",()=>{
               tabdiv.forEach(div=>{
                div.classList.add("hide")
               })
                tabdiv[index].classList.remove("hide")
    })
})