// This script is just to make the tabs work.
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




// This script connects the server to the website.
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
    tableRow.innerHTML = `<td>${rb.reimburseId}</td><td>${rb.employeeId}</td><td>${rb.requestLabel}</td><td>${rb.amount}</td><td>${rb.status}</td>`;
    tableBody.appendChild(tableRow);
  };
};




//This function will let an employee create a reimbursement request.
