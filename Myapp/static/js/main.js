// ============================================
// ALL CODE RUNS AFTER DOM IS FULLY LOADED
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize AOS
    AOS.init({
        duration: 800,
        once: true,
        offset: 100,
        easing: 'ease-in-out'
    });

    // Particle System
    (function createParticles() {
        const container = document.getElementById('particles');
        for (let i = 0; i < 30; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            const size = Math.random() * 4 + 2;
            particle.style.width = size + 'px';
            particle.style.height = size + 'px';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDuration = (Math.random() * 15 + 10) + 's';
            particle.style.animationDelay = (Math.random() * 10) + 's';
            particle.style.opacity = Math.random() * 0.3 + 0.1;
            container.appendChild(particle);
        }
    })();

    // Visitor Counter
    function getCSRFToken() {
        return document.cookie.split("; ").find(row => row.startsWith("csrftoken="))?.split("=")[1];
    }

    function isPageReload() {
        try {
            const navEntries = performance.getEntriesByType("navigation");
            if (navEntries.length > 0 && navEntries[0].type === 'reload') return true;
            if (performance.navigation && performance.navigation.type === performance.navigation.TYPE_RELOAD) return true;
        } catch (e) { console.error(e); }
        return false;
    }

    if (!isPageReload() && !sessionStorage.getItem("visitorCounted")) {
        sessionStorage.setItem("visitorCounted", "pending");
        fetch("/increase-visitor", {
                method: "POST",
                headers: { "X-CSRFToken": getCSRFToken() }
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    sessionStorage.setItem("visitorCounted", "true");
                    const countDisplay = document.getElementById("visitorCount");
                    if (countDisplay) countDisplay.innerText = data.count;
                } else sessionStorage.removeItem("visitorCounted");
            })
            .catch(err => { console.error(err);
                sessionStorage.removeItem("visitorCounted"); });
    }

    // Ticker clone
    const ticker = document.querySelector('.ticker-move');
    if (ticker) {
        ticker.setAttribute('data-content', ticker.textContent);
        ticker.innerHTML = ticker.innerHTML + ticker.innerHTML;
    }

    // Navbar close on mobile
    const navLinks = document.querySelectorAll('.nav-link');
    const collapse = document.getElementById('navbarContent');
    if (collapse) {
        const bsCollapse = bootstrap.Collapse.getInstance(collapse) || new bootstrap.Collapse(collapse, { toggle: false });
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth < 992 && collapse.classList.contains('show')) {
                    bsCollapse.hide();
                }
            });
        });

        collapse.addEventListener('show.bs.collapse', () => {
            document.body.classList.add('nav-open');
        });
        collapse.addEventListener('hide.bs.collapse', () => {
            document.body.classList.remove('nav-open');
        });
    }
function updateClock() {
        const timeEl = document.getElementById('live-time');
        const dateEl = document.getElementById('live-date');
        const now = new Date();
        
        if (timeEl) timeEl.textContent = now.toTimeString().split(' ')[0];
        if (dateEl) {
            const day = String(now.getDate()).padStart(2, '0');
            const month = String(now.getMonth() + 1).padStart(2, '0');
            dateEl.textContent = `${day}/${month}/${now.getFullYear()}`;
        }
    }
    updateClock();
    setInterval(updateClock, 1000);
    
    // Close navbar clicking outside
    document.addEventListener('click', function(event) {
        const toggler = document.querySelector('.navbar-toggler');
        const isClickInside = collapse?.contains(event.target) || toggler?.contains(event.target);
        if (!isClickInside && collapse?.classList.contains('show')) {
            const bsCollapse = bootstrap.Collapse.getInstance(collapse);
            if (bsCollapse) bsCollapse.hide();
        }
    });

}); // ← THIS WAS MISSING! The closing brace for the first DOMContentLoaded


// ============================================
// FITWISELY APK DOWNLOAD
// ============================================
document.addEventListener("DOMContentLoaded", () => {

    const modal = document.getElementById("app-download-modal");
    const stateConfirm = document.getElementById("modal-state-confirm");
    const stateProgress = document.getElementById("modal-state-progress");
    const stateSuccess = document.getElementById("modal-state-success");

    const btnOpen = document.getElementById("btn-open-app-modal");
    const btnCancel = document.getElementById("btn-cancel-download");
    const btnStart = document.getElementById("btn-start-download");
    const btnCloseSuccess = document.getElementById("btn-close-success");

    const APK_URL = "https://github.com/ajay9875/TaskCareMobile/releases/download/1.2.4/FitWisely.apk";
    // Verify required HTML elements
    if (!modal || !stateConfirm || !stateProgress ||
        !stateSuccess || !btnOpen || !btnCancel ||
        !btnStart || !btnCloseSuccess) {
        console.error("FitWisely download modal elements missing.");
        return;
    }

    let isDownloading = false;

    // Reset modal
    function resetModal() {
        modal.classList.remove("show");

        stateConfirm.style.display = "block";
        stateProgress.style.display = "none";
        stateSuccess.style.display = "none";

        btnStart.disabled = false;
        isDownloading = false;
    }

    // Open modal
    btnOpen.addEventListener("click", (e) => {
        e.preventDefault();

        resetModal();
        modal.classList.add("show");
    });

    // Close modal
    btnCancel.addEventListener("click", resetModal);
    btnCloseSuccess.addEventListener("click", resetModal);

    // Start APK download
    btnStart.addEventListener("click", () => {

        if (isDownloading) return;

        isDownloading = true;
        btnStart.disabled = true;

        stateConfirm.style.display = "none";
        stateProgress.style.display = "block";
        stateSuccess.style.display = "none";

        try {
            // Create a direct browser download request.
            // No iframe and no forced iframe removal.
            const downloadLink = document.createElement("a");

            downloadLink.href = APK_URL;
            downloadLink.target = "_blank";
            downloadLink.rel = "noopener noreferrer";
            downloadLink.style.display = "none";

            document.body.appendChild(downloadLink);

            // Trigger directly from the user's click
            downloadLink.click();

            downloadLink.remove();

            // Show request confirmation
            setTimeout(() => {
                stateProgress.style.display = "none";
                stateSuccess.style.display = "block";

                isDownloading = false;
                btnStart.disabled = false;

            }, 700);

        } catch (error) {

            console.error("FitWisely download error:", error);

            stateProgress.style.display = "none";
            stateConfirm.style.display = "block";

            btnStart.disabled = false;
            isDownloading = false;

            alert("Unable to start the download. Please try again.");
        }
    });

});
