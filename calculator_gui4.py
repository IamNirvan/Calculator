import tkinter as tk
import time

class Calculator():
    def __init__(self):
        self.bg="#111"
        self.sec = 2
        root = tk.Tk()
        root.resizable(False, False)
        root.configure(bg=self.bg)
        root.title("Calculator")

        def num(num):
            global current_num
            current_num = entry.get()
            entry.delete(0, "end")
            entry.insert(0 , str(current_num) + str(num))


        def clear(self):
            main_lbl.delete(0.0, "end")
            entry.delete(0, "end")


        def add(self):
            global first_num, operator
            try:
                first_num = int(entry.get())
                operator = "add"
                entry.delete(0, "end")

                main_lbl.delete(0.0, "end")
                main_lbl.insert(0.0, first_num)

            except ValueError:
                error_lbl.configure(text="Please enter a number")
                root.update_idletasks()
                time.sleep(self.sec)
                error_lbl.configure(text="")


        def sub(self):
            try:
                global first_num, operator
                first_num = int(entry.get())
                operator = "sub"
                entry.delete(0, "end")

                main_lbl.delete(0.0, "end")
                main_lbl.insert(0.0, first_num)

            except ValueError:
                error_lbl.configure(text="Please enter a number")
                root.update_idletasks()
                time.sleep(self.sec)
                error_lbl.configure(text="")


        def multiply(self):
            try:
                global first_num, operator
                first_num = int(entry.get())
                operator = "mul"
                entry.delete(0, "end")

                main_lbl.delete(0.0, "end")
                main_lbl.insert(0.0, first_num)

            except ValueError:
                error_lbl.configure(text="Please enter a number")
                root.update_idletasks()
                time.sleep(self.sec)
                error_lbl.configure(text="")


        def equal(self):
            try:
                second_num = int(entry.get())
                entry.delete(0, "end")
                if operator == "add":
                    answer= first_num + second_num
                    main_lbl.delete(0.0, "end")
                    main_lbl.insert(0.0, answer)

                elif operator == "sub":
                    answer = first_num - second_num
                    main_lbl.delete(0.0, "end")
                    main_lbl.insert(0.0, answer)

                elif operator == "mul":
                    answer = first_num * second_num
                    main_lbl.delete(0.0, "end")
                    main_lbl.insert(0.0, answer)
            except ValueError:
                error_lbl.configure(text="Please enter a number")
                root.update_idletasks()
                time.sleep(self.sec)
                error_lbl.configure(text="")


        # !Error label
        self.font_sm2 = ("century gothic", 11)
        self.error_lbl_fg = "#d71c1c"

        self.lbl_frm_bg = self.bg
        self.font = ("century gothic", 15)

        self.main_lbl_bg = self.bg
        self.main_lbl_fg = "#d71c1c"
        self.main_lbl_height = 5
        self.main_lbl_width = 22

        # !Entry
        self.entry_fg = "#d71c1c"
        self.entry_bg  = "#111"
        self.highlight = "#304ffe"
        self.selectfg = "#304ffe"
        self.selectbg = self.entry_fg
        self.insert_bg = "#304ffe"

        # !Operator button bg and fg:
        self.opbtn_bgColor = "#304ffe"
        self.opbtn_fgColor = "#080808"
        self.clr_btn_bg = "#d71c1c"
        self.clr_btn_fg = "#111"
        self.eql_btn_bg = "#388e3c"
        self.eql_btn_fg = "#111"


        # !Button(numbers, clear) bg, fg, padx, pady and borderwidth:
        self.btn_width = 14
        self.btn_height = 4
        self.btn_bg = "#141414"
        self.btn_fg = "#304ffe"
        self.width = 9
        self.height = 2
        self.padx=3
        self.pady=3
        self.font_sm = ("century gothic", 10)


        main_frm = tk.Frame(root, bg=self.lbl_frm_bg)
        main_frm.pack(side="top", fill="both")

        self.master1 = main_frm

        error_lbl = tk.Label(master=self.master1, text="", font=self.font_sm2, bg=self.main_lbl_bg, fg=self.error_lbl_fg, anchor="center", borderwidth=0, pady=5)
        error_lbl.pack()


        main_lbl = tk.Text(master=self.master1, font=self.font, height=self.main_lbl_height, width=self.main_lbl_width, bg=self.main_lbl_bg, fg=self.main_lbl_fg, padx=5, pady=5, borderwidth=0)
        main_lbl.pack()

        entry = tk.Entry(master=self.master1, bg=self.entry_bg, fg=self.entry_fg, borderwidth=0, highlightthickness=0.5, highlightcolor=self.highlight, highlightbackground=self.highlight, cursor="cross", selectbackground=self.selectbg, selectforeground=self.selectfg, insertbackground=self.insert_bg)
        entry.pack(fill="both", padx=5)

        btn_frm = tk.Frame(root, bg=self.lbl_frm_bg)
        btn_frm.pack(side="bottom", fill="both", expand=True, pady=5, padx=5)

        self.master2 = btn_frm

        btn7 = tk.Button(master=self.master2, text="7", width=self.width, height=self.height, borderwidth=0, bg=self.btn_bg, fg=self.btn_fg, font=self.font_sm, activebackground=self.btn_bg, activeforeground=self.btn_fg, command=lambda:num(7))
        btn7.grid(row=0, column=0, padx=self.padx, pady=self.pady)

        btn8 = tk.Button(master=self.master2, text="8", width=self.width, height=self.height, borderwidth=0, bg=self.btn_bg, fg=self.btn_fg, font=self.font_sm, activebackground=self.btn_bg, activeforeground=self.btn_fg, command=lambda:num(8))
        btn8.grid(row=0, column=1, padx=self.padx, pady=self.pady)

        btn9 = tk.Button(master=self.master2, text="9", width=self.width, height=self.height, borderwidth=0, bg=self.btn_bg, fg=self.btn_fg, font=self.font_sm, activebackground=self.btn_bg, activeforeground=self.btn_fg, command=lambda:num(9))
        btn9.grid(row=0, column=2, padx=self.padx, pady=self.pady)

        btn4 = tk.Button(master=self.master2, text="4", width=self.width, height=self.height, borderwidth=0, bg=self.btn_bg, fg=self.btn_fg, font=self.font_sm, activebackground=self.btn_bg, activeforeground=self.btn_fg, command=lambda:num(4))
        btn4.grid(row=1, column=0, padx=self.padx, pady=self.pady)

        btn5 = tk.Button(master=self.master2, text="5", width=self.width, height=self.height, borderwidth=0, bg=self.btn_bg, fg=self.btn_fg, font=self.font_sm, activebackground=self.btn_bg, activeforeground=self.btn_fg, command=lambda:num(5))
        btn5.grid(row=1, column=1, padx=self.padx, pady=self.pady)

        btn6 = tk.Button(master=self.master2, text="6", width=self.width, height=self.height, borderwidth=0, bg=self.btn_bg, fg=self.btn_fg, font=self.font_sm, activebackground=self.btn_bg, activeforeground=self.btn_fg, command=lambda:num(6))
        btn6.grid(row=1, column=2, padx=self.padx, pady=self.pady)

        btn1 = tk.Button(master=self.master2, text="1", width=self.width, height=self.height, borderwidth=0, bg=self.btn_bg, fg=self.btn_fg, font=self.font_sm, activebackground=self.btn_bg, activeforeground=self.btn_fg, command=lambda:num(1))
        btn1.grid(row=2, column=0, padx=self.padx, pady=self.pady)

        btn2 = tk.Button(master=self.master2, text="2", width=self.width, height=self.height, borderwidth=0, bg=self.btn_bg, fg=self.btn_fg, font=self.font_sm, activebackground=self.btn_bg, activeforeground=self.btn_fg, command=lambda:num(2))
        btn2.grid(row=2, column=1, padx=self.padx, pady=self.pady)

        btn3 = tk.Button(master=self.master2, text="3", width=self.width, height=self.height, borderwidth=0, bg=self.btn_bg, fg=self.btn_fg, font=self.font_sm, activebackground=self.btn_bg, activeforeground=self.btn_fg, command=lambda:num(3))
        btn3.grid(row=2, column=2, padx=self.padx, pady=self.pady)

        btn0 = tk.Button(master=self.master2, text="0", width=self.width, height=self.height, borderwidth=0, bg=self.btn_bg, fg=self.btn_fg, font=self.font_sm, activebackground=self.btn_bg, activeforeground=self.btn_fg, command=lambda:num(0))
        btn0.grid(row=3, column=0, padx=self.padx, pady=self.pady)

        add_btn = tk.Button(master=self.master2, text="+", width=self.width, height=self.height, borderwidth=0, bg=self.opbtn_bgColor, fg=self.opbtn_fgColor, activebackground=self.btn_bg, activeforeground=self.btn_fg, font=self.font_sm, command=lambda:add(self))
        add_btn.grid(row=3, column=1, padx=self.padx, pady=self.pady)

        sub_btn = tk.Button(master=self.master2, text="-", width=self.width, height=self.height, borderwidth=0, bg=self.opbtn_bgColor, fg=self.opbtn_fgColor, activebackground=self.btn_bg, activeforeground=self.btn_fg, font=self.font_sm, command=lambda:sub(self))
        sub_btn.grid(row=3, column=2, padx=self.padx, pady=self.pady)

        mul_btn = tk.Button(master=self.master2, text="*", width=self.width, height=self.height, borderwidth=0, bg=self.opbtn_bgColor, fg=self.opbtn_fgColor, activebackground=self.btn_bg, activeforeground=self.btn_fg, font=self.font_sm, command=lambda:multiply(self))
        mul_btn.grid(row=4, column=2, padx=self.padx, pady=self.pady)

        eql_btn = tk.Button(master=self.master2, text="=", width=self.width, height=self.height, borderwidth=0, bg=self.eql_btn_bg, fg=self.eql_btn_fg, activebackground=self.eql_btn_bg, activeforeground=self.eql_btn_fg, font=self.font_sm, command=lambda:equal(self))
        eql_btn.grid(row=4, column=1, padx=self.padx, pady=self.pady)

        clr_btn = tk.Button(master=self.master2, text="clear", width=self.width, height=self.height, borderwidth=0, bg=self.clr_btn_bg, fg=self.clr_btn_fg, font=self.font_sm, activebackground=self.clr_btn_bg, activeforeground=self.clr_btn_fg, command=lambda:clear(self))
        clr_btn.grid(row=4, column=0, padx=self.padx, pady=self.pady)

        root.mainloop()


obj1 = Calculator()
