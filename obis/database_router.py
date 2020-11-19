__author__ = 'Tyler Walker' # twalker1998@gmail.com
__author__ = 'Mark Stacy'

class obisRouter(object):
    """
    A router to control all database operations on models in the obis application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read obis models go to obis db.
        """
        if model._meta.app_label == 'obis':
            return 'obis'
        
        return None
    
    def db_for_write(self, model, **hints):
        """
        Attempts to write obis models go to obis db.
        """
        if model._meta.app_label == 'obis':
            return 'obis'
        
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the obis app is involved.
        """
        if obj1._meta.app_label == 'obis' or obj2._meta.app_label == 'obis':
            return True
        
        return None
