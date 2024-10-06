  
let searchinput=document.querySelector(".form-control-navbar")
let searchlenght=searchinput.value.length
let searchform=document.querySelector(".show-val")

    searchform.insertAdjacentHTML("afterbegin",'<div class="search-value"><a href="#"><section><h6>پروین اعتصامی</h6><hr><p>شاعر و مویسنده معاصر ایران که  نام نیک شعرای معاصر را به دوش میکشد ...</p></section><img src="../../../uni-project/uni-project/images/down3load.jpg" alt=""></a></div>'
    )
let searchvalue=document.querySelector("search-value")
let resultcontainer=document.getElementById("result-container")



searchinput.addEventListener("input",()=>{

  if(searchinput.value.length>=1){
  
      searchform.style.display='block'

  }
  else
  
      searchform.style.display='none'
  
})


