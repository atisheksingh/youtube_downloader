import requests #api-module

import json

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


from tkinter import *
import  random
font = ('verdana', 20)
root = Tk()
root.title("Youtube downloader")
root.iconbitmap("img/icon.ico")
root.geometry("500x600")

Fact = str(b[1])
fact2 = str(c[1])

l1=Label(text='id')
l1.pack(side=TOP)
T = Text(root, height = 1, width = 5)
T.pack(side=TOP)
T.insert(END, Fact)

l2=Label(text='url')
l2.pack(side=TOP)
T1 = Text(root, height = 1, width = 50)
T1.pack(side=TOP)
T1.insert(END, fact2)

downloadBtn = Button(root, text="Download Video", font=font, relief='ridge')#, command=btnClicked)
downloadBtn.pack(side=TOP, pady=20)




root.mainloop()

