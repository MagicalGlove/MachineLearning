import tkinter as tk
import requests

def predict():
    url = 'http://127.0.0.1:5000/predict'  # Change this if your Flask app runs on a different port
    data = {
    'color': color_entry.get(),
    'depth': depth_entry.get(),
    'table': table_entry.get(),
    'carat': carat_entry.get(),
    'cut': cut_entry.get(),
    'clarity': clarity_entry.get(),
    'x': x_entry.get(),
    'y': y_entry.get(),
    'z': z_entry.get()
}
    response = requests.post(url, json=data)
    result_label.config(text=response.json()['result'])

root = tk.Tk()
root.title("DIAMOND PRICE EVALUATION!!!")
root.geometry("400x300")  # Set width x height

def create_entry_with_label(root, label_text):
    frame = tk.Frame(root)
    frame.pack(pady=5)  # Add padding between frames
    frame.pack()
    
    label = tk.Label(frame, text=label_text)
    label.pack(side="left")

    entry = tk.Entry(frame)
    entry.pack(side="left")
    
    return entry

# Create entry fields with labels
carat_entry = create_entry_with_label(root, "Carat: ")
cut_entry = create_entry_with_label(root, "Cut: ")
clarity_entry = create_entry_with_label(root, "Clarity: ")
color_entry = create_entry_with_label(root, "Color: ")
depth_entry = create_entry_with_label(root, "Depth: ")
table_entry = create_entry_with_label(root, "Table: ")
x_entry = create_entry_with_label(root, "X: ")
y_entry = create_entry_with_label(root, "Y: ")
z_entry = create_entry_with_label(root, "Z: ")

predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()