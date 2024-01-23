# Ansel Newman

import tkinter as tk
from tkinter import ttk

import numpy as np
from PIL import Image, ImageTk
from scipy.stats import norm
from ttkthemes import ThemedStyle

N = norm.cdf

def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r * T) * N(d2)

def BS_PUT(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * N(-d2) - S * N(-d1)

def BS_CALL_DIV(S, K, T, r, q, sigma):
    d1 = (np.log(S / K) + (r - q + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * np.exp(-q * T) * N(d1) - K * np.exp(-r * T) * N(d2)

def BS_PUT_DIV(S, K, T, r, q, sigma):
    d1 = (np.log(S / K) + (r - q + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * N(-d2) - S * np.exp(-q * T) * N(-d1)

def calculate_option_value():
    try:
        # Get values from the entry widgets
        S_val = float(S.get())
        K_val = float(K.get())
        T_val = float(T.get())
        r_val = float(R.get())
        V_val = float(V.get())

        # Check the option type selected
        option_type = option_var.get()

        if option_type == "Call":
            result = BS_CALL(S_val, K_val, T_val, r_val, V_val)
        elif option_type == "Put":
            result = BS_PUT(S_val, K_val, T_val, r_val, V_val)
        elif option_type == "Call with Dividends":
            q_val = float(Q.get())
            result = BS_CALL_DIV(S_val, K_val, T_val, r_val, q_val, V_val)
        elif option_type == "Put with Dividends":
            q_val = float(Q.get())
            result = BS_PUT_DIV(S_val, K_val, T_val, r_val, q_val, V_val)
        else:
            result = None

        if result is not None:
            # Update the result label
            lbl_result.config(text=f"Estimated value: ${result:.2f}")
        else:
            lbl_result.config(text="Invalid option type selected.")

    except ValueError:
        # Handle invalid input (non-numeric)
        lbl_result.config(text="Invalid input. Please enter numeric values.")

def update_background(canvas, img_sequence, idx):
    img = img_sequence[idx]
    canvas.itemconfig(canvas_image, image=img)
    idx = (idx + 1) % len(img_sequence)
    window.after(100, update_background, canvas, img_sequence, idx)

def main():
    global S, K, T, R, V, Q, option_var, lbl_result, window, canvas_image

    window = tk.Tk()
    window.title("Black Scholes Calculator")

    # Apply ThemedStyle
    style = ThemedStyle(window)
    style.set_theme("equilux")

    # Load the GIF image
    img = Image.open("background_image.gif")  # Replace with the correct file name
    img = img.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
    img = ImageTk.PhotoImage(img)

    # Create a Canvas widget for the background image
    canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
    canvas.place(relx=0, rely=0, anchor="nw")
    canvas_image = canvas.create_image(0, 0, anchor="nw", image=img)

    # Start background update
    update_background(canvas, [img], 0)

    Title = ttk.Label(text="Black Scholes Calculator", font=("Helvetica", 16), foreground="white")
    Title.pack(pady=10)

    # Entry widgets for user input
    frm_entry_1 = ttk.Frame(master=window)
    S = ttk.Entry(master=frm_entry_1, width=40, font=("Helvetica", 12), foreground="white")
    lbl_S = ttk.Label(master=frm_entry_1, text="Current Asset Price", font=("Helvetica", 12), foreground="white")
    frm_entry_2 = ttk.Frame(master=window)
    K = ttk.Entry(master=frm_entry_2, width=40, font=("Helvetica", 12), foreground="white")
    lbl_K = ttk.Label(master=frm_entry_2, text="Strike Price", font=("Helvetica", 12), foreground="white")
    frm_entry_3 = ttk.Frame(master=window)
    R = ttk.Entry(master=frm_entry_3, width=40, font=("Helvetica", 12), foreground="white")
    lbl_R = ttk.Label(master=frm_entry_3, text="Risk-Free Rate", font=("Helvetica", 12), foreground="white")
    frm_entry_4 = ttk.Frame(master=window)
    T = ttk.Entry(master=frm_entry_4, width=40, font=("Helvetica", 12), foreground="white")
    lbl_T = ttk.Label(master=frm_entry_4, text="Time to Expiration (days)", font=("Helvetica", 12), foreground="white")
    frm_entry_5 = ttk.Frame(master=window)
    V = ttk.Entry(master=frm_entry_5, width=40, font=("Helvetica", 12), foreground="white")
    lbl_V = ttk.Label(master=frm_entry_5, text="Volatility", font=("Helvetica", 12), foreground="white")
    frm_entry_6 = ttk.Frame(master=window)
    Q = ttk.Entry(master=frm_entry_6, width=40, font=("Helvetica", 12), foreground="white")
    lbl_Q = ttk.Label(master=frm_entry_6, text="Dividend Yield (for options with dividends)", font=("Helvetica", 12), foreground="white")

    # Option type selection
    option_var = tk.StringVar(value="Call")
    option_types = ["Call", "Put", "Call with Dividends", "Put with Dividends"]
    option_menu = ttk.Combobox(window, textvariable=option_var, values=option_types, font=("Helvetica", 12))
    option_menu.set("Call")

    # Button and functional Logic
    btn_convert = ttk.Button(
        master=window,
        text="Calculate",
        command=calculate_option_value,
        style="TButton"
    )

    lbl_result = ttk.Label(master=window, text="Estimated value ($)", font=("Helvetica", 14), foreground="white")

    # Layout
    frm_entry_1.pack(pady=5)
    lbl_S.pack()
    S.pack()

    frm_entry_2.pack(pady=5)
    lbl_K.pack()
    K.pack()

    frm_entry_3.pack(pady=5)
    lbl_R.pack()
    R.pack()

    frm_entry_4.pack(pady=5)
    lbl_T.pack()
    T.pack()

    frm_entry_5.pack(pady=5)
    lbl_V.pack()
    V.pack()

    frm_entry_6.pack(pady=5)
    lbl_Q.pack()
    Q.pack()

    option_menu.pack(pady=10)
    btn_convert.pack(pady=10)
    lbl_result.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
