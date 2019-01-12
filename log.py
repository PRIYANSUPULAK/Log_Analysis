#! /usr/bin/env python3

import psycopg2

DBNAME = "news"

# 1. What are the most popular three articles of all time?


def query1():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "select title,views from article_views limit 3"
    c.execute(query)
    results = c.fetchall()
    print("Three most popular articles of all time are following:\n")
    for i in range(0, 3):
        print((str(results[i][0])+"---"+str(results[i][1])+" views"))
    print('\n')
    db.close()

# 2. Who are the most popular article authors of all time?


def query2():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """select authors.name, sum(article_views.views)
     as views from authors join article_views
     on authors.id=article_views.author
     group by authors.name order by views desc"""
    c.execute(query)
    results = c.fetchall()
    print("The most popular article authors of all time are:\n")
    for i in range(0, len(results)):
        print((str(results[i][0])+"---"+str(results[i][1])+" views"))
    print('\n')
    db.close()

# 3.On which days did more than 1% of requests lead to errors?


def query3():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "select * from errors_view where error_percent > 1"
    c.execute(query)
    results = c.fetchall()
    print("All days with more than 1% of requests leading to errors are:\n")
    for i in range(0, len(results)):
        print((str(results[i][0])+"---"+str(results[i][1])+"% errors"))
    db.close()


if __name__ == '__main__':
    query1()
    query2()
    query3()
