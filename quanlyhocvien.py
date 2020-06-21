import pyodbc
serverInfo = 'DESKTOP-27PHD9R'
databasename = 'quanlysanpham1'
username = 'hoangdangngo'
password = '123456'
driver = '{SQL Server}'
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+serverInfo+';DATABASE='+databasename+';Trusted_Connection=yes;')
pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+serverInfo+';DATABASE='+databasename+';UID='+username+';PWD='+ password)
cursor = connection.cursor()
HOC_VIEN = "CREATE TABLE HOC_VIEN (MESSAGES_HEADER VARCHAR(20), DATE VARCHAR(20), MA_HOC_VIEN VARCHAR(10), TEN_HOC_VIEN NVARCHAR(100),LOP NVARCHAR(100), EMAIL VARCHAR(100), SO_DIEN_THOAI VARCHAR(11))"
cursor.execute(HOC_VIEN)
cursor.commit()
try:
    f = open("d:/python/hoc_vien1.txt")
    listHV = f.readlines()
    print(listHV)
    #Header
    a=listHV[0].split(":")
    header = (a[1]).replace("\n","")
    print((header))
    #date
    b=listHV[1].split(":")
    date = (b[1]).replace("\n","")
    print(date)
    #maHV
    c=listHV[2].split(":")
    maHV = (c[1]).replace("\n","")
    print(maHV)
    #tenHV
    d=listHV[3].split(":")
    tenHV = (d[1]).replace("\n","")
    print(tenHV)
    #lopHV
    e=listHV[4].split(":")
    lopHV = (e[1]).replace("\n","")
    print(lopHV)
    #Email
    f=listHV[5].split(":")
    email = (f[1]).replace("\n","")
    print(email)
    #sdt
    g=listHV[6].split(":")
    sdt = (g[1]).replace("\n","")
    print(sdt)


except FileNotFoundError :
    print("duong dan khong ton tai")
cursor.execute("insert into HOC_VIEN VALUES(?,?,?,?,?,?,?)", (str(header),str(date),str(maHV),str(tenHV),str(lopHV),str(email),str(sdt)))
cursor.commit()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "ngohoang05071985@gmail.com"
toaddr = "tbtoanit@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Chuong trinh quan ly hoc vien"
file = open("d:/python/hoc_vien1.txt")
msg1 = MIMEText(file.read())
msg.attach(msg1)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "ngohoang05071985")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
