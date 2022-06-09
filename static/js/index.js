const headNav = document.getElementById('headNavOpen');
const Open = document.getElementById('navBarOpen');
const navbar = document.getElementById('navBar');

Open.addEventListener("click", () => {
    if(navbar.style.display == "none")
    {
        navbar.style.display = "block";
        navbar.style.transition = "0.3s linear";
        headNav.style.borderRadius = "0rem";
        headNav.style.transition = "0.3s linear";
    }
    else{
        navbar.style.display = "none";
        headNav.style.borderRadius = "1.2rem";
    }
})