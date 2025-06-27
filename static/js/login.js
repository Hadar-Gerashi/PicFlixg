
const fieldStates = {
    email: { touched: false, valid: false },
    password: { touched: false, valid: false }
};

function showError(fieldId, message) {
    const errorElement = document.getElementById(fieldId + '-error');
    const fieldElement = document.getElementById(fieldId + '-field');
    if (errorElement) {
        errorElement.textContent = message;
        errorElement.classList.add('show');
    }
    if (fieldElement) {
        fieldElement.classList.add('has-error');
    }
}

function hideError(fieldId) {
    const errorElement = document.getElementById(fieldId + '-error');
    const fieldElement = document.getElementById(fieldId + '-field');
    if (errorElement) {
        errorElement.textContent = '';
        errorElement.classList.remove('show');
    }
    if (fieldElement) {
        fieldElement.classList.remove('has-error');
        fieldElement.classList.add('has-success');
    }
}

function validateEmail(email, showMessage = false) {
    const isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    if (!isValid && showMessage) {
        showError('email', 'Please enter a valid email address');
    } else if (isValid) {
        hideError('email');
    }
    return isValid;
}

function validatePassword(password, showMessage = false) {
    const isValid = /^(?=.*[A-Za-z])(?=.*\d).{8,}$/.test(password);
    if (!isValid && showMessage) {
        showError('password', 'Password must be at least 8 characters long and include a letter and a number');
    } else if (isValid) {
        hideError('password');
    }
    return isValid;
}

function updateSubmitButton() {
    const submitBtn = document.getElementById('submit-btn');
    const allValid = fieldStates.email.valid && fieldStates.password.valid;
    if (submitBtn) submitBtn.disabled = !allValid;
}

function validateInitialFields() {
    const emailVal = document.getElementById('email').value.trim();
    const passwordVal = document.getElementById('password').value;

    fieldStates.email.valid = validateEmail(emailVal, false);
    fieldStates.password.valid = validatePassword(passwordVal, false);
    updateSubmitButton();
}

function togglePassword() {
    const passwordInput = document.getElementById("password");
    const eyeIcon = document.getElementById("eye-icon");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.innerHTML = `
                <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                <line x1="1" y1="1" x2="23" y2="23"></line>
            `;
    } else {
        passwordInput.type = "password";
        eyeIcon.innerHTML = `
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                <circle cx="12" cy="12" r="3"></circle>
            `;
    }
}

// Event listeners
window.addEventListener('load', validateInitialFields);

document.getElementById('email').addEventListener('input', function (e) {
    fieldStates.email.touched = true;
    fieldStates.email.valid = validateEmail(e.target.value.trim(), true);
    updateSubmitButton();
});

document.getElementById('password').addEventListener('input', function (e) {
    fieldStates.password.touched = true;
    fieldStates.password.valid = validatePassword(e.target.value, true);
    updateSubmitButton();
});

document.getElementById('login-form').addEventListener('submit', function (e) {
    const emailVal = document.getElementById('email').value.trim();
    const passwordVal = document.getElementById('password').value;

    fieldStates.email.touched = true;
    fieldStates.password.touched = true;

    const emailValid = validateEmail(emailVal, true);
    const passwordValid = validatePassword(passwordVal, true);

    if (!emailValid || !passwordValid) {
        e.preventDefault();
    }
});

