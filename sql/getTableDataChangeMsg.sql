/*
describe: get table data change message by table name and database name
author: cg
create time: 2018-06-12
*/

SELECT
	TABLE_NAME AS tableName,
	IFNULL(CREATE_TIME, '') AS createTime,
	IFNULL(UPDATE_TIME, '') AS updateTime,
	TABLE_COLLATION AS tableCollation,
	IFNULL(TABLE_ROWS, '') AS dataRowsNum
FROM
	information_schema.`TABLES`
WHERE
	TABLE_SCHEMA = %s
AND TABLE_NAME = %s