let $=document
let imgwindowbtn=$.getElementById("img-edit-btn")
let editdiv=$.getElementById("edit-div")
let imginput=$.getElementById("img-input")
let imgwatch=$.getElementById("img-watch")
let editalertbtn1=$.querySelector("#edit-alert-btn1")
let editalertbtn2 =$.querySelector("#edit-alert-btn2")
let alertion=$.getElementById("alertion")
let alertiontext=$.getElementById("alertion-text")
let submitalert=$.getElementById("edit-alert-submit")
let submitalertbtn2=$.getElementById("submit-alert-btn2")
let submitalert1=$.getElementById("submit-alert-btn1")
let formsubmit=$.getElementById("form-input")
let cancelBTN=$.getElementById("cancel-btn")
let editbtn1=$.querySelector("#edit-btn1")
let editbtn2=$.querySelector("#edit-btn2")
let editalertdiv=$.getElementById("edit-alertdiv")
// let jobselect=$.getElementById("job")
let checkbox=$.getElementById("checkbox")

// let joblevel=$.getElementById("joblevel")
let leveltext=$.getElementById("leve-text")
let studentcode=$.getElementById("student-number-select")
let jobselectname=$.getElementById("job-selector-name")

// let inputSkillss=$.getElementById("inputSkills")
// let subjectselect=$.getElementById("subject")
let divbtn=$.getElementById("div-button")



let submitbtn=$.getElementById("submit-btn")
let inputvallength
let inputvalues=$.querySelectorAll(".form-control")
let inputvalue
let inputval
let inputminlenght
imgwindowbtn.addEventListener("click",(event)=>{
    event.preventDefault()
editdiv.classList.remove("hide")

$.body.classList.add("no-interaction")
editdiv.classList.add("interaction")
$.body.classList.add("scroll-off")


})


imginput.addEventListener("change",(event)=>{
     const file=event.target.files[0]
     const filesize=file.size/1024/1024;
     if(filesize>1){
        
        alertion.classList.remove("hide")
        alertiontext.innerText=" حجم تصویر مورد نظر نمیتواند بالای 1 مگابایت باشد  "
        setTimeout(
            ()=>{
                alertion.classList.add("hide")
              alertiontext.innerText=""   
            }
      ,3000  )
        imginput.value="";
        
     }
     else if(file){
        const reader= new FileReader();
        reader.onload=(event)=>{
            imgwatch.style.backgroundImage="url("+event.target.result+")"
        }
         reader.readAsDataURL(file)
        

     }
})

editbtn1.addEventListener("click",()=>{
    if(imginput.value!=""){
         $.body.classList.remove("scroll-off")
    editdiv.classList.add("hide")
    
    imginput.value=""
    imgwatch.style.backgroundImage=""
    $.body.classList.remove("no-interaction")
    editdiv.classList.remove("interaction")
   


    }
    else{
        alertion.classList.remove("hide")
       
        alertiontext.innerText="لطفا عکسی را انتخاب کنید"
        setTimeout(
            ()=>{
                alertion.classList.add("hide")
              alertiontext.innerText=""   
            }
      ,2000  )

    }
})


editbtn2.addEventListener("click",()=>{
    if(imginput.value!=""){
        
    editalertdiv.classList.remove("hide")
    }

    else{
        editdiv.classList.add("hide")
        $.body.classList.remove("scroll-off")
    }

    $.body.classList.remove("no-interaction")
    editdiv.classList.remove("interaction")
})


editalertbtn1.addEventListener("click",()=>{
    $.body.classList.remove("scroll-off")

    editalertdiv.classList.add("hide")
    editdiv.classList.add("hide")
    $.body.classList.remove("no-interaction")
    editalertdiv.classList.remove("interaction")
    imginput.value=""
    imgwatch.style.backgroundImage=""
   
})

editalertbtn2.addEventListener("click",()=>{
    editalertdiv.classList.add("hide")
    
    $.body.classList.remove("no-interaction")
    editalertdiv.classList.remove("interaction")
})

cancelBTN.addEventListener("click",(event)=>{
    event.preventDefault()
    editalertdiv.classList.remove("hide")
    $.body.classList.add("no-interaction")
    editalertdiv.classList.add("interaction")
})
/*
jobselect.addEventListener("change",()=>{
    const selectoption=jobselect.options[jobselect.selectedIndex].value
   
    switch (selectoption){
        case "دانشجو":
            subjectselect.innerHTML='<option value="">انتخاب کنید </option><option value="کامپیوتر">کامپیوتر</option><option value="it">فناوری اطلاعات</option><option value="Wood Industry">صنایع چوب</option><option value="financial manager"> حسابداری</option><option value="architecture">معماری </option><option value="Electricity">برق </option>'

            jobselectname.innerHTML=" رشته تحصیلی دانشجو"
            inputSkillss.setAttribute("placeholder","کد دانشجویی(الزامی)")
            joblevel.innerHTML='<option value="">انتخاب مقطع</option><option value="کاردانی">کاردانی </option><option value="کارشناسی">کارشناسی </option>'
            studentcode.innerHTML="کد دانشجویی"
            leveltext.innerHTML="انتخاب مقطع"
       break;
       
       case "استاد":
             subjectselect.innerHTML=' <option value="software">انتخاب کنید</option><option value="software">نرم افزار</option><option value="it">فناوری اطلاعات</option><option value="Wood Industry">صنایع چوب</option><option value="financial manager"> حسابداری</option><option value="architecture">معماری </option><option value="Electricity">برق </option>'
             jobselectname.innerHTML="رشته درسی استاد "
            joblevel.innerHTML='<option value="software">انتخاب کنید</option><option value="diplom">کاردانی </option><option value="license">کارشناسی </option><option value="diplom">  کاردانی و کارشناسی </option>'
             inputSkillss.setAttribute("placeholder","کد استادی(الزامی)")
            studentcode.innerHTML="کد استادی"
            leveltext.innerHTML="انتخاب مقطع"


       break;
       
       case "کامند":
             subjectselect.innerHTML='<option value="software">انتخاب کنید</option><option value="software"> خدمات</option><option value="it"> پژوهش و فناوری</option><option value="Wood Industry"> حراست</option><option value="financial manager"> آموزش</option><option value="architecture">شبکه </option><option value="Electricity">برق </option>'
             studentcode.innerHTML="کد پرسنلی"
             inputSkillss.setAttribute("placeholder"," کد پرسنلی(الزامی)")
            joblevel.innerHTML=' <option value="software">انتخاب کنید</option><option value="آموزشکده فنی بندر انزلی - شهید خدادادی"> آموزشکده فنی بندر انزلی - شهید خدادادی</option><option value="آموزشکده فنی رستم آباد رودبار - سیدالشهداء"> آموزشکده فنی رستم آباد رودبار - سیدالشهداء </option><option value="آموزشکده فنی رشت - شهید چمران"> آموزشکده فنی رشت - شهید چمران</option>'
             jobselectname.innerHTML="پست سازمانی"
            leveltext.innerHTML="محل خدمت"

       break;
       
       case "choose":
             subjectselect.innerHTML='<option value="software"> انتخاب کنید</option>'
             leveltext.innerHTML=" پست دانشگاهی را انتخاب کنید"

             jobselectname.innerHTML=" پست دانشگاهی را انتخاب کنید"
             joblevel.innerHTML='<option value="software">انتخاب کنید</option>'
             studentcode.innerHTML=" پست دانشگاهی راانتخاب کنید"
            inputSkillss.setAttribute("placeholder","پست دانشگاهی راانتخاب کنید")
             
       break;
      default:

        break;
    }
})


*/
submitbtn.addEventListener("click",(event)=>{


    submitalert.classList.remove("hide")
    $.body.classList.add("no-interaction")
    submitalert.classList.add("interaction")
    $.body.classList.add("scroll-off")
    if(event.target.submit){
        alert("dsvfs")
    }
        


})


submitalertbtn2.addEventListener("click",()=>{

    submitalert.classList.add("hide")
    $.body.classList.remove("no-interaction")
    submitalert.classList.remove("interaction")
    $.body.classList.remove("scroll-off")
})*/
