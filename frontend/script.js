const API_URL = `http://${window.location.hostname}:8000`;
// ===============================
// PDF UPLOAD
// ===============================

const fileInput = document.getElementById("fileInput");
const uploadButton = document.getElementById("uploadButton");
const fileName = document.getElementById("fileName");
const uploadStatus = document.getElementById("uploadStatus");


// Show selected PDF name
fileInput.addEventListener("change", () => {

    if (fileInput.files.length > 0) {
        fileName.textContent = fileInput.files[0].name;
        uploadStatus.textContent = "";
    } else {
        fileName.textContent = "No file selected";
    }

});


// Upload PDF to FastAPI
uploadButton.addEventListener("click", async () => {

    if (!fileInput.files.length) {
        uploadStatus.textContent = "Please choose a PDF first.";
        return;
    }

    const file = fileInput.files[0];

    uploadStatus.textContent = "Uploading...";
    uploadButton.disabled = true;

    try {

        const formData = new FormData();

        formData.append("file", file);

        const response = await fetch(
    `${API_URL}/documents/upload`,
    {
        method: "POST",
        body: formData
    }
);

        if (!response.ok) {
            throw new Error("Upload failed");
        }

        const data = await response.json();

        uploadStatus.textContent =
            "✅ " + data.message;

    } catch (error) {

        console.error("Upload error:", error);

        uploadStatus.textContent =
            "❌ Could not upload the document.";

    }

    uploadButton.disabled = false;

});
const questionInput = document.getElementById("questionInput");
const askButton = document.getElementById("askButton");
const chatBox = document.getElementById("chatBox");
const askStatus = document.getElementById("askStatus");


askButton.addEventListener("click", async () => {

    const question = questionInput.value.trim();

    if (!question) {
        askStatus.textContent = "Please enter a question.";
        return;
    }

    // Show user's question
    const userMessage = document.createElement("div");
    userMessage.className = "message user";

    userMessage.innerHTML = `
        <strong>You:</strong>
        <p>${question}</p>
    `;

    chatBox.appendChild(userMessage);

    // Clear input
    questionInput.value = "";

    // Show status
    askStatus.textContent = "AI is thinking...";

    // Disable button
    askButton.disabled = true;

    try {
    const response = await fetch(`${API_URL}/ask`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    });

    if (!response.ok) {
        throw new Error("API request failed");
    }

    const data = await response.json();

    // Show AI answer
    const aiMessage = document.createElement("div");
    aiMessage.className = "message assistant";

    aiMessage.innerHTML = `
        <strong>AI:</strong>
        <p>${data.answer}</p>
    `;

    chatBox.appendChild(aiMessage);

    askStatus.textContent = "Answer generated.";

} catch (error) {
    console.error(error);

    const errorMessage = document.createElement("div");
    errorMessage.className = "message assistant";

    errorMessage.innerHTML = `
        <strong>AI:</strong>
        <p>Sorry, I couldn't connect to the AI server.</p>
    `;

    chatBox.appendChild(errorMessage);
}

askButton.disabled = false;
});