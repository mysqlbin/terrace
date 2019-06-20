from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.include import meta
from myapp.include import function as func
from myapp.include import sqlfilter
from myapp.tasks import parse_to_binlog2sql
from myapp.form import AddForm
from blacklist import blFunction as bc
from myapp.models import Db_instance,SlowQuery

# from form import AddForm,LoginForm,Captcha
from django.contrib import auth

from django.contrib.auth.decorators import login_required,permission_required




@login_required(login_url='/admin/login/')
def index(request):
    return render(request, 'index.html')

def slow_query(request):
    inslist = Db_instance.objects.filter(db_type='mysql').order_by("ip")
    # print(inslist)

    insname = Db_instance.objects.get(id=3)

    dbresult, col = meta.get_process_data(insname, 'show databases')

    if db_name:
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
            slowqueryhistory__hostname_max=( '{}:{}'.format(insname.ip,insname.port)),
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

    return HttpResponse(hostname_max)


@login_required(login_url='/admin/login/')

def binlog_parse(request):

    # insname.db_name_set.all()

    inslist = Db_instance.objects.filter(db_type='mysql').order_by("ip")
    if request.method == 'POST':
        try:

            parse_sql_number = [10,50,200]   #这里可以加入配置文件中
            #获取对象
            insname = Db_instance.objects.get(id=int(request.POST['ins_set']))
            # return HttpResponse(insname)   #192.168.0.252 3306 admin mysql

            #return HttpResponse(insname.db_name_set.all())   #252_test kpi

            binresult, col = meta.get_process_data(insname, 'show binary logs')
            #return HttpResponse(binresult)

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

