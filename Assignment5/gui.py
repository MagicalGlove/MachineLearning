import tkinter as tk
import requests

def chat():
    url = 'http://127.0.0.1:5000/chat'  # Change this if your Flask app runs on a different port
    data = {
    'query': query_entry.get(),
}
    response = requests.post(url, json=data)
    result_label.config(text=response.json()['result'])

root = tk.Tk()
root.title("Warhammer lore chat bot")
root.geometry("640x480")  

def create_entry_with_label(root, label_text):
    frame = tk.Frame(root)
    frame.pack(pady=10)  
    frame.pack()
    
    label = tk.Label(frame, text=label_text)
    label.pack(side="left")

    entry = tk.Entry(frame, width=70)
    entry.pack(side="left")
    
    return entry

query_entry = create_entry_with_label(root, "Ask away: ")

predict_button = tk.Button(root, text="Send", command=chat)
predict_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()