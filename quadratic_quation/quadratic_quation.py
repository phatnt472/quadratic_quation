from tkinter import *
from math import *
def calc_action():  
    try:
        a = float(string_a.get())
        b = float(string_b.get())
        c = float(string_c.get())
        if a == 0:
            string_ans.set("Vui lòng nhập a != 0")
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                string_ans.set("Vô nghiệm")
            elif delta == 0:
                string_ans.set(f"x = {round(-b/(2*a),2)}")
            else:
                string_ans.set(f"x1 = {round((-b-sqrt(delta))/(2*a),2)}\t, x2 = {round((-b+sqrt(delta))/(2*a),2)}")

    except:
        string_ans.set("Nhập sai!")


def delete_action():
    string_a.set("")
    string_b.set("")
    string_c.set("")
    string_ans.set("")

def make_center(root):
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = screen_width//2 - 300//2
    y = screen_height//2 - 150//2
    root.geometry(f'{300}x{180}+{x}+{y}')

def main():
    global string_a, string_b, string_c, string_ans
    root = Tk()
    string_a = StringVar()
    string_b = StringVar()
    string_c = StringVar()
    string_ans = StringVar()

    label_a = Label(root, width=10,  height=2, text="Hệ số a:", fg="blue").grid(row=0, columnspan=2)
    label_b = Label(root, width=10,  height=2, text="Hệ số b:", fg="blue").grid(row=1, columnspan=2)
    label_c = Label(root, width=10,  height=2, text="Hệ số c:", fg="blue").grid(row=2, columnspan=2)
    label_ans = Label(root, width=10,  height=2, text="Kết quả:", fg="blue").grid(row=4, columnspan=2)

    entry_a = Entry(root, width=20, textvariable=string_a).grid(row=0, column=2)
    entry_b = Entry(root, width=20, textvariable=string_b).grid(row=1, column=2)
    entry_c = Entry(root, width=20, textvariable=string_c).grid(row=2, column=2)
    entry_ans = Entry(root, width=20, textvariable=string_ans).grid(row=4, column=2)

    button_frame = Frame()
    calc_button = Button(button_frame, text="Giải", padx=10, pady=4, command=calc_action)
    calc_button.grid(row=0, column=0)
    delete_button = Button(button_frame, text="Xoá", padx=10, pady=4, command = delete_action)
    delete_button.grid(row=0, column=1)
    quit_button = Button(button_frame, text="Thoát", padx=10, pady=4, command = root.quit)
    quit_button.grid(row=0, column=2)
    button_frame.grid(row=3, columnspan=3)

    root.title("Quadratic Quation")
    root.resizable(height=False, width=False)
    root.minsize(height=150, width=300)
    make_center(root)
    root.mainloop()


if __name__ == '__main__':
    main()

