
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *
import requests
import json

def completeDownload(stream=None, file_path=None):
    print("download completed")
    showinfo("Message", "File has been downloaded...")
    downloadBtn['text'] = "Download Video"
    downloadBtn['state'] = "active"
    urlField.delete(0, END)


# onprogress callbackfunction
def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    downloadBtn['text'] = "{:00.0f}% downloaded ".format(percent)


# download function
def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return

    try:
        yt = YouTube(url)
        st = yt.streams.first()

        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path_to_save)

    except Exception as e:
        print(e)
        print("something went wrong")


def btnClicked():
    try:
        downloadBtn['text'] = "Please wait..."
        downloadBtn['state'] = 'disabled'
        url = str(c[0])
        if url == '':
            return
        print(url)
        thread = Thread(target=startDownload, args=(url,))
        thread.start()

    except Exception as e:
        print(e)


b=[2,1,1,3,4]
c=['https://www.youtube.com/watch?v=KHMTn9Az92w','https://www.youtube.com/watch?v=sfcf5ywCn4A']
print(b[1])

root = Tk()

Fact = str(b[1])
fact2 = c[0]

root.title('test')
root.geometry ("500x600")
l1=Label(text='id')
l1.pack(side=TOP)
T = Text(root, height = 1, width = 5)
T.pack(side=TOP)
T.insert(END, Fact)

l2=Label(text='url')
l2.pack(side=TOP)
urlField = Text(root, height = 1, width = 50)
urlField.pack(side=TOP)
urlField.insert(END, fact2)

downloadBtn = Button(root, text="Download Video", relief='ridge', command=btnClicked)
downloadBtn.pack(side=TOP, pady=20)

root.mainloop()