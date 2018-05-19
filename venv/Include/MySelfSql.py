import pymysql


def fetchData():
    db = pymysql.connect("localhost", "root", "nanjing1227!", "film", charset='utf8')
    cursor = db.cursor()
    cursor.execute("select * from film")
    data = cursor.fetchall()
    print(data)


def fetchData(name):
    db = pymysql.connect("localhost", "root", "nanjing1227!", name, charset='utf8')
    cursor = db.cursor()
    cursor.execute("select * from store.mt_zl")
    data = cursor.fetchall()
    print(data)


def insertData(datas):
    if len(datas) == 0:
        print("datas is empty")
        return
    db = pymysql.connect("localhost", "root", "nanjing1227!", "store", charset='utf8')
    cursor = db.cursor()
    for data in datas:
        list = data.split("|")
        print(list)
        sql = "insert into mt_zl(name, score, score_num, site, site_) values ('%s', '%s', '%d', '%s','%s')" % (
        list[0], list[1], int(list[2]), list[3], list[4])
        print(sql)
        cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
