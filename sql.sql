SELECT
	`myapp_db_name`.`id`,
	`myapp_db_name`.`dbtag`,
	`myapp_db_name`.`dbname`
FROM
	`myapp_db_name`
INNER JOIN `myapp_db_name_instance` ON (
	`myapp_db_name`.`id` = `myapp_db_name_instance`.`db_name_id`
)
WHERE
	`myapp_db_name_instance`.`db_instance_id` = 1;

SELECT
	`myapp_db_account`.`id`,
	`myapp_db_account`.`user`,
	`myapp_db_account`.`passwd`,
	`myapp_db_account`.`role`,
	`myapp_db_account`.`tags`
FROM
	`myapp_db_account`
INNER JOIN `myapp_db_account_dbname` ON (
	`myapp_db_account`.`id` = `myapp_db_account_dbname`.`db_account_id`
)
WHERE
	`myapp_db_account_dbname`.`db_name_id` = 1;



SELECT
	`myapp_db_account`.`id`,
	`myapp_db_account`.`user`,
	`myapp_db_account`.`passwd`,
	`myapp_db_account`.`role`,
	`myapp_db_account`.`tags`
FROM
	`myapp_db_name`
INNER JOIN `myapp_db_name_instance` ON (
	`myapp_db_name`.`id` = `myapp_db_name_instance`.`db_name_id`
)
INNER JOIN `myapp_db_account_dbname` ON (
	`myapp_db_account_dbname`.`db_name_id` = `myapp_db_name_instance`.`db_name_id`
)
INNER JOIN `myapp_db_account` ON (
	`myapp_db_account`.`id` =  `myapp_db_account_dbname`.`db_account_id`
)

WHERE
	`myapp_db_name_instance`.`db_instance_id` = 1;


p_res = Db_name.objects.filter(instance__id=1)

SELECT `myapp_db_name`.`id`, `myapp_db_name`.`dbtag`, `myapp_db_name`.`d
bname` FROM `myapp_db_name` INNER JOIN `myapp_db_name_instance` ON (`myapp_db_na
me`.`id` = `myapp_db_name_instance`.`db_name_id`) WHERE `myapp_db_name_instance`
.`db_instance_id` = 1 LIMIT 21;

# <QuerySet [<Db_name: terrace_db terrace_db>]>


p_res = Db_name.objects.select_related('instance').filter(instance__id=1)


