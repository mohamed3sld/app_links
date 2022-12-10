from tkinter import *
from tkinter import messagebox
import sqlite3
from displayurls import DisplayU
import re



con = sqlite3.connect('database_urls.db')
cur = con.cursor()


class AddUrl:
    def __init__(self, root2):
        self.root2 = root2

        
   
        #Start
        #image
        self.icon_add = PhotoImage(file='icons/add.png')
        self.icon_url_add = PhotoImage(file='icons/urladd.png')
        self.icon_name = PhotoImage(file='icons/name.png')



        self.regex = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
       

        self.enturl = Label(self.root2, text='Enter The Url:', fg='#22A39F', bg='#434242', font='times 15 bold').place(x=40, y=40)
        self.addurl = Entry(self.root2, width=30, bg='#F3EFE0', fg='#222222', font='arial 15 bold')
        self.addurl.place(x=240, y=40)
        self.urlimage = Label(self.root2, image=self.icon_url_add, bg='#434242').place(x=590, y=40)

        self.entname = Label(self.root2, text='Enter The Name:', fg='#22A39F', bg='#434242', font='times 15 bold').place(x=40, y=100)
        self.addname = Entry(self.root2, width=30, bg='#F3EFE0', fg='#222222', font='arial 15 bold')
        self.addname.place(x=240, y=100)
        self.name = Label(self.root2, image=self.icon_name, bg='#434242').place(x=590, y=100)



        #Button
        self.btn_add = Button(self.root2, text='  Add To DataBase', font='arial 15 bold', bg='#678983', fg='#181D31', image=self.icon_add, compound=LEFT, command=self.Funcadd).place(relx = 0.5, rely = 0.7, anchor = CENTER)
        self.btn_display = Button(self.root2, text='Display Links', font='arial 12 bold', bg='#678983', fg='#181D31', command=self.funcdisplay).place(relx = 0.5, rely = 0.9, anchor = CENTER)
        #End

    def Funcadd(self):
        links2 = cur.execute('SELECT * FROM links').fetchall()
        list_urls = []
        for item in links2:
            list_urls.append(item[2].lower())


        if re.findall(self.regex, self.addurl.get()):
            url = self.addurl.get()
            name = self.addname.get()

            if url.lower() in list_urls:
                messagebox.showinfo('Warning', 'This link is in the database!', icon='warning')

            else:
                if name != ' ':
                    query = "INSERT INTO 'links' (name, url) VALUES(?,?)"
                    cur.execute(query, (name, url))
                    con.commit()
                    messagebox.showinfo('Success', 'Successfully added to database', icon='info')
                    self.addurl.delete(0, END)
                    self.addname.delete(0, END)
 
                
        else:
            messagebox.showinfo('Warning', 'This Link is Wrong', icon='warning')


    def funcdisplay(self):
        windows_display = DisplayU()





def main():
    root = Tk()
    window = AddUrl(root)
    root.geometry('700x300')
    root.resizable(False, False)
    root.title('Add Url')
    root.config(bg='#434242')
    root.iconbitmap("icons/app-development.ico")
    root.mainloop()

if __name__ == '__main__':
    main()


 