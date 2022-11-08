from django.urls import path
from . import views as searchviews

app_name = 'searchapp'

urlpatterns = [
    path('', searchviews.searchResult, name='searchResult'),
<<<<<<< HEAD
]
=======
]    
>>>>>>> a76a52d93b449df4b91bdfbdb5dda88bbef8076f
