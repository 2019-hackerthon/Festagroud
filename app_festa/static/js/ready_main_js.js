window.onload = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.imgResize();
    this.leftSidebarTextLimit();

    this.festaInfoScroll();
    this.menuDisplay();
    this.textChange();
}
window.onresize = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.imgResize();
    this.leftSidebarTextLimit();

    this.festaInfoScroll();
    this.menuDisplay();
    this.textChange();
}

function menuDisplay(){
    var nowMenuView = document.getElementById('ready_menu_wrapper');
    nowMenuView.style.display = 'block';
}

function festaInfoScroll(){
    var scrollDiv = document.getElementById('festa_info');
    var maxHeight = scrollDiv.clientHeight;
    scrollDiv.style.height = maxHeight + 'px';
}

function textChange(){
    var textTitle = document.getElementById('title_text_wrapper');
    textTitle.innerHTML = 'Festa Ready'
}