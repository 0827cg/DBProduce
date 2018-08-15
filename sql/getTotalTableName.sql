/*
describe: get total table name from database
author: cg
create time: 2018-06-12
*/

SELECT
	TABLE_NAME AS tableName
FROM
	information_schema.`TABLES`
WHERE
	TABLE_SCHEMA = %s