from django.shortcuts import render
from django.conf import settings

from bokeh.embed import server_document

def index(request):
    url = settings.BOKEH_SERVER_ADDRESS + settings.BOKEH_LIVE_STREAMING_PATH
    script = server_document(url=url)
    return render(request, 'bus_monitor/index.html', {'script':script})