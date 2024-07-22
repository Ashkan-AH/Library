let $=document
const tabselect=$.querySelectorAll("#tab-select")
const tabdiv=$.querySelectorAll("#tab-div")
console.log(tabdiv,tabselect);

tabselect.forEach((Element,index)=>{
    Element.addEventListener("click",()=>{
               tabdiv.forEach(div=>{
                div.classList.add("hide")
               })
                tabdiv[index].classList.remove("hide")
    })
})