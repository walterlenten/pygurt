import tkinter as tk
from tkinter import messagebox
import time

class PinCrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PIN Cracker")
        
        self.label = tk.Label(root, text="Enter PIN (4 digits):")
        self.label.pack(pady=10)

        self.pin_entry = tk.Entry(root)
        self.pin_entry.pack(pady=5)
        
        self.crack_button = tk.Button(root, text="Crack PIN", command=self.crack_pin)
        self.crack_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
    
    def crack_pin(self):
        entered_pin = self.pin_entry.get()
        if not entered_pin.isdigit() or len(entered_pin) != 4:
            messagebox.showerror("Error", "Please enter a valid 4-digit PIN.")
            return
        
        start_time = time.time()
        
        for pin in range(10000): #why the fuck does this not work?
            attempt = f"{pin:04d}"
            self.result_label.config(text=f"Trying: {attempt}")
            self.root.update()
            time.sleep(0.001)
            
            if attempt == entered_pin:
                end_time = time.time()
                time_taken = end_time - start_time
                self.result_label.config(text=f"PIN {entered_pin} cracked in {time_taken:.2f} seconds.")
                break
        else:
            self.result_label.config(text="Failed to crack the PIN.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PinCrackerApp(root)
    root.mainloop()