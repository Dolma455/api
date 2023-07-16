
import tkinter as tk
from tkinter import messagebox
import login
import teacher_dashboard

class SchoolManagementSystemApp(tk.Tk):
    def __init__(self):
        super().__init__() 

        self.title("School Management System")
        self.geometry("800x600")

        self.current_page = "dashboard" 

        self.create_widgets()

    def create_widgets(self):
        # Create home page widgets
        if self.current_page == "dashboard":
            # Add more widgets for the dashboard
           
            self.title_label = tk.Label(self, text="School Management System", font=("Arial", 24), bg="white")
            self.title_label.pack(pady=50)

            self.login_button = tk.Button(self, text="Login", font=("Arial", 16), width=15, height=2, command=self.open_login)
            self.login_button.pack()

        elif self.current_page=="login":
            self.back_button = tk.Button(self, text="Back", command=self.open_dashboard)
            self.back_button.pack(side=tk.BOTTOM, pady=10)
    def open_dashboard(self):
        self.hide_widgets()  # Hide all existing widgets
        self.current_page = "dashboard"
        self.create_widgets()  # Recreate all the necessary widgets

    def hide_widgets(self):
        # Hide all the widgets in the teacher dashboard window
        for widget in self.winfo_children():
            widget.pack_forget()

    def open_login(self):
        # Hide the home page widgets
        self.title_label.pack_forget()
        self.login_button.pack_forget()

        # Create an instance of LoginPage and display it in the same window
        login_page = login.LoginPage(self)
        login_page.pack()

        # Create an instance of TeacherDashboard and display it in the same window
        teacher_dashboard = teacher_dashboard.TeacherDashboard(self, "username", show_home_page=True)
        teacher_dashboard.pack()

    def on_login(self, username, password):
    # Perform authentication and retrieve user role based on username and password
        role = self.authenticate(username, password)

        if role == "Teacher":
            # Create an instance of TeacherDashboard and display it in the same window
            teacher_dashboard = teacher_dashboard.TeacherDashboard(self, username, show_home_page=False)
            teacher_dashboard.pack()
        elif role == "Student":
            # Create an instance of StudentDashboard and display it in the same window
            student_dashboard = student_dashboard.StudentDashboard(self, username, show_home_page=False)
            student_dashboard.pack()
        elif role == "Staff":
            # Create an instance of StaffDashboard and display it in the same window
            staff_dashboard = staff_dashboard.StaffDashboard(self, username, show_home_page=False)
            staff_dashboard.pack()
        else:
            # Show error message if authentication fails
            messagebox.showerror("Error", "Invalid credentials")


    def show_home(self):
        # Show the home page widgets
        self.title_label.pack()
        self.login_button.pack()

        # Destroy any existing instances of TeacherDashboard
        for widget in self.winfo_children():
            if isinstance(widget, teacher_dashboard.TeacherDashboard):
                widget.destroy()

# Start the application
if __name__ == "__main__":
    app = SchoolManagementSystemApp()
    app.mainloop()



