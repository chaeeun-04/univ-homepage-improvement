from django.apps import AppConfig

class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'

    # [ 추가 ]
    def ready(self):
        import product.signals  # signals.py 파일을 import
