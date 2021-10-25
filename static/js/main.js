// show dropdown when user click on Account
let dropdownLinks = document.querySelectorAll(".dropdown-link");
let dropdown = document.querySelector(".dropdown-account");

dropdownLinks.forEach((link) => {
    link.addEventListener("click", () => {
        dropdown.classList.add("dropdown-show");
    });
});

let closeDropdown = document.querySelector(".dropdown-close");
closeDropdown.addEventListener("click", () => {
    dropdown.classList.remove("dropdown-show")
});

// When hamburger menu is clicked show side nav bar