const email=document.getElementById('email');
const password=document.getElementById('password');

var email_error = document.getElementById('email_error');
var pass_error = document.getElementById('pass_error');

email.addEventListener('input',email_verify);
password.addEventListener('input',pass_verify);

function isvalidate()
{
    if(email.value.length < 11){
        email.style.border = "2px solid red";
        email_error.style.display="block";
        email.focus();
        return false;
    }
    if(password.value.length < 8){
        password.style.border = "2px solid red";
        pass_error.style.display="block";
        password.focus();
        return false;
    }
}
function email_verify(){
    if(email.value.length >=10){
        email.style.border = "2px solid green";
        return true;
    }
}
function pass_verify(){
    if(password.value.length >=8){
        password.style.border = "2px solid green";
        return true;
    }
    
}
