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

覆盖数据
```shell
--hive-overwrite 
```

自定义hive field terminated
```shell
--fields-terminated-by '\001' \
```

# hive to mysql

【根据hive建mysql表】

由于sqoop的hive to mysql不支持自动创建mysql表，这里补充hivetomysql.py根据hive生成mysql表，先建表之后再使用sqoop进行导入
根据hive表字段的类型和mysql类型对比，得到如下对应关系，根据此对应进行mysql表创建时的类型转换（可能不全，可以根究需要在脚本的elif中添加即可）

```shell
【hive】                【mysql】
bigint                  BIGINT(20)
int                     INT(11) 
double                  DOUBLE
tinyint                 TINYINT(4)
smallint                SMALLINT(6)
date                    DATE
timestamp               TIMESTAMP NULL
decimal(n1,n2)          decimal(n1,n2)
other                   LONGTEXT
```
符上mysql各字段类型建表语句：
```shell
DROP TABLE IF EXISTS `sqoop_test`;
CREATE TABLE `sqoop_test` (
  `bigint_test` bigint(20) DEFAULT NULL,
  `bit_test` bit(1) DEFAULT NULL,
  `char_test` char(0) DEFAULT NULL,
  `date_test` date DEFAULT NULL,
  `datetime_test` datetime DEFAULT NULL,
  `decimal_test` decimal(10,0) DEFAULT NULL,
  `double_test` double DEFAULT NULL,
  `enum_test` enum('0','1','2','3') NOT NULL DEFAULT '0',
  `float_test` float DEFAULT NULL,
  `int_test` int(11) DEFAULT NULL,
  `integer_test` int(11) DEFAULT NULL,
  `json_test` json DEFAULT NULL,
  `longtext_test` longtext,
  `mediumint_test` mediumint(9) DEFAULT NULL,
  `mediumtext_test` mediumtext,
  `numeric_test` decimal(10,0) DEFAULT NULL,
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

SET FOREIGN_KEY_CHECKS = 1;
```

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
--username root \
--password root123 \
--table customer  \
--hcatalog-database tpch_flat_orc_10  \
--hcatalog-table customer \
--driver com.mysql.jdbc.Driver 
```

# 测试
用hive to mysql建表脚本配合sqoop的hive to mysql
测试了tpch和learnkylin的几张表hive to mysql后，mysql数据和hive的一致。
