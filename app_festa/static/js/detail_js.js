window.onload = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.horizentalBt();
}
window.onresize = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.horizentalBt();
}

function horizentalBt(){
    var bt = document.getElementById('staff_or_audience_bt');
    var audienceForm = document.getElementById('audience_form');
    var btStaff = document.getElementById('staffBt');
    var btAudience = document.getElementById('audienceBt');
    var staffForm = document.getElementById('staff_form');
    
    if(window.innerWidth <= 1220){
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