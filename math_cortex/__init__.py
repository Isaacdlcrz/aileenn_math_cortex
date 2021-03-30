"""Initialize Flask app."""
from flask import Flask, jsonify
from flask_cors import CORS
from .exceptions import AppError, InternalServerError, handle_error

def create_app():
    """Create Flask application."""
    application = Flask(__name__)
    application.config['JSON_SORT_KEYS'] = False # This line will keep the order of dictionary keys 
    application.config.from_object('config.Config')
    application.register_error_handler(AppError, handle_error)
    application.register_error_handler(InternalServerError, handle_error)
    CORS(application)
    

    with application.app_context():
        
        from .model.model import ma
        ma.init_app(application)

        # Importar nuestros blueprints
        #from .carpeta import blueprint
        from .pipeline import pipeline
        

        #Registrar un blueprint en la applicación
        #application.register_blueprint(carpeta.carpeta_bp, url_prefix="/un_prefijo")
        application.register_blueprint(pipeline.pipeline_bp, url_prefix="/pipeline")
        
        return application
