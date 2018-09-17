# -*- coding: UTF-8 -*-

import pyhs2

def mysql_table_sql(hivehost,database,tablename):

    mysql_sql_head = '''
    CREATE TABLE `{0}` (
    '''.format(tablename)+'\n'

    mysql_sql_tail = '''
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1
    '''+'\n'

    mysql_sql_columns = ''

    h_hivehost = hivehost
    h_port = 10000
    h_user = 'user'
    h_password = 'password'
    h_database = database
    h_table = tablename

    try:
        with pyhs2.connect(host=h_hivehost,
                           port=h_port,
                           authMechanism="PLAIN",
                           user=h_user,
                           password=h_password,
                           database=h_database) as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("desc " + h_table)
                    for i in cur.fetch():
                        if i[1] in ["bigint"]:
                            mysql_sql_columns = mysql_sql_columns+"`{0}` BIGINT(20) DEFAULT NULL,".format(i[0])+'\n'
                        elif i[1] in ["int"]:
                            mysql_sql_columns = mysql_sql_columns+"`{0}` INT(11) DEFAULT NULL,".format(i[0])+'\n'
                        elif i[1] in ["smallint"]:
                            mysql_sql_columns = mysql_sql_columns + "`{0}` SMALLINT(6) DEFAULT NULL,".format(i[0]) + '\n'
                        elif i[1] in ["double"]:
                            mysql_sql_columns = mysql_sql_columns+"`{0}` DOUBLE DEFAULT NULL,".format(i[0])+'\n'
                        elif i[1] in ["tinyint"]:
                            mysql_sql_columns = mysql_sql_columns + "`{0}` TINYINT(4) DEFAULT NULL,".format(i[0]) + '\n'
                        elif i[1] in ["date"]:
                            mysql_sql_columns = mysql_sql_columns + "`{0}` DATE DEFAULT NULL,".format(i[0]) + '\n'
                        elif i[1] in ["timestamp"]:
                            mysql_sql_columns = mysql_sql_columns + "`{0}` TIMESTAMP NULL DEFAULT NULL,".format(i[0]) + '\n'
                        else :
                            mysql_sql_columns = mysql_sql_columns+"`{0}` LONGTEXT,".format(i[0])+'\n'
            except Exception as e:
                print(e)

    finally:
        pass

    mysql_sql = mysql_sql_head+mysql_sql_columns[:-2]+mysql_sql_tail
    return mysql_sql

print mysql_table_sql('10.1.2.108','default','test_order')
