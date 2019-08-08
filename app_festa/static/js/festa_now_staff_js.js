window.onload = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.imgResize();
    this.leftSidebarTextLimit();
    this.menuDisplay();
}
window.onresize = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.imgResize();
    this.leftSidebarTextLimit();
    this.menuDisplay();
}

function menuDisplay(){
    var nowMenuView = document.getElementById('now_staff_menu_wrapper');
    nowMenuView.style.display = 'block';
}