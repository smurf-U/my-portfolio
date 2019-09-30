from flask_assets import Bundle

assets_frontend_js = [
    'lib/jquery-3.4.1/jquery-3.4.1.min.js',
    'lib/bootstrap-4.3.1/js/bootstrap.min.js',
    'lib/popper.js-1.14.7/popper.min.js',
    'lib/particles/particles.js',
    # 'lib/particles/stats.js',
    'website/src/js/loader.js',
    # 'website/src/js/menu.js',
]
assets_frontend_css = [
    'website/src/less/color.less',
    'website/src/less/common.less',
    'website/src/less/loader.less',
    'website/src/less/header.less',
    'website/src/less/sidebar.less',
    'website/src/less/footer.less',
    'website/src/less/contact.less',
    'website/src/less/about.less',
    'website/src/less/works.less',
    'website/src/less/homepage.less',
    'website/src/less/details_block.less',
    'website/src/less/ham.less',
]

assets_backend_js = [
    'lib/jquery-3.4.1/jquery-3.4.1.min.js',
    'lib/bootstrap-4.3.1/js/bootstrap.min.js',
    'lib/popper.js-1.14.7/popper.min.js',
]

assets_backend_css = [
    'lib/bootstrap-4.3.1/css/bootstrap.min.css',
    # 'website/src/css/common.css',
]

assets_bundles = {

    'assets_frontend_js': Bundle(
        *assets_frontend_js,
        output='gen/assets_frontend.js',
        filters='jsmin'),

    'assets_frontend_css': Bundle(
        *assets_frontend_css,
        output='gen/assets_frontend.css',
        filters='less,cssmin', extra={'rel': 'stylesheet/css'}),

    # 'assets_frontend_less': Bundle(
    #     *assets_frontend_css,
    #     output='gen/assets_frontend_less.less',
    #     filters='sass', extra={'rel': 'stylesheet/less'}),

    'assets_backend_js': Bundle(
        *assets_backend_js,
        output='gen/assets_backend.js',
        filters='jsmin'),

    'assets_backend_css': Bundle(
        *assets_backend_css,
        output='gen/assets_backend.css',
        filters='less,cssmin', extra={'rel': 'stylesheet/less'})
}
