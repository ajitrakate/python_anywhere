from django.apps import AppConfig
#from . import signals
#import HomeAutomation.Board_handller as kv


class BoardHandllerConfig(AppConfig):
    name = 'Board_handller'
    
    def ready(self):
        import Board_handller.signals

