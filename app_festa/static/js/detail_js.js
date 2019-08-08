window.onload = function () {
    // base.js
    this.fullScreen();
    this.imgSizeLimit();
    this.backgroundResize();
    this.imgResize();
    this.leftSidebarTextLimit();

    //detail.js
    this.horizentalBt();
    this.textSizeLimit();
}
window.onresize = function () {
    // base.js
    this.fullScreen();
    this.imgSizeLimit();
    this.backgroundResize();
    this.imgResize();
    this.leftSidebarTextLimit();

    //detail.js
    this.horizentalBt();
    this.textSizeLimit();
}

// 화면 작아지면서 세로 모드 될때
function horizentalBt(){
    var bt = document.getElementById('staff_or_audience_bt');
    var audienceForm = document.getElementById('audience_form');
    var btStaff = document.getElementById('staffBt');
    var btAudience = document.getElementById('audienceBt');
    var staffForm = document.getElementById('staff_form');
    
    if(window.innerWidth <= 1150){
        bt.style.display = 'block';
        audienceForm.style.marginLeft = '0%';
        btStaff.style.fontSize = '20px';
        btAudience.style.fontSize = '20px';
        staffForm.style.width = '28%';
        audienceForm.style.width = '28%';

        if(window.innerWidth <= 894){
            staffForm.style.width = '125.66px';
            audienceForm.style.width = '125.66px';
        }
    }
    else{
        bt.style.display = 'flex';
        audienceForm.style.marginLeft = '10%';
        btStaff.style.fontSize = '36px';
        btAudience.style.fontSize = '36px';
        }
    }
    // text 사이즈 제한
    function textSizeLimit(){
        var detailTextWrapper = document.getElementById('explain_role_box');

        detailTextWrapper.style.fontSize = '3vw';
        
        let detailText = document.querySelector('#explain_role_box');
        let computedDetailText = window.getComputedStyle(detailText);
        let currentDetailTextSize = computedDetailText.getPropertyValue('font-size').match(/\d+/);

        if(currentDetailTextSize > 30){
            detailTextWrapper.style.fontSize = '30px';
        }
    }