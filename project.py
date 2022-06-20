from tkinter import *
from pytube import YouTube
from pytube import Playlist


root = Tk()

root.state('withdraw')
root = Toplevel(root)
root.geometry("550x540+350+70")
root.configure(bg="#ebc3c3")
root.resizable(False, False)
root.title("Youtube downloader")
root.iconbitmap("lgicon.ico")


lb1=Label(root,
          text="Select what you want to download:",
          font=("Tahoma",20,'bold'))
lb1.pack(side='top',ipady=30)


vurl= StringVar()
purl= StringVar()


#########################################################
#########################################################


##############333------------------333##################3
#video.streams.filter(res=, type=, subtype=, only_audio=, only video=,).download()
#########################################################
#########################################################

def finish():
    print("download done!")
def dvideo():
    print("Video")
    btn2.place_forget()
    btn1.place_forget()
    lb1.pack_forget()
    #vlb1.pack_configure(ipadx=20,side=LEFT, ipady=30,pady=50, padx=20)
    vlb1.place_configure(relx=0.07, rely=0.22)
    vtil.place_configure(relx=0.2, rely=0.05)
    #place(relx=0:1, rely=0:1)
    dvbtn.place(relx=0.25, rely=0.6)
    vent.place(relx=0.3, rely=0.22)
    

def dplay():
    print("Playlist")
    btn2.place_forget()
    btn1.place_forget()
    lb1.pack_forget()
    vlb1.place_forget()
    vtil.place_forget()
    dvbtn.place_forget()
    vent.place_forget()
    plb1.place_configure(relx=0.07, rely=0.22)
    ptil.place_configure(relx=0.2, rely=0.05)
    #place(relx=0:1, rely=0:1)
    dpbtn.place(relx=0.25, rely=0.6)
    pent.place(relx=0.3, rely=0.23)



def down_video():
    print('pytube video')
    vent.configure(state='readonly',selectbackground='yellow')
    print(vurl.get())
    print(type(vurl.get()))
    video = YouTube(vurl.get())
    
    print(f"The video title is : \n {video.title} \n-----------------")
    print(f"The video description is:\n {video.description}\n -------")
    print(f"The video duration is :{video.length} seconds \n---------")


    #for stream in video.streams.filter(progressive=True, res="720p"):
    #   print(stream)
    #print("highest---------------------\n")
    #print(video.streams.get_highest_resolution())
    #print("lowest---------------------\n")
    #print(video.streams.get_lowest_resolution())

    ##---------------------------##
    print("Error after")
    video.streams.download(output_path="D:\برمجة محمد - full\Tk playlist")
    print("Error before")
    #video.register_on_complete_callback(finish())



    


def down_play():
    print('pytube playlist')
    pent.configure(state='readonly',selectbackground='yellow')
    print(purl.get())




btn1=Button(root,
            text="Single Video",
            width=15,
            heigh=3,
            bd=2,
            font=('courier', 18,'bold'),
            fg='yellow',
            bg='#1a3ef4',
            relief=RAISED,
            command=dvideo,
            )
btn1.place(relx=0.07,rely=0.4)

btn2=Button(root,
            text="Playlist",
            width=15,
            heigh=3,
            bd=2,
            font=('courier', 18,'bold'),
            fg='yellow',
            bg='#1a3ef4',
            relief=RAISED,
            command=dplay)
btn2.place(relx=0.55, rely=0.4)



#pack has two options : side, fill
# side: left, right, top, bottom
# fill: x,y,both
# expand: True,False
# (padding) padx: integer numbers
# ipadx: integer numbers   -- to fill the widget
#pack_forget()   to hidden this widget
#pack_configure()  to display the widget

vtil = Label(root,
            text="Download your video here",
            bg='black',
            fg='yellow',
            font=('courier',18),

            )
#label options:  anchor, width, height, wraplength, bitmap, justify, textvariable
#bitmap: error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, warning


vlb1 = Label(root,
            text="Video URL",
            bg='black',
            fg='yellow',
            font=('courier',15)
            )

dvbtn=Button(root,
            text="download",
            width=14,
            height=2,
            bd=2,
            font=('courier', 20,'bold'),
            fg='yellow',
            bg='red',
            relief=RAISED,
            command=down_video
            )
st_font = ("arial", 16)

vent = Entry(root,
             bg='#e3e2f1',
             relief=SUNKEN,
             bd=4,
             width=28,
             font=st_font,
             state='normal',
             textvariable=vurl
             )
    
#entre state: normal, active, disabled, readonly
#show('*')


############################################
#Playlist part
############################################

ptil = Label(root,
            text="Download your playlist here",
            bg='black',
            fg='yellow',
            font=('courier',18),

            )
plb1 = Label(root,
            text="Playlist URL",
            bg='black',
            fg='yellow',
            font=('courier',15),
            wraplength=110
            )

dpbtn=Button(root,
            text="download",
            width=14,
            height=2,
            bd=2,
            font=('courier', 20,'bold'),
            fg='yellow',
            bg='red',
            relief=RAISED,
            command=down_play
            )

pent = Entry(root,
             bg='#e3e2f1',
             relief=SUNKEN,
             bd=4,
             width=28,
             font=st_font,
             state='normal',
             textvariable=purl
             )





root.mainloop()