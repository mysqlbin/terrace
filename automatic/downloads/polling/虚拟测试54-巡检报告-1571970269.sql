1.数据表巡检项:
1.1 统计数据库存储引擎的数量:
   table_schema:db1              engine:InnoDB          engine_counts:12 
   table_schema:mydjango_db      engine:InnoDB          engine_counts:16 
   table_schema:niuniu_db        engine:InnoDB          engine_counts:80 
   table_schema:terrace_db       engine:InnoDB          engine_counts:22 
   table_schema:test_db          engine:InnoDB          engine_counts: 6 
1.2 超过多少G的大表:
   table_schema:niuniu_db        table_name:table_club_hundred_log_charge            size:707.70M
   table_schema:niuniu_db        table_name:table_lhd_players                        size:1089.50M
1.3 数据量排名前靠前的大表:
   table_schema:niuniu_db        table_name:table_lhd_players                        all_size:1089.50M        data_size:768.00M         index_size:321.50M         table_rows:10705699
   table_schema:niuniu_db        table_name:table_club_hundred_log_charge            all_size:707.70M         data_size:579.00M         index_size:128.70M         table_rows:5259408
   table_schema:niuniu_db        table_name:table_clubgamescoredetail_history        all_size:420.47M         data_size:376.89M         index_size:43.58M          table_rows:1643639
1.4 单表超过行数 100000 表:
   table_schema:niuniu_db       table_name:table_lhd_players                        table_rows:10705699 
   table_schema:niuniu_db       table_name:table_club_hundred_log_charge            table_rows:5259408 
   table_schema:niuniu_db       table_name:table_clubgamescoredetail_history        table_rows:1643639 
   table_schema:niuniu_db       table_name:table_clublogscore_history               table_rows:1610400 
   table_schema:test_db         table_name:t2                                       table_rows:998222 
   table_schema:niuniu_db       table_name:table_clubgameuserscoredetail            table_rows:867104 
   table_schema:niuniu_db       table_name:table_clublogplatformscore_history       table_rows:817169 
   table_schema:niuniu_db       table_name:table_bet_inout                          table_rows:640378 
   table_schema:db1             table_name:t1                                       table_rows:622544 
   table_schema:db1             table_name:t2                                       table_rows:588259 
   table_schema:niuniu_db       table_name:table_club_log_dudiamond                 table_rows:405544 
   table_schema:niuniu_db       table_name:table_club_hundred_log_dudiamond         table_rows:154715 
1.5 自增ID占比大于 5.0% 的表 :
   ###没有自增ID占比大于 5.0% 的表###
1.6 碎片大于多少 0.5G 的表 :
   ###没有碎片大于多少 0.5G 的表###
1.7 统计大字段表:
    table_schema:db1              engine:_table_clubgamelog_new         engine_counts:LogData         
    table_schema:db1              engine:_table_clubgamelog_new         engine_counts:CardData        
    table_schema:db1              engine:table_clubgamelog              engine_counts:LogData         
    table_schema:db1              engine:table_clubgamelog              engine_counts:CardData        
    table_schema:db1              engine:table_clubgamescoredetail      engine_counts:szExtChar       
    table_schema:niuniu_db        engine:table_club_task_member_data    engine_counts:TaskDay         
    table_schema:niuniu_db        engine:table_club_task_member_data    engine_counts:TaskTime        
1.8 统计字段类型varchar长度大于 50 的表:
    table_schema:db1             table_name:_table_clubgamelog_new                   column_name:szToken              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:db1             table_name:accountinfo                              column_name:Ip                   data_type:varchar              CHARACTER_MAXIMUM_LENGTH:512
    table_schema:db1             table_name:table_clubgamelog                        column_name:szToken              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:db1             table_name:table_clubgamescoredetail                column_name:szToken              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:db1             table_name:table_clubgamescoredetail                column_name:szCardData           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:db1             table_name:table_clubgamescoredetail                column_name:nCardData            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:db1             table_name:table_clubinfo                           column_name:nIconID              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:db1             table_name:table_clubinfo                           column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:db1             table_name:table_clubinfo                           column_name:szNoteMsg            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:db1             table_name:table_third_order                        column_name:szOrder              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:db1             table_name:table_third_order                        column_name:szOrderInfo          data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:mydjango_db     table_name:auth_group                               column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:80
    table_schema:mydjango_db     table_name:auth_permission                          column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:mydjango_db     table_name:auth_permission                          column_name:codename             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:mydjango_db     table_name:auth_user                                column_name:password             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:128
    table_schema:mydjango_db     table_name:auth_user                                column_name:username             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:150
    table_schema:mydjango_db     table_name:auth_user                                column_name:last_name            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:150
    table_schema:mydjango_db     table_name:auth_user                                column_name:email                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:254
    table_schema:mydjango_db     table_name:django_admin_log                         column_name:object_repr          data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:mydjango_db     table_name:django_celery_results_taskresult         column_name:task_id              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:mydjango_db     table_name:django_celery_results_taskresult         column_name:content_type         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:128
    table_schema:mydjango_db     table_name:django_celery_results_taskresult         column_name:content_encoding     data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:mydjango_db     table_name:django_celery_results_taskresult         column_name:task_name            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:mydjango_db     table_name:django_content_type                      column_name:app_label            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:mydjango_db     table_name:django_content_type                      column_name:model                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:mydjango_db     table_name:django_migrations                        column_name:app                  data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:mydjango_db     table_name:django_migrations                        column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:niuniu_db       table_name:accountinfo                              column_name:TreeCode             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:accountinfo                              column_name:RealName             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:niuniu_db       table_name:accountinfo                              column_name:EMail                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:accountinfo                              column_name:LoginToken           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:accountinfo                              column_name:Ip                   data_type:varchar              CHARACTER_MAXIMUM_LENGTH:512
    table_schema:niuniu_db       table_name:accountinrole                            column_name:TreeCode             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:accountorroleinrule                      column_name:TreeCode             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:enterprise                               column_name:Name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:niuniu_db       table_name:enterprise                               column_name:TreeCode             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:enterprise                               column_name:EnterSignature       data_type:varchar              CHARACTER_MAXIMUM_LENGTH:512
    table_schema:niuniu_db       table_name:enterprise                               column_name:Contact              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:niuniu_db       table_name:enterprise                               column_name:Address              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:512
    table_schema:niuniu_db       table_name:enterprise                               column_name:WeiXin               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:niuniu_db       table_name:enterprise                               column_name:Remark               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:1000
    table_schema:niuniu_db       table_name:enterprise                               column_name:IpAuthentication     data_type:varchar              CHARACTER_MAXIMUM_LENGTH:258
    table_schema:niuniu_db       table_name:enterprise                               column_name:openId               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:enterprise                               column_name:PageOpenId           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:enterpriselog                            column_name:Remark               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:500
    table_schema:niuniu_db       table_name:operationslog                            column_name:PKID                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:operationslog                            column_name:FormObject           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:rechargedetail                           column_name:BatchName            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:niuniu_db       table_name:rechargedetail                           column_name:OpEnterPriseTreeCode data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:rechargedetail                           column_name:EnterPriseTreeCode   data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:rechargedetail                           column_name:Remark               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:400
    table_schema:niuniu_db       table_name:rechargedetail                           column_name:UserCode             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:niuniu_db       table_name:roleinfo                                 column_name:TreeCode             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:roleinfo                                 column_name:RoleName             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:niuniu_db       table_name:roleinfo                                 column_name:Describe             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:2000
    table_schema:niuniu_db       table_name:ruleinfo                                 column_name:RuleName             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:niuniu_db       table_name:ruleinfo                                 column_name:Describe             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:2000
    table_schema:niuniu_db       table_name:ruleinfo                                 column_name:PagePath             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:ruleinfo                                 column_name:BtnClientClick       data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:ruleinfo                                 column_name:BtnServerClick       data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:ruleinfo                                 column_name:BtnIcon              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:ruleinfo                                 column_name:HandlePath           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:systemlog                                column_name:Msg                  data_type:varchar              CHARACTER_MAXIMUM_LENGTH:2000
    table_schema:niuniu_db       table_name:systemlog                                column_name:LogThread            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:systemlog                                column_name:Logger               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:1024
    table_schema:niuniu_db       table_name:table_agentgameresult                    column_name:szNickName           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_agentrec                           column_name:szNickName           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_agentrec                           column_name:RoomInfo             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_club_cc                            column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_club_cc_code                       column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_club_cc_low                        column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_club_hundred_cc                    column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_club_hundred_game_score            column_name:nDiamond_CardData    data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_club_hundred_game_score            column_name:nClub_CardData       data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_club_hundred_game_score            column_name:nHeart_CardData      data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_club_hundred_game_score            column_name:nSpade_CardData      data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_club_hundred_game_score            column_name:szBankCardData       data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_club_hundred_log_charge            column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubbiggamescore                   column_name:nTian_CardData       data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubbiggamescore                   column_name:nDi_CardData         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubbiggamescore                   column_name:nXuan_CardData       data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubbiggamescore                   column_name:nHuang_CardData      data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubbiggamescore                   column_name:szBankCardData       data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubevent                          column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubgamescore                      column_name:szRule               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubgamescore                      column_name:szRoundType          data_type:varchar              CHARACTER_MAXIMUM_LENGTH:60
    table_schema:niuniu_db       table_name:table_clubgamescoredetail                column_name:szRule               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubgamescoredetail                column_name:szCardData           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubgamescoredetail                column_name:szExtChar            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubgamescoredetail_history        column_name:szRule               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubgamescoredetail_history        column_name:szCardData           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubgamescoredetail_history        column_name:szExtChar            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubinfo                           column_name:nIconID              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubinfo                           column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubinfo                           column_name:szNoteMsg            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clublogdiamond                     column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clublogdiamond_history             column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clublogfreescore                   column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubloggold                        column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clublogplatformscore               column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clublogplatformscore_history       column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clublogplatformtax                 column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clublogscore                       column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clublogscore_history               column_name:szDesc               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_clubmember                         column_name:szNickName           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_clubmember                         column_name:szExtenDesc          data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_companyaudit                       column_name:Remark               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:400
    table_schema:niuniu_db       table_name:table_companyaudit                       column_name:Out_trade_no         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:table_companyaudit                       column_name:Prepay_no            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:niuniu_db       table_name:table_diamondactionlog                   column_name:szNickName           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_diamondactionlog                   column_name:szRemark             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:300
    table_schema:niuniu_db       table_name:table_gameid                             column_name:GameDesc             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:niuniu_db       table_name:table_getrrwardlog                       column_name:szNickName           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_getrrwardlog                       column_name:rewardname           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:300
    table_schema:niuniu_db       table_name:table_getrrwardlog                       column_name:szRemark             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:300
    table_schema:niuniu_db       table_name:table_goldactionlog                      column_name:szNickName           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_goldactionlog                      column_name:szRemark             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_goldrank                           column_name:szNickName           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_goldrank                           column_name:szHeadPicUrl         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:1000
    table_schema:niuniu_db       table_name:table_goldrank                           column_name:szSign               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:1000
    table_schema:niuniu_db       table_name:table_user                               column_name:szPass               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_user                               column_name:szOpenId             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:128
    table_schema:niuniu_db       table_name:table_user                               column_name:szNickName           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_user                               column_name:szHeadPicUrl         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:512
    table_schema:niuniu_db       table_name:table_user                               column_name:szSign               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:niuniu_db       table_name:table_user                               column_name:preLoginIp           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_user                               column_name:strre1               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:128
    table_schema:niuniu_db       table_name:table_user                               column_name:strre2               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:128
    table_schema:niuniu_db       table_name:table_user                               column_name:szThirdAccount       data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_user                               column_name:szThirdPass          data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:niuniu_db       table_name:table_user                               column_name:udid                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:terrace_db      table_name:auth_group                               column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:80
    table_schema:terrace_db      table_name:auth_permission                          column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:auth_permission                          column_name:codename             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:auth_user                                column_name:password             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:128
    table_schema:terrace_db      table_name:auth_user                                column_name:username             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:150
    table_schema:terrace_db      table_name:auth_user                                column_name:last_name            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:150
    table_schema:terrace_db      table_name:auth_user                                column_name:email                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:254
    table_schema:terrace_db      table_name:django_admin_log                         column_name:object_repr          data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:terrace_db      table_name:django_celery_results_taskresult         column_name:task_id              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:django_celery_results_taskresult         column_name:content_type         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:128
    table_schema:terrace_db      table_name:django_celery_results_taskresult         column_name:content_encoding     data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:terrace_db      table_name:django_celery_results_taskresult         column_name:task_name            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:django_content_type                      column_name:app_label            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_content_type                      column_name:model                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_migrations                        column_name:app                  data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:django_migrations                        column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:django_q_ormq                            column_name:key                  data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_q_schedule                        column_name:func                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:terrace_db      table_name:django_q_schedule                        column_name:hook                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:terrace_db      table_name:django_q_schedule                        column_name:task                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_q_schedule                        column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_q_task                            column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_q_task                            column_name:func                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:terrace_db      table_name:django_q_task                            column_name:hook                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:terrace_db      table_name:django_q_task                            column_name:group                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:myapp_db_instance                        column_name:password             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:300
    table_schema:terrace_db      table_name:myapp_db_instance                        column_name:user                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:mysql_slow_query_review_history          column_name:hostname_max         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:terrace_db      table_name:mysql_slow_query_review_history          column_name:client_max           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:terrace_db      table_name:mysql_slow_query_review_history          column_name:user_max             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:terrace_db      table_name:mysql_slow_query_review_history          column_name:db_max               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:terrace_db      table_name:tb_blacklist                             column_name:dbtag                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
2.索引巡检项:
2.1 获取索引数目大于 3 个的表:
   table_schema: db1              table_name: t_detail                                 ecolumn_name: nClubID              index_nam: idx_nClubID_bRobot_tEndTime_nPlayerID 
   table_schema: db1              table_name: t_detail                                 ecolumn_name: bRobot               index_nam: idx_nClubID_bRobot_tEndTime_nPlayerID 
   table_schema: db1              table_name: t_detail                                 ecolumn_name: tEndTime             index_nam: idx_nClubID_bRobot_tEndTime_nPlayerID 
   table_schema: db1              table_name: t_detail                                 ecolumn_name: nPlayerID            index_nam: idx_nClubID_bRobot_tEndTime_nPlayerID 
   table_schema: db1              table_name: table_clubgamescoredetail                ecolumn_name: tEndTime             index_nam: idx_tEndTime_bRobot 
   table_schema: db1              table_name: table_clubgamescoredetail                ecolumn_name: bRobot               index_nam: idx_tEndTime_bRobot 
   table_schema: db1              table_name: table_clubgamescoredetail                ecolumn_name: nPlayerID            index_nam: idx_nPlayerID_nGameType_bRobot_tEndTime 
   table_schema: db1              table_name: table_clubgamescoredetail                ecolumn_name: nGameType            index_nam: idx_nPlayerID_nGameType_bRobot_tEndTime 
   table_schema: db1              table_name: table_clubgamescoredetail                ecolumn_name: bRobot               index_nam: idx_nPlayerID_nGameType_bRobot_tEndTime 
   table_schema: db1              table_name: table_clubgamescoredetail                ecolumn_name: tEndTime             index_nam: idx_nPlayerID_nGameType_bRobot_tEndTime 
   table_schema: mydjango_db      table_name: auth_group_permissions                   ecolumn_name: group_id             index_nam: auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   table_schema: mydjango_db      table_name: auth_group_permissions                   ecolumn_name: permission_id        index_nam: auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   table_schema: mydjango_db      table_name: auth_permission                          ecolumn_name: content_type_id      index_nam: auth_permission_content_type_id_codename_01ab375a_uniq 
   table_schema: mydjango_db      table_name: auth_permission                          ecolumn_name: codename             index_nam: auth_permission_content_type_id_codename_01ab375a_uniq 
   table_schema: mydjango_db      table_name: auth_user_groups                         ecolumn_name: user_id              index_nam: auth_user_groups_user_id_group_id_94350c0c_uniq 
   table_schema: mydjango_db      table_name: auth_user_groups                         ecolumn_name: group_id             index_nam: auth_user_groups_user_id_group_id_94350c0c_uniq 
   table_schema: mydjango_db      table_name: auth_user_user_permissions               ecolumn_name: user_id              index_nam: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   table_schema: mydjango_db      table_name: auth_user_user_permissions               ecolumn_name: permission_id        index_nam: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   table_schema: mydjango_db      table_name: django_content_type                      ecolumn_name: app_label            index_nam: django_content_type_app_label_model_76bd3d3b_uniq 
   table_schema: mydjango_db      table_name: django_content_type                      ecolumn_name: model                index_nam: django_content_type_app_label_model_76bd3d3b_uniq 
   table_schema: niuniu_db        table_name: table_clubgamescoredetail                ecolumn_name: nClubID              index_nam: idx_nClubID_nTableID_nPlayerID_tStartTime 
   table_schema: niuniu_db        table_name: table_clubgamescoredetail                ecolumn_name: nTableID             index_nam: idx_nClubID_nTableID_nPlayerID_tStartTime 
   table_schema: niuniu_db        table_name: table_clubgamescoredetail                ecolumn_name: nPlayerID            index_nam: idx_nClubID_nTableID_nPlayerID_tStartTime 
   table_schema: niuniu_db        table_name: table_clubgamescoredetail                ecolumn_name: tStartTime           index_nam: idx_nClubID_nTableID_nPlayerID_tStartTime 
   table_schema: niuniu_db        table_name: table_clublogplatformscore               ecolumn_name: nClubID              index_nam: idx_nClubID_nGameID_nType_CreateTime 
   table_schema: niuniu_db        table_name: table_clublogplatformscore               ecolumn_name: nGameID              index_nam: idx_nClubID_nGameID_nType_CreateTime 
   table_schema: niuniu_db        table_name: table_clublogplatformscore               ecolumn_name: nType                index_nam: idx_nClubID_nGameID_nType_CreateTime 
   table_schema: niuniu_db        table_name: table_clublogplatformscore               ecolumn_name: CreateTime           index_nam: idx_nClubID_nGameID_nType_CreateTime 
   table_schema: niuniu_db        table_name: table_clublogscore                       ecolumn_name: nGameID              index_nam: idx_nGameID_clubid_nType_CreateTime 
   table_schema: niuniu_db        table_name: table_clublogscore                       ecolumn_name: clubid               index_nam: idx_nGameID_clubid_nType_CreateTime 
   table_schema: niuniu_db        table_name: table_clublogscore                       ecolumn_name: nType                index_nam: idx_nGameID_clubid_nType_CreateTime 
   table_schema: niuniu_db        table_name: table_clublogscore                       ecolumn_name: CreateTime           index_nam: idx_nGameID_clubid_nType_CreateTime 
   table_schema: terrace_db       table_name: auth_group_permissions                   ecolumn_name: group_id             index_nam: auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   table_schema: terrace_db       table_name: auth_group_permissions                   ecolumn_name: permission_id        index_nam: auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   table_schema: terrace_db       table_name: auth_permission                          ecolumn_name: content_type_id      index_nam: auth_permission_content_type_id_codename_01ab375a_uniq 
   table_schema: terrace_db       table_name: auth_permission                          ecolumn_name: codename             index_nam: auth_permission_content_type_id_codename_01ab375a_uniq 
   table_schema: terrace_db       table_name: auth_user_groups                         ecolumn_name: user_id              index_nam: auth_user_groups_user_id_group_id_94350c0c_uniq 
   table_schema: terrace_db       table_name: auth_user_groups                         ecolumn_name: group_id             index_nam: auth_user_groups_user_id_group_id_94350c0c_uniq 
   table_schema: terrace_db       table_name: auth_user_user_permissions               ecolumn_name: user_id              index_nam: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   table_schema: terrace_db       table_name: auth_user_user_permissions               ecolumn_name: permission_id        index_nam: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   table_schema: terrace_db       table_name: django_content_type                      ecolumn_name: app_label            index_nam: django_content_type_app_label_model_76bd3d3b_uniq 
   table_schema: terrace_db       table_name: django_content_type                      ecolumn_name: model                index_nam: django_content_type_app_label_model_76bd3d3b_uniq 
   table_schema: test_db          table_name: table_clubgamescoredetail                ecolumn_name: tEndTime             index_nam: idx_tEndTime_bRobot 
   table_schema: test_db          table_name: table_clubgamescoredetail                ecolumn_name: bRobot               index_nam: idx_tEndTime_bRobot 
2.2 获取没有主键索引的表:
   table_schema:db1              table_name:t_detail                                 
   table_schema:niuniu_db        table_name:table_club_cc_code                       
   table_schema:niuniu_db        table_name:table_gameid                             
3.参数巡检项:
3.1 InnoDB层参数:
3.1.1 InnoDB层缓冲池参数:
    innodb_buffer_pool_dump_at_shutdown : ON
    innodb_buffer_pool_instances : 4
    innodb_buffer_pool_load_at_startup : ON
    innodb_buffer_pool_size : 8589934592
    innodb_flush_neighbors : 0
    innodb_lru_scan_depth : 4000
    innodb_max_dirty_pages_pct : 50.000000
    innodb_old_blocks_pct : 37
    innodb_old_blocks_time : 1000
    innodb_random_read_ahead : OFF
    innodb_read_ahead_threshold : 56
3.1.2 InnoDB层redo参数:
    innodb_flush_log_at_trx_commit : 2
    innodb_log_buffer_size : 33554432
    innodb_log_file_size : 1073741824
    innodb_log_files_in_group : 3
3.1.3 InnoDB层持久化统计信息参数:
    innodb_stats_auto_recalc : ON
    innodb_stats_persistent : ON
    innodb_stats_persistent_sample_pages : 20
3.1.4 InnoDB层其它参数:
    innodb_adaptive_hash_index : ON
    innodb_autoinc_lock_mode : 1
    innodb_change_buffer_max_size : 25
    innodb_change_buffering : all
    innodb_data_file_path : ibdata1:1G:autoextend
    innodb_data_home_dir : 
    innodb_doublewrite : ON
    innodb_fast_shutdown : 1
    innodb_file_per_table : ON
    innodb_flush_method : O_DIRECT
    innodb_force_recovery : 0
    innodb_io_capacity : 4000
    innodb_io_capacity_max : 8000
    innodb_lock_wait_timeout : 60
    innodb_open_files : 65535
    innodb_page_cleaners : 4
    innodb_purge_threads : 4
    innodb_read_io_threads : 8
    innodb_rollback_on_timeout : ON
    innodb_thread_concurrency : 0
    innodb_write_io_threads : 8
3.2 Server层参数:
3.2.1 Server层binlog参数:
    binlog_cache_size : 4194304
    binlog_format : ROW
    binlog_group_commit_sync_delay : 0
    binlog_group_commit_sync_no_delay_count : 0
    binlog_row_image : FULL
    binlog_transaction_dependency_tracking : COMMIT_ORDER
    expire_logs_days : 7
    max_binlog_cache_size : 2147483648
    max_binlog_size : 1073741824
    sync_binlog : 10000
3.2.2 Server层线程/会话相关的内存参数:
    join_buffer_size : 4194304
    key_buffer_size : 33554432
    query_cache_size : 0
    read_buffer_size : 8388608
    read_rnd_buffer_size : 4194304
    sort_buffer_size : 4194304
    tmp_table_size : 10240
3.2.3 Server层其它参数:
    interactive_timeout : 3600
    log_queries_not_using_indexes : ON
    log_timestamps : SYSTEM
    long_query_time : 1.000000
    lower_case_table_names : 1
    max_allowed_packet : 33554432
    max_connect_errors : 1000000
    max_connections : 512
    max_execution_time : 0
    max_user_connections : 0
    net_buffer_length : 16384
    open_files_limit : 65535
    slow_query_log : ON
    sql_mode : STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION
    system_time_zone : CST
    table_open_cache : 1024
    time_zone : SYSTEM
    wait_timeout : 3600
4 状态巡检项:
4.1 InnoDB层缓冲池状态:
   Innodb_buffer_pool_pages_data : 91900
   Innodb_buffer_pool_pages_dirty : 29
   Innodb_buffer_pool_pages_flushed : 194417
   Innodb_buffer_pool_pages_free : 422441
   Innodb_buffer_pool_pages_total : 524224
   Innodb_buffer_pool_read_ahead : 40638
   Innodb_buffer_pool_read_ahead_evicted : 0
   Innodb_buffer_pool_read_requests : 463074440
   Innodb_buffer_pool_reads : 2844
   Innodb_buffer_pool_wait_free : 0
   脏页在缓冲池数据页中的占比为: 0.01%
   InnoDB buffer pool 缓冲池命中率: 99.99%
4.2 并发线程连接数:
   Threads_connected : 4
   Threads_created : 21
   Threads_running : 1
4.3 InnoDB行锁等待:
   Innodb_row_lock_current_waits : 0
   Innodb_row_lock_time : 555676
   Innodb_row_lock_time_avg : 46306
   Innodb_row_lock_time_max : 61018
   Innodb_row_lock_waits : 12
4.4 打开表的次数:
   Open_files : 4
   Open_tables : 1024
   Opened_tables : 96441
4.5 创建内存临时表和磁盘临时表的次数:
   Created_tmp_disk_tables : 8287
   Created_tmp_tables : 33901
4.6 InnoDB关键特性double write的使用情况:
   Innodb_dblwr_pages_written : 208917
   Innodb_dblwr_writes : 46730
   每次写操作合并page的个数: 4.0
