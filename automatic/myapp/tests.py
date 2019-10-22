from django.test import TestCase
from django.http import HttpResponse
from myapp.models import Db_instance
from myapp.include.meta import get_user_password
from myapp.engines import get_engine

# Create your tests here.

def test_01(request):
    instance = Db_instance.objects.get(id=1)
    query_engine = get_engine(instance=instance)
    # return HttpResponse(query_engine)
    binlog = query_engine.query_set('', 'show binary logs;').to_dict()
    return HttpResponse(binlog)


