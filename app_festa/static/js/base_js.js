        function imgSizeLimit() {
            var background_con = document.getElementById('left_container');
            if (window.innerWidth <= 1000) {
                background_con.style.width = '375px';
            } else {
                background_con.style.width = '35%';
            }
    
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

        // 백그라운드 이미지(id = detail_background_img) 리사이즈
        function backgroundResize() {
            var left_container = document.getElementById('left_container');
            var left_side_bar_background = document.getElementById('detail_background_img');
            left_side_bar_background.style.width = left_container.clientWidth + 'px';
            left_side_bar_background.style.height = left_container.clientWidth + 'px';
        }

        // fore_img_wrapper에 들어갈 이미지 리사이즈
        function imgResize() {
            var img = document.getElementById('fore_img');
            var img_width = img.clientWidth;
            img.style.height = (img_width * 0.68) + 'px';
        }

        // 왼쪽 사이드바 텍스트 사이즈 제한
        function leftSidebarTextLimit(){
            var titleWrapper = document.getElementById('title_text_wrapper');
            var infoWrapper = document.getElementById('festa_info_wrapper');
            var nowStaffMenuWrapper = document.getElementById('now_staff_menu_wrapper');
            var nowAudienceMenuWrapper = document.getElementById('now_audience_menu_wrapper');
            var readyMenuWrapper = document.getElementById('ready_menu_wrapper');
            var sidebarTextComponentsArray = [titleWrapper, infoWrapper, nowStaffMenuWrapper, nowAudienceMenuWrapper, readyMenuWrapper];

            for(var item in sidebarTextComponentsArray){
                sidebarTextComponentsArray[item].style.fontSize = '3vw';
            }

            let titleText = document.querySelector('#title_text_wrapper');
            let computedTitleText = window.getComputedStyle(titleText);
            let currentTextSize = computedTitleText.getPropertyValue('font-size').match(/\d+/);


            if(currentTextSize > 20){
                for(var item in sidebarTextComponentsArray){
                    sidebarTextComponentsArray[item].style.fontSize = '20px';
                }
            }

            var festaDate = document.getElementById('festa_date');
            festaDate.style.fontSize = '14px';
        }