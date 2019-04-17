# coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from salt import saltapi
from salt import apitest
import json
from salt.models import Saltrecord
from django.core.paginator import Paginator, InvalidPage, EmptyPage
# Create your views here.

def test(request):
    sapi = apitest.SaltAPI()
    # return HttpResponse(333)
    up_host = sapi.get_host_list('group1', 1)
    return HttpResponse(up_host)
    #info_all = sapi.remote_noarg_execution_sin(up_host, 'grains.items')

    #print(info_all)


    return HttpResponse(111)

def salt_exec(request):
    return render(request, 'exec.html', locals())

def execute(request):
    if request.method == 'POST':
        try:

            tgt = request.POST.get('tgt', "*")
            # fun = request.POST.get('fun', "cmd.run")
            fun = "cmd.run"

            arg = request.POST.get('arg', 'free -m')
            sapi = saltapi.SaltAPI()
            isgp = int(request.POST.get('isgroup', "0"))

            jid_auto = sapi.asyncMasterToMinion(tgt=tgt, fun=fun, arg=arg, group=isgp)

            sapi.record_salt(request.user.username, jid_auto, fun, tgt, arg)   # salt_record的数据写入操作

        except Exception as e:
            print(e)

    return render_to_response('auto_execute.html', locals())

def getjobinfo(request):
    context = {}
    jid_auto = request.GET['jid_auto']
    # print jid_auto
    if jid_auto:
        where = int(request.GET.get('where','123'))

        if where == 123:

            result = '/api/getjobinfo?jid_auto=%s&where=%s' % (jid_auto,0)
            return HttpResponse(result)
        else:

            hosts_result, host_result = saltapi.salt_query("select id,success,replace(replace(`return`,'\\\\n','</br>'),'\\\\t','&nbsp') from salt.salt_returns where jid='%s' limit %s,10000;" % (jid_auto, where) )
            # cursor = connection.cursor()
            # host_result = cursor.execute()
            # hosts_result = cursor.fetchall()
            where = len(hosts_result) + where
            result = []
            for host_result in hosts_result:

                if host_result[2]:
                    result.append(u'host:%s&nbsp;&nbsp;&nbsp;state:%s<br><pre>%s</pre><br>' % (host_result[0],host_result[1],host_result[2].strip('"')))
                else :
                    if host_result[1]:
                        result.append(u'host:%s&nbsp;&nbsp;&nbsp;state:%s<br/><pre>执行成功，但该命令无返回结果</pre><br/>' % (host_result[0],host_result[1]))
                    else :
                        result.append(u'host:%s&nbsp;&nbsp;&nbsp;state:%s<br/><pre>执行失败！</pre><br/>' % (host_result[0],host_result[1]))
            context = {
                "where":where,
                "result":result
            }
    # return HttpResponse(hosts_result)
        return HttpResponse(json.dumps(context))

def hardware_info(request):
    try:
        if request.method == 'POST':
            se_host = request.POST.get('search','none')
            isgp = int(request.POST.get('isgroup', "0"))
            #return HttpResponse(444)
            sapi = saltapi.SaltAPI()
            #return HttpResponse(333)
            up_host = sapi.get_host_list(se_host, isgp)
            #return HttpResponse(up_host)		

            jyp = []
            disk_all = {}
            for hostname in up_host:
                info_all = sapi.remote_noarg_execution_sin(hostname, 'grains.items')

                disk_use = sapi.remote_noarg_execution_sin(hostname, 'disk.usage')

                for key in disk_use:
                    if disk_use[key]['capacity'] is None:
                        continue
                    disk_info = {key: int(disk_use[key]['capacity'][:-1])}
                    disk_all.update(disk_info)
                    disk_dic = {'disk': disk_all}
                    info_all.update(disk_dic)
                disk_all = {}
                jyp += [info_all]
    except Exception as e:
        print(e)
    #return HttpResponse(locals)
    return render(request, 'hardware_info.html', locals())

def key_con(request):
    sapi = saltapi.SaltAPI()

    if request.POST:
        if 'accept' in request.POST:
            hostname = request.POST.get("accept")
            sapi.accept_key(hostname)
        elif 'delete' in request.POST:
            hostname = request.POST.get("delete")
            sapi.delete_key(hostname)
        elif 'reject' in request.POST:
            hostname = request.POST.get("reject")
            sapi.reject_key(hostname)
        elif 'listall' in request.POST:
            keys_all = sapi.list_all_key()
            return render(request, 'key_manager.html', locals())
        keys_all = sapi.list_all_key()
        return render(request, 'key_manager.html', locals())

    return  render(request,'key_manager.html',locals())

def salt_record(request):
    page_size = 10
    all_record = Saltrecord.objects.order_by('-id')
    paginator = Paginator(all_record,page_size)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, 'salt_record.html', locals())

def record_detail(request):
    if 'jid' in request.GET:
        job_id = request.GET.get('jid')
        hosts_result, host_result = saltapi.salt_query("select id,success,replace(replace(`return`,'\\\\n','</br>'),'\\\\t','&nbsp') from salt.salt_returns where jid='%s';" % (job_id))
        result=[]
        for host_result in hosts_result:
            # print "host_result"
            # print host_result
            if host_result[2]:
               # print(type(host_result[2]))
                result.append('host:%s&nbsp;&nbsp;&nbsp;state:%s<br><pre>%s</pre><br>' % (
                host_result[0], host_result[1], host_result[2].strip('"').encode('utf-8')))
            else:
                if host_result[1]:
                    result.append(u'host:%s&nbsp;&nbsp;&nbsp;state:%s<br/><pre>执行成功，但该命令无返回结果</pre><br/>' % (
                    host_result[0], host_result[1]))
                else:
                    result.append(u'host:%s&nbsp;&nbsp;&nbsp;state:%s<br/><pre>执行失败！</pre><br/>' % (
                    host_result[0], host_result[1]))

        print(result)
        return render(request, 'record_detail.html', locals())
