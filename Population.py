from tkinter import *
import requests
from tkinter import ttk
from PIL import ImageTk, Image
from bs4 import BeautifulSoup                                   


death = "https://www.livepopulation.com/"

dpage = requests.get(death)
dcode = BeautifulSoup(dpage.content,"html.parser")
 
data4 = dcode.find(class_="deaths-day").get_text()

birth = "https://www.livepopulation.com/"

bpage = requests.get(birth)
bcode = BeautifulSoup(bpage.content,"html.parser")
 
data3 = bcode.find(class_="births-day").get_text()


url = "https://www.worldometers.info/world-population/population-by-country/"

url1 = "https://www.livepopulation.com/"

ppage = requests.get(url1)
pcode = BeautifulSoup(ppage.content,"html.parser")
 
data = pcode.find(class_="current-population").get_text()


# page = requests.get(url)
# code = BeautifulSoup(page.content,"html.parser")

# country = code.find(class_="table-responsive").get_text()
# print(country)

root = Tk()
root.title("World's Population")
root.iconbitmap('H:\Python\population\world.jpg')
root.geometry('1280x720')
root.configure(bg='black')


mylabel1 = Label(root,text="Welcome To World's Population",font=("Helvetica", 20),bg="black",fg="green")
mylabel1.pack()

a = Label(root, text=" ",bg="black",fg="white")
a.pack()

mylabel2 = Label(root,text="Current World's Population",font=("Arial Bold",16 ),bg="black",fg="white")
mylabel2.pack()

b = Label(root, text=" ",bg="black",fg="white") 
b.pack()

current  = Label(root,text=data, font=("Arial", 20),bg="black",fg="white")
current.pack()
 
c = Label(root, text=" ",bg="black",fg="white")
c.pack()

mylabel3 = Label(root,text="Birth's Today",font=("Arial Bold",16 ),bg="black",fg="white")
mylabel3.pack()

b = Label(root, text=" ",bg="black",fg="white") 
b.pack()

birth1  = Label(root,text=data3, font=("Arial", 20),bg="black",fg="white")
birth1.pack()

c = Label(root, text=" ",bg="black",fg="white") 
c.pack()

mylabel3 = Label(root,text="Death's Today",font=("Arial Bold",16 ),bg="black",fg="white")
mylabel3.pack()

d = Label(root, text=" ",bg="black",fg="white") 
d.pack()

death1  = Label(root,text=data4, font=("Arial", 20),bg="black",fg="white")
death1.pack()


e = Label(root, text=" ",bg="black",fg="white")
e.pack()

def fresh():
    root.destroy(); 
    
def new():
    url9= "https://worldpopulationreview.com/"

    page = requests.get(url9)
    code = BeautifulSoup(page.content,"html.parser")

    table = code.find('table')

    table_row = table.find_all('tr')


    # pop_table = code.find(class_='datatableStyles__StyledTable-ysgkm4-1 dXImya table table-striped').get_text()
    # print(pop_table)
    Top= Toplevel()
    Top.title("Country Population")
    Top.iconbitmap("world2.ico")
    Top.geometry('1280x720')
    mylabel3 = Label(Top,text="2020 Live Count",font=("Arial BOLD",25))
    mylabel3.pack()   
    mylabel5 = Label(Top,text="")
    mylabel5.pack()
    main_frame = Frame(Top)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(fill=BOTH,expand=1,side=LEFT)

    my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="n")
    for tr in table_row:
        td = tr.find_all('td')
        row = [i.text for i in td]
        
        for xyz in range(len(row)):
            if xyz == 1:
                mylabel1 = Label(second_frame,text=row[xyz],font=("Arial BOLD",25))
                mylabel1.pack()
            elif xyz == 2:
                mylabel4 = Label(second_frame,text=row[xyz],font=("Arial",20))
                mylabel4.pack()
            elif xyz == 3:
                mylabel6 = Label(second_frame,text="")
                mylabel6.pack()
            else :
                mylabel2 = Label(second_frame,text=row[xyz],font=("Arial",20))
    Top.mainloop()
    
    
myButton2 = Button(root, text="COUNTRY POPULATION",font=("Arial Bold", 10), padx=20, fg="Lightgreen",pady=2,bg="darkblue",command=new)
myButton2.pack()

f = Label(root, text=" ",bg="black",fg="white")
f.pack()

myButton1 = Button(root, text="EXIT",font=("Arial Bold", 10), padx=20, fg="Lightgreen",pady=2,bg="darkblue",command=fresh)
myButton1.pack()

d = Label(root, text=" ",bg="black",fg="white")
d.pack()

right1 = Label(root,text ='Created By HARSH KOLI',font=("Arial Bold", 8), padx=20, fg="red",pady=2,bg="black") 
right1.place(relx = 1.0,rely = 0.0,anchor ='ne') 

image1 = Image.open("earth.jpg")
photo=ImageTk.PhotoImage(image1)

lbl = Label(root,image=photo)
lbl.pack()



root.mainloop()