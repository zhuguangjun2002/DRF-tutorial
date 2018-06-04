from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
]
