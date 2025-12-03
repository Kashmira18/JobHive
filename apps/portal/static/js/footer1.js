// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
  const submitBtn = document.getElementById("submitBtn");
  const emailInput = document.getElementById("email");

  submitBtn.addEventListener("click", function () {
    const email = emailInput.value.trim();

    if (email === "") {
      alert("⚠️ Please enter your email address!");
    } else if (!validateEmail(email)) {
      alert("❌ Please enter a valid email address!");
    } else {
      alert(`✅ Thank you! ${email} has been subscribed.`);
      emailInput.value = ""; // Clear input
    }
  });

  // Email validation function
  function validateEmail(email) {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
  }
});

// footer1.js
document.addEventListener("DOMContentLoaded", function () {
  const btn = document.querySelector(".btn-newsletter");
  btn.addEventListener("click", function (e) {
    e.preventDefault();
    btn.textContent = "Subscribed!";
    btn.style.backgroundColor = "#198754";
    setTimeout(() => {
      btn.textContent = "Subscribe Now";
      btn.style.backgroundColor = "#212529";
    }, 3000);
  });
});
