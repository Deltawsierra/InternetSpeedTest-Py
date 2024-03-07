from tkinter import *
import speedtest

root = Tk()
root.title("Speed Test")
root.geometry("400x650")
root.config(bg="light blue")
root.resizable(False, False)
 
def Check():
    test = speedtest.Speedtest()

    Uploading = round(test.upload()/(1024*1024),2)
    upload.config(text=Uploading)

    downloading = round(test.download()/(1024*1024),2)
    download.config(text=downloading)
    Download.config(text=downloading)

    servernames = []
    test.get_servers(servernames)
    ping.config(text=test.results.ping)

image_icon = PhotoImage(file="Icon.png")
root.iconphoto(False, image_icon)

Top=PhotoImage(file="TopBar.png")
Label(root,image=Top, bg="light blue").pack()

Main=PhotoImage(file="Background.jpg")
Label(root,image=Main, bg="light blue").pack(pady=(10,0))

button=PhotoImage(file="StartButton.png")
Button=Button(root,image=button, bg="light blue", bd=0, activebackground="blue", cursor="hand2", command=Check)
Button.pack(pady=10)

Label(root, text="PING", font=("Arial", 10, "bold"), bg="#384056").place(x=50, y=0)
Label(root, text="DOWNLOAD", font=("Arial", 10, "bold"), bg="#384056").place(x=1400, y=0)
Label(root, text="UPLOAD", font=("Arial", 10, "bold"), bg="#384056").place(x=260, y=0)

Label(root, text="MS", font="Arial 7 bold", bg="#384056", fg="white").place(x=60,y=80)
Label(root, text="MBPS", font="Arial 7 bold", bg="#384056", fg="white").place(x=165,y=80)
Label(root, text="MBPSS", font="Arial 7 bold", bg="#384056", fg="white").place(x=275,y=80)

Label(root,text="Download", font="arial 15 bold", bg="#384056", fg="white").place(x=140, y=280)
Label(root,text="MBPS", font="arial 15 bold", bg="#384056", fg="white").place(x=155, y=380)

ping=Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
ping.place(x=70, y=60, anchor="center")

download=Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
download.place(x=1800, y=60, anchor="center")

upload=Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
upload.place(x=290, y=60, anchor="center")

Download=Label(root, text="00", font="arial 40 bold", bg="#384056")
download.place(x=1850, y=350, anchor="center")

root.mainloop()