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
const newReimburseButton = document.getElementById("r-submit");
newReimburseButton.addEventListener("click", createReimbursement);
let requestMessage = document.getElementById("request-created");

async function createReimbursement(){
  let requestLabel = document.getElementById("purpose");
  let amount = document.getElementById("amount");

  if(requestLabel.value == "" || amount.value == "") {
    requestMessage.textContent = 'Please fill out both fields.'
  }
  else {
    const submitReimburseRoute = "http://127.0.0.1:5000/employee/reimbursement";

    let response = await fetch(submitReimburseRoute, {headers:{'Content-Type':'application/json'}, method:["POST"], body:JSON.stringify({
                          reimburseId: 0, 
                          employeeId: sessionStorage.getItem("valueEmp"),
                          amount: amount.value, 
                          status: "", 
                          empReason: requestLabel.value,
                          managerReason: ""}) 
                        });
    
    let createBody = await response.json();

    if(response.status == 201){
      requestLabel.value = ``;
      amount.value = ``;
      requestMessage.textContent = `Your request has been submitted.`;
    } 
    else {
      let error = createBody.Message;
      requestMessage.textContent = error;
    }
  }
};




let empId = sessionStorage.getItem("valueEmp");


// TO VIEW PENDING REIMBURSEMENT DATA
const pendingTableBody = document.getElementById("r-body-p");
let pendingButton = document.getElementById("pending");
pendingButton.addEventListener("click", getPendingData);

async function getPendingData(){
  pendingTableBody.innerHTML = ``;
  const pendingRoute = "http://127.0.0.1:5000/employee/pending/";

  let response = await fetch(pendingRoute + empId);
  let pendingBody = await response.json();

  if(response.status == 200){
    populatePendingData(pendingBody);
  } 
  else {
    alert("Could not retrieve reimbursement data!")
  };
};


// TO POPULATE THE PENDING REIMBURSEMENTS
function populatePendingData(jsonBody){
  for(let rb of jsonBody){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = `<td>${rb.empReason}</td><td>$${rb.amount}</td><td>${rb.status}</td><td>${rb.managerReason}</td>`;
    pendingTableBody.appendChild(tableRow);
  };
};



// TO VIEW APPROVED REIMBURSEMENT DATA
const approvedTableBody = document.getElementById("r-body-a");
let approvedButton = document.getElementById("approved");
approvedButton.addEventListener("click", getApprovedData);

async function getApprovedData(){
  approvedTableBody.innerHTML = ``;
  const approvedRoute = "http://127.0.0.1:5000/employee/approved/";

  let response = await fetch(approvedRoute + empId);
  let approvedBody = await response.json();

  if(response.status == 200){
    populateApprovedData(approvedBody);
  } 
  else {
    alert("Could not retrieve reimbursement data!")
  }
};


// TO POPULATE THE APPROVED DATA
function populateApprovedData(jsonBody) {
  for(let rb of jsonBody){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = `<td>${rb.empReason}</td><td>$${rb.amount}</td><td>${rb.status}</td><td>${rb.managerReason}</td>`;
    approvedTableBody.appendChild(tableRow);
  };
};





// TO VIEW DENIED REIMBURSEMENT DATA
const deniedTableBody = document.getElementById("r-body-d");
let deniedButton = document.getElementById("denied");
deniedButton.addEventListener("click", getDeniedData);

async function getDeniedData(){
  deniedTableBody.innerHTML = ``;
  const deniedRoute = "http://127.0.0.1:5000/employee/denied/";

  let response = await fetch(deniedRoute + empId);
  let deniedBody = await response.json();

  if(response.status == 200){
    populateDeniedData(deniedBody);
  } 
  else {
    alert("Could not retrieve reimbursement data!")
  }
};


// TO POPULATE THE DENIED DATA
function populateDeniedData(jsonBody){
  for(let rb of jsonBody){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = `<td>${rb.empReason}</td><td>$${rb.amount}</td><td>${rb.status}</td><td>${rb.managerReason}</td>`;
    deniedTableBody.appendChild(tableRow);
  };
};




// TO LOG OUT OF THE SESSION
function logout(){
  sessionStorage.clear();
  window.location.href = "index.html";
};
