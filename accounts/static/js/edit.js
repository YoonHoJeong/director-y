document.addEventListener("DOMContentLoaded", () => {
  const reviseBtn = document.querySelector(".btn--revise");
  const doneBtn = document.querySelector(".btn--done");
  const inputs = document.querySelectorAll(".profile-detail-item input");

  const onClickRevise = (e) => {
    e.preventDefault();

    doneBtn.style.display = "block";
    reviseBtn.style.display = "none";
    inputs.forEach((input) => {
      if (input.name === name) {
        current = input;
      }
      input.removeAttribute("readonly");
      input.style.borderBottom = "1px solid black";
    });
  };
  const onClickDone = (e) => {};
  reviseBtn.addEventListener("click", onClickRevise);
  doneBtn.addEventListener("click", onClickDone);
});
