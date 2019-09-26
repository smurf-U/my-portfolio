$('#lnk-view-menu').click(function(ev){
    $('.profile').toggleClass('open-menus')
    $(this).toggleClass('open');
    $(this).find('ham').toggleClass('active');

})