window.onload = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.horizentalEditText();
    this.btSearchResize();
    
}
window.onresize = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.horizentalEditText();
    this.btSearchResize();
    
}

window.onload = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.horizentalEditText();
    this.btSearchResize();
    
}
window.onresize = function () {
    this.fullScreen();
    this.backgroundResize();
    this.imgSizeLimit();
    this.horizentalEditText();
    this.btSearchResize();
    
}

function btSearchResize(){
    var loginInputBt = document.getElementById('certificateBt');
    var loginInputText = document.getElementById('num_editText');

    var loginBtWidth = loginInputBt.offsetWidth;

    loginInputBt.style.height = loginBtWidth + 'px';
    loginInputText.style.height = loginBtWidth + 'px';
}

function horizentalEditText(){
    var visiEditBox = document.getElementById('visible_edit_box');
    var btWrapper = document.getElementById('bt_wrapper');
    var editBoxForm = document.getElementById('edit_box_form');
    var numEditText = document.getElementById('num_editText');
    var certificateBt = document.getElementById('certificateBt');
    
    if(window.innerWidth <= 1150){
        visiEditBox.style.display = 'block';
        btWrapper.style.marginLeft = '0%';
        editBoxForm.style.width = '100%';
        btWrapper.style.width = '95%';
        numEditText.style.width = '90%';
        certificateBt.style.width = '10%';

        if(window.innerWidth <= 800){
            numEditText.style.width = '150px';
            certificateBt.style.width = '35px';
            btWrapper.style.width = '187px';

        }
    }
    else{
        visiEditBox.style.display = 'flex';
        btWrapper.style.marginLeft = '7%';
        btWrapper.style.width = '70%';
        editBoxForm.style.width = '80%';
    }
}