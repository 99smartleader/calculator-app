import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.configure(bg='black')
        

        # set the window size and disable resizing
        self.master.geometry("400x500")
        self.master.resizable(0, 0)

        # create the display widget
        self.display = tk.Entry(master, width=30, font=('Arial', 24))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # create buttons for numbers and operators
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+', 'C', 'Ans', 'clrAns'
        ]
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.handle_click(x)
            tk.Button(master, text=button, width=5, height=2, background="black",foreground="white", font=('Arial', 16), command=command).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.prev_ans = None
        # bind the Enter key to the equal button
        master.bind("<Return>", lambda event: self.handle_click('='))

        # create a menu bar
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        # create a File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # create an Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Copy", command=self.copy_result, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_number, accelerator="Ctrl+V")
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # create a Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        # bind keyboard shortcuts
        master.bind("<Control-c>", lambda event: self.copy_result())
        master.bind("<Control-v>", lambda event: self.paste_number())

        # create a status bar
        self.statusbar = tk.Label(master, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        #self.statusbar.grid(row=0, column=0, columnspan=3, sticky="ew")

    def handle_click(self, key):
        if key == '=':
            # evaluate the expression
            try:
                result = str(eval(self.display.get()))
                self.prev_ans = result
            except:
                result = "ERROR"
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        elif key == 'C':
            # clear the display
            self.display.delete(0, tk.END)
        elif key == 'Ans':
            if self.prev_ans:
                self.display.insert(tk.END, str(self.prev_ans))
        elif key == 'clrAns':
            self.prev_ans = None
        else:
            # append the key to the end of the display
            self.display.insert(tk.END, key)

    def copy_result(self):
        # copy the result to the clipboard
        self.master.clipboard_clear()
        self.master.clipboard_append(self.display.get())
        self.statusbar.configure(text="Result copied to clipboard")

    def paste_number(self):
        # insert the contents of the clipboard into the display
        self.display.insert(tk.END, self.master.clipboard_get())

    def show_about(self):
        # display an about message box
        messagebox.showinfo("About Calculator", "This is a simple calculator application.")


