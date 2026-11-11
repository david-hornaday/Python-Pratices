import tkinter as tk

#window
root = tk.Tk()
root.title("Mouse Click Counter")
root.geometry("300x200")

#counts the total clicks
count = 0

def count_click():
    global count
    count += 1
    label.config(text=f"Clicks: {count}")

#text on button
label = tk.Label(root, text="Clicks: 0", font=("Arial", 30))
label.pack(pady=20)

#button to count clicks
button = tk.Button(root, text="Click me", command=count_click, font=("Arial", 21))
button.pack(pady=10)

#runs the program
root.mainloop()