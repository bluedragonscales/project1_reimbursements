// TO MAKE THE TABS WORK
function openTab(evt, tabName) {
  let tabcontent = document.getElementsByClassName("tabcontent");
  for (let i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
    document.getElementById("status-message").textContent = ``;
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
// Employee with the highest dollar amount in reimbursement requests.
let highStatMessage = document.getElementById("stat-1");
let highStatButton = document.getElementById("stat-1-btn");
highStatButton.addEventListener("click", empWithHighestDollar);


async function empWithHighestDollar(){
  highStatMessage.textContent = '';
  const statsRoute = "http://127.0.0.1:5000/manager/highestReimburseTotal";
  let response = await fetch(statsRoute);
  let statsBody = await response.json();

  if(response.status == 200){
    // console.log(statsBody);
    let empName = statsBody.employeeName;
    let reimburseTotal = statsBody.reimbursementTotal;
    highStatMessage.textContent = `Employee ${empName} has the highest dollar total of reimbursement requests at $${reimburseTotal}.`;
  } 
  else {
    alert("Could not retrieve stats.")
  }
};



// Employee that has made the most reimbursement requests.
let mostStatMessage = document.getElementById("stat-2");
let mostStatButton = document.getElementById("stat-2-btn");
mostStatButton.addEventListener("click", empWithMostRequests);

async function empWithMostRequests(){
  mostStatMessage.textContent = '';
  const statsRoute = "http://127.0.0.1:5000/manager/mostReimburseRequests";
  let response = await fetch(statsRoute);
  let statsBody = await response.json();

  if(response.status == 200){
    // console.log(statsBody);
    let empName = statsBody.employeeName;
    let reimburseRequests = statsBody.amountOfRequests;
    mostStatMessage.textContent = `Employee ${empName} has the most reimbursement requests at ${reimburseRequests} requests.`;
  } 
  else {
    alert("Could not retrieve stats.")
  }
};



// Total dollar amount of all reimbursement requests that have been approved.
let approvedAmountMessage = document.getElementById("stat-3");
let approvedAmountButton = document.getElementById("stat-3-btn");
approvedAmountButton.addEventListener("click", approvedDollarTotal);

async function approvedDollarTotal(){
  approvedAmountMessage.textContent = '';
  const statsRoute = "http://127.0.0.1:5000/manager/dollarTotalOfApprovals";
  let response = await fetch(statsRoute);
  let statsBody = await response.json();

  if(response.status == 200){
    let approvedTotal = statsBody.dollarTotalApproved;
    approvedAmountMessage.textContent = `The dollar total of approved reimbursements comes to $${approvedTotal}.`;
  } 
  else {
    alert("Could not retrieve stats.")
  }
};




// The employee that has been denied the most times.
let empDeniedMessage = document.getElementById("stat-5");
let empDeniedButton = document.getElementById("stat-5-btn");
empDeniedButton.addEventListener("click", empWithMostDenials);

async function empWithMostDenials(){
  empDeniedMessage.textContent = '';
  const statsRoute = "http://127.0.0.1:5000/manager/employeeMostDenials";
  let response = await fetch(statsRoute);
  let statsBody = await response.json();

  if(response.status == 200){
    let empName = statsBody.employeeName;
    let denialsTotal = statsBody.amountOfDenials;
    empDeniedMessage.textContent = `Employee ${empName} has the most denied reimbursement requests at a total of ${denialsTotal}.`;
  } 
  else {
    alert("Could not retrieve stats.")
  }
};





// The employee that has been approved the most times.
let empApprovedMessage = document.getElementById("stat-4");
let empApprovedButton = document.getElementById("stat-4-btn");
empApprovedButton.addEventListener("click", empWithMostApprovals);

async function empWithMostApprovals(){
  empApprovedMessage.textContent = '';
  const statsRoute = "http://127.0.0.1:5000/manager/employeeMostApprovals";
  let response = await fetch(statsRoute);
  let statsBody = await response.json();

  if(response.status == 200){
    let empName = statsBody.employeeName;
    let approvalsTotal = statsBody.amountOfApprovals;
    empApprovedMessage.textContent = `Employee ${empName} has the most approved reimbursement requests at a total of ${approvalsTotal}.`;
  } 
  else {
    alert("Could not retrieve stats.")
  }
};






// TO LOGOUT
function logout(){
  sessionStorage.clear();
  window.location.href = "index.html";
};
