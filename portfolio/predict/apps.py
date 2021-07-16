from django.apps import AppConfig
from .ml_models.cnn_classif import Cnn

class PredictConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predict'
    cnn = Cnn()