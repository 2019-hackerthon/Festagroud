window.onload = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.imgResize();
    this.menuDisplay();
}
window.onresize = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.imgResize();
    this.menuDisplay();
}

function menuDisplay(){
    var menuView = document.getElementById('menu_wrapper');
    menuView.style.display = 'block';
}