function displayFileName() {
    const fileInput = document.getElementById('file');
    const fileNameDisplay = document.getElementById('file-name');
    
    if (fileInput.files.length > 0) {
        fileNameDisplay.textContent = `Selected File: ${fileInput.files[0].name}`;
    } else {
        fileNameDisplay.textContent = "No file selected";
    }
}
