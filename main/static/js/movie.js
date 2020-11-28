document.addEventListener("DOMContentLoaded", () => {
    const sectionBtns = document.querySelectorAll(".section-btn");
    const section = document.querySelector(".section");
    const sectionTitle = document.querySelector(".section-title");
    const sectionMain = document.querySelector(".section-main");
    const sectionBG = document.querySelector(".section-background");
    const cancleBtn = document.querySelector(".section-cancle");

    sectionBtns.forEach(sectionBtn => {
        sectionBtn.addEventListener("click", (e) => {
            e.preventDefault();
            section.style.display = 'flex';
            const sectionInfo = e.target.parentNode;
            const sectionName = sectionInfo.querySelector('.section-name').innerText;
            const sectionCon = sectionInfo.querySelector('.section-content').innerText;

            sectionTitle.innerText = sectionName
            sectionMain.innerHTML = sectionCon

            sectionBG.style.display = "flex";
        })
    })

    cancleBtn.addEventListener("click", (e) => {
        e.preventDefault();
        section.style.display = 'none';
        sectionBG.style.display = 'none';
    })
});