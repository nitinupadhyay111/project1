import pymysql
from django.conf import settings


dbhost = settings.DATABASES['mysql']['HOST']
dbuser = settings.DATABASES['mysql']['USER']
dbpassword = settings.DATABASES['mysql']['PASSWORD']
dbname = settings.DATABASES['mysql']['NAME']



def connectDatabase():
    return pymysql.connections.Connection(host=dbhost, user=dbuser, password=dbpassword, database=dbname)

    
