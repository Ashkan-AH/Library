
let bg3 =document.querySelector(".ftco-intro")
let bg2 =document.querySelector(".img-2")
let bg1 =document.querySelector(".hero-wrap")
let bg4=[bg1,bg2,bg3]
console.log(bg4);

let obj =document.querySelectorAll("#bg-edit")
 
bg4.forEach((element,index)=>{
    element.id='image'+String(index+1)
})
obj.forEach((element,index) => {
    element.insertAdjacentHTML("afterbegin",' <div class="bg-edit" "><input type=file accept=".jpg" onchange="previewImage(this,'+"'"+'image'+String(index+1)+"'"+',event)"> <h3>ویرایش عکس</h3></div>')

});
    


