$(".slider-wrapper").ready(() => {
  const sliderWrappers = document.querySelectorAll(".slider-wrapper");

  sliderWrappers.forEach((sliderWrapper) => {
    const prevBtn = sliderWrapper.querySelector(".prev-btn");
    const nextBtn = sliderWrapper.querySelector(".next-btn");
    const slider = sliderWrapper.querySelector(".slider");
    const sliderShowArea = sliderWrapper.querySelector(".slider-show-area");
    const slides = sliderWrapper.querySelectorAll(".slide");

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

    console.log(slideLengths);

    const sliderLength = slider.offsetWidth;

    let currentIdx = 0;

    prevBtn.style.display = "none";

    let left = 0;
    const moveSlide = (num) => {
      left = 0;
      for (let i = 0; i < num; i++) {
        left += slideLengths[i] + 20;
      }
      slider.style = `left: -${left}px`;
      currentIdx = num;
    };

    const handleClickPrev = (e) => {
      moveSlide(currentIdx - 1);
      if (currentIdx <= 0) {
        moveSlide(0);
        prevBtn.style.display = "none";
      }
    };
    const handleClickNext = (e) => {
      // console.log(left, areaLength, sliderLength);
      const areaLength = sliderShowArea.offsetWidth;
      if (left + areaLength > sliderLength) {
        moveSlide(0);
        prevBtn.style.display = "none";
      } else {
        moveSlide(currentIdx + 1);
      }
      if (currentIdx !== 0) {
        prevBtn.style.display = "flex";
      }
    };

    prevBtn.addEventListener("click", handleClickPrev);
    nextBtn.addEventListener("click", handleClickNext);
  });
});
