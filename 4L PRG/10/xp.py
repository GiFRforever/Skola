import tkinter as tk
from tkinter import ttk


def create_xp_theme():
    xp_theme = ttk.Style()
    xp_theme.theme_use("winnative")
    return xp_theme


def create_xp_window():
    xp_window = tk.Tk()
    xp_window.title("Windows XP Style App")

    xp_theme = create_xp_theme()

    # Customize specific widgets if needed
    xp_theme.configure("TButton", padding=(5, 2), font=("Arial", 10))
    xp_theme.map(
        "TButton",
        foreground=[("pressed", "black"), ("active", "blue")],
        background=[("pressed", "!disabled", "gray"), ("active", "white")],
    )

    return xp_window


if __name__ == "__main__":
    xp_window = create_xp_window()

    # Add your widgets and functionality here

    xp_window.mainloop()
