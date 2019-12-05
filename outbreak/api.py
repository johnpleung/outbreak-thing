from rest_framework import routers
#from core import views as myapp_views
from outbreaks.api_views import IncidentViewset, ContaminantViewset, ReferenceViewset, AffectedUSStateViewset

router = routers.DefaultRouter()
router.register(r'incidents', IncidentViewset)
router.register(r'contaminants', ContaminantViewset)
router.register(r'references', ReferenceViewset)
router.register(r'affected-us-states', AffectedUSStateViewset)