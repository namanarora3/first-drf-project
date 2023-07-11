from django.urls import path
from . import views

urlpatterns = [
    # path('delete/<int:id>/',views.del_prod),
    path('<int:id>/',views.get_prod),
    path('',views.list_create_prod),
    # path('all/',views.list_prod),
    path('<int:id>/update/',views.update_prod),
    path('<int:id>/delete/',views.del_prod)
]
