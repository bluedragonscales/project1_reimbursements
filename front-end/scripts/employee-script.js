// TO MAKE THE TABS WORK
function openTab(evt, tabName) {
  let tabcontent = document.getElementsByClassName("tabcontent");
  for (let i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
    // These delete message data that was populated inside the request new reimbursement section.
    document.getElementById("request-created").textContent = ``;
    document.getElementById("purpose").value = ``;
    document.getElementById("amount").value = ``;
  };
  let tablink = document.getElementsByClassName("tablink");
  for (let i = 0; i < tablink.length; i++) {
    tablink[i].className = tablink[i].className.replace(" active", "");
  };
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
};




// TO CREATE A NEW REIMBURSEMENT.
async function createReimbursement(){
  let requestLabel = document.getElementById("purpose");
  let amount = document.getElementById("amount");
  const submitReimburseRoute = "http://127.0.0.1:5000/employee/reimbursement";
  let response = await fetch(submitReimburseRoute, {headers:{'Content-Type': 'application/json'},
                            method:["POST"], body:JSON.stringify({"reimburseId": 0, "employeeId": sessionStorage.getItem("valueEmp"),
                            "requestLabel": requestLabel.value,
                            "amount": amount.value, "status": "", "reason": ""}) });
  if(response.status == 200){
    let createBody = await response.json();
    let requestMessage = document.getElementById("request-created");
    if(amount.value > 0){
      requestLabel.value = ``;
      amount.value = ``;
      requestMessage.textContent = `Your request has been submitted.`;
    } else {
      requestMessage.textContent = `Your request to submit has failed.`;
    };
  } else {
    requestMessage.textContent = `Your request to submit has failed.`;
  }
};




// TO VIEW PENDING REIMBURSEMENT DATA
// To activate the pending tab on the website.
let pendingButton = document.getElementById("pending");
button.addEventListener("click", getPendingData);

async function getPendingData(){
  // tableBody.innerHTML = ``;
  const pendingRoute = "http://127.0.0.1:5000/employee/pending/";
  // Fetching the information from the route.
  let response = await fetch(pendingRoute + sessionStorage.getItem("valueEmp"));
  if(response.status == 200){
    let pBody = await response.json();
    populateReimburseData(pBody);
  } else {
    alert("Could not retrieve reimbursement data!")
  }
};



// TO VIEW APPROVED REIMBURSEMENT DATA
// To activate the approved tab on the website.
let approvedButton = document.getElementById("approved");
button.addEventListener("click", getApprovedData);

async function getApprovedData(){
  // tableBody.innerHTML = ``;
  const approvedRoute = "http://127.0.0.1:5000/employee/approved/";
  // Fetching the information from the route.
  let response = await fetch(approvedRoute + sessionStorage.getItem("valueEmp"));
  if(response.status == 200){
    let aBody = await response.json();
    populateReimburseData(aBody);
  } else {
    alert("Could not retrieve reimbursement data!")
  }
};





// TO VIEW DENIED REIMBURSEMENT DATA
// To activate the denied tab on the website.
let deniedButton = document.getElementById("denied");
button.addEventListener("click", getDeniedData);

async function getDeniedData(){
  // tableBody.innerHTML = ``;
  const deniedRoute = "http://127.0.0.1:5000/employee/denied/";
  // Fetching the information from the route.
  let response = await fetch(deniedRoute + sessionStorage.getItem("valueEmp"));
  if(response.status == 200){
    let dBody = await response.json();
    populateReimburseData(dBody);
  } else {
    alert("Could not retrieve reimbursement data!")
  }
};





// TO POPULATE THE TABLE DATA
// This grabs the tables and table bodies so that we can populate data into them.
const table = document.getElementById("reimburse-table");
const tableBody = document.getElementById("r-body");

function populateReimburseData(jsonBody){
  for(let rb of jsonBody){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = `<td>${rb.reimburseId}</td><td>${rb.requestLabel}</td><td>$${rb.amount}</td><td>${rb.status}</td><td>${rb.reason}</td>`;
    tableBody.appendChild(tableRow);
  };
};






// TO LOG OUT OF THE SESSION
function logout(){
  sessionStorage.clear();
  window.location.href = "index.html";
};
