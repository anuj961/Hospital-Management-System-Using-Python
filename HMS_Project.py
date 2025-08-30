import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os

# File to store user credentials
USER_FILE = "users.txt"

class GraphicalElements:
    @staticmethod
    def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    @staticmethod
    def draw_hospital_logo(canvas, x, y, size=100):
        # Draw a red cross as hospital logo
        canvas.create_line(x, y-size/2, x, y+size/2, fill='sky blue', width=10)
        canvas.create_line(x-size/2, y, x+size/2, y, fill='blue', width=10)

def ensure_user_file():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            f.write("")

class LoginWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hospital Management System - Login")
        self.window.geometry("400x600")
        self.window.configure(bg='#263238')

        # Create canvas for custom graphics
        self.canvas = tk.Canvas(self.window, width=400, height=600, bg='#263238', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        # Draw decorative elements
        GraphicalElements.create_rounded_rectangle(self.canvas, 50, 50, 350, 550, 
                                                 radius=20, fill='white', outline='#ddd')
        GraphicalElements.draw_hospital_logo(self.canvas, 200, 120)

        # Login form elements
        self.canvas.create_text(200, 200, text="Hospital Management System", 
                              font=('Helvetica', 16, 'bold'), fill='#333')

        # Username field
        self.canvas.create_text(200, 260, text="Username", font=('Helvetica', 12))
        self.username_entry = tk.Entry(self.window, font=('Helvetica', 12))
        self.canvas.create_window(200, 290, window=self.username_entry, width=200)

        # Password field
        self.canvas.create_text(200, 330, text="Password", font=('Helvetica', 12))
        self.password_entry = tk.Entry(self.window, show="*", font=('Helvetica', 12))
        self.canvas.create_window(200, 360, window=self.password_entry, width=200)

        # Buttons
        login_btn = tk.Button(self.window, text="Login", command=self.login,
                            bg='#4CAF50', fg='black', font=('Helvetica', 12),
                            relief='flat', width=15)
        self.canvas.create_window(200, 420, window=login_btn)

        register_btn = tk.Button(self.window, text="Register", command=self.open_register_window,
                               bg='#2196F3', fg='black', font=('Helvetica', 12),
                               relief='flat', width=15)
        self.canvas.create_window(200, 470, window=register_btn)

        emergency_btn = tk.Button(self.window, text="Emergency", command=self.request_ambulance,
                                bg='#f44336', fg='black', font=('Helvetica', 12),
                                relief='flat', width=15)
        self.canvas.create_window(200, 520, window=emergency_btn)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        with open(USER_FILE, "r") as f:
            users = [line.strip().split(",") for line in f.readlines()]
        
        if [username, password] in users:
            messagebox.showinfo("Success", "Login successful!")
            self.window.destroy()
            HospitalManagementSystem()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def open_register_window(self):
        RegisterWindow(self.window)

    def request_ambulance(self):
        messagebox.showinfo("Emergency", "Ambulance dispatched!\nHelp is on the way!")

    def run(self):
        self.window.mainloop()

class RegisterWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Register")
        self.window.geometry("400x500")
        self.window.configure(bg='#f0f0f0')

        # Create canvas for custom graphics
        self.canvas = tk.Canvas(self.window, width=400, height=500, bg='#f0f0f0', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        # Draw decorative elements
        GraphicalElements.create_rounded_rectangle(self.canvas, 50, 50, 350, 450, 
                                                 radius=20, fill='white', outline='#ddd')
        GraphicalElements.draw_hospital_logo(self.canvas, 200, 120)

        # Registration form
        self.canvas.create_text(200, 200, text="New User Registration", 
                              font=('Helvetica', 16, 'bold'), fill='#333')

        # Username field
        self.canvas.create_text(200, 260, text="Username", font=('Helvetica', 12))
        self.username_entry = tk.Entry(self.window, font=('Helvetica', 12))
        self.canvas.create_window(200, 290, window=self.username_entry, width=200)

        # Password field
        self.canvas.create_text(200, 330, text="Password", font=('Helvetica', 12))
        self.password_entry = tk.Entry(self.window, show="*", font=('Helvetica', 12))
        self.canvas.create_window(200, 360, window=self.password_entry, width=200)

        # Register button
        register_btn = tk.Button(self.window, text="Register", command=self.register,
                               bg='#4CAF50', fg='black', font=('Helvetica', 12),
                               relief='flat', width=15)
        self.canvas.create_window(200, 420, window=register_btn)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            with open(USER_FILE, "a") as f:
                f.write(f"{username},{password}\n")
            messagebox.showinfo("Success", "Registration successful!")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Please fill all fields!")

class HospitalManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hospital Management System")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')

        # Create main canvas
        self.canvas = tk.Canvas(self.root, bg='#f0f0f0', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        # Draw header
        GraphicalElements.create_rounded_rectangle(self.canvas, 20, 20, 1180, 100,
                                                 radius=15, fill='#2196F3', outline='')
        self.canvas.create_text(600, 60, text="Hospital Management System",
                              font=('Helvetica', 24, 'bold'), fill='white')

        # Create notebook with custom styling
        style = ttk.Style()
        style.configure('Custom.TNotebook', background='#f0f0f0')
        style.configure('Custom.TNotebook.Tab', padding=[10, 5], font=('Helvetica', 10))

        self.notebook = ttk.Notebook(self.root, style='Custom.TNotebook')
        self.notebook.place(x=20, y=120, width=1160, height=660)

        # Initialize tabs with custom graphics
        self.init_tabs()
        self.root.mainloop()

    def init_tabs(self):
        # Create and add tabs with custom styling
        tabs = ['Doctors', 'Patients', 'Staff', 'Rooms', 'Laboratory', 'Emergency', 'Payments']
        self.tab_frames = {}
        
        for tab_name in tabs:
            frame = ttk.Frame(self.notebook)
            self.tab_frames[tab_name] = frame
            self.notebook.add(frame, text=tab_name)
            
            # Add custom graphics for each tab
            canvas = tk.Canvas(frame, bg='white', highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            
            # Add tab-specific content
            self.setup_tab_content(tab_name, canvas)

    def setup_tab_content(self, tab_name, canvas):
        # Draw header for each tab
        GraphicalElements.create_rounded_rectangle(canvas, 20, 20, 1120, 80,
                                                 radius=10, fill='#f5f5f5', outline='#ddd')
        canvas.create_text(570, 50, text=f"{tab_name} Management",
                         font=('Helvetica', 16, 'bold'), fill='#333')

        # Add specific content based on tab type
        if tab_name == 'Emergency':
            self.setup_emergency_tab(canvas)
        elif tab_name == 'Payments':
            self.setup_payment_tab(canvas)
        else:
            self.setup_general_tab(canvas, tab_name)

    def setup_emergency_tab(self, canvas):
        emergency_btn = tk.Button(canvas, text="Request Emergency Ambulance",
                                command=lambda: messagebox.showinfo("Emergency", "Ambulance dispatched!"),
                                bg='#f44336', fg='black', font=('Helvetica', 14),
                                relief='flat', width=25)
        canvas.create_window(570, 200, window=emergency_btn)

    def setup_payment_tab(self, canvas):
        payment_var = tk.StringVar(value="Cash")
        methods = ['Cash', 'Card', 'UPI']
        y_pos = 150
        
        for method in methods:
            rb = ttk.Radiobutton(canvas, text=method, variable=payment_var, value=method)
            canvas.create_window(570, y_pos, window=rb)
            y_pos += 40

        confirm_btn = tk.Button(canvas, text="Confirm Payment",
                              command=lambda: messagebox.showinfo("Success", f"Payment confirmed: {payment_var.get()}"),
                              bg='#4CAF50', fg='black', font=('Helvetica', 12),
                              relief='flat', width=15)
        canvas.create_window(570, y_pos + 20, window=confirm_btn)

    def setup_general_tab(self, canvas, tab_name):
        # Create a frame for the treeview
        tree_frame = ttk.Frame(canvas)
        canvas.create_window(570, 300, window=tree_frame)

        # Create Treeview
        columns = self.get_columns_for_tab(tab_name)
        tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=10)
        
        # Configure columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        tree.pack(side='left', fill='both', expand=True)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scrollbar.set)

        # Add buttons
        btn_frame = ttk.Frame(canvas)
        canvas.create_window(570, 500, window=btn_frame)

        ttk.Button(btn_frame, text=f"Add {tab_name[:-1]}", 
                  command=lambda: self.show_add_dialog(tab_name, tree)).pack(side='left', padx=5)
        ttk.Button(btn_frame, text=f"Delete {tab_name[:-1]}", 
                  command=lambda: self.delete_item(tree)).pack(side='left', padx=5)

    def get_columns_for_tab(self, tab_name):
        columns = {
            'Doctors': ['ID', 'Name', 'Specialization', 'Phone', 'Address'],
            'Patients': ['ID', 'Name', 'Disease', 'Phone', 'Address'],
            'Staff': ['ID', 'Name', 'Position', 'Phone', 'Address'],
            'Rooms': ['Room No', 'Patient Name', 'Status'],
            'Laboratory': ['Test ID', 'Patient Name', 'Test Type', 'Status']
        }
        return columns.get(tab_name, ['ID', 'Name', 'Status'])

    def show_add_dialog(self, tab_name, tree):
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Add {tab_name[:-1]}")
        dialog.geometry("400x300")

        columns = self.get_columns_for_tab(tab_name)
        entries = {}

        for i, col in enumerate(columns):
            tk.Label(dialog, text=f"{col}:").grid(row=i, column=0, pady=5, padx=5)
            entries[col] = tk.Entry(dialog)
            entries[col].grid(row=i, column=1, pady=5, padx=5)

        def save():
            values = [entries[col].get() for col in columns]
            tree.insert('', 'end', values=values)
            dialog.destroy()

        tk.Button(dialog, text="Save", command=save).grid(row=len(columns), column=0, columnspan=2, pady=10)

    def delete_item(self, tree):
        selected_item = tree.selection()
        if selected_item:
            tree.delete(selected_item)
            messagebox.showinfo("Success", "Item deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select an item to delete!")

if __name__ == "__main__":
    ensure_user_file()
    app = LoginWindow()
    app.run()
