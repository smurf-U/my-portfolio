from flask_assets import Bundle

assets_frontend_css = [
    'website/src/css/common.css',
]

assets_bundles = {
    'assets_frontend_css': Bundle(
        *assets_frontend_css
    )
}