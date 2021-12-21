const eUsername = document.getElementById("emp-username");
const ePassword = document.getElementById("emp-password");
const mUsername = document.getElementById("mana-username");
const mPassword = document.getElementById("mana-password");

// EMPLOYEE LOGIN
async function employeeLogin(){
  let response = await fetch("http://127.0.0.1:5000/employee/login", {method:["POST"],
  headers: {"Content-Type":"application/json"},
  body: JSON.stringify({"employeeId":eUsername.value, "password":ePassword.value}) });
  if(response.status == 200){
    let body = await response.json();
    console.log(body);
    if(body.Validated == true){
      sessionStorage.setItem("valueEmp", eUsername.value);
      window.location.href = "employee-home.html";
    } else {
      let errorMessage = document.getElementById("error-message");
      errorMessage.textContent = "Your credentials could not be validated. Please make sure your Employee ID and password are correct.";
    };
  } else {
    alert("Login credentials not validated.");
  };
};



// MANAGER LOGIN
async function managerLogin(){
  let response = await fetch("http://127.0.0.1:5000/manager/login", {method:["POST"],
  headers: {"Content-Type":"application/json"},
  body: JSON.stringify({"managerId": mUsername.value, "password": mPassword.value}) });
  if(response.status == 200){
    let body = await response.json();
    console.log(body);
    if(body.Validated == true){
      window.location.href = "manager-home.html";
    } else {
      let errorMessage = document.getElementById("error-message");
      errorMessage.textContent = "Your credentials could not be validated. Please make sure your Manager ID and password are correct.";
    };
  } else {
    alert("Login credentials not validated.");
  };
};
