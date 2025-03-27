import tkinter as tk
from tkinter import messagebox, filedialog

class StudentRegistrationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("School Student Registration")
        self.geometry("700x350")

        self.roll_number_label = tk.Label(self, text="Roll Number:")
        self.roll_number_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.roll_number_entry = tk.Entry(self)
        self.roll_number_entry.grid(row=0, column=1, padx=10, pady=5)

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.age_label = tk.Label(self, text="Age:")
        self.age_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        self.grade_label = tk.Label(self, text="Grade:")
        self.grade_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.grade_entry = tk.Entry(self)
        self.grade_entry.grid(row=3, column=1, padx=10, pady=5)

        self.class_label = tk.Label(self, text="Class:")
        self.class_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.class_entry = tk.Entry(self)
        self.class_entry.grid(row=4, column=1, padx=10, pady=5)

        self.contact_label = tk.Label(self, text="Contact:")
        self.contact_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.contact_entry = tk.Entry(self)
        self.contact_entry.grid(row=5, column=1, padx=10, pady=5)

        self.photo_button = tk.Button(self, text="Upload Photo", command=self.upload_photo)
        self.photo_button.grid(row=6, columnspan=2, padx=10, pady=5)

        self.marks_button = tk.Button(self, text="Upload Marks", command=self.upload_marks)
        self.marks_button.grid(row=7, columnspan=2, padx=10, pady=5)

        self.register_button = tk.Button(self, text="Register", command=self.register_student)
        self.register_button.grid(row=8, columnspan=2, padx=10, pady=5)

        self.announcement_label = tk.Label(self, text="Announcements:")
        self.announcement_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.announcement_text = tk.Text(self, width=40, height=10)
        self.announcement_text.grid(row=1, rowspan=8, column=2, padx=10, pady=5)

    def upload_photo(self):
        filename = filedialog.askopenfilename(title="Select a photo")
        if filename:
            messagebox.showinfo("Photo Uploaded", f"Photo {filename} uploaded successfully!")

    def upload_marks(self):
        filename = filedialog.askopenfilename(title="Select a marks file")
        if filename:
            messagebox.showinfo("Marks Uploaded", f"Marks file {filename} uploaded successfully!")

    def register_student(self):
        roll_number = self.roll_number_entry.get().strip()
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        grade = self.grade_entry.get().strip()
        class_ = self.class_entry.get().strip()
        contact = self.contact_entry.get().strip()

        if roll_number and name and age and grade and class_ and contact:
            messagebox.showinfo("Registration Successful", "Student registered successfully!")
            # Here you can add code to save the student details to a database or file
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def clear_fields(self):
        self.roll_number_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.class_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.announcement_text.delete(1.0, tk.END)

if __name__ == "__main__":
    app = StudentRegistrationApp()
    app.mainloop()
