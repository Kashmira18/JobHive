// Optional JS: Sticky effect or custom behavior
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.custom-navbar');
  if (window.scrollY > 30) {
    navbar.classList.add('shadow-sm');
  } else {
    navbar.classList.remove('shadow-sm');
  }
});
// footer 1js
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
