function Menu()
{
    var menu = document.getElementById("Profile_Select");

    if(menu.style.display == "flex")
        menu.style.display="none";
    else
        menu.style.display="flex";
}


function Manage()
{
    var menu = document.getElementById("lastForum");
    var but =  document.getElementById("for_button");
    var buttu =  document.getElementById("man_button");

    if(menu.style.display == "flex"){
        menu.style.display="none";
        buttu.style.borderBottom ="none";
        but.style.borderBottom = "2px solid rgb(184, 184, 252)";
    }
    else{
        menu.style.display="flex";
        buttu.style.borderBottom ="2px solid rgb(184, 184, 252)";
        but.style.borderBottom = "none";
    }
}