
const footer1 = document.querySelectorAll('footer p,footer h2,footer span');
const footera= document.querySelectorAll('footer .py-2');

const footera2= document.querySelectorAll('.block-23 a');
footera2.forEach((element)=>{
  element.addEventListener("click",(event)=>{
       event.preventDefault()
  })
  
})

let footer=Array.from(footer1)
  
footera.forEach((element,event)=>{
 
  
    element.addEventListener("click",(event)=>{
     event.preventDefault()

    })
    footer.push(element)
})

footer.forEach((element,index) => {
  
    
  element.classList.add('textedit-bg')
element

  
  element.id =" text2"+String(index); // اضافه کردن ID یکتا به هر تگ
  element.addEventListener('dblclick', () => {

      document.body.insertAdjacentHTML(
          'beforeend',' <div class="text-edit none"  id="editdiv2-'+String(index)+'"'+'><h3>متن جدید را وارد کنید</h3><textarea type="text" id="area2-'+String(index)+'"'+' minlength="1" maxlength="100" placeholder="متن جدید را وارد کنید"'+"'"+String(element.id)+"'"+',event'+')"></textarea><div><button class="bg-primary" id="buttonyes2-'+String(index)+'"'+'>تایید</button><button class="bg-danger btn"  id="buttonno2-'+String(index)+'"'+'>لغو</button></div></div>'
      );
       let textinput=document.getElementById("editdiv2-"+String(index)) // نمایش تکست‌آریا
        textinput.classList.remove('none')
       let textinputyesbtn=document.getElementById("buttonyes2-"+String(index))
       let textinputnobtn=document.getElementById("buttonno2-"+String(index))
     



      
  textinputyesbtn.addEventListener("click",()=>{

    let textinputarea=document.getElementById("area2-"+String(index)).value
    change(textinputarea,element.id)
    
    document.getElementById("editdiv2-"+String(index)).remove() 
 
  })
  
  
  textinputnobtn.addEventListener("click",()=>{
    document.getElementById("editdiv2-"+String(index)).remove()
    
  })
  });

  

});

function change(newtext, id) {

  
   let show = document.getElementById(id); // گرفتن تگ مورد نظر بر اساس ID یکتا

   if (show){
    show.textContent=newtext
   }
   else{
    console.log("eror");
    
   }

   
  
}