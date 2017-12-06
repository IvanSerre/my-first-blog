from django.conf.urls import url
from ApiRestEdif.views import ListResidentes


urlpatterns = [
    url(r'^ListResidentes/', ListResidentes.as_view()),
]
