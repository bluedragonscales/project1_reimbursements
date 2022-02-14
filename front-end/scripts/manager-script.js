// TO MAKE THE TABS WORK
function openTab(evt, tabName) {
  let tabcontent = document.getElementsByClassName("tabcontent");
  for (let i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
    document.getElementById("status-message").textContent = ``;
    document.getElementById("view-stats").textContent = ``;
  };
  let tablink = document.getElementsByClassName("tablink");
  for (let i = 0; i < tablink.length; i++) {
    tablink[i].className = tablink[i].className.replace(" active", "");
  };
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
};



// TO GET ALL THE PENDING REIMBURSEMENT DATA
const pendingTableBody = document.getElementById("r-body-p");
let pendButton = document.getElementById("view");
pendButton.addEventListener("click", getPendingReimburseData);

async function getPendingReimburseData(){
  pendingTableBody.innerHTML = ``;

  const viewPending = "http://127.0.0.1:5000/manager/pendingList";
  let response = await fetch(viewPending);
  let pendingBody = await response.json();

  if(response.status == 200){
    populatePendingReimburseData(pendingBody);
  } 
  else {
    alert("Could not populate reimbursement data!")
  }
};


function populatePendingReimburseData(jsonBody){
  for(let rb of jsonBody){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = `<td>${rb.reimburseId}</td><td>${rb.employeeId}</td><td>${rb.empReason}</td><td>${rb.amount}</td>`;
    pendingTableBody.appendChild(tableRow);
  };
};




// TO APPROVE REIMBURSEMENTS
let reimburseIdToChange = document.getElementById("r-id");
let statusReason = document.getElementById("status-reason");
let statusMessage = document.getElementById("status-message");

let approveButton = document.getElementById("approve-status");
approveButton.addEventListener("click", approveReimbursement);

async function approveReimbursement(){
  let approveStatus = "http://127.0.0.1:5000/manager/approve";
  let response = await fetch(approveStatus, {headers:{'Content-Type': 'application/json'}, 
                              method: ["PATCH"], 
                              body:JSON.stringify({reimburseId: reimburseIdToChange.value, 
                                                  managerReason: statusReason.value}) });

  let approveBody = await response.json();

  if(response.status == 200){
    statusMessage.textContent = `Reimbursement ID ${reimburseIdToChange.value} has been approved.`;
    reimburseIdToChange.value = ``;
    statusReason.value = ``;
  } 
  else {
    statusMessage.textContent = "Failed to update reimbursement status.";
  };
};



// TO DENY REIMBURSEMENTS
let denyButton = document.getElementById("deny-status");
denyButton.addEventListener("click", denyReimbursement);

async function denyReimbursement(){
  let denyStatus = "http://127.0.0.1:5000/manager/deny";
  let response = await fetch(denyStatus, {headers:{'Content-Type': 'application/json'}, 
                              method: ["PATCH"], 
                              body:JSON.stringify({reimburseId: reimburseIdToChange.value, 
                                                  managerReason: statusReason.value}) });

  let denyBody = await response.json();

  if(response.status == 200){
    statusMessage.textContent = `Reimbursement ID ${reimburseIdToChange.value} has been denied.`;
    reimburseIdToChange.value = ``;
    statusReason.value = ``;
  } 
  else {
    statusMessage.textContent = "Failed to update reimbursement status.";
  };
};





// TO VIEW PAST APPROVED REIMBURSEMENTS
let pastApprovedTBody = document.getElementById("r-body-a");
const pastReimburseButton = document.getElementById("past");
pastReimburseButton.addEventListener("click", viewPastApprovals);

async function viewPastApprovals(){
  pastApprovedTBody.innerHTML = ``;

  const pastApprovalsRoute = "http://127.0.0.1:5000/manager/approvals";
  let response = await fetch(pastApprovalsRoute);
  let approvalsBody = await response.json();

  if(response.status == 200){
    populatePastApprovals(approvalsBody);
    viewPastDenials();
  } 
  else {
    alert("Could not retrieve reimbursement data!");
  }
};


function populatePastApprovals(jsonBody){
  for(let rb of jsonBody){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = `<td>${rb.reimburseId}</td><td>${rb.employeeId}</td><td>${rb.empReason}</td><td>$${rb.amount}</td><td>${rb.managerReason}</td>`;
    pastApprovedTBody.appendChild(tableRow);
  };
};





// TO VIEW PAST DENIED REIMBURSEMENTS
let pastDeniedTBody = document.getElementById("r-body-d");

async function viewPastDenials(){
  pastDeniedTBody.innerHTML = ``;

  const pastDenialsRoute = "http://127.0.0.1:5000/manager/denials";
  let response = await fetch(pastDenialsRoute);
  let denialsBody = await response.json();

  if(response.status == 200){
    populatePastDenials(denialsBody);
  } 
  else {
    alert("Could not retrieve reimbursement data!");
  }
};


function populatePastDenials(jsonBody){
  for(let rb of jsonBody){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = `<td>${rb.reimburseId}</td><td>${rb.employeeId}</td><td>${rb.empReason}</td><td>$${rb.amount}</td><td>${rb.managerReason}</td>`;
    pastDeniedTBody.appendChild(tableRow);
  };
};






// TO VIEW REIMBURSEMENT STATISTICS




// TO LOGOUT
function logout(){
  sessionStorage.clear();
  window.location.href = "index.html";
};
