window.addEventListener("load", function () {
  const prevBtn = document.querySelector(".prev-btn");
  const nextBtn = document.querySelector(".next-btn");
  const slider = document.querySelector(".slider");
  const sliderShowArea = document.querySelector(".slider-show-area");
  const productCount = document.querySelectorAll(".movie").length;
  const sliderLength = slider.width;

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
    const areaLength = sliderShowArea.offsetWidth;
    const maxCount = Math.ceil(areaLength / 210);
    console.log(sliderShowArea);

    moveSlide(currentIdx + 1);
    if (productCount < currentIdx + maxCount) {
      moveSlide(0);
    }
  };

  prevBtn.addEventListener("click", handleClickPrev);
  nextBtn.addEventListener("click", handleClickNext);
});
