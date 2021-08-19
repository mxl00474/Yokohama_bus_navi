import os
import sys
from django.apps import AppConfig
from django.conf import settings
from threading import Thread
from tornado.ioloop import IOLoop
from bokeh.server.server import Server

sys.path.append(os.path.join(os.path.dirname(__file__), './plotter'))
from start_live_streaming import start_live_streaming
from BusInfo import BusInfo

class BusMonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bus_monitor'

    def ready(self):
        if not sys.argv[0].endswith('manage.py') or sys.argv[1] == 'runserver':
            print('Getting bus stops and bus routes')
            BusInfo.init()
            print('Starting bokeh server thread')
            Thread(target=self.bk_worker).start()

    def bk_worker(self):
        server = Server(
            {
                settings.BOKEH_LIVE_STREAMING_PATH: start_live_streaming,
            },
            io_loop=IOLoop())
        server.start()
        server.io_loop.start()
