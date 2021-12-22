// TO MAKE THE TABS WORK
function openTab(evt, tabName) {
  let tabcontent = document.getElementsByClassName("tabcontent");
  for (let i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
    document.getElementById("request-created").textContent = ``;
  };
  let tablink = document.getElementsByClassName("tablink");
  for (let i = 0; i < tablink.length; i++) {
    tablink[i].className = tablink[i].className.replace(" active", "");
  };
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
};




// TO VIEW REIMBURSMENT DATA FOR THAT EMPLOYEE THAT LOGGED IN
// Putting a reference to the table inside of a JS variable.
const table = document.getElementById("reimburse-table");
const tableBody = document.getElementById("r-body");
// Making an event to activate the request with the button.
let button = document.getElementById("view");
button.addEventListener("click", getReimburseData);

// The function to send a request and create a promise while this loads.
async function getReimburseData(){
  tableBody.innerHTML = ``;
  // Adding a reference to the route.
  const viewReimburseRoute = "http://127.0.0.1:5000/employee/reimbursement/";
  // Fetching the information from the route.
  let response = await fetch(viewReimburseRoute + sessionStorage.getItem("valueEmp"));
  if(response.status == 200){
    // Storing a reference to the json inside "rBody".
    let body = await response.json();
    // So long as we get the status of 200 back, the data will be populated into the table.
    console.log(body);
    populateReimburseData(body);
  } else {
    alert("Could not retrieve reimbursement data!")
  }
};


// This function will put the json data into the table on the website.
function populateReimburseData(jsonBody){
  for(let rb of jsonBody){
    let tableRow = document.createElement("tr");
    tableRow.innerHTML = `<td>${rb.reimburseId}</td><td>${rb.employeeId}</td><td>${rb.requestLabel}</td><td>${rb.amount}</td><td>${rb.status}</td><td>${sessionStorage.getItem("reason")}</td>`;
    tableBody.appendChild(tableRow);
  };
};





// TO CREATE A NEW REIMBURSEMENT.
async function createReimbursement(){
  let requestLabel = document.getElementById("purpose");
  let amount = document.getElementById("amount");
  const submitReimburseRoute = "http://127.0.0.1:5000/employee/reimbursement";
  let response = await fetch(submitReimburseRoute, {headers:{'Content-Type': 'application/json'},
                            method:["POST"], body:JSON.stringify({"reimburseId": 0,"employeeId": sessionStorage.getItem("valueEmp"), "requestLabel": requestLabel.value,
                          "amount": amount.value, "status": ""}) });
  let requestMessage = document.getElementById("request-created");
  if(response.status == 200){
    if(amount > 0){
      let createBody = await response.json();
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




function logout(){
  sessionStorage.clear();
  window.location.href = "index.html";
};
