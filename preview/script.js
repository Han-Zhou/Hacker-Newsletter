function displayCurrentDate() {
    var today = new Date();
    var date = today.toLocaleDateString(); // Format the date as a string
    document.getElementById('currentDate').textContent = date;
}

// Function to add a news item dynamically
function addNewsItem(titleText, summaryText) {
    // Create the news div
    const newsDiv = document.createElement('div');
    newsDiv.className = 'news';

    // Create the title div
    const titleDiv = document.createElement('div');
    titleDiv.className = 'title';
    titleDiv.textContent = titleText;

    // Create the summary div
    const summaryDiv = document.createElement('div');
    summaryDiv.className = 'summary';
    summaryDiv.textContent = summaryText;

    // Append the title and summary to the news div
    newsDiv.appendChild(titleDiv);
    newsDiv.appendChild(summaryDiv);

    // Append the news div to the container
    const container = document.getElementById('news-container');
    container.appendChild(newsDiv);
}




// Call the function when the page loads
window.onload = displayCurrentDate;