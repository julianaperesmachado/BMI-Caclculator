import tkinter
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

def bmi_calculator():
    try:
        name = usernameentry.get()
        age = int(userageentry.get())
        height = float(userheightentry.get()) / 100  # Convert cm to meters
        weight = float(userweightentry.get())

        if not name:
            raise ValueError("Name cannot be empty.")
        if age <= 0:
            raise ValueError("Age must be greater than 0.")
        if height <= 0:
            raise ValueError("Height must be greater than 0.")
        if weight <= 0:
            raise ValueError("Weight must be greater than 0.")

        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi < 24.9:
            category = 'Normal'
        elif 25 <= bmi < 29.9:
            category = 'Overweight'
        else:
            category = 'Obese'


        with open("bmi_data.txt", "a") as file:
            file.write(f"{name},{age},{height},{weight},{bmi:.2f},{category}\n")

        messagebox.showinfo("BMI Result", f"{name}, your BMI is: {bmi:.2f}. Your BMI is {category}.")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def show_graph():
    try:
        with open("bmi_data.txt", "r") as file:
            data = file.readlines()

        categories = {'Underweight': 0, 'Normal': 0, 'Overweight': 0, 'Obese': 0}
        for line in data:
            category = line.strip().split(",")[-1]
            if category in categories:
                categories[category] += 1

        labels = categories.keys()
        sizes = categories.values()

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels,autopct='%1.1f%%', startangle=140)
        plt.title('BMI Categories Chart\n')
        plt.axis('equal')
        plt.show()
    except FileNotFoundError:
        messagebox.showerror("File Error", "No data available to show the graph.")


window = tkinter.Tk()
window.title('BMI CALCULATOR')

frame = tkinter.Frame(window)
frame.pack(padx=10, pady=10)

usernamelabel = tkinter.Label(frame, text="Name:")
usernamelabel.grid(row=0, column=0, padx=5, pady=5)
usernameentry = tkinter.Entry(frame)
usernameentry.grid(row=0, column=1, padx=5, pady=5)

useragelabel = tkinter.Label(frame, text="Age:")
useragelabel.grid(row=1, column=0, padx=5, pady=5)
userageentry = tkinter.Entry(frame)
userageentry.grid(row=1, column=1, padx=5, pady=5)

userheightlabel = tkinter.Label(frame, text="Height (cm):")
userheightlabel.grid(row=2, column=0, padx=5, pady=5)
userheightentry = tkinter.Entry(frame)
userheightentry.grid(row=2, column=1, padx=5, pady=5)

userweightlabel = tkinter.Label(frame, text='Weight (kg):')
userweightlabel.grid(row=3, column=0, padx=5, pady=5)
userweightentry = tkinter.Entry(frame)
userweightentry.grid(row=3, column=1, padx=5, pady=5)

calculatebtn = tkinter.Button(frame, text="Calculate BMI", command=bmi_calculator)
calculatebtn.grid(row=4, column=0, columnspan=2, pady=10)

graphbtn = tkinter.Button(frame, text="Show Graph", command=show_graph)
graphbtn.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
