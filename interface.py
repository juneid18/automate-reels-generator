import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def save_script():
    script_content = script_text.get("1.0", tk.END)
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if file_path:
        with open(file_path, 'w') as file:
            file.write(script_content)
        status_label.config(text=f"Script saved to {file_path}", foreground="green")
    else:
        status_label.config(text="Save canceled", foreground="red")

# Create the main window
root = tk.Tk()
root.title("Video Script Form")

# Styling
style = ttk.Style()
style.configure("TFrame", background="#333")
style.configure("TLabel", background="#333", foreground="white", font=("Arial", 12))
style.configure("TButton", background="#4CAF50", foreground="white", font=("Arial", 12))
style.configure("TText", font=("Arial", 12))

# Create and place widgets in the window
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

script_label = ttk.Label(frame, text="Enter your video script:")
script_label.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)

script_text = tk.Text(frame, wrap="word", width=50, height=10)
script_text.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.W)

save_button = ttk.Button(frame, text="Generate", command=save_script)
save_button.grid(row=2, column=0, columnspan=2, pady=10)

status_label = ttk.Label(frame, text="", foreground="black")
status_label.grid(row=3, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
