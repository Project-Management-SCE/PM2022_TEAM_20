function ShowRegister(){
    var login = document.getElementById('log_form');
    var register = document.getElementById('Register_Form');
    var Login_content = document.getElementById('Log_content');
    var register_content = document.getElementById('Register_content');
    var picture = document.getElementById('books');

    login.style.display = "none";
    register_content.style.display = "none";
    register.style.display = "flex";
    Login_content.style.display="flex";

    picture.style.marginTop = "180px";
}

function ShowLogin(){
    var login = document.getElementById('log_form');
    var register = document.getElementById('Register_Form');
    var Login_content = document.getElementById('Log_content');
    var register_content = document.getElementById('Register_content');
    var picture = document.getElementById('books');

    login.style.display = "flex";
    register_content.style.display = "flex";
    register.style.display = "none";
    Login_content.style.display="none";

    picture.style.marginTop = "100px";
}