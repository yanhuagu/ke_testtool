# mysql to hive
sqoop import支持mysql的表数据导入到hive，其中包括自动根据mysql表创建hive表，同时会将hive和mysql column的差异进行自动转换
导入执行语句如下：
```shell
sqoop import   \
--connect jdbc:mysql://10.1.40.102:3306/longtest  \
--username root  \
--password root123 \
--table resulttest   \
--hive-table resulttesttest \
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
hive to mysql不支持自动创建mysql表，可以用脚本hivetomysql.py根据hive生成mysql表先建表之后再进行导入

【方法1--将hdfs文件导入mysql】
```shell
sqoop export   \
--connect jdbc:mysql://10.1.2.50:3306/yanhuaok  \
--username root  \
--password root123 \
--table test_account   \
--export-dir hdfs://sandbox.hortonworks.com:8020/apps/hive/warehouse/test_account \
--driver com.mysql.jdbc.Driver 
```
【方法2--将hive表导入mysql】
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
