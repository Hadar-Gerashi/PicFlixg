window.addEventListener('pageshow', function (event) {
    if (event.persisted || performance.navigation.type === 2) {
        location.reload();
    }
});


window.scrollingEnabled = false;
window.myFullpage = null;


window.addEventListener('DOMContentLoaded', function () {
    const currentHash = window.location.hash;
    console.log('Current hash:', currentHash);


    if (currentHash && currentHash !== '#slide01') {
        console.log('Detected return from another page, enabling scrolling');
        window.scrollingEnabled = true;


        const btn = document.querySelector('.view-videos-btn');
        if (btn) {
            btn.style.display = 'none';
        }
    }
});


window.enableScrolling = function () {
    console.log('enableScrolling called');
    window.scrollingEnabled = true;


    const btn = document.querySelector('.view-videos-btn');
    if (btn) {
        btn.style.display = 'none';
    }


    setTimeout(() => {
        console.log('Moving to first video');
        if (window.myFullpage) {
            window.myFullpage.moveSectionDown();
        } else if (typeof fullpage_api !== 'undefined') {
            fullpage_api.moveSectionDown();
        }
    }, 200);
}


window.moveToVideos = function () {
    window.enableScrolling();
}
