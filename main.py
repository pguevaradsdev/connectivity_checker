"""6. Comprobador de Conectividad de Sitios Web
La idea de este proyecto es crear un program que pruebe la conectividad de sitios web.
Puedes usar los modulos urllib y tkinter para crear una interfaz gráfica de usuario (GUI) que
permita a los usuarios ingresar una dirección web. Después de haber recopilado la dirección
web del usuario, puedes pasarla a una función para devolver un código de estado HTTP para
el sitio web actual mediante la función .getcode() del módulo urllib.
En este ejemplo, simplemente determinamos si el código HTTP es 200. Si lo es, sabemos que
el sitio está funcionando; de lo contrario, informamos al usuario de que no está disponible."""


import tkinter as tk
from urllib.request import urlopen
from urllib.error import URLError

windows1 = tk.Tk()
windows1.geometry("1200x300+350+250")
windows1.title(" ")

label1 = tk.Label(windows1, text="Welcome!", font=("Times New Roman", 20))
label1.pack()

label2 = tk.Label(windows1,
                text="Enter the website you want to check in the writting field below.", 
                font=("Times New Roman", 20)
                )
label2.pack()

url = tk.Entry(windows1, 
            width=50, 

            g="light cyan",
            font=("Arial", 20)
            )

url.pack(fill="x", 
        padx=10, 
        pady=10
        )


def show_message(message):

    messageWindow = tk.Tk()
    messageWindow.title(" ")
    messageWindow.geometry("1900x900+500+250")

    label3 = tk.Label(messageWindow, 
                    text=message, 
                    font=("Times New Roman", 20))
    label3.pack()

    exitButton = tk.Button(messageWindow, 
                        text= "Exit", 
                        font=("Times New Roman", 20), 
                        command=messageWindow.destroy)
    exitButton.pack()

def send_url():
    "This function have the tast of recover the introduced website from the user and send "
    "it to the urllib to check teh status of it"
    urlcode = url.get()

    if not urlcode.startswith(("http://", "https://")):
        urlcode = "http://" + urlcode

    try:
        answer = urlopen(urlcode)
        status = answer.getcode()

        if status == 200:
            message = "The website is working."
        else:
            message = "Website unavailable."

    except URLError as error:
        message = "An Error is ocurred.", error

    show_message(message)



sendButton = tk.Button(windows1, 
                    text="Send", 
                    command=send_url)
sendButton.pack()

url.bind("<Return>", lambda event: send_url())

windows1.mainloop()


