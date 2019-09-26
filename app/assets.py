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
    'website/src/scss/color.less',
    'website/src/scss/common.less',
    'website/src/scss/loader.less',
    'website/src/scss/homepage.less',
    'website/src/scss/details_block.less',
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

    # 'assets_frontend_scss': Bundle(
    #     *assets_frontend_css,
    #     output='gen/assets_frontend_scss.scss',
    #     filters='sass', extra={'rel': 'stylesheet/scss'}),

    'assets_backend_js': Bundle(
        *assets_backend_js,
        output='gen/assets_backend.js',
        filters='jsmin'),

    'assets_backend_css': Bundle(
        *assets_backend_css,
        output='gen/assets_backend.css',
        filters='less,cssmin', extra={'rel': 'stylesheet/less'})
}
