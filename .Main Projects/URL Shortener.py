import tkinter as tk
import pyshorteners
import pyperclip

def shorten_url():
    long_url = entry_long_url.get()
    short_url = shorten(long_url)
    entry_short_url.delete(0, tk.END)  # Clear previous content
    entry_short_url.insert(0, short_url)

def copy_short_url():
    short_url = entry_short_url.get()
    pyperclip.copy(short_url)

def shorten(url):
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        return short_url
    except pyshorteners.exceptions.ShorteningErrorException:
        return "Error: Unable to shorten URL"

# Create the main window
root = tk.Tk()
root.title("URL Shortener")

# Create the widgets
label_long_url = tk.Label(root, text="Long URL:")
label_long_url.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_long_url = tk.Entry(root, width=50)
entry_long_url.grid(row=0, column=1, padx=5, pady=5)

label_short_url = tk.Label(root, text="Short URL:")
label_short_url.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entry_short_url = tk.Entry(root, width=50)
entry_short_url.grid(row=1, column=1, padx=5, pady=5)

button_shorten = tk.Button(root, text="Shorten", command=shorten_url)
button_shorten.grid(row=2, column=1, padx=5, pady=5, sticky="e")

button_copy = tk.Button(root, text="Copy", command=copy_short_url)
button_copy.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Run the application
root.mainloop()
