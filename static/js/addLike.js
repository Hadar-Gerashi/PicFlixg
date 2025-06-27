
document.querySelectorAll(".like-btn").forEach(button => {
    button.addEventListener("click", function () {
        const videoId = this.dataset.videoId;

        fetch("/toggle_like", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `video_id=${encodeURIComponent(videoId)}`
        })
            .then(res => res.json())
            .then(data => {
                if (data.status === "success") {
                    const countElem = document.getElementById("like-count-" + videoId);
                    if (countElem) {
                        countElem.textContent = data.likes_count;
                    }

                    if (data.action === "liked") {
                        this.classList.add("liked");
                    } else if (data.action === "unliked") {
                        this.classList.remove("liked");
                    }
                } else {
                    alert(data.message || "Error");
                }
            });
    });
});

