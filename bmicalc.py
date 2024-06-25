import tkinter
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt


def bmi_calculator():
    height = float(userheightentry.get()) / 100  # Convert cm to meters
    weight = float(userweightentry.get())

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
        file.write(f"{height},{weight},{bmi:.2f},{category}\n")

        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}. You are {category}.")

def show_graph():
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
    plt.pie(sizes, labels=labels, startangle=140)
    plt.title('BMI Categories Distribution')
    plt.axis('equal')
    plt.show()

window = tkinter.Tk()
window.title('BMI CALCULATOR')

frame = tkinter.Frame(window)
frame.pack(padx=10, pady=10)

userheightlabel = tkinter.Label(frame, text="Height (cm):")
userheightlabel.grid(row=2, column=0)
userheightentry = tkinter.Entry(frame)
userheightentry.grid(row=2, column=1)

userweightlabel = tkinter.Label(frame, text='Weight (kg):')
userweightlabel.grid(row=3, column=0)
userweightentry = tkinter.Entry(frame)
userweightentry.grid(row=3, column=1)

calculatebtn = tkinter.Button(frame, text="Calculate BMI", command=bmi_calculator)
calculatebtn.grid(row=4, column=0)

graphbtn = tkinter.Button(frame, text="Show Graph", command=show_graph)
graphbtn.grid(row=5, column=0)

window.mainloop()
