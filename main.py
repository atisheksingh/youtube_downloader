from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *
import requests
import json
i = 0


def genrate_link():
    url = "http://smartgsc.rannlabprojects.com/api/CMS/SearchAdvertisement"

    #authencation keys
    headers = {"Gender":"All","MacAddress":"b8:27:eb:45:c7:21","Location":"","Business":"","Age":""}

    headers["Content-Type"] = "application/json"

    payload = """
    {
      "Id": 12345,
      }
    """


    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.status_code)
    d2 = response.json()
    d3= json.loads(d2)
    print(type(d3))
    d3 = d3[0:]
    g =[]
    a=[]

    for id in d3:
        #print(id['ID'])
        #print(id["VideoUrl"])
        g.append(id["ID"])
        a.append(id['VideoUrl'])

    link = dict(zip(g,a))
    print(link)
    return g,a

b , c = genrate_link()
l=len(b)
def nxtClicked():
        pass


def completeDownload(stream=None, file_path=None):
    print("download completed")
    showinfo("Message", "File has been downloaded...")
    downloadBtn['text'] = "Download Video"
    downloadBtn['state'] = "active"
    urlField.delete(str(''), END)
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
        st.download (output_path=path_to_save, filename=str(b[i]))

    except Exception as e:
        print(e)
        print("something went wrong")


#button funtion
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



font = ('verdana', 20)
root = Tk()
root.title("Youtube downloader")
root.iconbitmap("img/icon.ico")
root.geometry("500x600")

Fact = str(b[i])
fact2 = str(c[i])

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

l3=Label(text='stack id')
l3.pack(side=TOP)
T2 = Text(root, height = 1, width = 50)
T2.pack(side=TOP)
T2.insert(END,b[0:])

l4=Label(text='stack url')
l4.pack(side=TOP)
T5 = Text(root, height = 11, width = 50)
T5.pack(side=TOP)
T5.insert(END,c[0:])




downloadBtn = Button(root, text="Download Video", font=font, relief='ridge', command=btnClicked)
downloadBtn.pack(side=TOP, pady=20)


NextBtn = Button(root, text="NextButton", font=font, relief='ridge', command=nxtClicked)
NextBtn.pack(side=TOP, pady=20)

b1=Button(root,text="1")
b1.pack(side=LEFT)

b2=Button(root,text="2")
b2.pack(side=LEFT)

b3=Button(root,text="3")
b3.pack(side=LEFT)

b4=Button(root,text="4")
b4.pack(side=LEFT)

b5=Button(root,text="5")
b5.pack(side=LEFT)

b6=Button(root,text="6")
b6.pack(side=LEFT)

b7=Button(root,text="7")
b7.pack(side=LEFT)

b8=Button(root,text="8")
b8.pack(side=LEFT)

b9=Button(root,text="9")
b9.pack(side=LEFT)

b10=Button(root,text="10")
b10.pack(side=LEFT)


root.mainloop()
