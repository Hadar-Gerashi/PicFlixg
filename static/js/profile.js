
function validateForm() {
    const selected = document.querySelectorAll('input[name="category_id[]"]:checked');
    const fileInput = document.querySelector('input[name="file"]');
    const uploadBtn = document.getElementById('uploadBtn');

    uploadBtn.disabled = !(selected.length > 0 && fileInput.files.length > 0);
}

document.querySelectorAll('input[name="category_id[]"]').forEach(el => {
    el.addEventListener('change', validateForm);
});

document.querySelector('input[name="file"]').addEventListener('change', validateForm);




