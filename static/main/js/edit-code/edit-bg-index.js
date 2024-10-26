
let bg3 =document.querySelector(".ftco-intro")
let bg2 =document.querySelector(".img-2")
let bg1 =document.querySelector(".hero-wrap")
let bg4=[bg1,bg2,bg3]
let formbtn=document.querySelector("#form-update-btn")
let form=document.querySelector("#form-update")

 

bg4.forEach((element,index)=>{
    element.id='image'+String(index+1)
})
bg4.forEach((element,index) => {
    element.insertAdjacentHTML("afterbegin",'<input type=file accept=".jpg" name="image'+String(index+1)+'" onchange="previewImage(this,'+"'"+'image'+String(index+1)+"'"+',event)"> <h3>ویرایش عکس</h3></div>')

});
    
formbtn.addEventListener("click",(event)=>{
   
let bgedit=document.querySelectorAll(".bg-edit input")
bgedit.forEach(element => {
    const final=element

    form.insertAdjacentElement("beforeend",final)
    console.log(final.value);
    
    
});

console.log(form);
})