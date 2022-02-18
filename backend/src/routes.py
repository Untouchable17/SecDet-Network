from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Social Media",
        default_version='v1',
        description="Социальная сеть TeamDet",
        contact=openapi.Contact(url="https://www.youtube.com/channel/UCVRFfnrUrcb4GsvKw7SOL-g"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('profile/', include('src.auth_system.urls', namespace="profile")),
    path('tracks/', include('src.tracks.urls', namespace="tracks")),
    path('feed/', include('src.posts.urls', namespace="feed")),

    path('messages/', include('src.chat.urls', namespace='chat')),
    path('groups/', include('src.groups.urls', namespace='groups'))

]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name="index.html"))]