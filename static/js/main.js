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
let hamburger = document.querySelector(".hamburger");
let navSide = document.querySelector(".side-nav");
let closeNav = document.querySelector(".nav-close");
let sideMenu = document.querySelector(".side-nav-menu");
hamburger.addEventListener("click", () => {
    navSide.classList.add("show-side-nav");
    sideMenu.classList.add("side-menu-open");
    sideMenu.classList.remove("side-menu-close");
});

closeNav.addEventListener("click", () => {
    sideMenu.classList.remove("side-menu-open");
    sideMenu.classList.add("side-menu-close");

    setTimeout(() => {
        navSide.classList.remove("show-side-nav");
    }, 500);
});

// on scroll change top-nav color

window.addEventListener("scroll", () => {
    let topNav = document.querySelector(".top-nav");
    if(window.scrollY >= 100) {
        topNav.classList.add("top-nav-scroll");
    } else {
        topNav.classList.remove("top-nav-scroll");
    }
});

// on scroll animate review section and Newsletter


window.addEventListener('scroll', reveal);

function reveal(){
const reveals = document.querySelectorAll('.reveal');

for(var i = 0; i < reveals.length; i++){

const windowheight = window.innerHeight;
const revealtop = reveals[i].getBoundingClientRect().top;
const revealpoint = 100;

if(revealtop < windowheight - revealpoint){
    reveals[i].classList.add('active');
    }
    else{
    reveals[i].classList.remove('active');
    }
}
}


// Code from Bootstrap to initialize the toasts
let toastElList = [].slice.call(document.querySelectorAll('.toast'));
let toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl);
});
toastList.forEach((toast) => {
    toast.show();
});
