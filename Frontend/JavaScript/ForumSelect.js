function Menu()
{
    var menu = document.getElementById("Profile_Select");

    if(menu.style.display == "flex")
        menu.style.display="none";
    else
        menu.style.display="flex";
}