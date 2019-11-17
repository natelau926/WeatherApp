import tkinter as tk
import requests
#Weather API
#4bc230b47769f8f60210ae97728367da
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print(entry)


def format_response(weather):
    try:
        name = (weather['name'])
        description = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])

        result = 'City: %s \nConditions: %s \nTemperature (F): %s' % (name, description, temp)
    except:
        result = 'There was a problem retrieving that information'

    return result

    return str(name) + ' ' + str(description) + ' ' + str(temp)


def get_weather(city):
    weather_key = '4bc230b47769f8f60210ae97728367da'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

# create a window
root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
frame = tk.Frame(root, bg='#99ddff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheigh=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheigh=1)

# create a button, you can use different function to change color, background color.. you name it
button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#99ddff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheigh=1)

root.mainloop()