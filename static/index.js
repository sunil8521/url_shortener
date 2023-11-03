
let ham=document.querySelector(".hamburgur")
let items=document.querySelector(".navItems")
ham.addEventListener("click",()=>{
  ham.classList.toggle("active")
  items.classList.toggle("active")
  
})
document.querySelectorAll("li").forEach(ele=> ele.addEventListener("click",()=>{
  ham.classList.toggle("active")
  items.classList.toggle("active")
}))