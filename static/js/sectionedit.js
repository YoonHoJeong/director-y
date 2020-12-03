document.addEventListener("DOMContentLoaded", () => {
  const initProfileRevise = () => {
    const reviseBtn = document.querySelector(".btn--revise");
    const doneBtn = document.querySelector(".btn--done");
    const plusBtn = document.querySelector(".section-plus");
    const sectionEdits = document.querySelectorAll(".section-editing");
    const movieEdit = document.querySelector(".movie-editing");
    const boxes = document.querySelectorAll(".section-box-frame");
    const likeBtn = document.querySelector(".like-btn-container");

    const onClickRevise = (e) => {
      e.preventDefault();

      doneBtn.style.display = "block";
      reviseBtn.style.display = "none";
      plusBtn.style.display = "block";
      movieEdit.style.display = "block";
      likeBtn.style.display = "none";

      sectionEdits.forEach(sectionEdit => {
        sectionEdit.style.display = "inline-flex";
      })

      boxes.forEach(box => {
        box.style.display = "none";
      })
    };
    const onClickDone = (e) => {
      e.preventDefault();

      doneBtn.style.display = "none";
      reviseBtn.style.display = "block";
      plusBtn.style.display = "none";
      movieEdit.style.display = "none";
      likeBtn.style.display = "block";

      sectionEdits.forEach(sectionEdit => {
        sectionEdit.style.display = "none";
      })

      boxes.forEach(box => {
        box.style.display = "block";
      })
    };
    reviseBtn.addEventListener("click", onClickRevise);
    doneBtn.addEventListener("click", onClickDone);
  };

  initProfileRevise();
});
