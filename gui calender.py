import calendar
from tkinter import *
from tkinter import messagebox


class EnhancedCalendarApp:

    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calendar Pro")
        self.root.geometry("380x320")

        # Track theme state (True for Dark Mode, False for Light Mode)
        self.dark_mode = False

        # Define color palettes
        self.themes = {
            "light": {
                "bg": "#f0f0f0",
                "accent1": "#ffb6c1",  # Light Pink
                "accent2": "#add8e6",  # Light Blue
                "btn_bg": "#333333",
                "btn_fg": "#ffffff",
                "text": "#000000",
            },
            "dark": {
                "bg": "#1e1e1e",
                "accent1": "#ff6b81",  # Vibrant Pink
                "accent2": "#70a1ff",  # Vibrant Blue
                "btn_bg": "#ffffff",
                "btn_fg": "#1e1e1e",
                "text": "#ffffff",
            },
        }

        # Main Layout Setup
        self.root.configure(background=self.themes["light"]["bg"])
        self.create_widgets()

    def create_widgets(self):
        current_theme = self.themes["light"]

        # Theme Toggle Button
        self.theme_btn = Button(
            self.root,
            text="🌙 Dark Mode",
            font=("Arial", 10, "bold"),
            command=self.toggle_theme,
            bg=current_theme["btn_bg"],
            fg=current_theme["btn_fg"],
        )
        self.theme_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="e")

        # Title App Label
        self.name_label = Label(
            self.root,
            text="Advanced Calendar",
            bg=current_theme["accent1"],
            fg="#000000",
            font=("Arial", 18, "bold"),
            padx=10,
            pady=5,
        )
        self.name_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Year Inputs
        self.year_label = Label(
            self.root,
            text="Enter Year (YYYY):",
            bg=current_theme["accent2"],
            fg="#000000",
            font=("Arial", 12, "bold"),
            padx=5,
        )
        self.year_label.grid(row=2, column=0, pady=5, padx=10, sticky="e")

        self.year_entry = Entry(self.root, font=("Arial", 12, "bold"), width=10)
        self.year_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w")
        self.year_entry.insert(0, "2026")  # Default placeholder

        # Month Inputs
        self.month_label = Label(
            self.root,
            text="Enter Month (1-12):",
            bg=current_theme["accent2"],
            fg="#000000",
            font=("Arial", 12, "bold"),
            padx=5,
        )
        self.month_label.grid(row=3, column=0, pady=5, padx=10, sticky="e")

        self.month_entry = Entry(self.root, font=("Arial", 12, "bold"), width=10)
        self.month_entry.grid(row=3, column=1, pady=5, padx=10, sticky="w")
        self.month_entry.insert(0, "1")  # Default placeholder

        # Actions Buttons Frame
        self.btn_frame = Frame(self.root, bg=current_theme["bg"])
        self.btn_frame.grid(row=4, column=0, columnspan=2, pady=15)

        self.show_year_btn = Button(
            self.btn_frame,
            text="Show Full Year",
            fg="white",
            bg="#2ed573",
            font=("Arial", 11, "bold"),
            command=self.show_year_calendar,
        )
        self.show_year_btn.pack(side=LEFT, padx=5)

        self.show_month_btn = Button(
            self.btn_frame,
            text="Show Month",
            fg="white",
            bg="#1e90ff",
            font=("Arial", 11, "bold"),
            command=self.show_month_calendar,
        )
        self.show_month_btn.pack(side=LEFT, padx=5)

        self.check_leap_btn = Button(
            self.btn_frame,
            text="Leap Year?",
            fg="white",
            bg="#ffa502",
            font=("Arial", 11, "bold"),
            command=self.check_leap_year,
        )
        self.check_leap_btn.pack(side=LEFT, padx=5)

    def get_valid_year(self):
        try:
            return int(self.year_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric year.")
            return None

    def get_valid_month(self):
        try:
            month = int(self.month_entry.get())
            if 1 <= month <= 12:
                return month
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter a valid month between 1 and 12."
            )
            return None

    def show_year_calendar(self):
        year = self.get_valid_year()
        if year is None:
            return

        theme = self.themes["dark"] if self.dark_mode else self.themes["light"]

        window = Toplevel(self.root)
        window.configure(background=theme["bg"])
        window.title(f"Calendar - Year {year}")
        window.geometry("640x640")

        window_content = calendar.calendar(year)
        year_cal = Label(
            window,
            text=window_content,
            font=("Courier", 11, "bold"),
            justify=LEFT,
            bg=theme["bg"],
            fg=theme["text"],
        )
        year_cal.pack(padx=10, pady=10, fill=BOTH, expand=True)

    def show_month_calendar(self):
        year = self.get_valid_year()
        month = self.get_valid_month()
        if year is None or month is None:
            return

        theme = self.themes["dark"] if self.dark_mode else self.themes["light"]

        window = Toplevel(self.root)
        window.configure(background=theme["bg"])
        window.title(f"{calendar.month_name[month]} {year}")
        window.geometry("320x240")

        window_content = calendar.month(year, month)
        month_cal = Label(
            window,
            text=window_content,
            font=("Courier", 14, "bold"),
            justify=LEFT,
            bg=theme["bg"],
            fg=theme["text"],
        )
        month_cal.pack(padx=20, pady=20, fill=BOTH, expand=True)

    def check_leap_year(self):
        year = self.get_valid_year()
        if year is None:
            return

        if calendar.isleap(year):
            messagebox.showinfo(
                "Leap Year Checker", f"🎉 Yes! {year} is a leap year (366 days)."
            )
        else:
            messagebox.showinfo(
                "Leap Year Checker",
                f"❌ No. {year} is a standard year (365 days).",
            )

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        theme = self.themes["dark"] if self.dark_mode else self.themes["light"]

        # Update root and buttons
        self.root.configure(background=theme["bg"])
        self.btn_frame.configure(background=theme["bg"])

        if self.dark_mode:
            self.theme_btn.config(
                text="☀️ Light Mode", bg=theme["btn_bg"], fg=theme["btn_fg"]
            )
        else:
            self.theme_btn.config(
                text=" 🌙 Dark Mode", bg=theme["btn_bg"], fg=theme["btn_fg"]
            )

        # Update dynamic coloring label accents
        self.name_label.config(bg=theme["accent1"])
        self.year_label.config(bg=theme["accent2"])
        self.month_label.config(bg=theme["accent2"])


if __name__ == "__main__":
    root = Tk()
    app = EnhancedCalendarApp(root)
    root.mainloop()