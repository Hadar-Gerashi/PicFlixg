document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("profileImageInput");
    const fileNameSpan = document.getElementById("fileNameText");
    const updateButton = document.getElementById("updateImageButton");

    fileInput.addEventListener("change", function () {
        if (this.files && this.files.length > 0) {
            fileNameSpan.textContent = this.files[0].name;
            updateButton.disabled = false;
        } else {
            fileNameSpan.textContent = 'Click to upload a profile image';
            updateButton.disabled = true;
        }
    });
});
