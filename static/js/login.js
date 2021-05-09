let users=localStorage.getItem('users');
if(users==null){
    localStorage.setItem('users',JSON.stringify({"admin":"admin"}));
}
users=localStorage.getItem('users');
users=JSON.parse(users)
let signUpButton = document.getElementById('signUp');
let signInButton = document.getElementById('signIn');
let container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});



document.getElementById('login').addEventListener('click',()=>{
    let user = document.getElementById('useremail').value;
    let pass = document.getElementById('userpass').value;
    if(users!=null && users[user]==pass){
        window.location.replace("/home");
    }
    else{
        document.getElementById('login-msg').textContent="Wrong email/password";
    }
});

document.getElementById('signup').addEventListener('click',()=>{
    let user = document.getElementById('useremailreg').value;
    let pass = document.getElementById('userpassreg').value;
    if(users[user]!=pass){
        users[user]=pass
        localStorage.setItem('users',JSON.stringify(users));
        document.getElementById('register-msg').textContent="Registeration sucessfull";
    }
    else{
        document.getElementById('register-msg').textContent="User already registered";
    }
});
