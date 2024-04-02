function validate_customer_login(){
    email=document.getElementById('email').value
password=document.getElementById('password').value
if (email==""||password==""){
    document.getElementById('msg').innerHTML='Please enter your Email and password'
    return false
}
else {
    return true
}
}