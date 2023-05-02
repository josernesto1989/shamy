#apps.py
from django.apps import AppConfig
import threading
import time

class MyAppConfig(AppConfig):
    name = 'apk_data_collector_app'

    def ready(self):
        def print_logo():
            LOGO = r"""
              __  __      _       _     
             |  \/  | ___| |_ ___| |__  
             | |\/| |/ _ \ __/ __| '_ \ 
             | |  | |  __/ || (__| | | |
             |_|  |_|\___|\__\___|_| |_|
            """
            while True:
                print(LOGO)
                time.sleep(300)  # Esperamos 5 minutos

        # Creamos el hilo de ejecución
        t = threading.Thread(target=print_logo)

        # Indicamos que el hilo se ejecutará en segundo plano
        t.daemon = True

        # Iniciamos el hilo de ejecución
        t.start()