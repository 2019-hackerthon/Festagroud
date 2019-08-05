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
    var readyMenuView = document.getElementById('ready_menu_wrapper');
    readyMenuView.style.display = 'block';
}