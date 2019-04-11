from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.include import meta
from myapp.include import function as func
from myapp.include import sqlfilter
from myapp.tasks import parse_binlog,parse_binlogfirst,parse_binlog_update,parse_binlog_self
from myapp.form import AddForm
from blacklist import blFunction as bc
from myapp.models import Db_instance

def index(request):
    return render(request, 'index.html')

def metas(request):
    inslist = Db_instance.objects.filter(db_type='mysql').order_by("ip")
    if request.method == 'POST':
        insname = Db_instance.objects.get(id=int(request.POST['ins_set']))
        if 'fullpro' in request.POST:
            data_list, collist = meta.process(insname)
            return render(request, 'meta.html', locals())

        elif 'kill_list' in request.POST:
            idlist = request.POST.getlist('choosedlist')
            tmpstr = ''
            for i in idlist:
                tmpstr = tmpstr + 'kill ' + i + ';'
            datalist, col = meta.process(insname, 4, tmpstr)
            return render(request, 'meta.html', locals())

        elif 'showactive' in request.POST:
            data_list, collist = meta.process(insname, 2)
            return render(request, 'meta.html', locals())

        elif 'showengine' in request.POST:
            datalist, col = meta.process(insname, 3)
            return render(request, 'meta.html', locals())

        elif 'showbigtb' in request.POST:
            datalist, col = meta.process(insname, 6)
            return render(request, 'meta.html', locals())

        elif 'slavestatus' in request.POST:
            sql = "show slave status"
            datalist, col = meta.process(insname, 7, sql)

        elif 'showstatus' in request.POST:
            vir = request.POST['variables'].strip()
            sql = "show global status like '%" + vir + "%'"
            datalist, col = meta.process(insname, 7, sql)
            return render(request, 'meta.html', locals())

        elif 'showvari' in request.POST:
            vir = request.POST['variables'].strip()
            sql = "show global variables like '%" + vir + "%'"
            datalist, col = meta.process(insname, 7, sql)
            return render(request, 'meta.html', locals())

        elif 'showinc' in request.POST:
            datalist, col = meta.process(insname, 8)
            return render(request, 'meta.html', locals())


    else:
        return render(request, 'meta.html', locals())


'''
def mysql_binlog_parse_test(request):

    insname = Db_instance.objects.get(id=int(1))

    countnum = 10
    binname = 'mysql-bin.000026'
    if countnum not in [10, 50, 200]:
        countnum = 10
    begintime = '2018-05-17 09:51:09'
    tbname = ''

    dbselected = ''
    sqllist = parse_binlog_update(insname, binname, begintime, tbname, dbselected, countnum)

    return HttpResponse(sqllist)
'''

def mysql_binlog_rollback(request):
    inslist = Db_instance.objects.filter(db_type='mysql').order_by("ip")
    '''
    SELECT
	`myapp_db_instance`.`id`,
	`myapp_db_instance`.`ip`,
	`myapp_db_instance`.`port`,
	`myapp_db_instance`.`role`,
	`myapp_db_instance`.`db_type`
FROM
	`myapp_db_instance`
WHERE
	`myapp_db_instance`.`db_type` = 'mysql'
ORDER BY
	`myapp_db_instance`.`ip` ASC
    '''
    #局部变量：id,ip,port,role,db_type
    #return HttpResponse(inslist)
    if request.method == 'POST':
        insname = Db_instance.objects.get(id=int(request.POST['ins_set']))
        binresult, col = meta.get_process_data(insname, 'show binary logs')
        #return HttpResponse(col)  #返回字段名称
        #binresult: ('mysql-bin.000060', 62656542)('mysql-bin.000061', 13319)('mysql-bin.000062', 18837956)
        dbresult, col = meta.get_process_data(insname, 'show databases')
        #return HttpResponse(dbresult)
        #dbresult: ('information_schema',)('dezhou_db',)('mysql',)('niu201812_db',)('niuniu_db',)('performance_schema',)('sql_db',)('sys',)('terrace_db',)('test_db',)('undolog',)
        binlist = []
        dblist = []
        for i in binresult:
            #print(i[0])
            #return HttpResponse(i[0])
            binlist.append(i[0])
        for i in dbresult:
            dblist.append(i[0])

        if 'show_binary' in request.POST:
            return render(request, 'binlog_rollback.html', locals())
            #return HttpResponse(locals())

        elif 'parse_commit' in request.POST:

            binname = request.POST['binary_list']
            begintime = request.POST['begin_time']
            tbname = request.POST['tbname']
            dbselected = request.POST['dblist']
            if dbselected == 'all':
                dbselected = ''
            countnum = int(request.POST['countnum'])
            if countnum not in [10, 50, 200]:
                countnum = 10

            sqllist = parse_binlog_self(insname, binname, begintime, tbname, dbselected)
            # sqllist=1
            return HttpResponse(sqllist)

            return render(request, 'binlog_rollback.html', locals())
    return render(request, 'binlog_rollback.html', locals())   #返回字典类型的局部变量： {'z': 1, 'arg': 4} ,用于传递多个变量给模板中不同的模块

'''
def mysql_binlog_rollback(request):
    inslist = Db_instance.objects.filter(db_type='mysql').order_by("ip")
    # `myapp_db_instance`.`db_type` = 'mysql' ORDER BY `myapp_db_instance`.`ip` ASC

    if request.method == 'POST':
        try:
            binlist = []
            dblist = []
            insname = Db_instance.objects.get(id=int(request.POST['ins_set']))
            # FROM `myapp_db_instance` WHERE `myapp_db_instance`.`id` = 1
            # `myapp_db_instance`.`id`, `myapp_db_instance`.`ip`, `myapp_db_instance`.`port`, `myapp_db_instance`.`role`, `myapp_db_instance`.`db_type`

            # insname = ''
            datalist, col = meta.get_process_data(insname, 'show binary logs')
            return HttpResponse(datalist)

            dbresult, col = meta.get_process_data(insname, 'show databases')
            if col != ['error']:
                dblist.append('all')
                for i in datalist:
                    binlist.append(i[0])
                for i in dbresult:
                    dblist.append(i[0])
            else:
                del binlist
                return render(request, 'binlog_parse.html', locals())
            if 'show_binary' in request.POST:
                return render(request, 'binlog_parse.html', locals())

            elif 'parse_first' in request.POST:
                # return '333'
                # print '444'
                countnum = int(request.POST['countnum'])
                binname = request.POST['binary_list']
                if countnum not in [10, 50, 200]:
                    countnum = 10
                begintime = request.POST['begin_time']
                tbname = request.POST['tbname']
                dbselected = request.POST['dblist']
                if dbselected == 'all':
                    dbselected = ''
                sqllist = parse_binlog_update(insname, binname, begintime, tbname, dbselected, countnum)

                # return sqlllist
                # return HttpResponse(sqllist)
                # sqllist = parse_binlogfirst(insname, binname, 5)

        except Exception as e:
            print(e)
        return render(request, 'binlog_rollback.html', locals())
    else:

        return render(request, 'binlog_rollback.html', locals())
'''

def mysql_binlog_parse(request):
    inslist = Db_instance.objects.filter(db_type='mysql').order_by("ip")
                          #`myapp_db_instance`.`db_type` = 'mysql' ORDER BY `myapp_db_instance`.`ip` ASC
    if request.method == 'POST':
        try:
            binlist = []
            dblist = []
            insname = Db_instance.objects.get(id=int(request.POST['ins_set']))
            #FROM `myapp_db_instance` WHERE `myapp_db_instance`.`id` = 1
            #`myapp_db_instance`.`id`, `myapp_db_instance`.`ip`, `myapp_db_instance`.`port`, `myapp_db_instance`.`role`, `myapp_db_instance`.`db_type`

            # insname = ''
            datalist, col = meta.get_process_data(insname, 'show binary logs')
            #return HttpResponse(datalist)
            #('mysql-bin.000060', 62656542)('mysql-bin.000061', 13319)('mysql-bin.000062', 18837956)

            dbresult, col = meta.get_process_data(insname, 'show databases')
            if col != ['error']:
                dblist.append('all')
                for i in datalist:
                    binlist.append(i[0])
                for i in dbresult:
                    dblist.append(i[0])
            else:
                del binlist
                return render(request, 'binlog_parse.html', locals())

            if 'show_binary' in request.POST:
                return render(request, 'binlog_parse.html', locals())

            elif 'parse_commit' in request.POST:

                countnum = int(request.POST['countnum'])
                binname = request.POST['binary_list']
                if countnum not in [10, 50, 200]:
                    countnum = 10
                begintime = request.POST['begin_time']
                tbname = request.POST['tbname']
                dbselected = request.POST['dblist']
                if dbselected == 'all':
                 dbselected = ''
                sqllist = parse_binlog_update(insname, binname, begintime, tbname, dbselected, countnum)

                #return sqlllist
                # return HttpResponse(sqllist)
                #sqllist = parse_binlogfirst(insname, binname, 5)

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

