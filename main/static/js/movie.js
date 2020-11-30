document.addEventListener("DOMContentLoaded", () => {
    const sectionBtns = document.querySelectorAll(".section-btn");
    const section = document.querySelector(".section");
    const sectionTitle = document.querySelector(".section-title");
    const sectionMain = document.querySelector(".section-main");
    const sectionBG = document.querySelector(".section-background");
    const cancleBtn = document.querySelector(".section-cancle");
    const sectionThumb = document.querySelector(".section-thumbnail");

    sectionBtns.forEach(sectionBtn => {
        sectionBtn.addEventListener("click", (e) => {
            e.preventDefault();
            section.style.display = 'flex';
            const sectionInfo = e.target.parentNode;
            const sectionName = sectionBtn.querySelector('.section-name').innerText;
            const sectionCon = sectionBtn.querySelector('.section-content').innerText;
            const sectionUrl = sectionBtn.querySelector('.section-url').src;

            sectionTitle.innerText = sectionName;
            sectionMain.innerHTML = sectionCon;
            sectionThumb.src = sectionUrl;

            sectionBG.style.display = "flex";
        })
    })

    cancleBtn.addEventListener("click", (e) => {
        e.preventDefault();
        section.style.display = 'none';
        sectionBG.style.display = 'none';
    })
});