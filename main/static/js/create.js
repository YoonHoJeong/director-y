const sectionAddBtn = document.querySelector(".section-add-btn");
const sectionList = document.querySelector(".sections");

const onSectionAddClick = (e) => {
    e.preventDefault();
    console.log(e.target);
    const sectionItem = document.createElement("li");
    sectionItem.className = "section-item";

    const inputTitle = document.createElement("input");
    const inputImage = document.createElement("input");
    const inputText = document.createElement("input");

    // inputTitle.classList.add("section-title");
    // inputImage.classList.add("section-image");
    // inputText.classList.add("section-text");
    inputTitle.name = "section-title";
    inputImage.name = "section-image";
    inputText.name = "section-text";
    inputImage.type = "file";
    inputTitle.setAttribute("required", "True");
    inputText.setAttribute("required", "True");
    sectionItem.appendChild(inputTitle);
    sectionItem.appendChild(inputImage);
    sectionItem.appendChild(inputText);

    sectionList.appendChild(sectionItem);
}

sectionAddBtn.addEventListener("click", onSectionAddClick);