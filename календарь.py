from tkinter import *
import calendar

window = Tk()
window.title('Календарь')
window.geometry('600x450')
while True:
    year = int(input("Year:"))
    month = int(input("Month:"))
    if month>=1 and month<=12:
        cal = calendar.TextCalendar(0)
        str = cal.formatmonth(year, month)
        lbl = Label(window, text=str, font = ('Arial Bold', 20))
        lbl.pack()
        break
    if month<1 or month>12:
        print("Text again")
window.mainloop()