document.addEventListener("DOMContentLoaded", () => {
  const currentHref = window.location.href;
  const navItems = document.querySelectorAll(".category-item");
  let current;

  navItems.forEach((item) => {
    let href = item.querySelector("a").href;

    if (currentHref === href) {
      current = item;
    }
  });
  if (current) {
    current.style.borderBottom = "2px solid black";
  }
});
