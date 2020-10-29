const navItems = document.querySelectorAll(".category-item");

document.addEventListener("DOMContentLoaded", () => {
  const currentHref = window.location.href;
  let current;

  navItems.forEach((item) => {
    let href = item.querySelector("a").href;

    if (currentHref === href) {
      current = item;
    }
  });
  if (current) {
    current.style.borderBottom = "1px solid black";
  }
});
