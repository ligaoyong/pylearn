
if __name__ == '__main__':
    file = open("C:\\Users\\john\\Desktop\\src_btm.sql",encoding="GB2312",errors="ignore")  # sql文件位置
    out_path = "C:\\Users\\john\\Desktop\\aa"  # 切割后的文件存放位置 文件夹
    suf = 1
    rows = 0
    while 1:
        max_rows = 500  # 5000
        newStr = file.readline()
        if newStr:
            out_file = open(out_path + "\\src_btm_%s.sql" % suf, "a+",encoding="UTF-8")
            out_file.write(newStr)
            while max_rows > 0:
                str = file.readline()
                for i in range(10):
                    str += file.readline()
                    max_rows -= 1
                    rows += 1
                out_file.write(str)
                print("大约完成%s行" % rows)
        else:
            break
        suf += 1