// EMPLOYEE LOGIN
const eUsername = document.getElementById("emp-username");
const ePassword = document.getElementById("emp-password");
const empLoginButton = document.getElementById("emp-button");
empLoginButton.addEventListener("click", employeeLogin);


async function employeeLogin(){
  let response = await fetch("http://127.0.0.1:5000/employee/login", {method:["POST"], headers: {"Content-Type":"application/json"},
  body: JSON.stringify({"username":eUsername.value, "password":ePassword.value}) });

  if(response.status == 201){
    let loginBody = await response.json();
    sessionStorage.setItem("valueEmp", loginBody.employeeId);
    window.location.href = "employee-home.html";
  } 
  else {
    let errorMessage = document.getElementById("error-message");
    errorMessage.textContent = "Your credentials could not be validated. Please make sure your username and password are correct.";
  };
};



// MANAGER LOGIN
const mUsername = document.getElementById("mana-username");
const mPassword = document.getElementById("mana-password");
const manaLoginButton = document.getElementById("mana-button");
manaLoginButton.addEventListener("click", managerLogin);


async function managerLogin(){
  let response = await fetch("http://127.0.0.1:5000/manager/login", {method:["POST"], headers: {"Content-Type":"application/json"},
  body: JSON.stringify({"username":mUsername.value, "password":mPassword.value}) });

  if(response.status == 201){
    let loginBody = await response.json();
    window.location.href = "manager-home.html";
  } 
  else {
    let errorMessage = document.getElementById("error-message");
    errorMessage.textContent = "Your credentials could not be validated. Please make sure your username and password are correct.";
  };
};