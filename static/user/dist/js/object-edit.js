let row= document.querySelectorAll("#rowob")
let choose= document.querySelectorAll(".choosebtn")

choose.forEach((button,index)=>{
    button.addEventListener("click",()=>{
         row.forEach((div)=>{
            div.classList.add("hide")
          })
          row[index].classList.remove('hide')

        })  
    })
    





    /// image edit start


function previewImage(input,imageId,e) {
    
    const file=e.target.files[0]
    const filesize=file.size/1024/1024;
    if(filesize<3){
     
  const file1 = input.files[0];
  if (file && file.type === 'image/jpeg') {
    const reader = new FileReader();
    reader.onload = function (e) {
      const imgElement = document.getElementById(imageId);
      imgElement.src = e.target.result; // تنظیم محتوای تصویر برای نمایش
    };
    reader.readAsDataURL(file1);
  } else {
    alert('لطفاً فقط فایل‌های JPG را انتخاب کنید.');
  }
}
else{
    
        alert("حجم تصویر باید زیر 3مگابایت باشد")
        input.value=""
    }
    }
    ////
    