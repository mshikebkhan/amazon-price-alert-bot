import smtplib
from tkinter import messagebox

def send_email(user_email, user_password, recipient_email, product_url, price):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user_email, user_password)

        subject = "Amazon Price Drop Alert!"
        body = f"Your product is now available at ₹{price}!\nCheck here: {product_url}"
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(user_email, recipient_email, message)
        server.quit()
        
        messagebox.showinfo("Email Sent", f"Price drop alert sent to {recipient_email}!")

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Email Error", "Authentication failed! Check your email and password.")
    
    except smtplib.SMTPException as e:
        messagebox.showerror("Email Error", f"Failed to send email: {e}")
