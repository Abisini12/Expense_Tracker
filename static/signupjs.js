function validated() {
    const username = document.getElementById('username');
    const name = document.getElementById('name');
    const role = document.getElementById('role');
    const phone = document.getElementById('phone');
    const password = document.getElementById('password');
    const cpassword = document.getElementById('confirm_password');

    var user_error = document.getElementById('user_error');
    var name_error = document.getElementById('name_error');
    var role_error = document.getElementById('role_error');
    var phone_error = document.getElementById('phone_error');
    var pass_error = document.getElementById('pass_error');
    var cpass_error = document.getElementById('cpass_error');

    user_error.style.display = "none";
    name_error.style.display = "none";
    role_error.style.display = "none";
    phone_error.style.display = "none";
    pass_error.style.display = "none";
    cpass_error.style.display = "none";
    var false_cond;

    if (username.value.length < 10) {
        user_error.style.display = "block";
        username.style.border = "2px solid red";
        false_cond=false;
    }

    if (name.value.length < 5) {
        name_error.style.display = "block";
        name.style.border = "2px solid red";
        false_cond=false;
    }

    if (role.value === "Choose your role") {
        role_error.style.display = "block";
        role.style.border = "2px solid red";
        false_cond=false;
    }

    if (phone.value.length !== 10) {
        phone_error.style.display = "block";
        phone.style.border = "2px solid red";
        false_cond=false;
    }

    if (password.value.length < 8) {
        pass_error.style.display = "block";
        password.style.border = "2px solid red";
        false_cond=false;
    }

    if (password.value !== cpassword.value) {
        cpass_error.style.display = "block";
        cpassword.style.border = "2px solid red";
        console.log('error in pass')
        false_cond=false;
    }

    if(false_cond==false)
    {
        return false;
    }
    else{
        return true;
    }
  
}
