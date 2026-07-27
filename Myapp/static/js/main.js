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