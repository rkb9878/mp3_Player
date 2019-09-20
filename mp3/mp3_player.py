import os
try:
    from tkinter import *
except:
    from tkinter.ttk import *
from tkinter.filedialog import askdirectory
import pygame
import tkinter.ttk as ttk
listofsong=[]
index=0

class mp3_song:
    def bt_Resume(self):
        global index
        pygame.mixer.music.load(listofsong[index])
        pygame.mixer.music.play()
        self.songlabel.config(text=listofsong[index])
        self.en_title.config(state="normal")
        self.en_title.insert(0, listofsong[index])
        self.en_title.config(state="readonly")
    def prevsong(self):
        global index
        index -= 1
        pygame.mixer.music.load(listofsong[index])
        pygame.mixer.music.play()
        self.songlabel.config(text=listofsong[index])
        self.en_title.config(state="normal")
        self.en_title.insert(0, listofsong[index])
        self.en_title.config(state="readonly")
    def nextmusic(self):
        global index
        index+=1
        pygame.mixer.music.load(listofsong[index])
        pygame.mixer.music.play()
        self.songlabel.config(text=END)
        self.songlabel.config(text=listofsong[index])
        self.en_title.config(state="normal")
        self.en_title.insert(0,listofsong[index])
        self.en_title.config(state="readonly")

    def stopmusic(self):
        pygame.mixer.music.stop()

    def directorychooser(self):
        global realnames
        global listofsong
        try:
            directory = askdirectory()
            os.chdir(directory)
            # print(os.listdir(directory))
            for file in os.listdir(directory):
                if file.endswith(".mp3"):
                    listofsong.append(file)
                # else:
                #     print("error")
            if len(listofsong):
                pygame.mixer.init()
                a=pygame.mixer.music.load(listofsong[0])
                self.songlabel.config(text=listofsong[0])
                self.en_title.config(state="normal")
                self.en_title.insert(0, listofsong[index])
                self.en_title.config(state="readonly")
                pygame.mixer.music.play()

            t=listofsong
            t.reverse()
            for items in t:
                self.tree.insert("",index=1, value=items)
        except:
            print("error")
    def __init__(self):
        self.root=Tk()
        self.root.config(background="snow")
        self.root.resizable(0, 0)
        pygame.mixer.init()
        #---------------------Frame---------------
        top=Frame(self.root)
        middel=Frame(self.root,bg="snow")
        top.pack()
        middel.pack()
        #---------------------------------------
        Label(top,text="Media Player",font=("times new roman", 48, "bold","underline"),bg="snow",fg="green").pack()
        #--------------------------------------
        self.songlabel=Label(middel,bg="snow")
        self.songlabel.pack()
        self.en_title=Entry(middel,width=100,state="readonly",justify='center')
        self.en_title.pack(pady=20)
        #--------------------------------------
        self.tree = ttk.Treeview(middel, column=("song"))
        vsb = ttk.Scrollbar(middel, orient="vertical", command=self.tree.yview)
        vsb.pack(side="right", fill=Y)
        self.tree.heading("song", text="Song")
        self.tree.pack(fill="both", expand=1)
        self.tree.column("#0", width=0)
        self.tree.configure(yscrollcommand=vsb.set)

        #--------------------------down frame-----------
        down=Frame(self.root)
        down.pack()

        def set_vol(val):
            volume = int(val) / 100
            try:
                pygame.mixer.music.set_volume(volume)
            except:
                print('please select Directory')
        Button(down,text="Select Folder",command=self.directorychooser,width="10",fg="#047a69",font=("time new roman",12,"bold")).grid(row=0,column=0,padx=15)
        Button(down,text="<<",command=self.prevsong,width="3",fg="#047a69",font=("time new roman",14,"bold")).grid(row=0,column=1,padx=15)
        Button(down,text="Resume",command=self.bt_Resume,width="10",fg="#047a69",font=("time new roman",12,"bold")).grid(row=0,column=2,padx=15)
        Button(down,text="Stop",command=self.stopmusic,width="10",fg="#047a69",font=("time new roman",12,"bold")).grid(row=0,column=3,padx=15)
        Button(down,text=">>",command=self.nextmusic,width="3",fg="#047a69",font=("time new roman",14,"bold")).grid(row=0,column=4,padx=15)
        Label(down,text="Volume:",fg="#047a69",font=("time new roman",12,"bold")).grid(row=0,column=5,padx=15)
        scale=Scale(down,from_=0,to=100, orient=HORIZONTAL,command=set_vol)
        scale.grid(row=0,column=6)

        self.root.mainloop()
mp3_song()