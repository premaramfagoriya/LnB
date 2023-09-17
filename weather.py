import tkinter as tk
import requests

root=tk.Tk()

def show_info():

    city_name=t1.get()
    api_key="be7a6268cda2f463ca579cfd91ba3245"
    weather=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

    print(weather)


    if weather.json()["cod"]=="404":
        print("Enter correct city name")
    else:
        w=weather.json()["weather"][0]["main"]
        l2=tk.Label(root,text=f"Waether of {city_name} is {w}")
        t=weather.json()["main"]["temp"]
        l3=tk.Label(root,text=f"Weather of {city_name} is {w}")
        l2.grid(row=1,column=1)
        l3.grid(row=2,column=1)
    


l1=tk.Label(root,text="City Name")
t1=tk.Entry(root)
b1=tk.Button(text="Submit",command=show_info)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
b1=b1.grid(row=0,column=2)
tk.mainloop()