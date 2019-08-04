let container_height = 0;
    
        function imgSizeLimit() {
            var background_con = document.getElementById('festa_image');
            if (window.innerWidth <= 1000) {
                background_con.style.width = '375px';
            } else {
                background_con.style.width = '40%';
            }
    
        }
    
        function fullScreen() {
            // offsetHeight, clientHeight, innerHeight, outerHeight
            // 브라우저 안쪽 넓이
            var window_height = window.innerHeight;
            // 붙여넣을 실질 컨테이너
            var container = document.getElementById('container_select_staff_audience');
            // base.html 의 nav 높이
    
            var footer_height = document.getElementById('footer_container').clientHeight;
            var nav_height = document.getElementById('nav_container').clientHeight;
            container_height = window_height - nav_height - footer_height;
            container.style.height = container_height + 'px';
        }
    
        function backgroundResize() {
            var detail_background = document.getElementById('detail_background_img');
            detail_background.style.height = container_height + 'px';
            detail_background.style.width = document.getElementById('festa_image').clientWidth + 'px';
        }

        function imgResize() {
            // 브라우저 크기 확인
            var wrapper = document.getElementById('fore_img_wrapper');
            var img = document.getElementById('fore_img');
            var wrapper_width = wrapper.clientWidth;
            img.style.width = wrapper_width + 'px';
            img.style.height = (wrapper_width * 0.68) + 'px';
            console.log(wrapper_width);
            console.log(img.style.width);
        
            // var thumnail = document.getElementsByClassName('thumnail');
            // var cWidth = 0;
            // var cHeight = 0;
        
            // for (var i = 0; i < thumnail.length; i++) {
            //     cWidth = thumnail[i].clientWidth;
        
            //     // alert(cWidth);
        
            //     this.imgSizeLimit(browser_width, cWidth, thumnail[i]);
        
            //     //가로 세로 비율 유지 및 적용
            //     cHeight = customWidth * 0.68;
            //     var heightToPixel = cHeight + 'px';
            //     thumnail[i].style.height = heightToPixel;
            // }
        }