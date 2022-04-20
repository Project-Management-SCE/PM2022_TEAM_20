var sibling;
var address;
let elementsArray = document.querySelectorAll(".check");
elementsArray.forEach(function(elem) {
    elem.addEventListener("click", function() {
      sibling=this.parentElement.nextElementSibling.nextElementSibling;
      address=sibling.textContent;
      document.querySelector("#sendMail").setAttribute('action',"mailto:"+address);
    });
});
var flag=0;
document.querySelector(".user_botton").addEventListener("click",function(){
  if(flag == 0){
    document.querySelector("#Profile_Select").classList.remove("invisible");
    flag=1;
  }
  else{
    document.querySelector("#Profile_Select").classList.add("invisible");
    flag=0;
  }
})
