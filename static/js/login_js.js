window.onload = function () {
    // base.js
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.imgResize();
    this.leftSidebarTextLimit();

    //login.js
    this.horizentalEditText();
    this.btSearchResize();
    this.textSizeLimit();
}
window.onresize = function () {
    
    // base.js
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.imgResize();
    this.leftSidebarTextLimit();

    //login.js
    this.horizentalEditText();
    this.btSearchResize();
    this.textSizeLimit();
    
}

function btSearchResize(){
    var loginInputBt = document.getElementById('certificateBt');
    var loginNumInputText = document.getElementById('num_editText');
    var loginNameInputText = document.getElementById('name_editText');

    var loginBtWidth = loginInputBt.offsetWidth;

    loginInputBt.style.height = loginBtWidth + 'px';
    loginNumInputText.style.height = loginBtWidth + 'px';
    loginNameInputText.style.height = loginBtWidth + 'px';
}

function horizentalEditText(){
    var visiEditBox = document.getElementsByClassName('visible_edit_box');
    var btWrapper = document.getElementsByClassName('bt_wrapper');
    var editBoxForm = document.getElementById('edit_box_form');
    var numEditText = document.getElementById('num_editText');
    var nameEditText = document.getElementById('name_editText');
    var certificateBt = document.getElementById('certificateBt');

    editBoxForm.style.width = '80%';
    numEditText.style.width = '90%';
    nameEditText.style.width = '90%';
    certificateBt.style.width = '10%';
    
    if(window.innerWidth <= 1150){
        // visiEditBox.style.display = 'block';
        // btWrapper.style.marginLeft = '0%';
        // btWrapper.style.width = '95%';
        editBoxForm.style.width = '100%';

        for(var i2 = 0; i2 < visiEditBox.length; i2++){
            visiEditBox[i2].style.display = 'block';
        }

        for(var i = 0; i < btWrapper.length; i++){
            btWrapper[i].style.marginLeft = '0%';
            btWrapper[i].style.width = '95%';
        }

        if(window.innerWidth <= 800){
            numEditText.style.width = '150px';
            nameEditText.style.width = '150px';
            certificateBt.style.width = '35px';

            for(var j = 0; j < btWrapper.length; j++){
                btWrapper[j].style.width = '187px';
            }

        }
    }
    else{

        for(var k2 = 0; k2 < visiEditBox.length; k2++){
            visiEditBox[k2].style.display = 'flex';
        }
        for(var k = 0; k < btWrapper.length; k++){
            btWrapper[k].style.marginLeft = '7%';
            btWrapper[k].style.width = '70%';
        }
    }

    btWrapper[0].style.width = (numEditText.offsetWidth+2) + 'px';
    nameEditText.style.width = '100%';
}

// text 사이즈 제한
function textSizeLimit(){
    var detailTextWrapper = document.getElementById('explain_text_box');

    detailTextWrapper.style.fontSize = '3vw';
    
    let detailText = document.querySelector('#explain_text_box');
    let computedDetailText = window.getComputedStyle(detailText);
    let currentDetailTextSize = computedDetailText.getPropertyValue('font-size').match(/\d+/);

    if(currentDetailTextSize > 30){
        detailTextWrapper.style.fontSize = '30px';
    }
}