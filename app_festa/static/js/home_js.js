let customWidth = 0;

window.onload = function () {
    this.imgResize();
    this.btSearchResize();
}
// 썸네일 브라우저 크기에 따른 변화
window.onresize = function () {
    this.imgResize();
    this.btSearchResize();
}

function imgResize() {
    // 브라우저 크기 확인
    var browser_width = document.body.clientWidth;
    var browser_height = document.body.clientHeight;

    var thumnail = document.getElementsByClassName('thumnail');
    var cWidth = 0;
    var cHeight = 0;

    for (var i = 0; i < thumnail.length; i++) {
        cWidth = thumnail[i].clientWidth;

        // alert(cWidth);

        this.imgSizeLimit(browser_width, cWidth, thumnail[i]);

        //가로 세로 비율 유지 및 적용
        cHeight = customWidth * 0.68;
        var heightToPixel = cHeight + 'px';
        thumnail[i].style.height = heightToPixel;
    }
}

//썸네일 이미지 크기 최대최소 제한
function imgSizeLimit(browserWidth, containerWidth, objectItem) {
    if (browserWidth >= 1290) {
        containerWidth = 320;
        objectItem.style.width = '320px';
        var iWrapper = document.getElementsByClassName('item_object');
        for (var j = 0; j < iWrapper.length; j++) {
            iWrapper[j].style.width = '320px';
        }
    } else if (browserWidth <= 600) {
        containerWidth = 120;
        objectItem.style.width = '120px';
        var iWrapper = document.getElementsByClassName('item_object');
        for (var j = 0; j < iWrapper.length; j++) {
            iWrapper[j].style.width = '120px';
        }
    } else {
        var iWrapper = document.getElementsByClassName('item_object');
        for (var j = 0; j < iWrapper.length; j++) {
            iWrapper[j].style.width = '25%';
        }
        objectItem.style.width = '100%';
        containerWidth = objectItem.width;
    }

    customWidth = containerWidth;
}

function btSearchResize(){
    var inputBt = document.getElementById('searchBt');
    var inputText = document.getElementById('editText');

    var btWidth = inputBt.clientWidth;

    inputBt.style.height = btWidth + 'px';
    inputText.style.height = btWidth + 'px';
}