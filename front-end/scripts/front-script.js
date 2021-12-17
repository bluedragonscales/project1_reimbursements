const eUsername = document.getElementById("emp-username");
const ePassword = document.getElementById("emp-password");
const mUsername = document.getElementById("mana-username");
const mPassword = document.getElementById("mana-password");


async function employeeLogin(){
  let response = await fetch("http://127.0.0.1:5000/employee/login/", {method:["POST"],
  headers: {"Content-Type":"application/json"},
  body: JSON.stringify({"username":eUsername.value, "password":ePassword.value}) });

  if(response.status == 200){
    let body = await response.json();
    console.log(body);
  } else {
    alert("Login credentials not validated.");
  };
};
