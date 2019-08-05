window.onload = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.horizentalEditText();
    this.btSearchResize();
    this.imgResize();
    
}
window.onresize = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.horizentalEditText();
    this.btSearchResize();
    this.imgResize();
    
}

function btSearchResize(){
    var loginInputBt = document.getElementById('certificateBt');
    var loginInputText = document.getElementById('num_editText');

    var loginBtWidth = loginInputBt.offsetWidth;

    loginInputBt.style.height = loginBtWidth + 'px';
    loginInputText.style.height = loginBtWidth + 'px';
}

function horizentalEditText(){
    var visiEditBox = document.getElementsByClassName('visible_edit_box');
    var btWrapper = document.getElementsByClassName('bt_wrapper');
    var editBoxForm = document.getElementById('edit_box_form');
    var numEditText = document.getElementById('num_editText');
    var certificateBt = document.getElementById('certificateBt');
    
    if(window.innerWidth <= 1150){
        // visiEditBox.style.display = 'block';
        // btWrapper.style.marginLeft = '0%';
        editBoxForm.style.width = '100%';
        // btWrapper.style.width = '95%';
        numEditText.style.width = '90%';
        certificateBt.style.width = '10%';

        for(var i2 = 0; i2 < visiEditBox.length; i2++){
            visiEditBox[i2].style.display = 'block';
        }

        for(var i = 0; i < btWrapper.length; i++){
            btWrapper[i].style.marginLeft = '0%';
            btWrapper[i].style.width = '95%';
        }

        if(window.innerWidth <= 800){
            numEditText.style.width = '150px';
            certificateBt.style.width = '35px';
            // btWrapper.style.width = '187px';

            for(var j = 0; j < btWrapper.length; j++){
                btWrapper[j].style.width = '187px';
            }

        }
    }
    else{
        // visiEditBox.style.display = 'flex';
        // btWrapper.style.marginLeft = '7%';
        // btWrapper.style.width = '70%';
        editBoxForm.style.width = '80%';

        for(var k = 0; k < btWrapper.length; k++){
            btWrapper[k].style.marginLeft = '7%';
            btWrapper[k].style.width = '70%';
        }

        for(var k2 = 0; k2 < visiEditBox.length; k2++){
            visiEditBox[k2].style.display = 'flex';
        }
    }
}