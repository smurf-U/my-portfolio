$('nav .navbar-toggler').click(function(ev){
    $('.sidenav').toggleClass('open-menus')
    $(this).toggleClass('open');
    $(this).find('ham').toggleClass('active');

})