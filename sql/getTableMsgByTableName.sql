/*
describe: get table msg by table name and databse name
author: cg
create time: 2018-06-12
*/


SELECT
	COLUMN_NAME AS columnName,
	IS_NULLABLE AS isNull,
	COLUMN_TYPE AS columnType,

IF (COLUMN_KEY = 'PRI', 'YES', '') AS isKey,
 IFNULL(COLUMN_COMMENT, '') AS columnComment
FROM
	information_schema.`COLUMNS`
WHERE
	TABLE_SCHEMA = %s
AND TABLE_NAME = %s