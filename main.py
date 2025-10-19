from request import get_coordinates, get_weather
import tkinter as tk
def fetch_weather():
    city_name = city_entry.get()
    lat, lon = get_coordinates(city_name)
    if lat and lon:
        result = get_weather(lat, lon)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(result))
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "City not found.")

root = tk.Tk()
root.title("Weather Analyzer")
root.geometry("500x400")

tk.Label(root, text="Enter City Name:").pack(pady=10)
city_entry = tk.Entry(root, width=30)
city_entry.pack()

tk.Button(root, text="Get Weather", command=fetch_weather).pack(pady=10)

result_text = tk.Text(root, height=15, width=60)
result_text.pack(pady=10)

root.mainloop()