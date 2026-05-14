from django.urls import path
from .views import start_page_view, single_gadget_int_view, \
    single_gadget_post_view, GadgetView



urlpatterns = [
    path('start/', start_page_view),

    path('', start_page_view),
    path('gadget/', single_gadget_post_view),
    path('gadget/<int:gadget_id>', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url"),
]
