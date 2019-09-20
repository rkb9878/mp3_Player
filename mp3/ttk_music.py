import os
# import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk

# from mutagen.mp3 import MP3
from pygame import mixer
mixer.init()
playlist = []
pushed = FALSE
muted = FALSE
index=0
#---------------------function section-----------
def nextmusic():
    global index
    index +=1
    mixer.music.load(playlist[index])
    mixer.music.play()
    statusbar['text']=playlist[index]

def previousmusic():
    global index
    index -= 1
    mixer.music.load(playlist[index])
    mixer.music.play()
    statusbar['text']=playlist[index]
def mute_music():
    global muted
    if muted:  # Unmute the music
        mixer.music.set_volume(0.7)
        volume_bt.configure(image=volumePhoto)
        scale.set(70)
        muted = FALSE
    else:  # mute the music
        mixer.music.set_volume(0)
        volume_bt.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music Paused"
def stop_music():
    mixer.music.stop()
    statusbar['text']="Music Stopped"

def play_music():
    global pushed
    if pushed:
        mixer.music.unpause()
        statusbar['text']="Music Resumed"
        pushed=FALSE
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song=playlistbox.curselection()
            selected_song=int(selected_song[0])
            play_it=playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text'] = "Playing music" + ' - ' + os.path.basename(play_it)
            # show_details(play_it)
        except:
            tkinter.messagebox.showerror('File not found', 'Melody could not find the file. Please check again.')


def set_vol(val):
    volume=float(val)/100
    mixer.music.set_volume(volume)
def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)
    if filename_path:
        mixer.music.queue(filename_path)
    else:
        print("error")
    print(playlist)

def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1

def del_song():
    try:
        selected_song = playlistbox.curselection()
        selected_song = int(selected_song[0])
        playlistbox.delete(selected_song)
        playlist.pop(selected_song)
    except:
        tkinter.messagebox.showerror("","No mp3 Available")
#-----------------------------------------------

root=tk.ThemedTk()
root.get_themes()
# root.set_theme("radiance")
root.set_theme("clam")
# root.set_theme("classic")
root.title("Music")
root.resizable(0,0)
#--------------menu-----------------
menubar=Menu(root)
root.config(menu=menubar)
subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

statusbar = ttk.Label(root, text="Welcome to Music Player", relief=SUNKEN, anchor=W, font='Times 10 italic',justify='center')
statusbar.pack(side=BOTTOM, fill=X)

#-----------------Frame-----------------------------
leftFrame=Frame(root)
leftFrame.pack(side=LEFT)
rightframe=Frame(root)
rightframe.pack()
topframe=Frame(root)
topframe.pack()
middleframe = Frame(rightframe)
middleframe.pack(pady=30, padx=30)
bottomframe=Frame(root)
bottomframe.pack()
#--------------------------------------------------

playlistbox=Listbox(leftFrame,width=50)
playlistbox.pack()
addmusic=PhotoImage(file='images/a.png')
addBtn = ttk.Button(leftFrame, image=addmusic, command=browse_file)
addBtn.pack(side=LEFT)
delphoto=PhotoImage(file='images/del.png')
delBtn = ttk.Button(leftFrame, image=delphoto, command=del_song)
delBtn.pack(side=LEFT)
#----------------------------------------------------
#------------------------------------------------------
playphoto=PhotoImage(file='images/play.png')
play_Bt=ttk.Button(middleframe,image=playphoto,command=play_music)
play_Bt.grid(row=0,column=1,padx=15)

stopphoto=PhotoImage(file='images/stop.png')
stop_bt=ttk.Button(middleframe,image=stopphoto,command=stop_music)
stop_bt.grid(row=0,column=0,padx=10)

pauseimage=PhotoImage(file="images/pause1.png")
pause_bt=ttk.Button(middleframe,image=pauseimage,command=pause_music)
pause_bt.grid(row=0,column=2,padx=10)

previous=PhotoImage(file="images/pri.png")
previous_bt=ttk.Button(middleframe,image=previous,command=previousmusic)
previous_bt.grid(row=1,column=0,pady=10)

nextphoto=PhotoImage(file="images/next2.png")
previous_bt=ttk.Button(middleframe,image=nextphoto,command=nextmusic)
previous_bt.grid(row=1,column=2,pady=10)
#---------------------------------------------
mutePhoto = PhotoImage(file='images/mute.png')
volumePhoto = PhotoImage(file='images/volume.png')
volume_bt=ttk.Button(bottomframe,image=volumePhoto,command=mute_music)
volume_bt.grid(row=0,column=0,padx=10,pady=20)
scale=ttk.Scale(bottomframe,from_=0,to=100,orient=HORIZONTAL,command=set_vol)
scale.set(10)
mixer.music.set_volume(0.7)
scale.grid(row=0,column=1,padx=20,pady=20)
root.mainloop()