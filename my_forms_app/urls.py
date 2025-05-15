from django.urls import path
from . import views

app_name = 'my_app'
urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('students/', views.students_result, name='students_result'),
    path('add_program/', views.add_program, name='add_program'),
    path('programs/', views.program_result, name='program_result'),
    path('add_managers/', views.add_managers, name='add_managers'),
    path('managers/', views.managers_result, name='managers_result'),
    path('add_fellows/', views.add_fellows, name='add_fellows'),
    path('fellows/', views.fellows_result, name='fellows_result'),

    path('', views.index, name='index')
    # path('datetime_nov/', views.datetime_nov, name='datetime_nov'),
    # path('var_list_dict/', views.var_list_dict, name='var_list_dict'),
    # path('abc_form/', views.abc_form, name='abc_form'),
    # path('abc_get/', views.abc_get, name='abc_get'),
    # path('abc_model_form/', views.abc_model_form, name='abc_model_form'),
    # path('abc_tweaks_form/', views.abc_tweaks_form, name='abc_tweaks_form'),
    # path('abc_result/', views.abc_result, name='abc_result'),
    # path('table/', views.table, name='table'),
]
