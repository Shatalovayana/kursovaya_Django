from django.urls import path
from django.views.decorators.cache import cache_page

from messaging_service.apps import MessagingServiceConfig
from messaging_service.views import MessagesCreateView, MessagesListView, MessagesDetailView, MessagesUpdateView, \
    ClientsCreateView, ClientsListView, ClientsDetailView, ClientsUpdateView, MailingSettingsCreateView, \
    MailingSettingsListView, \
    MailingSettingsDetailView, MailingSettingsUpdateView, MailingSettingsDeleteView, ClientsDeleteView, \
    MessagesDeleteView, homepage

app_name = MessagingServiceConfig.name

urlpatterns = [
    path('', cache_page(60)(homepage), name='homepage'),

    path('messages/create/', MessagesCreateView.as_view(), name='messages-form'),
    path('messages/list/', cache_page(60)(MessagesListView.as_view()), name='messages-list'),
    path('messages/view/<int:pk>/', MessagesDetailView.as_view(), name='messages-view'),
    path('messages/edit/<int:pk>/', MessagesUpdateView.as_view(), name='messages-edit'),
    path('messages/delete/<int:pk>/', MessagesDeleteView.as_view(), name='messages-delete'),

    path('clients/create/', ClientsCreateView.as_view(), name='clients-form'),
    path('clients/list/', ClientsListView.as_view(), name='clients-list'),
    path('clients/view/<int:pk>/', ClientsDetailView.as_view(), name='clients-view'),
    path('clients/edit/<int:pk>/', ClientsUpdateView.as_view(), name='clients-edit'),
    path('clients/delete/<int:pk>/', ClientsDeleteView.as_view(), name='clients-delete'),

    path('settings/create/', MailingSettingsCreateView.as_view(), name='settings-form'),
    path('settings/list/', MailingSettingsListView.as_view(), name='settings-list'),
    path('settings/view/<int:pk>/', MailingSettingsDetailView.as_view(), name='settings-view'),
    path('settings/edit/<int:pk>/', MailingSettingsUpdateView.as_view(), name='settings-edit'),
    path('settings/delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='settings-delete'),
]
