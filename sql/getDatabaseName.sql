/*
describe: get total database name
author: cg
create time: 2018-08-09
*/


SELECT
	`SCHEMA_NAME` AS databaseName
FROM
	`information_schema`.`SCHEMATA`