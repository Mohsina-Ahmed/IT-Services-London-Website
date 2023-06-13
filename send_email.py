import smtplib
my_gmail = "mohsinaahmedchowdhury@gmail.com"
password = "vwsxmhhsfyvieiov"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()#make connection secure
connection.login(user=my_gmail, password=password)
connection.sendmail(from_addr=my_gmail, to_addrs=my_gmail, msg="Hello World!")