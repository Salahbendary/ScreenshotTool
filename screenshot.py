import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot Tool")

        # Set a minimum window size
        self.root.minsize(400, 250)

        # Create a frame to contain the widgets
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Create a label with the tool creator's name
        self.creator_label = tk.Label(self.frame, text="Screenshot Tool created by Salah Bendary", font=("Arial", 12))
        self.creator_label.pack(pady=(0, 10))

        # URL entry
        self.url_label = tk.Label(self.frame, text="Enter URL:", font=("Arial", 12))
        self.url_label.pack(pady=(0, 5))
        self.url_entry = tk.Entry(self.frame, width=50, font=("Arial", 12))
        self.url_entry.pack(pady=(0, 10))

        # File name entry
        self.filename_label = tk.Label(self.frame, text="Enter file name (without extension):", font=("Arial", 12))
        self.filename_label.pack(pady=(0, 5))
        self.filename_entry = tk.Entry(self.frame, width=50, font=("Arial", 12))
        self.filename_entry.pack(pady=(0, 10))

        # Create a button to take the screenshot
        self.button = tk.Button(self.frame, text="Take Screenshot", command=self.take_screenshot, font=("Arial", 12))
        self.button.pack(pady=(0, 10))

        # Create a label to display the result
        self.result_label = tk.Label(self.frame, text="", font=("Arial", 10))
        self.result_label.pack()

    def take_screenshot(self):
        url = self.url_entry.get()
        file_name = self.filename_entry.get()

        if not url or not file_name:
            messagebox.showerror("Error", "Please enter both URL and file name.")
            return

        screenshot_path = f'{file_name}.png'

        try:
            # Configure the webdriver
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

            # Navigate to the website
            driver.get(url)

            # Take a screenshot
            driver.save_screenshot(screenshot_path)

            # Close the browser
            driver.quit()

            # Update the result label
            self.result_label.config(text=f"Screenshot saved to {screenshot_path}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
