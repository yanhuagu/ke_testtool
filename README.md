# mysql to hive
sqoop import支持mysql的表数据导入到hive，其中包括自动根据mysql表创建hive表，同时会将hive和mysql column的差异进行自动转换
导入执行语句如下：
```shell
sqoop import   \
--connect jdbc:mysql://10.1.40.102:3306/longtest  \
--username root  \
--password root123 \
--table sqoop_test   \
--hive-table sqoop_test \
--hive-database testgu \
--hive-import \
--driver com.mysql.jdbc.Driver \
-m1
```
追加数据
```shell
上述语句
```
sqoop import --connect jdbc:mysql://192.168.56.104:3306/test?useSSL=false --username root --password 123456 --table t1 --hive-import --hive-table test.mysql_t1

覆盖数据
```shell
--hive-overwrite 
```

存在异常数据的时候
```shell
--fields-terminated-by '\001' \
```

# hive to mysql

【根据hive建mysql表】

hive to mysql不支持自动创建mysql表，可以用脚本hivetomysql.py根据hive生成mysql表先建表之后再进行导入

【导入数据方法1--将hdfs文件导入mysql】
```shell
sqoop export   \
--connect jdbc:mysql://10.1.2.50:3306/yanhuaok  \
--username root  \
--password root123 \
--table test_account   \
--export-dir hdfs://sandbox.hortonworks.com:8020/apps/hive/warehouse/test_account \
--driver com.mysql.jdbc.Driver 
```
【导入数据方法2--将hive表导入mysql】
```shell
sqoop export   \
--connect jdbc:mysql://10.1.40.102:3306/longtest \
--user name root \
--password root123 \
--table resulttest  \
--hcatalog-database testgu  \
--hcatalog-table resulttest \
--driver com.mysql.jdbc.Driver 
```

# 测试
1 创建一张mysql表sqoop_test，表存在所有的字段类型，如下：
```shell
DROP TABLE IF EXISTS `sqoop_test`;
CREATE TABLE `sqoop_test` (
  `bigint_test` bigint(20) DEFAULT NULL,
  `binary_test` binary(0) DEFAULT NULL,
  `bit_test` bit(1) DEFAULT NULL,
  `blob_test` blob,
  `char_test` char(0) DEFAULT NULL,
  `date_test` date DEFAULT NULL,
  `datetime_test` datetime DEFAULT NULL,
  `decimal_test` decimal(10,0) DEFAULT NULL,
  `double_test` double DEFAULT NULL,
  `enum_test` enum('0','1','2','3') NOT NULL DEFAULT '0',
  `float_test` float DEFAULT NULL,
  `geometry_test` geometry DEFAULT NULL,
  `geometrycollection_test` geometrycollection DEFAULT NULL,
  `int_test` int(11) DEFAULT NULL,
  `integer_test` int(11) DEFAULT NULL,
  `json_test` json DEFAULT NULL,
  `linestring_test` linestring DEFAULT NULL,
  `longblob_test` longblob,
  `longtext_test` longtext,
  `mediumblob_test` mediumblob,
  `mediumint_test` mediumint(9) DEFAULT NULL,
  `mediumtext_test` mediumtext,
  `multilinestring_test` multilinestring DEFAULT NULL,
  `multipoint_test` multipoint DEFAULT NULL,
  `multipolygon_test` multipolygon DEFAULT NULL,
  `numeric_test` decimal(10,0) DEFAULT NULL,
  `point_test` point DEFAULT NULL,
  `polygon_test` polygon DEFAULT NULL,
  `smallint_test` smallint(6) DEFAULT NULL,
  `text_test` text,
  `time_test` time DEFAULT NULL,
  `timestamp_test` timestamp NULL DEFAULT NULL,
  `tinyblob_test` tinyblob,
  `tinyint_test` tinyint(4) DEFAULT NULL,
  `tinytext_test` tinytext,
  `varbinary_test` varbinary(0) DEFAULT NULL,
  `varchar_test` varchar(0) DEFAULT NULL,
  `year_test` year(4) DEFAULT NULL
) ENGINE=ndbcluster DEFAULT CHARSET=latin1;
```
