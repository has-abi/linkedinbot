template = {
    "swagger": "2.0",
    "info": {
        "title": "SKYLARK Resume Parser",
        "description": "Resume parser using Deep Information Extraction, Computer Vision, and NLP",
        "version": "1.0"
    },
    "basePath": "/",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/api/docs",
    "title":"Resume Parser Docs",
}