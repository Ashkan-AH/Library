
const bg=document.querySelector(".hero-wrap")

const currentUrl = window.location.href;

// گرفتن نام فایل با پسوند
const fileNameWithExtension = currentUrl.substring(currentUrl.lastIndexOf('/') + 1);

// پیدا کردن موقعیت نقطه (.) در نام فایل
const dotIndex = fileNameWithExtension.lastIndexOf('.');

// حذف پسوند و گرفتن نام فایل بدون پسوند
const fileNameWithoutExtension = fileNameWithExtension.substring(0, dotIndex);
bg.id='image1'
bg.insertAdjacentHTML("afterbegin",'<form action="/account/themes/update/'+fileNameWithoutExtension+'/" method="post"><div class="bg-edit"><input type=file accept=".jpg" name="image1" onchange="previewImage(this,'+"'"+'image1'+"'"+',event)"> <h3>ویرایش عکس</h3><button class="btn btn-danger" type="submit">تایید</button></div></form>')
