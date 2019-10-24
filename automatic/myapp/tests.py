from django.test import TestCase
from django.http import HttpResponse
from myapp.models import Db_instance
from myapp.include.meta import get_user_password
from myapp.engines import get_engine
from myapp.engines.models import ResultsSet
from myapp.include.polling_settings import innodb_buffer_pool_param
from django.conf import settings
from myapp.include.polling_sql import get_table_schema_engine

from myapp.include.polling_settings import innodb_buffer_pool_status_list

from django_q.tasks import async_task, result, fetch


import time
# Create your tests here.


def test_03(request):
    instance = Db_instance.objects.get(id=1)
    query_engine = get_engine(instance=instance)
    sql_content = 'select * from test_db.t2 where id=1;'
    # result = query_engine.query_set(sql=sql_content).rows
    # return HttpResponse(result)
    task_id = async_task(query_engine.query_set(sql=sql_content).rows)
    task_result = result(task_id, cached=True)
    return HttpResponse(task_result)

def test_04(request):
    instance = Db_instance.objects.get(id=1)
    query_engine = get_engine(instance=instance)
    # sql_content = 'select * from test_db.t2 order by a;'
    sql_content = 'select * from test_db.t2 where id=1;'
    task_id = async_task(query_engine.query_set(sql=sql_content).rows)
    task_result = fetch(task_id, wait=1 * 1000000, cached=True)
    return HttpResponse(task_result)


def test_05(request):

    result = {'status': 0, 'msg': 'ok', 'data': {}}

    instance = Db_instance.objects.get(id=1)
    query_engine = get_engine(instance=instance)
    sql_content = 'select * from test_db.t2 group by a order by a limit 2;'
    # sql_content = 'select * from test_db.t2 where id=1;'
    task_id = async_task(query_engine.query_set(sql=sql_content))
    query_task = fetch(task_id, wait=1 * 100, cached=True)

    if query_task:
        if query_task.success:
            query_result = query_task.result
            query_result.query_time = query_task.time_taken()
        else:
            query_result = ResultsSet(full_sql=sql_content)
            query_result.error = query_task.result
    # 等待超时，async_task主动关闭连接
    else:
        query_result = ResultsSet(full_sql=sql_content)
        query_result.error = '查询时间超过 0.1 秒，已被主动终止，请优化语句或者联系管理员。'

    # 查询异常
    if query_result.error:
        result['status'] = 1
        result['msg'] = query_result.error
    else:
        result['data'] = query_result.__dict__

    return HttpResponse(result)


def test_01(request):
    return HttpResponse(1)
    # instance = Db_instance.objects.get(id=1)
    # query_engine = get_engine(instance=instance)
    # # return HttpResponse(query_engine)
    # # binlog = query_engine.query_set('', 'show binary logs;').to_dict()
    # innodb_buffer_pool_status = query_engine.get_status(innodb_buffer_pool_status_list).rows
    # # get_table_schema_engine_data = query_engine.query_set(sql=get_table_schema_engine()).rows
    # innodb_buffer_pool_pages_dirty = query_engine.get_status('Innodb_buffer_pool_pages_dirty').to_dict()
    # # return HttpResponse(innodb_buffer_pool_pages_dirty)
    # return HttpResponse(innodb_buffer_pool_pages_dirty[0].get('VARIABLE_VALUE'))




def test_02(request):
    instance = Db_instance.objects.get(id=1)
    query_engine = get_engine(instance=instance)
    binlog = query_engine.query_set('', 'select version()').rows
    data = binlog[0][0][0:3]
    data = data.replace('.', '')

    return HttpResponse(data)


def polling_test(request):
    try:
        instance = Db_instance.objects.get(id=int(1))
    except Db_instance.DoesNotExist:
        res = {'status': 0, 'msg': '实例不存在'}
        return HttpResponse(json.dumps(res))

    # return HttpResponse(instance)
    query_engine = get_engine(instance=instance)

    innodb_buffer_pool_param = ['innodb_random_read_ahead',
                                'innodb_read_ahead_threshold',
                                'innodb_buffer_pool_load_at_startup',
                                'innodb_buffer_pool_dump_at_shutdown',
                                'innodb_flush_neighbors',
                                'innodb_buffer_pool_size',
                                'innodb_buffer_pool_instances',
                                'innodb_lru_scan_depth',
                                'innodb_max_dirty_pages_pct',
                                'innodb_old_blocks_pct',
                                'innodb_old_blocks_time',
                                ]
    # return HttpResponse(1)
    buffer_pool_data = query_engine.get_variables(innodb_buffer_pool_param).rows

    timestamp = int(time.time())
    path = os.path.join(settings.BASE_DIR, 'downloads/polling/')
    filename = os.path.join(path, f"的巡检报告{timestamp}.sql")

    # return HttpResponse(buffer_pool_data)
    with open(filename, 'a+') as f:
        for v in buffer_pool_data:
            # return HttpResponse(v)
            f.write('{}   {} : {}'.format('',v[0], v[1]) + '\n')

    return HttpResponse(1)