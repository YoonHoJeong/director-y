document.addEventListener("DOMContentLoaded", () => {
  const sectionItems = document.querySelectorAll(".section-item");
  const section = document.querySelector(".section");
  const sectionTitle = document.querySelector(".section-title");
  const sectionMain = document.querySelector(".section-main");
  const sectionBG = document.querySelector(".section-background");
  const cancleBtn = document.querySelector(".section-cancle");
  const sectionThumb = document.querySelector(".section-thumbnail");

  var keys = { 37: 1, 38: 1, 39: 1, 40: 1 };

  function preventDefault(e) {
    e.preventDefault();
  }

  function preventDefaultForScrollKeys(e) {
    if (keys[e.keyCode]) {
      preventDefault(e);
      return false;
    }
  }

  // modern Chrome requires { passive: false } when adding event
  var supportsPassive = false;
  try {
    window.addEventListener(
      "test",
      null,
      Object.defineProperty({}, "passive", {
        get: function () {
          supportsPassive = true;
        },
      })
    );
  } catch (e) {}

  var wheelOpt = supportsPassive ? { passive: false } : false;
  var wheelEvent =
    "onwheel" in document.createElement("div") ? "wheel" : "mousewheel";

  // call this to Disable
  function disableScroll() {
    window.addEventListener("DOMMouseScroll", preventDefault, false); // older FF
    window.addEventListener(wheelEvent, preventDefault, wheelOpt); // modern desktop
    window.addEventListener("touchmove", preventDefault, wheelOpt); // mobile
    window.addEventListener("keydown", preventDefaultForScrollKeys, false);
  }

  // call this to Enable
  function enableScroll() {
    window.removeEventListener("DOMMouseScroll", preventDefault, false);
    window.removeEventListener(wheelEvent, preventDefault, wheelOpt);
    window.removeEventListener("touchmove", preventDefault, wheelOpt);
    window.removeEventListener("keydown", preventDefaultForScrollKeys, false);
  }

  sectionItems.forEach((sectionItem) => {
    sectionItem.addEventListener("click", (e) => {
      e.preventDefault();
      section.style.display = "flex";
      const sectionInfo = e.target.parentNode;
      const sectionName = sectionItem.querySelector(".section-name").innerText;
      const sectionCon = sectionItem.querySelector(".section-content")
        .innerText;
      const sectionUrl = sectionItem.querySelector(".section-url").value;

      sectionTitle.innerText = sectionName;
      sectionMain.innerHTML = sectionCon;

      sectionThumb.style.backgroundImage = `url('${sectionUrl}')`;
      console.log(sectionThumb, sectionUrl);

      sectionBG.style.display = "flex";
      disableScroll();
    });
  });

  cancleBtn.addEventListener("click", (e) => {
    e.preventDefault();
    section.style.display = "none";
    sectionBG.style.display = "none";
    enableScroll();
  });
});
