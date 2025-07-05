// MindWell Landing Page Script

// Greet user based on time of day
function greetUser() {
  const greetingElement = document.createElement('p');
  const hour = new Date().getHours();
  let greeting = "Hello!";

  if (hour < 12) {
    greeting = "Good morning ☀️";
  } else if (hour < 18) {
    greeting = "Good afternoon 🌞";
  } else {
    greeting = "Good evening 🌙";
  }

  greetingElement.textContent = greeting + " Welcome to MindWell!";
  greetingElement.style.textAlign = "center";
  greetingElement.style.marginTop = "20px";
  greetingElement.style.fontSize = "1.2rem";
  greetingElement.style.color = "#4a90e2";

  document.body.insertBefore(greetingElement, document.body.children[1]);
}

// Highlight features on scroll
function revealOnScroll() {
  const features = document.querySelectorAll('.feature-card');

  features.forEach(card => {
    const rect = card.getBoundingClientRect();
    if (rect.top < window.innerHeight - 100) {
      card.style.opacity = 1;
      card.style.transform = "translateY(0)";
    }
  });
}

// Initial setup
document.addEventListener("DOMContentLoaded", () => {
  greetUser();

  // Prepare feature cards for animation
  const features = document.querySelectorAll('.feature-card');
  features.forEach(card => {
    card.style.opacity = 0;
    card.style.transform = "translateY(40px)";
    card.style.transition = "all 0.6s ease-out";
  });

  window.addEventListener("scroll", revealOnScroll);
  revealOnScroll(); // initial check
});
