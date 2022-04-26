document.querySelector("#delForum").addEventListener("click",function(){
   document.querySelector("#delForum").classList.add("invisible");
   document.querySelector(".delConf").classList.remove("invisible");
});
document.querySelector("#butNo").addEventListener("click",function(){
  document.querySelector(".delConf").classList.add("invisible");
  document.querySelector("#delForum").classList.remove("invisible");
})

document.querySelector("#plus").addEventListener("click",function(){
  document.querySelector("#addForum").classList.add("display");
  document.querySelector(".fillForum").classList.remove("display");
})

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
