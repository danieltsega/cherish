document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".fade-in-out");
  
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
        } else {
          entry.target.classList.remove("in-view");
        }
      });
    });
  
    // Observe each element
    elements.forEach((el) => observer.observe(el));
  });