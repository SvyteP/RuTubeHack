const translateButton = document.querySelector(".translate-button"),
	  languagesContainer = document.querySelector(".languages-container"),
	  arrayOfLanguages = document.querySelectorAll(".languages-container > ul > li");

const openLanguagesContainer = e => {
	if (!translateButton.classList.contains("translate-button_clicked")) {
		translateButton.classList.add("translate-button_clicked");
		languagesContainer.classList.remove("display-none");
	} else {
		translateButton.classList.remove("translate-button_clicked");
		languagesContainer.classList.add("display-none");
	}
}

function main() {
	translateButton.addEventListener("click", openLanguagesContainer);
}

main();