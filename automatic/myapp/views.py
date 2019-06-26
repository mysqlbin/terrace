from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.include import meta
from myapp.include import function as func
from myapp.include import sqlfilter
from myapp.tasks import parse_to_binlog2sql
from myapp.form import AddForm
from blacklist import blFunction as bc
from myapp.models import Db_instance,SlowQuery,SlowQueryHistory

# from form import AddForm,LoginForm,Captcha
from django.contrib import auth

from django.contrib.auth.decorators import login_required,permission_required

from django.db.models import F,Max,Sum,Value as V

from django.db.models.functions import Concat

from django.forms.models import model_to_dict

import datetime,time


@login_required(login_url='/admin/login/')
def index(request):
    return render(request, 'index.html')


def slow_query(request):

    inslist = Db_instance.objects.filter(db_type='mysql').order_by("ip")
    insname = Db_instance.objects.get(id=int(request.POST.get('instance', '3')))
    dbname_res = insname.db_name_set.all().values('dbname')

    dblist = []
    if dbname_res.exists():
        dblist.append('全部数据库')
        for res in dbname_res:
            dblist.append(res.get('dbname'))

    db_name = request.POST.get('dbname')

    default_begin_time = time.strftime("%Y-%m-%d")
    default_begin_time = datetime.datetime.strptime(default_begin_time, '%Y-%m-%d') + datetime.timedelta(days=-1)

    default_stop_time  = time.strftime('%Y-%m-%d %X', time.localtime())
    default_range_time = '{} To {}'.format(default_begin_time, default_stop_time)
    range_time = request.POST.get('range-time', default_range_time)
    range_time_split = range_time.split("To")

    start_time = range_time_split[0].strip()
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')

    end_time = range_time_split[1].strip()
    end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    if db_name and db_name != '全部数据库':
        # 获取慢查数据
        slowsql_obj = SlowQuery.objects.filter(
            slowqueryhistory__hostname_max=('{}:{}'.format(insname.ip, insname.port)),
            slowqueryhistory__db_max=db_name,
            slowqueryhistory__ts_min__range=(start_time, end_time)
        ).annotate(SQLText=F('fingerprint'), SQLId=F('checksum')).values('SQLText', 'SQLId').annotate(
            CreateTime=Max('slowqueryhistory__ts_max'),
            DBName=Max('slowqueryhistory__db_max'),  # 数据库
            QueryTimeAvg=Sum('slowqueryhistory__query_time_sum') / Sum('slowqueryhistory__ts_cnt'),  # 平均执行时长
            MySQLTotalExecutionCounts=Sum('slowqueryhistory__ts_cnt'),  # 执行总次数
            MySQLTotalExecutionTimes=Sum('slowqueryhistory__query_time_sum'),  # 执行总时长
            ParseTotalRowCounts=Sum('slowqueryhistory__rows_examined_sum'),  # 扫描总行数
            ReturnTotalRowCounts=Sum('slowqueryhistory__rows_sent_sum'),  # 返回总行数
        )
    else:
        # 获取慢查数据
        slowsql_obj = SlowQuery.objects.filter(
            slowqueryhistory__hostname_max=('{}:{}'.format(insname.ip, insname.port)),
            slowqueryhistory__ts_min__range=(start_time, end_time),
        ).annotate(SQLText=F('fingerprint'), SQLId=F('checksum')).values('SQLText', 'SQLId').annotate(
            CreateTime=Max('slowqueryhistory__ts_max'),
            DBName=Max('slowqueryhistory__db_max'),  # 数据库
            QueryTimeAvg=Sum('slowqueryhistory__query_time_sum') / Sum('slowqueryhistory__ts_cnt'),  # 平均执行时长
            MySQLTotalExecutionCounts=Sum('slowqueryhistory__ts_cnt'),  # 执行总次数
            MySQLTotalExecutionTimes=Sum('slowqueryhistory__query_time_sum'),  # 执行总时长
            ParseTotalRowCounts=Sum('slowqueryhistory__rows_examined_sum'),  # 扫描总行数
            ReturnTotalRowCounts=Sum('slowqueryhistory__rows_sent_sum'),  # 返回总行数
        )

    slow_sql_result = slowsql_obj.order_by('-MySQLTotalExecutionCounts')

    return render(request, 'show_query.html', locals())


def slowquery_review_history(request, SQLId, startTime, endTime):

    """
    把需要的SQL查询出来
    select hostname_max from mysql_slow_query_review_history where `checksum`='751B6804D43917F6CFBAB7F3D65EB9CB'  limit 1;
    select * from myapp_db_instance where ip='39.108.17.17' and `port`=3306;
    select dbname from myapp_db_name db_name join myapp_db_name_instance db_instance on db_name.id=db_instance.db_name_id where db_instance_id=3;
    """

    hostname_db_max_results = SlowQueryHistory.objects.filter(checksum=SQLId).values('hostname_max', 'db_max')[0:1]

    ip_addr = '127.0.0.1'
    port = 3306
    has_db_name = ''
    if hostname_db_max_results.exists():
        hostname_max = ''
        for res in hostname_db_max_results:
            hostname_max = res.get('hostname_max')
            has_db_name = res.get('db_max')
        hostname_max_list = hostname_max.split(":")
        ip_addr = hostname_max_list[0]
        port = hostname_max_list[1]

    instance_res = Db_instance.objects.get(ip=ip_addr, port=port)
    dbname_res = instance_res.db_name_set.all().values('dbname')

    dblist = []
    if dbname_res.exists():
        dblist.append('全部数据库')
        for res in dbname_res:
            dblist.append(res.get('dbname'))

    sql_id = ''
    db_name = request.POST.get('dbname', has_db_name)
    if db_name == '' and has_db_name == '':
        sql_id = '{}'.format(SQLId)


    default_begin_time = startTime
    default_stop_time = endTime
    default_range_time = '{} To {}'.format(default_begin_time, default_stop_time)

    range_time = request.POST.get('range-time', default_range_time)
    range_time_split = range_time.split("To")

    start_time = range_time_split[0].strip()
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time = range_time_split[1].strip()
    end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    if sql_id:
        # 获取慢查明细数据
        slow_sql_record_result = SlowQueryHistory.objects.filter(
            hostname_max=('{}:{}'.format(instance_res.ip, instance_res.port)),
            checksum=sql_id,
            ts_min__range=(start_time, end_time)
        ).annotate(ExecutionStartTime=F('ts_min'),  # 本次统计(每5分钟一次)该类型sql语句出现的最小时间
                   DBName=F('db_max'),  # 数据库名
                   HostAddress=Concat(V('\''), 'user_max', V('\''), V('@'), V('\''), 'client_max', V('\'')),  # 用户名
                   SQLText=F('sample'),  # SQL语句
                   TotalExecutionCounts=F('ts_cnt'),  # 本次统计该sql语句出现的次数
                   QueryTimePct95=F('query_time_pct_95'),  # 本次统计该sql语句95%耗时
                   QueryTimes=F('query_time_sum'),  # 本次统计该sql语句花费的总时间(秒)
                   LockTimes=F('lock_time_sum'),  # 本次统计该sql语句锁定总时长(秒)
                   ParseRowCounts=F('rows_examined_sum'),  # 本次统计该sql语句解析总行数
                   ReturnRowCounts=F('rows_sent_sum')  # 本次统计该sql语句返回总行数
                   )
    else:
        if db_name and db_name != '全部数据库':
            # 获取慢查明细数据
            slow_sql_record_result = SlowQueryHistory.objects.filter(
                hostname_max=('{}:{}'.format(instance_res.ip, instance_res.port)),
                db_max=db_name,
                ts_min__range=(start_time, end_time)
            ).annotate(ExecutionStartTime=F('ts_min'),  # 本次统计(每5分钟一次)该类型sql语句出现的最小时间
                       DBName=F('db_max'),  # 数据库名
                       HostAddress=Concat(V('\''), 'user_max', V('\''), V('@'), V('\''), 'client_max', V('\'')), # 用户名
                       SQLText=F('sample'),  # SQL语句
                       TotalExecutionCounts=F('ts_cnt'),  # 本次统计该sql语句出现的次数
                       QueryTimePct95=F('query_time_pct_95'),  # 本次统计该sql语句出现的次数
                       QueryTimes=F('query_time_sum'),  # 本次统计该sql语句花费的总时间(秒)
                       LockTimes=F('lock_time_sum'),  # 本次统计该sql语句锁定总时长(秒)
                       ParseRowCounts=F('rows_examined_sum'),  # 本次统计该sql语句解析总行数
                       ReturnRowCounts=F('rows_sent_sum')  # 本次统计该sql语句返回总行数
                       )
        else:
            # 获取慢查明细数据
            slow_sql_record_result = SlowQueryHistory.objects.filter(
                hostname_max=('{}:{}'.format(instance_res.ip, instance_res.port)),
                ts_min__range=(start_time, end_time)
            ).annotate(ExecutionStartTime=F('ts_min'),  # 本次统计(每5分钟一次)该类型sql语句出现的最小时间
                       DBName=F('db_max'),  # 数据库名
                       HostAddress=Concat(V('\''), 'user_max', V('\''), V('@'), V('\''), 'client_max', V('\'')), # 用户名
                       SQLText=F('sample'),  # SQL语句
                       TotalExecutionCounts=F('ts_cnt'),  # 本次统计该sql语句出现的次数
                       QueryTimePct95=F('query_time_pct_95'),  # 本次统计该sql语句95%耗时
                       QueryTimes=F('query_time_sum'),  # 本次统计该sql语句花费的总时间(秒)
                       LockTimes=F('lock_time_sum'),  # 本次统计该sql语句锁定总时长(秒)
                       ParseRowCounts=F('rows_examined_sum'),  # 本次统计该sql语句解析总行数
                       ReturnRowCounts=F('rows_sent_sum')  # 本次统计该sql语句返回总行数
                       )

    return render(request, 'showsql_info.html', locals())


@login_required(login_url='/admin/login/')
def binlog_parse(request):

    # insname.db_name_set.all()

    inslist = Db_instance.objects.filter(db_type='mysql').order_by("ip")
    if request.method == 'POST':
        try:

            parse_sql_number = [10,50,200]   #这里可以加入配置文件中

            insname = Db_instance.objects.get(id=int(request.POST['ins_set']))

            binresult, col = meta.get_process_data(insname, 'show binary logs')

            dbresult, col = meta.get_process_data(insname, 'show databases')

            binlist = []
            dblist = []

            dblist.append('all')

            for i in binresult:
                binlist.append(i[0])

            for i in dbresult:
                dblist.append(i[0])

            if 'show_binary' in request.POST:
                start_pos = 4
                return render(request, 'binlog_parse.html', locals())

            elif 'parse_commit' in request.POST:

                binname    = request.POST['binary_list']

                start_pos  = str(request.POST['start_pos'])
                if start_pos == '4':
                    start_pos = 4
                else:
                    start_pos = int(start_pos)

                stop_pos   = str(request.POST['stop_pos'])
                if stop_pos == '0' or stop_pos == '':
                    stop_pos = ''
                else:
                    stop_pos = int(stop_pos)

                begin_time = request.POST['begin_time']
                stop_time = request.POST['stop_time']
                tbname     = request.POST['tbname']
                dbselected = request.POST['dblist']
                if dbselected == 'all':
                    dbselected = ''

                countnum = int(request.POST['countnum'])
                if countnum not in [1, 10, 50, 200]:
                    countnum = 1

                sql_type = int(request.POST['sql_type'])
                if sql_type == 1:
                    flashback = True
                else:
                    flashback = False

                sqllist = parse_to_binlog2sql(insname, binname, start_pos, stop_pos, begin_time, tbname, dbselected, flashback, countnum)

                return render(request, 'binlog_parse.html', locals())

        except Exception as e:
            print(e)
            return render(request, 'binlog_parse.html', locals())
    else:
        return render(request, 'binlog_parse.html', locals())

def mysql_querys(request):

    objlist = func.get_mysql_hostlist('binbin')

    choosed_host = 'tags'

    a = 'select * from myapp_db_account'

    try:
        # print func.sql_init_filter(a)
        a = sqlfilter.get_sql_detail(sqlfilter.sql_init_filter(a), 1)[0]
    except Exception as e:
        a = 'wrong'
        pass

    advice = func.get_advice(choosed_host, a, request)
    return HttpResponse(advice)

# def mysql_querys(request):
#     #print request.user.username
#     # print request.user.has_perm('myapp.can_mysql_query')
#
#     objlist = func.get_mysql_hostlist('binbin')
#
#     choosed_host = 'tags'
#
#     a = 'select * from myapp_db_account'
#
#     # get first valid statement
#     try:
#         #print func.sql_init_filter(a)
#         a = sqlfilter.get_sql_detail(sqlfilter.sql_init_filter(a), 1)[0]
#     except Exception as e:
#         a='wrong'
#         pass
#
#     #return HttpResponse(a)
#
#
#     a,numlimit = func.check_mysql_query(a,'binbin')
#     return HttpResponse(a)
#     (data_list) = func.get_mysql_data(choosed_host,a,'binbin',request,numlimit)
#     return HttpResponse(data_list)
#     if a == func.wrong_msg:
#         del a
#         # print choosed_host
#         #return HttpResponse(locals)
#         #return render(request, 'mysql_query.html', locals())
#     #return HttpResponse(locals)

def mysql_query(request):
    #print request.user.username
    # print request.user.has_perm('myapp.can_mysql_query')
    try:
        favword = request.COOKIES['myfavword']
    except Exception as e:
        pass
    objlist = func.get_mysql_hostlist('binbin')
    if request.method == 'POST':
        form = AddForm(request.POST)
        # request.session['myfavword'] = request.POST['favword']
        choosed_host = request.POST['cx']

        # if not User.objects.get(username='binbin').db_name_set.filter(dbtag=choosed_host)[:1]:
        #     return HttpResponseRedirect("/")

        if 'searchdb' in request.POST:
            db_se = request.POST['searchdbname']
            objlist_tmp = func.get_mysql_hostlist('binbin', 'tag', db_se)
            # incase not found any db
            if len(objlist_tmp) > 0:
                objlist = objlist_tmp

        if form.is_valid():
            a = form.cleaned_data['a']
            # get first valid statement
            try:
                #print func.sql_init_filter(a)
                a = sqlfilter.get_sql_detail(sqlfilter.sql_init_filter(a), 1)[0]
            except Exception as e:
                a='wrong'
                pass
            try:
                #show explain
                if 'explain' in request.POST:
                    a = func.check_explain (a)
                    (data_list,collist,dbname) = func.get_mysql_data(choosed_host,a,'binbin',request,100)
                    return render(request, 'mysql_query.html', locals())
                    # return render(request,'mysql_query.html',{'form': form,'objlist':objlist,'data_list':data_list,'collist':collist,'choosed_host':choosed_host,'dbname':dbname})
                    #export csv
                elif 'query' in request.POST:
                    #check if table in black list and if user has permit to query
                    inBlackList,blacktb = bc.Sqlparse(a).check_query_table(choosed_host,'binbin')
                    if inBlackList:
                        return render(request, 'mysql_query.html', locals())
                    #get nomal query
                    a,numlimit = func.check_mysql_query(a,'binbin')
                    (data_list,collist,dbname) = func.get_mysql_data(choosed_host,a,'binbin',request,numlimit)
                    # donot show wrong message sql
                    if a == func.wrong_msg:
                        del a
                    # print choosed_host
                    return render(request, 'mysql_query.html', locals())
                elif 'sqladvice' in request.POST:

                    advice = func.get_advice(choosed_host, a, request)
                    return render(request, 'mysql_query.html', locals())

                return render(request, 'mysql_query.html', locals())

            except Exception as e:
                print(e)
                return render(request, 'mysql_query.html', locals())

        else:
            return render(request, 'mysql_query.html', locals())
            # return render(request, 'mysql_query.html', {'form': form,'objlist':objlist})
    else:
        form = AddForm()
        return render(request, 'mysql_query.html', locals())
        # return render(request, 'mysql_query.html', {'form': form,'objlist':objlist})

