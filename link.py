import tkinter as tk
import pyshorteners

# Create GUI window
window = tk.Tk()
window.title("Link Shortener")

# Create label
label = tk.Label(window, text="Enter a URL to shorten:")
label.pack()

# Create entry box
entry = tk.Entry(window)
entry.pack()

# Create button
def shorten_link():
    url = entry.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    tk.messagebox.showinfo("Shortened Link", shortened_url)

button = tk.Button(window, text="Shorten", command=shorten_link)
button.pack()

# Run GUI window
window.mainloop()
