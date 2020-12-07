
import smtplib
import poplib
import imaplib
import getpass


def get_qq_mail():
    pass
    serv = 'pop.163.com'
    uname = '18625500030'
    passwd = 'JHHXTSQMDFXKWXIB'
    return {"serv":serv, "uname":uname, "passwd":passwd}


if __name__=="__main__":
    pass
    p=get_qq_mail()
    # print(p)
    # print(type(p))
    email_obj = poplib.POP3_SSL(p["serv"])
    print(email_obj.getwelcome(),'\n')
    
    email_obj.user(p["uname"])
    email_obj.pass_(p["passwd"])
    email_stat = email_obj.stat()
    NumofMsgs = email_stat[0]
    
    print(type(email_obj))
    
    print(email_stat, 111)
    print(NumofMsgs, 222)
    
    # 逐行输出邮件内容
    for i in range(NumofMsgs):
       for mail in email_obj.retr(i+1)[1]:
           print(bytes.decode(mail))
       print('-'*50)

