document.addEventListener("DOMContentLoaded", () => {
  const initProfileRevise = () => {
    const reviseBtn = document.querySelector(".btn--revise");
    const doneBtn = document.querySelector(".btn--done");
    const plusBtn = document.querySelector(".section-plus");
    const sectionEdits = document.querySelectorAll(".section-editing");
    const movieEdit = document.querySelector(".movie-editing");

    const onClickRevise = (e) => {
      e.preventDefault();

      doneBtn.style.display = "block";
      reviseBtn.style.display = "none";
      plusBtn.style.display = "block";
      movieEdit.style.display = "block";

      sectionEdits.forEach(sectionEdit => {
        sectionEdit.style.display = "inline-flex";
      })
    };
    const onClickDone = (e) => {
      e.preventDefault();

      doneBtn.style.display = "none";
      reviseBtn.style.display = "block";
      plusBtn.style.display = "none";
      movieEdit.style.display = "none";

      sectionEdits.forEach(sectionEdit => {
        sectionEdit.style.display = "none";
      })
    };
    reviseBtn.addEventListener("click", onClickRevise);
    doneBtn.addEventListener("click", onClickDone);
  };

  initProfileRevise();
});
