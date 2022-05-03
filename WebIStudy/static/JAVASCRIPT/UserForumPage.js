//Functionallity
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

document.querySelector("#addButton").addEventListener("click",function(){
  document.querySelector("#addButton").classList.add("display");
  document.querySelector(".newMessage").classList.remove("display");
})
document.querySelector("#post").addEventListener("click",function(){
  document.querySelector(".newMessage").classList.add("display");
  document.querySelector("#addButton").classList.remove("display");
})
