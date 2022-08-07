from django.urls import path
from . import views
urlpatterns =[path('',views.login),path('createuser',views.create),path('save',views.save),path('usercreate',views.usercreate),path('loginn',views.loggedin),path('success',views.success),path('successuser',views.successuser),path('trainer',views.trainer),path('traineruser',views.traineruser),path('new-trainer',views.newtrainer),path('add-trainer',views.addtrainer),path('view-trainer',views.trainer),path('view-traineruser',views.traineruser),path('delete-record',views.delete),path('edit-record',views.edit),path('add-Trainer',views.AddTrainer),path('search-trainer',views.searchTrainer),path('search-traineruser',views.searchTraineruser),path('search2-Trainer',views.SearchTrainer),path('search2-Traineruser',views.SearchTraineruser),path('package',views.package),path('new-package',views.newpackage),path('add-package',views.addpackage),path('edit-package',views.editpackage),path('add-Package',views.AddPackage),path('delete-package',views.deletepackage),path('view-package',views.packageview),path('search-package',views.searchPackage),path('search2-Package',views.SearchPackage),path('user',views.loginuser),path('loginnuser',views.loginnuser),]