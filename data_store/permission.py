from rest_framework import permissions
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from itertools import chain

class dataStorePermission(permissions.BasePermission):
    """
    Create records within collections.
    """

    def has_permission(self, request, view):
        perms=list(request.user.get_all_permissions()) 
        for itm in perms:
            print itm
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            django_app = 'data_store'
            admin_perm = 'data_store.datastore_admin'
            path = request.path
            path=path.split('/')
            code_perm= "{0}.edit_{1}_{2}".format(django_app,path[-3],path[-2])
            perms=list(request.user.get_all_permissions())
            if request.user.is_superuser or admin_perm in perms or code_perm in perms:
                return True
            else:
                return False 

class createDataStorePermission(permissions.BasePermission):
    """
    Create Database and Collections permissions.
    """
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            django_app = 'data_store'
            admin_perm = 'data_store.datastore_admin'
            code_perm= "{0}.{1}".format(django_app,'datastore_create')
            perms=list(request.user.get_all_permissions())
            if request.user.is_superuser or admin_perm in perms or code_perm in perms:
                return True
            else:
                return False