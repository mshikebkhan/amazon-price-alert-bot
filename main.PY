import tkinter as tk
from tkinter import messagebox
import threading
import time
from price_checker import check_price

def start_tracking():
    amazon_url = url_entry.get()
    buy_price = price_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()
    target_email = target_email_entry.get().strip()  # Get recipient email

    if not amazon_url or not buy_price.isdigit() or not user_email or not user_password:
        messagebox.showerror("Input Error", "Please enter all required details.")
        return

    # If no recipient email is provided, use the user's email
    recipient_email = target_email if target_email else user_email

    def run_checker():
        while True:
            check_price(amazon_url, int(buy_price), user_email, user_password, recipient_email)
            time.sleep(3600)  # Check price every hour

    threading.Thread(target=run_checker, daemon=True).start()
    messagebox.showinfo("Tracking Started", "The bot will check the price every hour.")

# GUI Setup
root = tk.Tk()
root.title("Amazon Price Alert BOT")
root.geometry("400x400")

tk.Label(root, text="Amazon Product URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Label(root, text="Buy Price (₹):").pack(pady=5)
price_entry = tk.Entry(root, width=20)
price_entry.pack(pady=5)

tk.Label(root, text="Your Email:").pack(pady=5)
email_entry = tk.Entry(root, width=50)
email_entry.pack(pady=5)

tk.Label(root, text="Your Email Password:").pack(pady=5)
password_entry = tk.Entry(root, width=50, show="*")  # Hide password input
password_entry.pack(pady=5)

tk.Label(root, text="Recipient Email (optional):").pack(pady=5)
target_email_entry = tk.Entry(root, width=50)  # New input field for optional recipient email
target_email_entry.pack(pady=5)

track_button = tk.Button(root, text="Start Tracking", command=start_tracking)
track_button.pack(pady=10)

root.mainloop()
