document.getElementById('searchForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const q = document.getElementById('q').value.trim();
    const loc = document.getElementById('location').value;
    const type = document.getElementById('type').value;
    alert(`Searching for: "${q || 'any job'}" | Location: ${loc || 'Anywhere'} | Type: ${type}`);
});
// _______numbering_________

document.addEventListener('DOMContentLoaded', function () {
    const statNumbers = document.querySelectorAll('.stat-number');
    const statsSection = document.querySelector('.stats-section');
    let counterExecuted = false;

    // Counter function
    function runCounter() {
        statNumbers.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            const duration = 2000; // 2 seconds duration
            const increment = target / (duration / 16); // ~60fps

            let current = 0;

            const updateCounter = () => {
                current += increment;
                if (current < target) {
                    counter.innerText = Math.ceil(current).toLocaleString();
                    requestAnimationFrame(updateCounter);
                } else {
                    // Ensure the final number is exact
                    counter.innerText = target.toLocaleString();
                }
            };

            updateCounter();
        });
    }

    // Intersection Observer to run the counter when the section becomes visible
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            // Check if the section is intersecting and the counter hasn't run yet
            if (entry.isIntersecting && !counterExecuted) {
                runCounter();
                counterExecuted = true;
                observer.unobserve(statsSection); // Stop observing after execution
            }
        });
    }, {
        threshold: 0.1 // Run when 10% of the section is visible
    });

    // Start observing the statistics section
    observer.observe(statsSection);
});