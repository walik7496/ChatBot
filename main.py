import tkinter as tk
from tkinter import scrolledtext
import os

class ChatBot:
    def __init__(self, master):
        self.master = master
        master.title("Chat Bot")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.chat_history.pack(expand=True, fill="both")

        self.input_field = tk.Entry(master, width=40)
        self.input_field.pack(side=tk.LEFT, expand=True, fill="x")

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        self.input_field.bind("<Return>", self.send_on_enter)

        self.responses = {}

        if os.path.exists("responses.txt"):
            with open("responses.txt", "r") as file:
                for line in file:
                    key, value = line.strip().split(":")
                    self.responses[key.strip()] = value.strip()

    def send_message(self):
        user_input = self.input_field.get()
        self.chat_history.insert(tk.END, "You: " + user_input + "\n")
        self.input_field.delete(0, tk.END)
        if user_input.lower() in self.responses:
            response = self.responses[user_input.lower()]
            self.chat_history.insert(tk.END, "Bot: " + response + "\n")
        else:
            self.chat_history.insert(tk.END, "Bot: Sorry, I don't understand.\n")
        self.chat_history.see(tk.END)

    def send_on_enter(self, event):
        self.send_message()

    def save_responses(self):
        with open("responses.txt", "w") as file:
            for key, value in self.responses.items():
                file.write(f"{key}: {value}\n")

    def add_response(self, key, value):
        self.responses[key.lower()] = value
        self.save_responses()

root = tk.Tk()
chat_bot = ChatBot(root)
root.mainloop()