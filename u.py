from tkinter import *
import datetime
import time
from tkinter import filedialog

def gettime():
    global timestr
    timestr = time.strftime('%Y%m%d.%H%M%S',time.localtime(time.time()))
    lb1 = Label(root, text='系统时间：'+ timestr)
    lb1.place(relx=0.05, rely=0, relwidth=0.3, relheight=0.08)

def anys(str1):
    j = 0
    k = 0
    for i in str1:
        k = k + 1
        if (i == '/'):
            j = k
    return str1[j:]

def comit(timestr):
    filenum = CheckVar1.get() + CheckVar2.get() + CheckVar3.get() + CheckVar4.get() + CheckVar5.get()
    f = open('test.ini', 'w')
    fnum = 1
    f.write("BEGIN SNOLT\n[USB CONFIG]\n")
    f.write("SN=" + timestr+'\n')
    f.write("[DEVICE DESCRIPTION]\nESN=DEFAULT\nMAC=DEFAULT\n[UPGRADE INFO]\nDIRECTORY=/upgrade\n")
    f.write("FILENUM="+str(filenum)+'\n')

    str1 = inp1.get()
    str1 = anys(str1)
    str2 = inp4.get()
    str2 = anys(str2)
    str3 = inp7.get()
    str3 = anys(str3)
    str4 = inp9.get()
    str4 = anys(str4)
    str5 = inp11.get()
    str5 = anys(str5)

    if(CheckVar1.get() == 1):
        f.write("TPYE"+str(fnum)+'='+'SYSTEM-SOFTWARE\n')
        f.write("FILENAME" +str(fnum) + '=' + str1 + '\n')
        f.write("FILE_MD5SUM" +str(fnum)+ '=' + inp2.get() + '\n')
        fnum = fnum + 1
    if (CheckVar2.get() == 1):
        f.write("TPYE" + str(fnum) + '=' + 'SDK-SOFTWARE\n')
        f.write("FILENAME" + str(fnum) + '=' + str2 + '\n')
        f.write("FILE_MD5SUM" + str(fnum) + '=' + inp5.get() + '\n')
        fnum = fnum + 1
    if (CheckVar3.get() == 1):
        f.write("TPYE" + str(fnum) + '=' + 'SNMPD-CONFIG\n')
        f.write("FILENAME" + str(fnum) + '=' + str3 + '\n')
        f.write("FILE_MD5SUM" + str(fnum) + '=' + inp8.get() + '\n')
        fnum = fnum + 1
    if (CheckVar4.get() == 1):
        f.write("TPYE" + str(fnum) + '=' + 'SYSTEM-CONFIG\n')
        f.write("FILENAME" + str(fnum) + '=' + str4 + '\n')
        f.write("FILE_MD5SUM" + str(fnum) + '=' + inp10.get() + '\n')
        fnum = fnum + 1
    if (CheckVar5.get() == 1):
        f.write("TPYE" + str(fnum) + '=' + 'STARTUP-CONFIG\n')
        f.write("FILENAME" + str(fnum) + '=' + str5 + '\n')
        f.write("FILE_MD5SUM" + str(fnum) + '=' + inp12.get() + '\n')
        fnum = fnum + 1
    if (CheckVar1.get() == 1):
        f.write("SYSTEM_VERSION" + '=' + inp3.get() + '\n')
    if (CheckVar2.get() == 1):
        f.write("SDK_VERSION" + '=' + inp6.get() + '\n')
    f.write("END SNOLT")
    f.close()

def run():
    if (CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 0 and CheckVar4.get() == 0 and CheckVar5.get() == 0):
        s = '您还没选择任何升级项目'
    else:
        s1 = "系统软件" if CheckVar1.get() == 1 else ""
        s2 = "SDK软件" if CheckVar2.get() == 1 else ""
        s3 = "SNMPD-CONFIG文件" if CheckVar3.get() == 1 else ""
        s4 = "SYSTEM-CONFIG文件" if CheckVar4.get() == 1 else ""
        s5 = "STARTUP-CONFIG文件" if CheckVar5.get() == 1 else ""
        s = "您选择了%s %s %s %s %s" % (s1, s2, s3, s4, s5)
    lb2.config(text=s)

def get_path(entry_text):
    path = filedialog.askopenfilename(title='请选择文件')
    entry_text.set(path)

def get_md5(entry_text):
    path = filedialog.askopenfilename(title='请选择文件')
    file_text = '111'
    if path is not None:
        with open(file=path, mode='r+', encoding='utf-8') as file:
            file_text = file.read()
    entry_text.set(file_text)

root=Tk()
root.title('U盘开局索引文件制作工具')
root.geometry('800x800')
lb1=Label(root,text='请选择您的升级项目')
lb1.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()

ch1 = Checkbutton(root,text='系统软件',variable = CheckVar1,onvalue=1,offvalue=0)
ch2 = Checkbutton(root,text='SDK软件',variable = CheckVar2,onvalue=1,offvalue=0)
ch3 = Checkbutton(root,text='SNMPD-CONFIG文件',variable = CheckVar3,onvalue=1,offvalue=0)
ch4 = Checkbutton(root,text='SYSTEM-CONFIG文件',variable = CheckVar4,onvalue=1,offvalue=0)
ch5 = Checkbutton(root,text='STARTUP-CONFIG文件',variable = CheckVar5,onvalue=1,offvalue=0)

ch1.pack()
ch2.pack()
ch3.pack()
ch4.pack()
ch5.pack()

btn = Button(root,text="OK",command=run)
btn.pack()

lb2 = Label(root,text='')
lb2.pack()

timestr=' '
gettime()

btn1 = Button(root, text='刷新', command=gettime)
btn1.place(relx=0.16, rely=0.08, relwidth=0.065, relheight=0.06)

btn3 = Button(root, text='提交', command=lambda:comit(timestr))
btn3.place(relx=0.85, rely=0.85, relwidth=0.08, relheight=0.08)

entry_text1 = StringVar()
inp1 = Entry(root, textvariable=entry_text1, font=('FangSong', 10), width=30)
inp1.place(relx=0.23, rely=0.33, relwidth=0.25, relheight=0.05)
entry_text2 = StringVar()
inp2 = Entry(root, textvariable=entry_text2, font=('FangSong', 10), width=30)
inp2.place(relx=0.23, rely=0.41, relwidth=0.25, relheight=0.05)
entry_text3 = StringVar()
inp3 = Entry(root)
inp3.place(relx=0.23, rely=0.49, relwidth=0.25, relheight=0.05)
entry_text4 = StringVar()
inp4 = Entry(root, textvariable=entry_text4, font=('FangSong', 10), width=30)
inp4.place(relx=0.23, rely=0.57, relwidth=0.25, relheight=0.05)
entry_text5 = StringVar()
inp5 = Entry(root, textvariable=entry_text5, font=('FangSong', 10), width=30)
inp5.place(relx=0.23, rely=0.65, relwidth=0.25, relheight=0.05)
entry_text6 = StringVar()
inp6 = Entry(root)
inp6.place(relx=0.23, rely=0.73, relwidth=0.25, relheight=0.05)
entry_text7 = StringVar()
inp7 = Entry(root, textvariable=entry_text7, font=('FangSong', 10), width=30)
inp7.place(relx=0.73, rely=0.33, relwidth=0.25, relheight=0.05)
entry_text8 = StringVar()
inp8 = Entry(root, textvariable=entry_text8, font=('FangSong', 10), width=30)
inp8.place(relx=0.73, rely=0.41, relwidth=0.25, relheight=0.05)
entry_text9 = StringVar()
inp9 = Entry(root, textvariable=entry_text9, font=('FangSong', 10), width=30)
inp9.place(relx=0.73, rely=0.49, relwidth=0.25, relheight=0.05)
entry_text10 = StringVar()
inp10 = Entry(root, textvariable=entry_text10, font=('FangSong', 10), width=30)
inp10.place(relx=0.73, rely=0.57, relwidth=0.25, relheight=0.05)
entry_text11 = StringVar()
inp11 = Entry(root, textvariable=entry_text11, font=('FangSong', 10), width=30)
inp11.place(relx=0.73, rely=0.65, relwidth=0.25, relheight=0.05)
entry_text12 = StringVar()
inp12 = Entry(root, textvariable=entry_text12, font=('FangSong', 10), width=30)
inp12.place(relx=0.73, rely=0.73, relwidth=0.25, relheight=0.05)

btn4 = Button(root, text='系统软件文件路径', command=lambda:get_path(entry_text1))
btn4.place(relx=0.03, rely=0.33, relwidth=0.2, relheight=0.05)
btn5 = Button(root, text='系统软件md5值', command=lambda:get_md5(entry_text2))
btn5.place(relx=0.03, rely=0.41, relwidth=0.2, relheight=0.05)
lb3=Label(root,text='系统软件版本号')
lb3.place(relx=0.03, rely=0.49, relwidth=0.2, relheight=0.05)
btn7 = Button(root,text='SDK软件文件路径', command=lambda:get_path(entry_text4))
btn7.place(relx=0.03, rely=0.57, relwidth=0.2, relheight=0.05)
btn8 = Button(root,text='SDK软件MD5值', command=lambda:get_md5(entry_text5))
btn8.place(relx=0.03, rely=0.65, relwidth=0.2, relheight=0.05)
lb6=Label(root,text='SDK软件版本号')
lb6.place(relx=0.03, rely=0.73, relwidth=0.2, relheight=0.05)
btn10 = Button(root,text='SNMPD-CONFIG文件', command=lambda:get_path(entry_text7))
btn10.place(relx=0.5, rely=0.33, relwidth=0.23, relheight=0.05)
btn11 = Button(root,text='SNMPD-CONFIG MD5', command=lambda:get_md5(entry_text8))
btn11.place(relx=0.5, rely=0.41, relwidth=0.23, relheight=0.05)
btn12 = Button(root,text='SYSTEM-CONFIG文件', command=lambda:get_path(entry_text9))
btn12.place(relx=0.5, rely=0.49, relwidth=0.23, relheight=0.05)
btn13 = Button(root,text='SYSTEM-CONFIG MD5', command=lambda:get_md5(entry_text10))
btn13.place(relx=0.5, rely=0.57, relwidth=0.23, relheight=0.05)
btn14 = Button(root,text='STARTUP-CONFIG文件', command=lambda:get_path(entry_text11))
btn14.place(relx=0.5, rely=0.65, relwidth=0.23, relheight=0.05)
btn15 = Button(root,text='STARTUP-CONFIG MD5', command=lambda:get_md5(entry_text12))
btn15.place(relx=0.5, rely=0.73, relwidth=0.23, relheight=0.05)


root.mainloop()
