from tkinter import *
from tkinter import messagebox
import requests as rt
import bs4
import os
a=Tk()
a.geometry('1000x400')
a.config(bg='black')
i=Label(a,text='Medical Assistance',font=('times',50,'bold'))
i.pack()
i.config(fg='white',bg='black')
i2=Label(a,text='Name',font=('times',30))
i2.place(x=250,y=150)
v=StringVar()
t=Entry(a,font=('times',20),textvariable=v)
i2.config(fg='white',bg='black')
t.place(x=450,y=160)
b=Button(a,text='SUBMIT',activebackground='blue')
b.config(font=('times',15,'bold'))
b.place(x=450,y=270)
def fun():
    print(v.get())
    if v.get()=='':
        messagebox.showerror('Error','Enter Name!')
    else:
        fun1()
b.config(command=fun)
def fun2():
    print('hello')
def fun1():
    c=Tk()
    c.geometry('1000x500')
    i3=Label(c,text='Information',font=('times',50,'bold'))
    i3.pack()
    i4=Label(c,bg='blue')
    i4.place(x=100,y=100)
    i5=Label(c,bg='blue')
    i5.place(x=500,y=100)
    b1=Button(c,text='Next',activebackground='blue',font=('times',15))
    b1.config(command=fun2)
    b1.place(x=450,y=400)
    fun3()

def fun3():
    data=rt.request('get','https://www.1mg.com/search/all?name={}'.format(v.get()))
    s=bs4.BeautifulSoup(data.text,'html.parser')
    try:
        os.mkdir('images')
    except:
        pass
    os.chdir(os.path.abspath('images'))
    n_i=1
    for i in s.findAll('div',{'class':'col-md-3 col-sm-4 col-xs-6 style__container___jkjS2'}):
        j=i.find('a')
        head={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        nt=rt.request('get','https://www.1mg.com'+j.get('href'),headers=head)
        st=bs4.BeautifulSoup(nt.text,'html.parser')
        image=st.find('div',{'class':'col-xs-10 ProductImage__preview-container___2oTeX'})
        try:
            image=image.find('img')
            file='img{}.png'.format(n_i)
            open(file,'wb').write(rt.request('get',image.get('src')).content)
            n_i+=1
        except Exception as e:
            print(e)
    try:
            print(st.find('div',{'class':'ProductDescription__product-description___1PfGf'}).text)
    except:
        try:
            print(st.find('div',{'class':'DrugIndex__index-wrapper___uQ3dq'}).text)
        except:
            pass
