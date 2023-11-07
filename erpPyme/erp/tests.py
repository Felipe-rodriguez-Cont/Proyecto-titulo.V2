from erpPyme.wsgi import *
from erp.models import Type

# Create your tests here.
query = Type.objects.all()
print (query)