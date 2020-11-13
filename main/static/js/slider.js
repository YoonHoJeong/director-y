window.addEventListener("load", function () {
  const prevBtn = document.querySelector(".prev-btn");
  const nextBtn = document.querySelector(".next-btn");
  const slider = document.querySelector(".slider");
  const sliderShowArea = document.querySelector(".slider-show-area");
  const sliderWrapper = document.querySelector(".slider-wrapper");
  const slides = document.querySelectorAll(".slide");

  const slideHeight = slides[0].offsetHeight;

  console.log(slideHeight);

  slider.style.height = `${slideHeight}px`;
  sliderShowArea.style.height = `${slideHeight}px`;
  sliderWrapper.style.height = `${slideHeight}px`;
  prevBtn.style.top = `${(slideHeight - 50) / 2}px`;
  nextBtn.style.top = `${(slideHeight - 50) / 2}px`;

  const slideLengths = [];

  slides.forEach((slide) => {
    slideLengths.push(slide.offsetWidth);
  });

  const sliderLength = slider.offsetWidth;
  const areaLength = sliderShowArea.offsetWidth;

  let currentIdx = 0;
  let left = 0;
  const moveSlide = (num) => {
    left = 0;
    for (let i = 0; i < num; i++) {
      left += slideLengths[i];
    }
    slider.style = `left: -${left}px`;
    currentIdx = num;
  };

  const handleClickPrev = (e) => {
    moveSlide(currentIdx - 1);
    if (currentIdx <= 0) {
      moveSlide(0);
    }
  };
  const handleClickNext = (e) => {
    if (left + areaLength > sliderLength) {
      moveSlide(0);
    } else {
      moveSlide(currentIdx + 1);
    }
  };

  prevBtn.addEventListener("click", handleClickPrev);
  nextBtn.addEventListener("click", handleClickNext);
});
