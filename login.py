import tkinter as tk
import mysql.connector
import tkinter.messagebox as messagebox
import home
import student_dashboard
import teacher_dashboard
import staff_dashboard
import admin_dashboard

# Database connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="school_management_system"
)
cursor = db.cursor()


class LoginPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        # Create login page widgets
        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

        self.back_button = tk.Button(self, text="Back", command=self.back)
        self.back_button.pack()

    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Query the respective tables to validate the user credentials and determine the designation
        designation = None

        # Check if the user is a Teacher
        query = "SELECT * FROM teachers WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result:
            designation = "Teacher"

        # Check if the user is a Student
        if not designation:
            query = "SELECT * FROM students WHERE username = %s AND password = %s"
            cursor.execute(query, values)
            result = cursor.fetchone()
            if result:
                designation = "Student"

        # Check if the user is an Admin
        if not designation:
            query = "SELECT * FROM admins WHERE username = %s AND password = %s"
            cursor.execute(query, values)
            result = cursor.fetchone()
            if result:
                designation = "Admin"

        # Check if the user is a Non-teaching Staff
        if not designation:
            query = "SELECT * FROM non_teaching_staff WHERE username = %s AND password = %s"
            cursor.execute(query, values)
            result = cursor.fetchone()
            if result:
                designation = "Non-teaching Staff"

        if designation:
            # If the user credentials are valid and the role is determined, open the respective dashboard
            if designation == "Teacher":
                # Open the teacher dashboard
                self.open_teacher_dashboard(username)
            elif designation == "Student":
                # Open the student dashboard
                self.open_student_dashboard(username)
            elif designation == "Admin":
                # Open the admin dashboard
                self.open_admin_dashboard(username)
            elif designation == "Non-teaching Staff":
                # Open the non-teaching staff dashboard
                self.open_non_teaching_staff_dashboard(username)

        else:
            # If the user credentials are invalid, show an error message
            messagebox.showerror("Login Failed", "Invalid username or password")

    def back(self):
        self.pack_forget()
        home.show_home(self.parent)

    def open_teacher_dashboard(self, username):
        self.pack_forget()

        # Create the teacher dashboard page
        teacher_dashboard.TeacherDashboard(self.parent, username)

    def open_student_dashboard(self, username):
        # Implement the student dashboard opening logic
        self.pack_forget()

        # Create the student dashboard page
        student_dashboard.StudentDashboard(self.parent, username)

    def open_admin_dashboard(self, username):
        self.pack_forget()

        # Create the admin dashboard page
        admin_dashboard.AdminDashboard(self.parent, username)

    def open_non_teaching_staff_dashboard(self, username):
        # Implement the non-teaching staff dashboard opening logic
        self.pack_forget()

        # Create the non-teaching staff dashboard page
        staff_dashboard.StaffDashboard(self.parent, username)


if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    login_page.pack()
    root.mainloop()


# import tkinter as tk
# import mysql.connector
# import tkinter.messagebox as messagebox
# import home
# import teacher_dashboard
# import student_dashboard
# import staff_dashboard
# import admin_dashboard

# # Database connection setup
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="school_management_system"
# )
# cursor = db.cursor()


# class LoginPage(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)

#         self.parent = parent

#         self.create_widgets()

#     def create_widgets(self):
#         # Create login page widgets
#         self.username_label = tk.Label(self, text="Username")
#         self.username_label.pack()

#         self.username_entry = tk.Entry(self)
#         self.username_entry.pack()

#         self.password_label = tk.Label(self, text="Password")
#         self.password_label.pack()

#         self.password_entry = tk.Entry(self, show="*")
#         self.password_entry.pack()

#         self.login_button = tk.Button(self, text="Login", command=self.login)
#         self.login_button.pack()

#         self.back_button = tk.Button(self, text="Back", command=self.back)
#         self.back_button.pack()

#     def login(self):
#         # Get the entered username and password
#         username = self.username_entry.get()
#         password = self.password_entry.get()

#         # Query the respective tables to validate the user credentials and determine the designation
#         designation = None

#         # Check if the user is a Teacher
#         query = "SELECT * FROM teachers WHERE username = %s AND password = %s"
#         values = (username, password)
#         cursor.execute(query, values)
#         result = cursor.fetchone()
#         if result:
#             designation = "Teacher"

#         # Check if the user is a Student
#         if not designation:
#             query = "SELECT * FROM students WHERE username = %s AND password = %s"
#             cursor.execute(query, values)
#             result = cursor.fetchone()
#             if result:
#                 designation = "Student"

#         # Check if the user is an Admin
#         if not designation:
#             query = "SELECT * FROM admins WHERE username = %s AND password = %s"
#             cursor.execute(query, values)
#             result = cursor.fetchone()
#             if result:
#                 designation = "Admin"

#         # Check if the user is a Non-teaching Staff
#         if not designation:
#             query = "SELECT * FROM non_teaching_staff WHERE username = %s AND password = %s"
#             cursor.execute(query, values)
#             result = cursor.fetchone()
#             if result:
#                 designation = "Non-teaching Staff"

#         if designation:
#             # If the user credentials are valid and the role is determined, open the respective dashboard
#             if designation == "Teacher":
#                 # Open the teacher dashboard
#                 self.open_teacher_dashboard(username)
#             elif designation == "Student":
#                 # Open the student dashboard
#                 self.open_student_dashboard(username)
#             elif designation == "Admin":
#                 # Open the admin dashboard
#                 self.open_admin_dashboard(username)
#             elif designation == "Non-teaching Staff":
#                 # Open the non-teaching staff dashboard
#                 self.open_non_teaching_staff_dashboard(username)
       
#         else:
#             # If the user credentials are invalid, show an error message
#             messagebox.showerror("Login Failed", "Invalid username or password")
#         # self.destroy()
#         # self.back_callback()
#     def back(self):
#         self.pack_forget()
#         home.SchoolManagementSystemApp(self.parent, self.username)
        
#         home.show_home(self)
        


#     def open_teacher_dashboard(self, username):
#         self.pack_forget()

#         # Create the teacher dashboard page
#         teacher_dashboard.TeacherDashboard(self.parent, username)
    

#     def open_student_dashboard(self, username):
#         # Implement the student dashboard opening logic
#         self.pack_forget()

#         # Create the teacher dashboard page
#         student_dashboard.StudentDashboard(self.parent, username)
     

#     def open_admin_dashboard(self, username):
#         self.pack_forget()

#         # Create the teacher dashboard page
#         admin_dashboard.AdminDashboard(self.parent, username)
        
        

#     def open_non_teaching_staff_dashboard(self, username):
#         # Implement the non-teaching staff dashboard opening logic
#         self.pack_forget()

#         # Create the teacher dashboard page
#         staff_dashboard.StaffDashboard(self.parent, username)
       

    


# # Create an instance of LoginPage and run it directly if required
# if __name__ == "__main__":
#     root = tk.Tk()
#     home = home.SchoolManagementSystemApp()
#     home.withdraw()
#     login_page = LoginPage(root)
#     login_page.pack()
#     root.mainloop()
    
