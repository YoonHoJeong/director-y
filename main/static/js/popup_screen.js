window.addEventListener("load", function () {
  const images = document.querySelectorAll(".slider .profile-image");
  const backScreen = document.querySelector(".back-screen");
  const header = document.querySelector("header");
  const closeBtn = document.querySelector(".close-bs-btn");

  // left: 37, up: 38, right: 39, down: 40,
  // spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36
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

  const handleClickImage = (e) => {
    const scrollTop = document.documentElement.scrollTop;
    const width = document.body.clientWidth;
    const height = document.body.clientHeight;

    header.style.display = "none";

    backScreen.style.display = "flex";
    backScreen.style.top = `${scrollTop}px`;
    backScreen.style.zIndex = "0";
    backScreen.style.opacity = "1";

    disableScroll();
  };
  const handleClickClose = (e) => {
    header.style.display = "flex";
    // backScreen.style.display = "none";
    backScreen.style.zIndex = "-1";

    backScreen.style.opacity = "0";
    enableScroll();
  };

  const handleOverImage = (e) => {
    const image = e.target;
    const hoverScreen = image.querySelector(".hover-screen");
    hoverScreen.style.visibility = "visible";
  };

  const handleLeaveImage = (e) => {
    const image = e.target;
    const hoverScreen = image.querySelector(".hover-screen");
    hoverScreen.style.visibility = "hidden";
  };

  const initPFRevise = () => {
    const reviseBtn = document.querySelector(".actor-portfolio .btn--revise");
    const doneBtn = document.querySelector(".actor-portfolio .btn--done");
    const onClickRevise = (e) => {
      doneBtn.style.display = "block";
      reviseBtn.style.display = "none";

      images.forEach((image) => {
        image.removeEventListener("click", handleClickImage);
        image.addEventListener("mouseover", handleOverImage);
        image.addEventListener("mouseleave", handleLeaveImage);
      });
    };
    const onClickDone = (e) => {
      doneBtn.style.display = "none";
      reviseBtn.style.display = "block";
      images.forEach((image) => {
        image.addEventListener("click", handleClickImage);
        image.removeEventListener("mouseover", handleOverImage);
        image.removeEventListener("mouseleave", handleLeaveImage);
      });
    };

    reviseBtn.addEventListener("click", onClickRevise);
    doneBtn.addEventListener("click", onClickDone);
  };

  closeBtn.addEventListener("click", handleClickClose);
  images.forEach((image) => {
    image.addEventListener("click", handleClickImage);
    // const deleteBtn = image.querySelector("a");
    // deleteBtn.addEventListener("click", (e) => {
    //   e.preventDefault();
    //   const onDelete = confirm();
    //   if onDelete:

    // })
  });
  initPFRevise();
});
