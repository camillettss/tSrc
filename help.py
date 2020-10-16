import tkinter as tk
import webbrowser
import json
import subprocess
import smtplib, ssl
from string import Template
import tkinter.font as font

_basepath='C:/tSrc/data'

classdata=json.loads(open(_basepath+'/data.json').read()) #class_name and position

MY_ADDRESS = 'liceogalielicvv1@gmail.com'
PASSWORD = 'gal1le0gal1le1'
_isShowed=False

#read data files
def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# funcs
def sendmail(fn='message'):
    port=587
    smtp_server='smtp.gmail.com'
    sender_email=MY_ADDRESS
    receiver_email=''
    msg_template = read_template(_basepath+'/'+fn+'.txt')
    if fn=='message':
            message=msg_template.substitute(CLASS_NAME=classdata['classname'], CLASS_LOC=classdata['loc'])
    elif fn=='ADMIN':
        message=msg_template.substitute(CLASS_NAME=classdata['classname'], DATA=shdata(), CLASS_LOC=classdata['loc'])
    context=ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(MY_ADDRESS, PASSWORD)
        print(message)
        for email in get_contacts(_basepath+'/contacts.txt'):
            server.sendmail(sender_email, email, message)

def shdata():
    tastks=subprocess.run(['tasklist'], stdout=subprocess.PIPE)
    return str(tastks)

def check():
    x=input('password: ')
    if not x == '50m3d4y5':
        print('[!!] Invalid password')
    else:
        sendmail('ADMIN')

#graphic side
root=tk.Tk()
root.title('Designed developed and installed by Francesco Camilletti :)')
frame=tk.Frame(root)
frame.pack()

btn_ask=tk.Button(frame, text='avvisa un tecnico', width=25, height=10, bg='#0052cc', fg='#ffffff', command=sendmail)
btn_ask['font']=font.Font(size=30)
btn_ask.pack(side=tk.LEFT)

btn_shdata=tk.Button(frame, text='share system data', width=25, height=10, bg='red', fg='#ffffff', command=check)#lambda: sendmail('ADMIN'))
btn_shdata['font']=font.Font(size=30)
btn_shdata.pack(side=tk.LEFT)

root.mainloop()
