
let selectedCategories = [];

function toggleDropdown() {
    const options = document.getElementById('categoryOptions');
    const arrow = document.getElementById('dropdownArrow');
    const dropdown = document.querySelector('.multi-select-dropdown');

    options.classList.toggle('show');
    arrow.classList.toggle('rotated');
    dropdown.classList.toggle('active');
}

function toggleCategory(id, name) {
    const checkbox = document.getElementById('cat' + id);
    const index = selectedCategories.findIndex(cat => cat.id === id);

    if (checkbox.checked) {
        if (index === -1) {
            selectedCategories.push({ id: id, name: name });
        }
    } else {
        if (index > -1) {
            selectedCategories.splice(index, 1);
        }
    }

    updateSelectedDisplay();
    updateUploadButton();
}

function removeCategory(id) {
    const checkbox = document.getElementById('cat' + id);
    checkbox.checked = false;

    const index = selectedCategories.findIndex(cat => cat.id === id);
    if (index > -1) {
        selectedCategories.splice(index, 1);
    }

    updateSelectedDisplay();
    updateUploadButton();
}

function updateSelectedDisplay() {
    const container = document.getElementById('selectedCategories');

    if (selectedCategories.length === 0) {
        container.innerHTML = '<span style="color: #9ca3af;">Select Categories...</span>';
    } else {
        container.innerHTML = selectedCategories.map(cat =>
            `<span class="category-tag">
                    ${cat.name}
                    <span class="remove" onclick="removeCategory('${cat.id}')">&times;</span>
                </span>`
        ).join('');
    }
}

function updateFileName(input) {
    const fileText = document.getElementById('fileText');
    if (input.files.length > 0) {
        fileText.textContent = input.files[0].name;
    } else {
        fileText.textContent = '🎥 Click to select a video file or drag it here';
    }
    updateUploadButton();
}

function updateUploadButton() {
    const uploadBtn = document.getElementById('uploadBtn');
    const fileInput = document.querySelector('input[type="file"]');

    const hasFile = fileInput.files.length > 0;
    const hasCategories = selectedCategories.length > 0;

    uploadBtn.disabled = !(hasFile && hasCategories);
}

function confirmDeleteSubmit() {
    return confirm('Are you sure you want to delete the video?');
}

function closeDeleteModal() {
    document.getElementById('deleteModal').classList.remove('show');
}

// Close dropdown when clicking outside
document.addEventListener('click', function (event) {
    const container = document.querySelector('.multi-select-container');
    if (!container.contains(event.target)) {
        document.getElementById('categoryOptions').classList.remove('show');
        document.getElementById('dropdownArrow').classList.remove('rotated');
        document.querySelector('.multi-select-dropdown').classList.remove('active');
    }
});
