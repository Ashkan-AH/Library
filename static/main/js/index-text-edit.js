

const texthead1 = document.querySelectorAll('.textcontain-bgcolor *');
const services = document.querySelectorAll('.services-wrap h3');
const about = document.querySelectorAll('.justify-content-center ');
const warpabout = document.querySelectorAll('.wrap-about p , .wrap-about span, .wrap-about h2');
const endtext = document.querySelector('.ftco-intro h2');

let texthead=Array.from(texthead1);
texthead.push(endtext)

warpabout.forEach(element=>{
  texthead.push(element)

})
services.forEach(element => {
  texthead.push(element)
});



texthead[2].remove()

texthead.forEach((element,index) => {
  
    
  element.classList.add('textedit-bg')


  
  element.id =" text"+String(index); // اضافه کردن ID یکتا به هر تگ
  element.addEventListener('dblclick', () => {

      document.body.insertAdjacentHTML(
          'beforeend',' <div class="text-edit none"  id="editdiv-'+String(index)+'"'+'><h3>متن جدید را وارد کنید</h3><textarea type="text" id="area-'+String(index)+'"'+' minlength="1" maxlength="100" placeholder="متن جدید را وارد کنید"'+"'"+String(element.id)+"'"+',event'+')"></textarea><div><button class="bg-primary" id="buttonyes-'+String(index)+'"'+'>تایید</button><button class="bg-danger btn"  id="buttonno-'+String(index)+'"'+'>لغو</button></div></div>'
      );
       let textinput=document.getElementById("editdiv-"+String(index)) // نمایش تکست‌آریا
        textinput.classList.remove('none')
       let textinputyesbtn=document.getElementById("buttonyes-"+String(index))
       let textinputnobtn=document.getElementById("buttonno-"+String(index))
     



      
  textinputyesbtn.addEventListener("click",()=>{

    let textinputarea=document.getElementById("area-"+String(index)).value
    change(textinputarea,element.id)
    
    document.getElementById("editdiv-"+String(index)).remove() 
 
  })
  
  
  textinputnobtn.addEventListener("click",()=>{
    document.getElementById("editdiv-"+String(index)).remove()
    
  })
  });

  

});

function change(newtext, id) {

  
   let show = document.getElementById(id); // گرفتن تگ مورد نظر بر اساس ID یکتا

   if (show){
    show.innerHTML=newtext
   }
   else{
    console.log("eror");
    
   }

   
  
}//onblur="change('+"'"+'input-'+String(index)+"'"