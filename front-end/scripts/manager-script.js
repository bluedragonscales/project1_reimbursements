// TO MAKE THE TABS WORK
function openTab(evt, tabName) {
  let tabcontent = document.getElementsByClassName("tabcontent");
  for (let i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  };
  let tablink = document.getElementsByClassName("tablink");
  for (let i = 0; i < tablink.length; i++) {
    tablink[i].className = tablink[i].className.replace(" active", "");
  };
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
};



// TO GET ALL THE REIMBURSEMENT DATA
// The function to send a request and create a promise while this loads.
async function getReimburseData(){
  tableBody.innerHTML = ``;
  // Adding a reference to the route.
  const viewAllReimbursements = "http://127.0.0.1:5000/manager/reimbursement";
  // Fetching the information from the route.
  let response = await fetch(viewAllReimbursements);
  // Storing a reference to the json inside "rBody".
  // let body = await response.json;
  // So long as we get the status of 200 back, the data will be populated into the table.
  if(response.status == 200){
    let body = await response.json();
    console.log(body);
    populateReimburseData(body);
  } else {
    alert("Could not populate reimbursement data!")
  }
};


// TO VIEW ALL REIMBURSEMENTS
// Putting a reference to the table inside of a JS variable.
const tableBody = document.getElementById("r-body");
// Making an event to activate the request with the button.
let button = document.getElementById("view");
button.addEventListener("click", getReimburseData);

// This function will put the json data into the table on the website.
function populateReimburseData(jsonBody){
  for(let rb of jsonBody){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = `<td>${rb.reimburseId}</td><td>${rb.employeeId}</td><td>${rb.requestLabel}</td><td>${rb.amount}</td><td>${rb.status}</td>`;
    tableBody.appendChild(tableRow);
  };
};




// TO SET REIMBURSEMENT STATUS
async function setReimburseStatus(){
  let managerInput = document.getElementById("r-id");
  let statusInput = document.getElementById("reimburse-status");
  let requestStatus = "http://127.0.0.1:5000/manager/reimbursement/";
  let response = await fetch(requestStatus + managerInput.value, {headers:{'Content-Type': 'application/json'}, method: "PATCH", body:JSON.stringify({"status": statusInput.value}) });
  let statusBody = await response.json();
  console.log(statusBody);
};
let statusButton = document.getElementById("submit-status");
statusButton.addEventListener("click", setReimburseStatus);





// TO VIEW REIMBURSEMENT STATISTICS
async function viewStatistics(){
  let statView = document.getElementById("select-statistic");
  let viewStatsRoute = "http://127.0.0.1:5000/manager/statistics";
  let response = await fetch(viewStatsRoute, {headers:{"Content-Type":"application/json"}, method:["POST"], body:JSON.stringify({"statistic": statView.value}) });
  if(response.status == 200){
    let statBody = await response.json();
    populateStats(statBody);
  } else {
    alert("Could not populate statistics!")
  };
};

function populateStats(jsonStats){
  let statHeading = document.getElementById("view-stats");
  statHeading.textContent = `${jsonStats}`;
};




// TO LOGOUT
function logout(){
  sessionStorage.clear();
  window.location.href = "index.html";
};
