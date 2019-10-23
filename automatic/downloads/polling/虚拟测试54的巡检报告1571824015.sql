1.数据表巡检项:
1.1 统计数据库存储引擎的数量:
   table_schema:db1              engine:InnoDB          engine_counts:12 
   table_schema:mydjango_db      engine:InnoDB          engine_counts:16 
   table_schema:niuniu_db        engine:InnoDB          engine_counts:80 
   table_schema:terrace_db       engine:InnoDB          engine_counts:19 
   table_schema:test_db          engine:InnoDB          engine_counts: 6 
1.2 超过多少G的大表:
   table_schema:niuniu_db        table_name:table_clubgameuserscoredetail            size:91.64M
   table_schema:niuniu_db        table_name:table_bet_inout                          size:83.64M
   table_schema:niuniu_db        table_name:table_clublogplatformscore_history       size:83.11M
   table_schema:niuniu_db        table_name:table_club_hundred_log_charge            size:707.70M
   table_schema:niuniu_db        table_name:table_user                               size:7.73M
   table_schema:niuniu_db        table_name:table_club_reboot_nscore_count2          size:7.06M
   table_schema:test_db          table_name:t2                                       size:63.66M
   table_schema:db1              table_name:t1                                       size:45.08M
   table_schema:db1              table_name:t2                                       size:45.08M
   table_schema:niuniu_db        table_name:table_clubgamescoredetail_history        size:420.47M
   table_schema:niuniu_db        table_name:table_club_log_dudiamond                 size:42.09M
   table_schema:niuniu_db        table_name:table_clubmember                         size:4.89M
   table_schema:niuniu_db        table_name:table_club_hundred_log_dudiamond         size:18.58M
   table_schema:niuniu_db        table_name:table_clublogscore_history               size:159.20M
   table_schema:niuniu_db        table_name:table_clubgamescore                      size:12.58M
   table_schema:niuniu_db        table_name:table_lhd_players                        size:1089.50M
   table_schema:niuniu_db        table_name:table_club_task_member_data              size:1.77M
   table_schema:niuniu_db        table_name:enterpriselog                            size:1.67M
   table_schema:niuniu_db        table_name:operationslog                            size:1.52M
   table_schema:niuniu_db        table_name:table_clubloggold                        size:0.77M
   table_schema:niuniu_db        table_name:table_club_cc                            size:0.27M
   table_schema:niuniu_db        table_name:table_club_intable_scoredata             size:0.20M
   table_schema:niuniu_db        table_name:table_clubinfo                           size:0.16M
   table_schema:niuniu_db        table_name:table_clubevent                          size:0.14M
   table_schema:niuniu_db        table_name:table_club_exswitch_config               size:0.13M
   table_schema:niuniu_db        table_name:table_clubapplication                    size:0.11M
   table_schema:niuniu_db        table_name:rechargedetail                           size:0.09M
   table_schema:niuniu_db        table_name:sys_code                                 size:0.09M
   table_schema:niuniu_db        table_name:table_award_2019                         size:0.09M
   table_schema:niuniu_db        table_name:table_club_cc_low                        size:0.09M
   table_schema:niuniu_db        table_name:table_club_hundred_game_score_detail     size:0.09M
   table_schema:niuniu_db        table_name:table_club_hundred_user_enter_info       size:0.09M
   table_schema:niuniu_db        table_name:table_clubbiggamescore                   size:0.09M
   table_schema:niuniu_db        table_name:table_clubbiggamescoredetail             size:0.09M
   table_schema:niuniu_db        table_name:table_clubgamescoredetail                size:0.09M
   table_schema:niuniu_db        table_name:table_clublogscore                       size:0.09M
   table_schema:db1              table_name:table_clubgamescoredetail                size:0.08M
   table_schema:db1              table_name:table_third_order                        size:0.08M
   table_schema:niuniu_db        table_name:table_club_game_cfg                      size:0.08M
   table_schema:niuniu_db        table_name:table_club_member_authority              size:0.08M
   table_schema:niuniu_db        table_name:table_clublogplatformscore               size:0.08M
   table_schema:test_db          table_name:t1                                       size:0.08M
   table_schema:db1              table_name:table_clubinfo                           size:0.06M
   table_schema:niuniu_db        table_name:accountinfo                              size:0.06M
   table_schema:niuniu_db        table_name:enterprise                               size:0.06M
   table_schema:niuniu_db        table_name:table_award_rebate_2019                  size:0.06M
   table_schema:niuniu_db        table_name:table_club_arrears                       size:0.06M
   table_schema:niuniu_db        table_name:table_club_hundred_free_charge           size:0.06M
   table_schema:niuniu_db        table_name:table_club_hundred_game_score            size:0.06M
   table_schema:niuniu_db        table_name:table_club_hundred_roominfo              size:0.06M
   table_schema:niuniu_db        table_name:table_clublogdiamond                     size:0.06M
   table_schema:niuniu_db        table_name:table_clublogfreescore                   size:0.06M
   table_schema:test_db          table_name:geek                                     size:0.06M
   table_schema:db1              table_name:_table_clubgamelog_new                   size:0.05M
   table_schema:db1              table_name:table_clubgamelog                        size:0.05M
   table_schema:mydjango_db      table_name:auth_group_permissions                   size:0.05M
   table_schema:mydjango_db      table_name:auth_user_groups                         size:0.05M
   table_schema:mydjango_db      table_name:auth_user_user_permissions               size:0.05M
   table_schema:mydjango_db      table_name:django_admin_log                         size:0.05M
   table_schema:mydjango_db      table_name:django_celery_results_taskresult         size:0.05M
   table_schema:niuniu_db        table_name:table_agentrec                           size:0.05M
   table_schema:niuniu_db        table_name:table_club_flow_data                     size:0.05M
   table_schema:niuniu_db        table_name:table_club_hundred_cc                    size:0.05M
   table_schema:niuniu_db        table_name:table_club_hundred_game_score_banker     size:0.05M
   table_schema:niuniu_db        table_name:table_club_member_exswitch_config        size:0.05M
   table_schema:niuniu_db        table_name:table_club_task_info                     size:0.05M
   table_schema:niuniu_db        table_name:table_club_task_log                      size:0.05M
   table_schema:niuniu_db        table_name:table_club_task_switch_config            size:0.05M
   table_schema:niuniu_db        table_name:table_clublogplatformtax                 size:0.05M
   table_schema:niuniu_db        table_name:table_diamond_not_enough                 size:0.05M
   table_schema:niuniu_db        table_name:table_goldactionlog                      size:0.05M
   table_schema:terrace_db       table_name:auth_group_permissions                   size:0.05M
   table_schema:terrace_db       table_name:auth_user_groups                         size:0.05M
   table_schema:terrace_db       table_name:auth_user_user_permissions               size:0.05M
   table_schema:terrace_db       table_name:django_admin_log                         size:0.05M
   table_schema:terrace_db       table_name:django_celery_results_taskresult         size:0.05M
   table_schema:terrace_db       table_name:myapp_db_name                            size:0.05M
   table_schema:terrace_db       table_name:mysql_slow_query_review_history          size:0.05M
   table_schema:terrace_db       table_name:tb_blacklist_user_permit                 size:0.05M
   table_schema:db1              table_name:t                                        size:0.03M
   table_schema:db1              table_name:table_numerical_param                    size:0.03M
   table_schema:mydjango_db      table_name:auth_group                               size:0.03M
   table_schema:mydjango_db      table_name:auth_permission                          size:0.03M
   table_schema:mydjango_db      table_name:auth_user                                size:0.03M
   table_schema:mydjango_db      table_name:django_content_type                      size:0.03M
   table_schema:mydjango_db      table_name:index_city                               size:0.03M
   table_schema:mydjango_db      table_name:index_person                             size:0.03M
   table_schema:mydjango_db      table_name:index_product                            size:0.03M
   table_schema:niuniu_db        table_name:t1                                       size:0.03M
   table_schema:niuniu_db        table_name:table_agentgameresult                    size:0.03M
   table_schema:niuniu_db        table_name:table_club_cc_code                       size:0.03M
   table_schema:niuniu_db        table_name:table_club_exten_config                  size:0.03M
   table_schema:niuniu_db        table_name:table_club_game_dudiamond_rate           size:0.03M
   table_schema:niuniu_db        table_name:table_club_hundred_cfg                   size:0.03M
   table_schema:niuniu_db        table_name:table_club_hundred_dudiamond_cfg         size:0.03M
   table_schema:niuniu_db        table_name:table_club_hundred_switch                size:0.03M
   table_schema:niuniu_db        table_name:table_club_info_notauthority             size:0.03M
   table_schema:niuniu_db        table_name:table_club_reboot_nscore_count           size:0.03M
   table_schema:niuniu_db        table_name:table_clublogdiamond_history             size:0.03M
   table_schema:niuniu_db        table_name:table_companyaudit                       size:0.03M
   table_schema:niuniu_db        table_name:table_diamondactionlog                   size:0.03M
   table_schema:niuniu_db        table_name:table_getrrwardlog                       size:0.03M
   table_schema:niuniu_db        table_name:table_goldrank                           size:0.03M
   table_schema:terrace_db       table_name:auth_group                               size:0.03M
   table_schema:terrace_db       table_name:auth_permission                          size:0.03M
   table_schema:terrace_db       table_name:auth_user                                size:0.03M
   table_schema:terrace_db       table_name:django_content_type                      size:0.03M
   table_schema:terrace_db       table_name:django_session                           size:0.03M
   table_schema:terrace_db       table_name:myapp_db_instance                        size:0.03M
   table_schema:terrace_db       table_name:mysql_slow_query_review                  size:0.03M
   table_schema:terrace_db       table_name:tb_blacklist                             size:0.03M
   table_schema:test_db          table_name:geek_index_structure                     size:0.03M
   table_schema:test_db          table_name:table_clubgamescoredetail                size:0.03M
   table_schema:db1              table_name:accountinfo                              size:0.02M
   table_schema:db1              table_name:t_detail                                 size:0.02M
   table_schema:db1              table_name:table_clublogscore                       size:0.02M
   table_schema:mydjango_db      table_name:django_migrations                        size:0.02M
   table_schema:mydjango_db      table_name:django_session                           size:0.02M
   table_schema:mydjango_db      table_name:index_province                           size:0.02M
   table_schema:mydjango_db      table_name:index_type                               size:0.02M
   table_schema:niuniu_db        table_name:accountinrole                            size:0.02M
   table_schema:niuniu_db        table_name:accountorroleinrule                      size:0.02M
   table_schema:niuniu_db        table_name:effectivenumber_daylog                   size:0.02M
   table_schema:niuniu_db        table_name:enterpricemanage                         size:0.02M
   table_schema:niuniu_db        table_name:roleinfo                                 size:0.02M
   table_schema:niuniu_db        table_name:ruleinfo                                 size:0.02M
   table_schema:niuniu_db        table_name:systemlog                                size:0.02M
   table_schema:niuniu_db        table_name:table_game_score                         size:0.02M
   table_schema:niuniu_db        table_name:table_gameid                             size:0.02M
   table_schema:terrace_db       table_name:django_migrations                        size:0.02M
   table_schema:terrace_db       table_name:myapp_oper_log                           size:0.02M
   table_schema:terrace_db       table_name:myapp_permission                         size:0.02M
   table_schema:test_db          table_name:t                                        size:0.02M
1.3 数据量排名前靠前的大表:
   table_schema:niuniu_db        table_name:table_lhd_players                        all_size:1089.50M        data_size:768.00M         index_size:321.50M         table_rows:10705699
   table_schema:niuniu_db        table_name:table_club_hundred_log_charge            all_size:707.70M         data_size:579.00M         index_size:128.70M         table_rows:5259408
   table_schema:niuniu_db        table_name:table_clubgamescoredetail_history        all_size:420.47M         data_size:376.89M         index_size:43.58M          table_rows:1643639
   table_schema:niuniu_db        table_name:table_clublogscore_history               all_size:159.20M         data_size:137.66M         index_size:21.55M          table_rows:1610400
   table_schema:niuniu_db        table_name:table_clubgameuserscoredetail            all_size:91.64M          data_size:60.58M          index_size:31.06M          table_rows:867104
   table_schema:niuniu_db        table_name:table_bet_inout                          all_size:83.64M          data_size:55.58M          index_size:28.06M          table_rows:640378
   table_schema:niuniu_db        table_name:table_clublogplatformscore_history       all_size:83.11M          data_size:71.59M          index_size:11.52M          table_rows:817169
   table_schema:test_db          table_name:t2                                       all_size:63.66M          data_size:32.56M          index_size:31.09M          table_rows:998222
   table_schema:db1              table_name:t1                                       all_size:45.08M          data_size:31.56M          index_size:13.52M          table_rows:622544
   table_schema:db1              table_name:t2                                       all_size:45.08M          data_size:32.56M          index_size:12.52M          table_rows:588259
   table_schema:niuniu_db        table_name:table_club_log_dudiamond                 all_size:42.09M          data_size:19.55M          index_size:22.55M          table_rows:405544
   table_schema:niuniu_db        table_name:table_club_hundred_log_dudiamond         all_size:18.58M          data_size:8.52M           index_size:10.06M          table_rows:154715
   table_schema:niuniu_db        table_name:table_clubgamescore                      all_size:12.58M          data_size:6.52M           index_size:6.06M           table_rows:55979
   table_schema:niuniu_db        table_name:table_user                               all_size:7.73M           data_size:3.52M           index_size:4.22M           table_rows:19213
   table_schema:niuniu_db        table_name:table_club_reboot_nscore_count2          all_size:7.06M           data_size:2.52M           index_size:4.55M           table_rows:43473
   table_schema:niuniu_db        table_name:table_clubmember                         all_size:4.89M           data_size:2.52M           index_size:2.38M           table_rows:19805
   table_schema:niuniu_db        table_name:table_club_task_member_data              all_size:1.77M           data_size:1.52M           index_size:0.25M           table_rows: 4535
   table_schema:niuniu_db        table_name:enterpriselog                            all_size:1.67M           data_size:1.52M           index_size:0.16M           table_rows: 5926
   table_schema:niuniu_db        table_name:operationslog                            all_size:1.52M           data_size:1.52M           index_size:0.00M           table_rows: 3666
   table_schema:niuniu_db        table_name:table_clubloggold                        all_size:0.77M           data_size:0.31M           index_size:0.45M           table_rows: 3381
1.4 单表超过行数 20000000 表:
   ###没有单表超过行数 20000000 表###
1.5 自增ID占比大于 10.01% 的表 :
   ###没有自增ID占比大于 10.01% 的表###
1.6 碎片大于多少 1e-06G 的表 :
     table_schema:niuniu_db        table_name:table_club_hundred_log_charge            fragment:363.00M   
     table_schema:db1              table_name:t2                                       fragment:206.00M   
     table_schema:db1              table_name:t1                                       fragment:189.00M   
     table_schema:niuniu_db        table_name:table_clubgamescoredetail_history        fragment:7.00M     
     table_schema:niuniu_db        table_name:table_club_log_dudiamond                 fragment:6.00M     
     table_schema:niuniu_db        table_name:table_lhd_players                        fragment:6.00M     
     table_schema:niuniu_db        table_name:table_bet_inout                          fragment:5.00M     
     table_schema:niuniu_db        table_name:table_clublogplatformscore_history       fragment:5.00M     
     table_schema:test_db          table_name:t2                                       fragment:5.00M     
     table_schema:niuniu_db        table_name:enterpriselog                            fragment:4.00M     
     table_schema:niuniu_db        table_name:operationslog                            fragment:4.00M     
     table_schema:niuniu_db        table_name:table_club_hundred_log_dudiamond         fragment:4.00M     
     table_schema:niuniu_db        table_name:table_club_reboot_nscore_count2          fragment:4.00M     
     table_schema:niuniu_db        table_name:table_club_task_member_data              fragment:4.00M     
     table_schema:niuniu_db        table_name:table_clubgamescore                      fragment:4.00M     
     table_schema:niuniu_db        table_name:table_clubgameuserscoredetail            fragment:4.00M     
     table_schema:niuniu_db        table_name:table_clublogscore_history               fragment:4.00M     
     table_schema:niuniu_db        table_name:table_clubmember                         fragment:4.00M     
     table_schema:niuniu_db        table_name:table_user                               fragment:4.00M     
1.7 统计大字段表:
    table_schema:db1              engine:_table_clubgamelog_new         engine_counts:LogData         
    table_schema:db1              engine:_table_clubgamelog_new         engine_counts:CardData        
    table_schema:db1              engine:table_clubgamelog              engine_counts:LogData         
    table_schema:db1              engine:table_clubgamelog              engine_counts:CardData        
    table_schema:db1              engine:table_clubgamescoredetail      engine_counts:szExtChar       
    table_schema:niuniu_db        engine:table_club_task_member_data    engine_counts:TaskDay         
    table_schema:niuniu_db        engine:table_club_task_member_data    engine_counts:TaskTime        
1.8 统计字段类型varchar长度大于 500 的表:
    table_schema:db1             table_name:accountinfo                              column_name:Ip                   data_type:varchar              CHARACTER_MAXIMUM_LENGTH:512
    table_schema:niuniu_db       table_name:accountinfo                              column_name:Ip                   data_type:varchar              CHARACTER_MAXIMUM_LENGTH:512
    table_schema:niuniu_db       table_name:enterprise                               column_name:EnterSignature       data_type:varchar              CHARACTER_MAXIMUM_LENGTH:512
    table_schema:niuniu_db       table_name:enterprise                               column_name:Address              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:512
    table_schema:niuniu_db       table_name:enterprise                               column_name:Remark               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:1000
    table_schema:niuniu_db       table_name:roleinfo                                 column_name:Describe             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:2000
    table_schema:niuniu_db       table_name:ruleinfo                                 column_name:Describe             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:2000
    table_schema:niuniu_db       table_name:systemlog                                column_name:Msg                  data_type:varchar              CHARACTER_MAXIMUM_LENGTH:2000
    table_schema:niuniu_db       table_name:systemlog                                column_name:Logger               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:1024
    table_schema:niuniu_db       table_name:table_goldrank                           column_name:szHeadPicUrl         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:1000
    table_schema:niuniu_db       table_name:table_goldrank                           column_name:szSign               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:1000
    table_schema:niuniu_db       table_name:table_user                               column_name:szHeadPicUrl         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:512
2.索引巡检项:
2.1 获取索引数目大于 5 个的表:
