from tkinter import *
import datetime
import time


def gettime():
    global timestr
    timestr = time.strftime('%Y%m%d.%H%M%S',time.localtime(time.time()))
    lb1 = Label(root, text='系统时间：'+ timestr)
    lb1.place(relx=0.05, rely=0, relwidth=0.3, relheight=0.08)


def comit(timestr):
    filenum = CheckVar1.get() + CheckVar2.get() + CheckVar3.get() + CheckVar4.get() + CheckVar5.get()
    f = open('test.ini', 'w')
    fnum = 1
    f.write("BEGIN SNOLT\n[USB CONFIG]\n")
    f.write("SN=" + timestr+'\n')
    f.write("[DEVICE DESCRIPTION]\nESN=DEFAULT\nMAC=DEFAULT\n[UPGRADE INFO]\nDIRECTORY=/upgrade\n")
    f.write("FILENUM="+str(filenum)+'\n')
    if(CheckVar1.get() == 1):
        f.write("TPYE"+str(fnum)+'='+'SYSTEM-SOFTWARE\n')
        f.write("FILENAME" +str(fnum) + '=' + inp1.get() + '\n')
        f.write("FILE_MD5SUM" +str(fnum)+ '=' + inp2.get() + '\n')
        fnum = fnum + 1
    if (CheckVar2.get() == 1):
        f.write("TPYE" + str(fnum) + '=' + 'SDK-SOFTWARE\n')
        f.write("FILENAME" + str(fnum) + '=' + inp4.get() + '\n')
        f.write("FILE_MD5SUM" + str(fnum) + '=' + inp5.get() + '\n')
        fnum = fnum + 1
    if (CheckVar3.get() == 1):
        f.write("TPYE" + str(fnum) + '=' + 'SNMPD-CONFIG\n')
        f.write("FILENAME" + str(fnum) + '=' + inp7.get() + '\n')
        f.write("FILE_MD5SUM" + str(fnum) + '=' + inp8.get() + '\n')
        fnum = fnum + 1
    if (CheckVar4.get() == 1):
        f.write("TPYE" + str(fnum) + '=' + 'SYSTEM-CONFIG\n')
        f.write("FILENAME" + str(fnum) + '=' + inp9.get() + '\n')
        f.write("FILE_MD5SUM" + str(fnum) + '=' + inp10.get() + '\n')
        fnum = fnum + 1
    if (CheckVar5.get() == 1):
        f.write("TPYE" + str(fnum) + '=' + 'STARTUP-CONFIG\n')
        f.write("FILENAME" + str(fnum) + '=' + inp11.get() + '\n')
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

inp1 = Entry(root)
inp1.place(relx=0.23, rely=0.33, relwidth=0.25, relheight=0.05)
inp2 = Entry(root)
inp2.place(relx=0.23, rely=0.41, relwidth=0.25, relheight=0.05)
inp3 = Entry(root)
inp3.place(relx=0.23, rely=0.49, relwidth=0.25, relheight=0.05)
inp4 = Entry(root)
inp4.place(relx=0.23, rely=0.57, relwidth=0.25, relheight=0.05)
inp5 = Entry(root)
inp5.place(relx=0.23, rely=0.65, relwidth=0.25, relheight=0.05)
inp6 = Entry(root)
inp6.place(relx=0.23, rely=0.73, relwidth=0.25, relheight=0.05)
inp7 = Entry(root)
inp7.place(relx=0.73, rely=0.33, relwidth=0.25, relheight=0.05)
inp8 = Entry(root)
inp8.place(relx=0.73, rely=0.41, relwidth=0.25, relheight=0.05)
inp9 = Entry(root)
inp9.place(relx=0.73, rely=0.49, relwidth=0.25, relheight=0.05)
inp10 = Entry(root)
inp10.place(relx=0.73, rely=0.57, relwidth=0.25, relheight=0.05)
inp11 = Entry(root)
inp11.place(relx=0.73, rely=0.65, relwidth=0.25, relheight=0.05)
inp12 = Entry(root)
inp12.place(relx=0.73, rely=0.73, relwidth=0.25, relheight=0.05)

lb3=Label(root,text='系统软件文件路径')
lb3.place(relx=0.03, rely=0.33, relwidth=0.2, relheight=0.05)
lb4=Label(root,text='系统软件MD5值')
lb4.place(relx=0.03, rely=0.41, relwidth=0.2, relheight=0.05)
lb5=Label(root,text='系统软件版本号')
lb5.place(relx=0.03, rely=0.49, relwidth=0.2, relheight=0.05)
lb6=Label(root,text='SDK软件文件路径')
lb6.place(relx=0.03, rely=0.57, relwidth=0.2, relheight=0.05)
lb7=Label(root,text='SDK软件MD5值')
lb7.place(relx=0.03, rely=0.65, relwidth=0.2, relheight=0.05)
lb8=Label(root,text='SDK软件版本号')
lb8.place(relx=0.03, rely=0.73, relwidth=0.2, relheight=0.05)
lb9=Label(root,text='SNMPD-CONFIG文件')
lb9.place(relx=0.5, rely=0.33, relwidth=0.23, relheight=0.05)
lb10=Label(root,text='SNMPD-CONFIG MD5')
lb10.place(relx=0.5, rely=0.41, relwidth=0.23, relheight=0.05)
lb11=Label(root,text='SYSTEM-CONFIG文件')
lb11.place(relx=0.5, rely=0.49, relwidth=0.23, relheight=0.05)
lb12=Label(root,text='SYSTEM-CONFIG MD5')
lb12.place(relx=0.5, rely=0.57, relwidth=0.23, relheight=0.05)
lb13=Label(root,text='STARTUP-CONFIG文件')
lb13.place(relx=0.5, rely=0.65, relwidth=0.23, relheight=0.05)
lb14=Label(root,text='STARTUP-CONFIG MD5')
lb14.place(relx=0.5, rely=0.73, relwidth=0.23, relheight=0.05)

root.mainloop()
