document.getElementById('profileImageInput').addEventListener('change', function () {
    const fileNameSpan = document.getElementById('fileNameText');
    if (this.files && this.files.length > 0) {
        fileNameSpan.textContent = this.files[0].name;
    } else {
        fileNameSpan.textContent = 'Click to upload a profile picture';

    }
});



