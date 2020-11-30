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

            const portfolioInfo = e.tartget;

            const portfolioName = portfolioInfo.querySelector('.portfolio-name');
            const portfolioNameEng = portfolioInfo.querySelector('.sportfolio-name-eng');
            const portfolioAvatar = portfolioInfo.querySelector('.portfolio-avatar');
            const portfolioPart = portfolioInfo.querySelector('.portfolio-part');
            const portfolioSpecial = portfolioInfo.querySelector('.portfolio-special');
            const portfolioT = portfolioInfo.querySelector('.portfolio-info');
            const portfolioThumb = portfolioInfo.querySelector('.portfolio-thumbnail');
            const portfolioCon = portfolioInfo.querySelector('.portfolio-content');

            staffName.innerText = portfolioName.innerText;
            staffNameEng.innerText = portfolioNameEng.innerText;
            staffImg.src = portfolioAvatar.src;
            staffPart.innerText = portfolioPart.innerText;
            staffSpecial.innerText = portfolioSpecial.innerText;
            portfolioImg.src = portfolioThumb.src;
            portfolioTitle.innerText = portfolioT.innerText;
            portfolioMain.innerHTML = portfolioCon.innerText;
            
        })
    })

    cancleBtn.addEventListener("click", (e) => {
        e.preventDefault();
        portfolio.style.display = 'none';
        portfolioBG.style.display = 'none';
    })

});