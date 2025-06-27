
const input = document.getElementById("searchInput");
const suggestionsBox = document.getElementById("suggestions");
const searchContainer = document.querySelector('.search-container');

// Search functionality with your server API
input.addEventListener("input", function () {
    const query = input.value;
    if (query.length === 0) {
        suggestionsBox.innerHTML = "";
        suggestionsBox.style.display = 'none';
        return;
    }

    fetch(`/search_users?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            const users = data.users;
            suggestionsBox.innerHTML = "";

            if (users.length === 0) {
                suggestionsBox.innerHTML = '<div class="suggestion-item">No results found</div>';

            } else {
                users.forEach(user => {
                    const div = document.createElement("div");
                    div.classList.add("suggestion-item");

                    // Create user profile structure like TikTok
                    div.innerHTML = `
                        <div style="width: 30px; height: 30px; background: linear-gradient(45deg, #ff0050, #ff4080); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 12px;">
                            ${user.name.charAt(0)}
                        </div>
                        <div>
                            <div style="font-weight: 500;">${user.name}</div>
                            <div style="font-size: 12px; color: rgba(255,255,255,0.6);">@${user.name.toLowerCase().replace(' ', '_')}</div>
                        </div>
                    `;

                    div.onclick = () => {
                        input.value = user.name;
                        suggestionsBox.innerHTML = "";
                        suggestionsBox.style.display = 'none';
                        window.location.href = `/profile/${user.id}`;
                    };

                    suggestionsBox.appendChild(div);
                });
            }

            suggestionsBox.style.display = 'block';
        })
        .catch(err => {
            console.error("Search error:", err);
            suggestionsBox.innerHTML = '<div class="suggestion-item" style="color: #ff6b6b;">Search error</div>';
            suggestionsBox.style.display = 'block';
        });
});

// Focus animations
input.addEventListener('focus', function () {
    searchContainer.classList.add('focused');
});

input.addEventListener('blur', function () {
    searchContainer.classList.remove('focused');
    // Delay hiding suggestions to allow for clicks
    setTimeout(() => {
        if (!input.matches(':focus')) {
            suggestionsBox.style.display = 'none';
        }
    }, 200);
});

// Mobile menu toggle
document.querySelector('.navbar-toggle').addEventListener('click', function () {
    const navLinks = document.querySelector('.nav-links');
    if (navLinks.style.display === 'flex') {
        navLinks.style.display = 'none';
    } else {
        navLinks.style.display = 'flex';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '100%';
        navLinks.style.left = '0';
        navLinks.style.right = '0';
        navLinks.style.background = 'rgba(0,0,0,0.95)';
        navLinks.style.flexDirection = 'column';
        navLinks.style.padding = '20px';
        navLinks.style.borderRadius = '0 0 15px 15px';
        navLinks.style.backdropFilter = 'blur(20px)';
    }
});

// Close mobile menu when clicking outside
document.addEventListener('click', function (e) {
    const navLinks = document.querySelector('.nav-links');
    const toggleButton = document.querySelector('.navbar-toggle');

    if (!toggleButton.contains(e.target) && !navLinks.contains(e.target)) {
        if (window.innerWidth <= 768) {
            navLinks.style.display = 'none';
        }
    }
});

// Handle window resize
window.addEventListener('resize', function () {
    const navLinks = document.querySelector('.nav-links');
    if (window.innerWidth > 768) {
        navLinks.style.display = 'flex';
        navLinks.style.position = 'static';
        navLinks.style.flexDirection = 'row';
        navLinks.style.background = 'none';
        navLinks.style.padding = '0';
    } else {
        navLinks.style.display = 'none';
    }
});


