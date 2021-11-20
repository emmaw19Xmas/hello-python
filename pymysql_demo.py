# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/20/2021 11:20 AM
# @Function:

import pymysql
# def pymysql_demo():
#     # 1. 打开连接
#     conn = pymysql.connect(host='127.0.0.1',
#                            user='root',
#                            password='123456',
#                            database='classicmodels',
#                            charset="utf8mb4")
#     # 2.获取游标
#     cursor = conn.cursor()
#
#     # 3. 执行sql
#     cursor.execute("SELECT VERSION();")
#
#     # 4. 获取结果
#     version = cursor.fetchone()
#     print(version)
#     # 5. 关闭连接
#     conn.close()
#
# # pymysql_demo()


def test_create():
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='123456',
                           database='classicmodels',
                           charset="utf8mb4")  # 获取连接
    cursor = conn.cursor()  # 获取游标

    sql = """
    CREATE TABLE `testcase` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `title` varchar(255) COLLATE utf8_bin NOT NULL,
    `expect` varchar(255) COLLATE utf8_bin NOT NULL,
    `owner` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
    """
    cursor.execute(sql)  # 执行SQL
    conn.close()  # 关闭连接

