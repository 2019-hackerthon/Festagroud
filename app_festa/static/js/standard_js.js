window.onload = function () {
    this.fullScreen();
}
window.onresize = function () {
    this.fullScreen();
}

// 스크롤 없이, 하나의 윈도우만 가져오기
function fullScreen() {
    // offsetHeight, clientHeight, innerHeight, outerHeight

    // 브라우저 안쪽 넓이
    var browser_height = window.innerHeight;

    // 붙여넣을 실질 컨테이너
    var contents_container = document.getElementById('contents_container');

    //nav 높이
    var nav_height = document.getElementById('nav_container').clientHeight;

    //footer 높이
    var footer_height = document.getElementById('footer_container').clientHeight;
    
    var contents_container_height = (browser_height - nav_height - footer_height);
    contents_container.style.height = contents_container_height + 'px';
}