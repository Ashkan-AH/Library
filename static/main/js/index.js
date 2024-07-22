let $$=document
let searchinput=$$.getElementById("search-input")
let searchspan=$$.getElementById("search-span")

let resultcontainer=$$.getElementById("result-container")

console.log(resultcontainer);

searchinput.addEventListener("input",()=>{
  if(searchinput.value.length>0){

    searchspan.classList.add("hide")


    resultcontainer.classList.remove("hide")
  }
  else{
    
    resultcontainer.classList.add("hide")
    searchspan.classList.remove("hide")
    

  }
  })
  
  