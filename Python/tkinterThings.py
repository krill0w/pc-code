import tkinter as tk

root = tk.Tk()

root.title("Tkinter")

msg = tk.Message(root, text = "poop")

def test_command():
  msg.pack()

tk.Button(root, text="What comes out of a bum?", command=test_command).pack()
tk.mainloop()