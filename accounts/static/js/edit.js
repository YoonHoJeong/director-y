document.addEventListener("DOMContentLoaded", () => {
  const reviseBtn = document.querySelector(".btn--revise");
  const editBtns = document.querySelectorAll(".btn--edit");
  const doneBtn = document.querySelector(".btn--done");
  const inputs = document.querySelectorAll(".profile-detail-item input");

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
    inputs.forEach((input) => {
      input.setAttribute("readonly");
    });
  };
  const onClickEdit = (e) => {
    e.preventDefault();
    const name = e.target.name ? e.target.name : e.target.parentNode.name;
    let current = null;

    inputs.forEach((input) => {
      if (input.name === name) {
        current = input;
      }
    });

    current.removeAttribute("readonly");
    current.style.borderBottom = "1px solid black";
  };

  editBtns.forEach((editBtn) => {
    editBtn.addEventListener("click", onClickEdit);
  });
  reviseBtn.addEventListener("click", onClickRevise);
  doneBtn.addEventListener("click", onClickDone);
});
