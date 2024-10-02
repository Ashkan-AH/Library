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
let jobselect=$.getElementById("job")
let checkbox=$.getElementById("checkbox")
let profileImage = $.getElementById("profile-img");
let joblevel=$.getElementById("joblevel")
let leveltext=$.getElementById("leve-text")
let studentcode=$.getElementById("student-number-select")
let jobselectname=$.getElementById("job-selector-name")

let inputSkillss=$.getElementById("inputSkills")
let subjectselect=$.getElementById("subject")
let divbtn=$.getElementById("div-button")

let st_id = $.getElementById("id_st_id")
let st_major = $.getElementById("id_st_major")
let st_grade = $.getElementById("id_st_grade")

let pro_id = $.getElementById("id_pro_id")
let pro_major = $.getElementById("id_pro_major")
let pro_grade = $.getElementById("id_pro_grade")

let emp_id = $.getElementById("id_emp_id")
let emp_unit = $.getElementById("id_emp_unit")
let emp_grade = $.getElementById("id_emp_grade")

let default1 = $.getElementById("id_default1")
let default2 = $.getElementById("id_default2")
let default3 = $.getElementById("id_default3")



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
            profileImage.style.backgroundImage="url("+event.target.result+")"
        }
         reader.readAsDataURL(file)
        

     }
})

editbtn1.addEventListener("click",()=>{
    if(imginput.value!=""){
         $.body.classList.remove("scroll-off")
    editdiv.classList.add("hide")
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
    $.body.classList.remove("scroll-off")
    editdiv.classList.add("hide")
    imginput.value=""
    imgwatch.style.backgroundImage=""
    $.body.classList.remove("no-interaction")
    editdiv.classList.remove("interaction")
})



jobselect.addEventListener("change",()=>{
    const selectoption=jobselect.options[jobselect.selectedIndex].value
   
    switch (selectoption){
        case "دانشجو":
            st_id.classList.remove("hide")
            st_major.classList.remove("hide")
            st_grade.classList.remove("hide")
            pro_id.classList.add("hide")
            pro_major.classList.add("hide")
            pro_grade.classList.add("hide")
            emp_id.classList.add("hide")
            emp_unit.classList.add("hide")
            emp_grade.classList.add("hide")
            default1.classList.add("hide")
            default2.classList.add("hide")
            default3.classList.add("hide")
st_id.setAttribute("required", "")            
st_major.setAttribute("required", "")
st_grade.setAttribute("required", "")
pro_id.removeAttribute("required", "")            
pro_major.removeAttribute("required", "")
pro_grade.removeAttribute("required", "")
emp_id.removeAttribute("required", "")            
emp_unit.removeAttribute("required", "")
emp_grade.removeAttribute("required", "")

            
    
            jobselectname.innerHTML=" رشته تحصیلی"
            studentcode.innerHTML="کد دانشجویی"
            leveltext.innerHTML="مقطع تحصیلی"
       break;
       
       case "استاد":
        st_id.classList.add("hide")
        st_major.classList.add("hide")
        st_grade.classList.add("hide")
        pro_id.classList.remove("hide")
        pro_major.classList.remove("hide")
        pro_grade.classList.remove("hide")
        emp_id.classList.add("hide")
        emp_unit.classList.add("hide")
        emp_grade.classList.add("hide")
        default1.classList.add("hide")
        default2.classList.add("hide")
        default3.classList.add("hide")
        st_id.removeAttribute("required", "")            
st_major.removeAttribute("required", "")
st_grade.removeAttribute("required", "")
pro_id.setAttribute("required", "")            
pro_major.setAttribute("required", "")
pro_grade.setAttribute("required", "")
emp_id.removeAttribute("required", "")            
emp_unit.removeAttribute("required", "")
emp_grade.removeAttribute("required", "")

        jobselectname.innerHTML=" رشته آموزشی"
        studentcode.innerHTML="کد استادی"
        leveltext.innerHTML="مقطع آموزشی"
       break;
       
       case "کارمند":
        st_id.classList.add("hide")
        st_major.classList.add("hide")
        st_grade.classList.add("hide")
        pro_id.classList.add("hide")
        pro_major.classList.add("hide")
        pro_grade.classList.add("hide")
        default1.classList.add("hide")
        default2.classList.add("hide")
        default3.classList.add("hide")
        emp_id.classList.remove("hide")
        emp_unit.classList.remove("hide")
        emp_grade.classList.remove("hide")
        st_id.removeAttribute("required", "")            
st_major.removeAttribute("required", "")
st_grade.removeAttribute("required", "")
pro_id.removeAttribute("required", "")            
pro_major.removeAttribute("required", "")
pro_grade.removeAttribute("required", "")
emp_id.setAttribute("required", "")            
emp_unit.setAttribute("required", "")
emp_grade.setAttribute("required", "")

        jobselectname.innerHTML="سمت شغلی"
        studentcode.innerHTML="کد پرسنلی"
        leveltext.innerHTML="محل کار"
       break;
       
           default:
            st_id.classList.add("hide")
            st_major.classList.add("hide")
            st_grade.classList.add("hide")
            pro_id.classList.add("hide")
            pro_major.classList.add("hide")
            pro_grade.classList.add("hide")
            emp_id.classList.add("hide")
            emp_unit.classList.add("hide")
            emp_grade.classList.add("hide")
            default1.classList.remove("hide")
            default2.classList.remove("hide")
            default3.classList.remove("hide")

            st_id.removeAttribute("required", "")            
            st_major.removeAttribute("required", "")
            st_grade.removeAttribute("required", "")
            pro_id.removeAttribute("required", "")            
            pro_major.removeAttribute("required", "")
            pro_grade.removeAttribute("required", "")
            emp_id.removeAttribute("required", "")            
            emp_unit.removeAttribute("required", "")
            emp_grade.removeAttribute("required", "")
            jobselectname.innerHTML="پست دانشگاهی را وارد کنید"
            studentcode.innerHTML="پست دانشگاهی را وارد کنید"
            leveltext.innerHTML="پست دانشگاهی را وارد کنید"

        break;
    }
})
window.addEventListener("load",()=>{
    const selectoption=jobselect.options[jobselect.selectedIndex].value
   
    switch (selectoption){
        case "دانشجو":
            st_id.classList.remove("hide")
            st_major.classList.remove("hide")
            st_grade.classList.remove("hide")
            pro_id.classList.add("hide")
            pro_major.classList.add("hide")
            pro_grade.classList.add("hide")
            emp_id.classList.add("hide")
            emp_unit.classList.add("hide")
            emp_grade.classList.add("hide")
            default1.classList.add("hide")
            default2.classList.add("hide")
            default3.classList.add("hide")
st_id.setAttribute("required", "")            
st_major.setAttribute("required", "")
st_grade.setAttribute("required", "")
pro_id.removeAttribute("required", "")            
pro_major.removeAttribute("required", "")
pro_grade.removeAttribute("required", "")
emp_id.removeAttribute("required", "")            
emp_unit.removeAttribute("required", "")
emp_grade.removeAttribute("required", "")

            
    
            jobselectname.innerHTML=" رشته تحصیلی"
            studentcode.innerHTML="کد دانشجویی"
            leveltext.innerHTML="مقطع تحصیلی"
       break;
       
       case "استاد":
        st_id.classList.add("hide")
        st_major.classList.add("hide")
        st_grade.classList.add("hide")
        pro_id.classList.remove("hide")
        pro_major.classList.remove("hide")
        pro_grade.classList.remove("hide")
        emp_id.classList.add("hide")
        emp_unit.classList.add("hide")
        emp_grade.classList.add("hide")
        default1.classList.add("hide")
        default2.classList.add("hide")
        default3.classList.add("hide")
        st_id.removeAttribute("required", "")            
st_major.removeAttribute("required", "")
st_grade.removeAttribute("required", "")
pro_id.setAttribute("required", "")            
pro_major.setAttribute("required", "")
pro_grade.setAttribute("required", "")
emp_id.removeAttribute("required", "")            
emp_unit.removeAttribute("required", "")
emp_grade.removeAttribute("required", "")

        jobselectname.innerHTML=" رشته آموزشی"
        studentcode.innerHTML="کد استادی"
        leveltext.innerHTML="مقطع آموزشی"
       break;
       
       case "کارمند":
        st_id.classList.add("hide")
        st_major.classList.add("hide")
        st_grade.classList.add("hide")
        pro_id.classList.add("hide")
        pro_major.classList.add("hide")
        pro_grade.classList.add("hide")
        default1.classList.add("hide")
        default2.classList.add("hide")
        default3.classList.add("hide")
        emp_id.classList.remove("hide")
        emp_unit.classList.remove("hide")
        emp_grade.classList.remove("hide")
        st_id.removeAttribute("required", "")            
st_major.removeAttribute("required", "")
st_grade.removeAttribute("required", "")
pro_id.removeAttribute("required", "")            
pro_major.removeAttribute("required", "")
pro_grade.removeAttribute("required", "")
emp_id.setAttribute("required", "")            
emp_unit.setAttribute("required", "")
emp_grade.setAttribute("required", "")

        jobselectname.innerHTML="سمت شغلی"
        studentcode.innerHTML="کد پرسنلی"
        leveltext.innerHTML="محل کار"
       break;
       
           default:
            st_id.classList.add("hide")
            st_major.classList.add("hide")
            st_grade.classList.add("hide")
            pro_id.classList.add("hide")
            pro_major.classList.add("hide")
            pro_grade.classList.add("hide")
            emp_id.classList.add("hide")
            emp_unit.classList.add("hide")
            emp_grade.classList.add("hide")
            default1.classList.remove("hide")
            default2.classList.remove("hide")
            default3.classList.remove("hide")

            st_id.removeAttribute("required", "")            
            st_major.removeAttribute("required", "")
            st_grade.removeAttribute("required", "")
            pro_id.removeAttribute("required", "")            
            pro_major.removeAttribute("required", "")
            pro_grade.removeAttribute("required", "")
            emp_id.removeAttribute("required", "")            
            emp_unit.removeAttribute("required", "")
            emp_grade.removeAttribute("required", "")
            jobselectname.innerHTML="پست دانشگاهی را وارد کنید"
            studentcode.innerHTML="پست دانشگاهی را وارد کنید"
            leveltext.innerHTML="پست دانشگاهی را وارد کنید"

        break;
    }
    
})



// submitbtn.addEventListener("click",(event)=>{


//     submitalert.classList.remove("hide")
//     $.body.classList.add("no-interaction")
//     submitalert.classList.add("interaction")
//     $.body.classList.add("scroll-off")
//     if(event.target.submit){
//         alert("dsvfs")
//     }
        


// })


// submitalertbtn2.addEventListener("click",()=>{

//     submitalert.classList.add("hide")
//     $.body.classList.remove("no-interaction")
//     submitalert.classList.remove("interaction")
//     $.body.classList.remove("scroll-off")
// })
