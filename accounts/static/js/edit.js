document.addEventListener("DOMContentLoaded", () => {
  const initProfileRevise = () => {
    const reviseBtn = document.querySelector(".btn--revise");
    const doneBtn = document.querySelector(".btn--done");
    const inputs = document.querySelectorAll(".profile-detail-item input");

    const staffreviseBtn = document.querySelector(".staff-btn--revise");
    const staffdoneBtn = document.querySelector(".staff-btn--done");
    const staffEdits = document.querySelectorAll(".staff-editing");

    const onClickStaffRevise = (e) => {
      staffreviseBtn.style.display = 'none';
      staffdoneBtn.style.display = 'block';

      staffEdits.forEach(staffEdit => {
        staffEdit.style.display = 'block';
      })
    };

    const onClickStaffDone = (e) => {
      staffreviseBtn.style.display = 'block';
      staffdoneBtn.style.display = 'none';

      staffEdits.forEach(staffEdit => {
        staffEdit.style.display = 'none';
      })
    };

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
    staffreviseBtn.addEventListener("click", onClickStaffRevise);
    staffdoneBtn.addEventListener("click", onClickStaffDone);
  };

  initProfileRevise();
});
