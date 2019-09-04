import subprocess


if __name__ == '__main__':
    try:
        subprocess.call("pip install PyMySQL-0.9.3-py2.py3-none-any.whl")
    except Exception as e:
        print("安装模块错误！"+e)

    import pymysql

    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='karst',
        charset='utf8'
    )
    cursor = connect.cursor()
    file = open("C:\\Users\\john\\Desktop\\src_btm.sql",encoding="GB2312",errors="ignore")
    count = 0

    for i in range(80):
        file.readline()

    while 1:
        sqls = file.readline()
        count += 1
        
        if sqls.split() == "":
            for i in range(10):
                sqls += file.readline()
                count += 1
            # print(sqls)
            try:
                cursor.execute(sqls)
            except Exception as s:
                print(s)
                connect.rollback()
            else:
                connect.commit()
                print(sqls)
                print("已处理 %s 条" % count)
        else:
            print("ok!!!!")
            print("共处理 %s 条！！" % count)
            break



