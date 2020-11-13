document.addEventListener("DOMContentLoaded", () => {
  const reviseBtn = document.querySelector(".btn--revise");
  const editBtns = document.querySelectorAll(".btn--edit");
  const doneBtn = document.querySelector(".btn--done");

  const onClickRevise = (e) => {
    e.preventDefault();
    editBtns.forEach((editBtn) => {
      editBtn.style.display = "block";
    });
    doneBtn.style.display = "block";
  };
  const onClickDone = (e) => {
    editBtns.forEach((editBtn) => {
      editBtn.style.display = "none";
    });
    doneBtn.style.display = "none";
  };
  const onClickEdit = (e) => {
    e.preventDefault();
    console.log(e.target.name);
  };

  editBtns.forEach((editBtn) => {
    editBtn.addEventListener("click", onClickEdit);
  });
  reviseBtn.addEventListener("click", onClickRevise);
  doneBtn.addEventListener("click", onClickDone);
});
