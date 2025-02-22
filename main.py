import tkinter as tk
from tkinter import ttk

class DigitalNotebook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Notebook")
        self.geometry("800x600")

        self.pages = []
        self.current_page = 0

        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(self, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill='x')

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.prev_page)
        self.prev_button.pack(side='left')

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_page)
        self.next_button.pack(side='right')

        self.new_page_button = tk.Button(self.button_frame, text="New Page", command=self.new_page)
        self.new_page_button.pack(side='left')

        self.load_page()

    def load_page(self):
        if self.pages:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, self.pages[self.current_page])
        else:
            self.text_area.delete(1.0, tk.END)

    def save_page(self):
        if len(self.pages) > self.current_page:
            self.pages[self.current_page] = self.text_area.get(1.0, tk.END)
        else:
            self.pages.append(self.text_area.get(1.0, tk.END))

    def prev_page(self):
        if self.current_page > 0:
            self.save_page()
            self.current_page -= 1
            self.load_page()

    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.save_page()
            self.current_page += 1
            self.load_page()

    def new_page(self):
        self.save_page()
        self.current_page = len(self.pages)
        self.pages.append("")
        self.load_page()

if __name__ == "__main__":
    app = DigitalNotebook()
    app.mainloop()