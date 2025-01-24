import tkinter as tk
from tkinter import messagebox
import webbrowser

class AutoSearch:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Search")

        # Create search entry field
        self.search_label = tk.Label(root, text="Search:")
        self.search_label.pack()
        self.search_entry = tk.Entry(root, width=50)
        self.search_entry.pack()

        # Create buttons for different search platforms
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        self.youtube_button = tk.Button(self.button_frame, text="YouTube", command=self.search_youtube)
        self.youtube_button.pack(side=tk.LEFT)
        self.instagram_button = tk.Button(self.button_frame, text="Instagram", command=self.search_instagram)
        self.instagram_button.pack(side=tk.LEFT)
        self.google_button = tk.Button(self.button_frame, text="Google", command=self.search_google)
        self.google_button.pack(side=tk.LEFT)

    def search_youtube(self):
        search_query = self.search_entry.get()
        if search_query:
            url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(url)
        else:
            messagebox.showerror("Error", "Please enter a search query")

    def search_instagram(self):
        search_query = self.search_entry.get()
        if search_query:
            url = f"https://www.instagram.com/{search_query}/"
            webbrowser.open(url)
        else:
            messagebox.showerror("Error", "Please enter a search query")

    def search_google(self):
        search_query = self.search_entry.get()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
        else:
            messagebox.showerror("Error", "Please enter a search query")

if __name__ == "__main__":
    root = tk.Tk()
    auto_search = AutoSearch(root)
    root.mainloop()