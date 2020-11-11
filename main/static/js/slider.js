window.addEventListener("load", function () {
  const prevBtn = document.querySelector(".prev-btn");
  const nextBtn = document.querySelector(".next-btn");
  const slider = document.querySelector(".slider");
  const productCount = document.querySelectorAll(".movie").length;

  let currentIdx = 0;

  const moveSlide = (num) => {
    slider.style = `left: ${num * -210}px`;
    currentIdx = num;
  };

  const handleClickPrev = (e) => {
    moveSlide(currentIdx - 1);
    if (currentIdx <= 0) {
      moveSlide(0);
    }
  };
  const handleClickNext = (e) => {
    moveSlide(currentIdx + 1);
    if (currentIdx + 4 >= productCount) {
      moveSlide(0);
    }
  };

  prevBtn.addEventListener("click", handleClickPrev);
  nextBtn.addEventListener("click", handleClickNext);
});
