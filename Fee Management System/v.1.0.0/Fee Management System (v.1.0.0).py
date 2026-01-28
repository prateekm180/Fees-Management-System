import tkinter as tk
from tkinter import ttk, messagebox

class ThemeManager:
    LIGHT = {
        "bg": "#f5f5f5",
        "fg": "#000000",
        "card": "#ffffff",
        "accent": "#4a90e2",
        "entry": "#ffffff"
    }

    DARK = {
        "bg": "#121212",
        "fg": "#ffffff",
        "card": "#1e1e1e",
        "accent": "#4a90e2",
        "entry": "#2b2b2b"
    }

class FeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fee Management System")
        self.root.geometry("900x550")
        self.root.resizable(False, False)

        self.dark_mode = False
        self.theme = ThemeManager.LIGHT

        self.setup_styles()
        self.build_ui()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("default")

    def build_ui(self):
        self.root.configure(bg=self.theme["bg"])

        # Header
        header = tk.Frame(self.root, bg=self.theme["bg"])
        header.pack(fill="x", pady=10)

        tk.Label(
            header, text="Fee Management System",
            font=("Segoe UI", 20, "bold"),
            bg=self.theme["bg"], fg=self.theme["fg"]
        ).pack(side="left", padx=20)

        self.toggle_btn = ttk.Button(
            header, text="🌙 Night Mode", command=self.toggle_theme
        )
        self.toggle_btn.pack(side="right", padx=20)

        # Main container
        container = tk.Frame(self.root, bg=self.theme["bg"])
        container.pack(fill="both", expand=True, padx=20)

        # Left Card (Form)
        self.form_card = tk.Frame(container, bg=self.theme["card"], bd=0)
        self.form_card.place(x=0, y=0, width=350, height=400)

        tk.Label(
            self.form_card, text="Add Fee Record",
            font=("Segoe UI", 14, "bold"),
            bg=self.theme["card"], fg=self.theme["fg"]
        ).pack(pady=15)

        self.name_entry = self.create_entry("Student Name")
        self.class_entry = self.create_entry("Class")
        self.amount_entry = self.create_entry("Fee Amount")

        ttk.Button(
            self.form_card, text="Add Record",
            command=self.add_record
        ).pack(pady=20)

        # Right Card (Table)
        self.table_card = tk.Frame(container, bg=self.theme["card"])
        self.table_card.place(x=380, y=0, width=480, height=400)

        tk.Label(
            self.table_card, text="Fee Records",
            font=("Segoe UI", 14, "bold"),
            bg=self.theme["card"], fg=self.theme["fg"]
        ).pack(pady=10)

        self.table = ttk.Treeview(
            self.table_card,
            columns=("Name", "Class", "Amount"),
            show="headings"
        )
        self.table.heading("Name", text="Name")
        self.table.heading("Class", text="Class")
        self.table.heading("Amount", text="Amount")

        self.table.pack(fill="both", expand=True, padx=10, pady=10)

    def create_entry(self, label_text):
        frame = tk.Frame(self.form_card, bg=self.theme["card"])
        frame.pack(pady=8, padx=20, fill="x")

        tk.Label(
            frame, text=label_text,
            bg=self.theme["card"], fg=self.theme["fg"]
        ).pack(anchor="w")

        entry = tk.Entry(
            frame,
            bg=self.theme["entry"],
            fg=self.theme["fg"],
            insertbackground=self.theme["fg"],
            relief="flat"
        )
        entry.pack(fill="x", pady=5)
        return entry

    def add_record(self):
        name = self.name_entry.get()
        cls = self.class_entry.get()
        amt = self.amount_entry.get()

        if not name or not cls or not amt:
            messagebox.showerror("Error", "All fields required")
            return

        self.table.insert("", "end", values=(name, cls, amt))

        self.name_entry.delete(0, "end")
        self.class_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.theme = ThemeManager.DARK if self.dark_mode else ThemeManager.LIGHT
        self.root.destroy()
        root = tk.Tk()
        FeeApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = FeeApp(root)
    root.mainloop()
