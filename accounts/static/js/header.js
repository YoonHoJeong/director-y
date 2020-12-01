document.addEventListener("DOMContentLoaded", () => {
  const currentHref = window.location.href;
  const navItems = document.querySelectorAll(".category-item");
  let current;

  const setDropdown = () => {
    const navSetting = document.querySelector(".nav-bar__setting");

    if (navSetting) {
      const dropdownBar = document.querySelector(".dropdown-status");
      dropdownBar.style.display = "none";

      const handleOverSetting = () => {
        dropdownBar.style.display = "flex";
        console.log("hover");
      };

      const handleLeaveSetting = () => {
        setTimeout(() => {
          dropdownBar.style.display = "none";
          console.log("leave");
        }, 200);
      };
      navSetting.addEventListener("mouseover", handleOverSetting);
      navSetting.addEventListener("mouseleave", handleLeaveSetting);
    }
  };

  setDropdown();

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
