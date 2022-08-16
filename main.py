from tkinter import Label, Tk
from time import strftime

window = Tk()
window.title('Reloj Digital')
window.config(bg='white')
window.geometry('350x250+10+10')
window.minsize(width=250, height=200)
window.iconbitmap(r'assets/clock icon.ico')

window.columnconfigure(0, weight=15)
window.rowconfigure(0, weight=15)
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.rowconfigure(2, weight=1)


def obtener_time():
    hour = strftime('%H:%M:%S')
    day = strftime('%A')
    date = strftime('%d - %m - %y')

    x = texto_hora.winfo_height()
    t = int((x-5)*0.32)

    if day == 'Monday':
        day = 'Lunes'
    elif day == 'Tuesday':
        day = 'Martes'
    elif day == 'Wednesday':
        day = 'Miercoles'
    elif day == 'Thursday':
        day = 'Jueves'
    elif day == 'Friday':
        day = 'Viernes'
    elif day == 'Saturday':
        day = 'Sabado'
    elif day == 'Sunday':
        day = 'Domingo'

    texto_hora.config(text=hour, font=('Radioland', t))
    texto_dia.config(text=day)
    texto_fecha.config(text=date)

    texto_hora.after(1000, obtener_time)


texto_hora = Label(window, fg='aqua', bg='black')
texto_hora.grid(row=0, sticky="nsew", ipadx=5, ipady=20)

texto_dia = Label(window, fg='white', bg='gray2',
                  font=('Lucida Calligraphy', 20))
texto_dia.grid(row=1, sticky="nsew")

texto_fecha = Label(window, fg='green2', bg='gray3',
                    font=('Comic Sans MS', 20, 'bold'))
texto_fecha.grid(row=2, sticky="nsew")

obtener_time()

window.mainloop()
