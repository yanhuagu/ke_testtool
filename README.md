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
【hive】       【mysql】
bigint       BIGINT(20)
int          INT(11) 
double       DOUBLE
tinyint      TINYINT(4)
smallint     SMALLINT(6)
date         DATE
other        LONGTEXT
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


--driver com.mysql.jdbc.Driver 
--driver com.mysql.jdbc.Driver 
