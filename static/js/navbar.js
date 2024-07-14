function toggleMenu() {
    var links = document.querySelector('.nav-link ul');
    var hamburger = document.querySelector('.hamburger-box');
    var navbtn = document.querySelector('.nav-button');
    links.classList.toggle('active');
    hamburger.classList.toggle('active');
    navbtn.classList.toggle('active');
}