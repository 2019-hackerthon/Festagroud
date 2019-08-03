let container_height = 0;
    
        function imgSizeLimit() {
            var background_con = document.getElementById('festa_image');
            if (window.innerWidth <= 1000) {
                background_con.style.width = '375px';
            } else {
                background_con.style.width = '35%';
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