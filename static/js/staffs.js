document.addEventListener("DOMContentLoaded", () => {

    const portfolioBG = document.querySelector('.portfolio-background');
    const portfolio = document.querySelector('.portfolio-pop');
    const cancleBtn = document.querySelector('.portfolio-cancle');
    const staffName = document.querySelector('.staff-name-kr');
    const staffNameEng = document.querySelector('.staff-name-eng');
    const staffImg = document.querySelector('.staff-avatar');
    const staffPart = document.querySelector('.staff-part');
    const staffSpecial = document.querySelector('.staff-special');
    const portfolioTitle = document.querySelector('.portfolio-title');
    const portfolioBtns = document.querySelectorAll('.portfolio');
    const portfolioImg = document.querySelector('.portfolio-thumbnail-pop');
    const portfolioMain = document.querySelector('.portfolio-main');

    portfolioBtns.forEach(portfolioBtn => {
        portfolioBtn.addEventListener("click", (e) => {
            e.preventDefault();
            portfolioBG.style.display = 'flex';
            portfolio.style.display = 'flex';

            const portfolioInfo = e.target.parentNode;

            const portfolioName = portfolioBtn.querySelector('.portfolio-name');
            const portfolioNameEng = portfolioBtn.querySelector('.portfolio-name-eng');
            const portfolioAvatar = portfolioBtn.querySelector('.portfolio-avatar');
            const portfolioPart = portfolioBtn.querySelector('.portfolio-part');
            const portfolioSpecial = portfolioBtn.querySelector('.portfolio-special');
            const portfolioT = portfolioBtn.querySelector('.portfolio-info');
            const portfolioThumb = portfolioBtn.querySelector('.portfolio-thumbnail-url');
            const portfolioCon = portfolioBtn.querySelector('.portfolio-content');

            staffName.innerText = portfolioName.value;
            staffNameEng.innerText = portfolioNameEng.value;
            staffImg.src = portfolioAvatar.src;
            staffPart.innerText = portfolioPart.value;
            staffSpecial.innerText = portfolioSpecial.value;
            portfolioImg.src = portfolioThumb.value;
            portfolioTitle.innerText = portfolioT.innerText;
            portfolioMain.innerHTML = portfolioCon.value;
            
        })
    })

    cancleBtn.addEventListener("click", (e) => {
        e.preventDefault();
        portfolio.style.display = 'none';
        portfolioBG.style.display = 'none';
    })

});