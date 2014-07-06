import ConfigParser
import os
import sys

def strToArray(line):
    arr = []
    for value in line.split(','):
        arr.append(value)
    return arr

def get_mail_conf(section, option):
    script_home = sys.path[0]
    config_path = os.path.join(script_home, "config/mail.conf")
    cf = ConfigParser.ConfigParser()
    cf.read(config_path)
    opt = cf.get(section, option)
    if opt:
        return opt
    else:
        return ""

def get_smtp_server():
    default_smtp_server = 'smtp.163.com'
    smtp_server = get_mail_conf('mail', 'smtp_server') 
    if smtp_server == "":
        return default_smtp_server
    else:
        return smtp_server

def get_sent_user():
    default_sent_user = 'hscavenger@163.com'
    sent_user = get_mail_conf('mail', 'sent_user') 
    if sent_user == "":
        return default_sent_user
    else:
        return sent_user

def get_sent_password():
    default_sent_password = 'scavenger'
    sent_password = get_mail_conf('mail', 'sent_password') 
    if sent_password == "":
        return default_sent_password
    else:
        return sent_password

def get_mail_to():
    default_mail_to = ['wangjiankui1989@163.com']
    mail_to = get_mail_conf('mail', 'mail_to') 
    if mail_to == "":
        return default_mail_to
    else:
        return strToArray(mail_to)

if __name__ == '__main__':
    print strToArray('wangjiankui1989@163.com')
    print get_mail_to()
