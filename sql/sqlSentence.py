#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-22
# update time: 2018-08-15


class SqlSentence:

    # 因为使用pyinstaller打包到时候, 不会将.sql文件打包进入exe, 所以就有了这个文件
    # 将sql语句写入到代码中, 这样打包之后就可以直接执行查询

    strDatabaseNameSql = "  SELECT" \
                         "      `SCHEMA_NAME` AS databaseName" \
                         "  FROM" \
                         "      `information_schema`.`SCHEMATA`"


    strTableDataChangeMsgSql = "    SELECT" \
                               "        TABLE_NAME AS tableName," \
                               "        IFNULL(CREATE_TIME, '') AS createTime," \
                               "        IFNULL(UPDATE_TIME, '') AS updateTime," \
                               "        TABLE_COLLATION AS tableCollation," \
                               "        IFNULL(TABLE_ROWS, '') AS dataRowsNum" \
                               "    FROM" \
                               "        information_schema.`TABLES`" \
                               "    WHERE" \
                               "        TABLE_SCHEMA = %s" \
                               "    AND TABLE_NAME = %s"

    strTableMsgByTableName = "   SELECT" \
                            "       COLUMN_NAME AS columnName," \
                            "       IS_NULLABLE AS isNull," \
                            "       COLUMN_TYPE AS columnType," \
                            "       IF (COLUMN_KEY = 'PRI', 'YES', '') AS isKey," \
                            "       IFNULL(COLUMN_COMMENT, '') AS columnComment" \
                            "   FROM" \
                            "       information_schema.`COLUMNS`" \
                            "   WHERE" \
                            "       TABLE_SCHEMA = %s" \
                            "   AND TABLE_NAME = %s"

    strTotalTableName = "   SELECT" \
                        "       TABLE_NAME AS tableName" \
                        "   FROM" \
                        "       information_schema.`TABLES`" \
                        "   WHERE" \
                        "       TABLE_SCHEMA = %s"