
const bg=document.querySelector(".hero-wrap")
bg.id='image1'
bg.insertAdjacentHTML("afterbegin",' <div class="bg-edit"><input type=file accept=".jpg" onchange="previewImage(this,'+"'"+'image1'+"'"+',event)"> <h3>ویرایش عکس</h3></div>')
