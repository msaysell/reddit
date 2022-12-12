const apiBaseUrl = "http://localhost:8000";
const submissionEndpoint = "/reddit/submissions/"

var totalCount = null;
var pageSize = 5;

const fetchSubmissions = async (offset) => {
    
    const submission_endpoint = apiBaseUrl + submissionEndpoint + "?limit=" + pageSize + "&offset=" + offset;
    const response = await fetch(submission_endpoint);
    
    const responseJson = await response.json();
    console.table(responseJson);
    if(totalCount === null)
        setupPagination(responseJson.count);
        totalCount = responseJson.count;

    const submissionDiv = document.getElementById("submissions");
    submissionDiv.innerHTML = "";

    (responseJson.results).forEach(element => {
        submissionDiv.appendChild(createSubmissionCard(element));
    });

    return false;
};

function setupPagination(count) {

    const pagination = document.createElement("ul");
    pagination.className = "pagination flex-wrap justify-content-center"; 

    var current_page = 0;
    while (current_page < count) {
        const paginationTab = document.createElement("li");
        paginationTab.className = "page-item";

        const paginationLink = document.createElement("a");
        paginationLink.href = "javascript:fetchSubmissions(" + current_page + ")";
        paginationLink.className = "page-link";
        paginationLink.appendChild(document.createTextNode((current_page + 1) + " - " + (Math.min(current_page + pageSize, count))));

        paginationTab.appendChild(paginationLink);
        pagination.appendChild(paginationTab);

        current_page += pageSize;
    }

    const paginationDiv = document.getElementById("pagination");
    paginationDiv.appendChild(pagination);

}

function createSubmissionCard(submissionData) {
    const responseCard = document.createElement("div");
    responseCard.className = "card mb-3";

    const responseCardHeader = document.createElement("div");
    responseCardHeader.className = "card-header";


    const responseCardTitle = document.createElement("h5");
    responseCardTitle.className = "card-title";
    responseCardTitle.appendChild(document.createTextNode(submissionData.title));
    
    const responseCardBody = document.createElement("div");
    responseCardBody.className = "card-body";

    const responseCardSubTitle = document.createElement("h6");
    responseCardSubTitle.className = "card-subtitle mb-2 text-muted";
    responseCardSubTitle.appendChild(document.createTextNode(submissionData.author));
    
    const responseCardLink = document.createElement("a");
    responseCardLink.href = submissionData.url;
    responseCardLink.className = "card-link";
    responseCardLink.appendChild(document.createTextNode("View more"));

    responseCardHeader.appendChild(responseCardTitle);
    responseCardBody.appendChild(responseCardSubTitle);
    responseCardBody.appendChild(responseCardLink);
    responseCard.appendChild(responseCardHeader)
    responseCard.appendChild(responseCardBody)

    return responseCard;
}

fetchSubmissions(0);