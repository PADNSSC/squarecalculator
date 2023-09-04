import tkinter as tk

def calculate_area():
    length = float(length_entry.get())
    width = float(width_entry.get())
    area = length * width
    result_label.config(text=f"พื้นที่: {area} ตารางหน่วย")


window = tk.Tk()
window.title("คำนวณพื้นที่สี่เหลี่ยมผืนผ้า")
window.geometry("300x200")

length_label = tk.Label(window, text="ความยาว:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

width_label = tk.Label(window, text="ความกว้าง:")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack()

calculate_button = tk.Button(window, text="คำนวณพื้นที่", command=calculate_area)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
