import tkinter as tk
from PIL import Image, ImageTk



class streamGUI():
    def __init__(self):
        self.parent = tk.Tk()
        self.parent.geometry("1920x1080")
        self.parent.title("Mt. Battle Stream Overlay")

        to_resize = Image.open(r'/Users/ryanjacobs/Desktop/Files/Mt. Battle Overlay/overlay1.png')
        to_resize = to_resize.resize((1152, 648), Image.LANCZOS)
        print(to_resize)
        self.score = ImageTk.PhotoImage(to_resize)

        self.score_display = tk.Canvas(self.parent, width=1920, height=1080)
        self.score_display.pack()
        self.score_display.create_image(165,0, image=self.score, anchor='nw')
        self.p1_label = tk.Label(self.parent, font=("copperplate", 28), bg='#53347b', fg='white')
        self.p1_label.place(x=210, y=60, anchor="center")
        self.p1_team = tk.Label(self.parent, font=("copperplate", 28), bg='#53347b', fg='gray')
        self.p1_team.place(x=210, y=60, anchor="center")
        self.p2_team = tk.Label(self.parent, font=("copperplate", 28), bg='#53347b', fg='gray')
        self.p2_team.place(x=1115, y=60, anchor="center")
        self.p2_label = tk.Label(self.parent, font=("copperplate", 28), bg='#53347b', fg='white')
        self.p2_label.place(x=1115, y=55, anchor="center")
        self.p1_score = tk.Label(self.parent, font=("copperplate", 30), bg='#53347b', fg='white')
        self.p1_score.place(x=582, y=60, anchor="center")
        self.p2_score = tk.Label(self.parent, font=("copperplate", 30), bg='#53347b', fg='white')
        self.p2_score.place(x=887, y=60, anchor="center")
        self.tournament = tk.Label(self.parent, font=("copperplate", 18), bg='#53347b', fg='white')
        self.tournament.place(x=382, y=117, anchor="center")
        self.round = tk.Label(self.parent, font=("copperplate", 18), bg='#53347b', fg='white')
        self.round.place(x=1062, y=120, anchor="center")
        self.set_format = tk.Label(self.parent, font=("copperplate", 22), bg='#53347b', fg='white')
        self.set_format.place(x=1232, y=120, anchor="center")
        self.p1_label_centered = False


    def update_p1_label(self, tag, team):
        label_font_size = 28
        team_font_size = 28
        right_shift = 0
        self.p1_label_centered = False
        p1_label_height = 40
        self.p1_label.config(text=tag, font=("copperplate", label_font_size), bg="#53347b")
        self.p1_label.place(x=355, y=58)
        self.p1_team.config(text=team, font=("copperplate", team_font_size), bg="#53347b")
        self.p1_team.place(x=2100, y=60)


        if team == "Team":
            while not self.p1_label_centered:
                p1_label_height = 58
                self.parent.update_idletasks()
                tag_width = float(self.p1_label.winfo_width())
                if tag_width > 290:
                    label_font_size -= 1
                    p1_label_height += 0.6
                    self.p1_label.config(font=("copperplate",label_font_size))
                else:
                    self.p1_label.place(x=355, y=p1_label_height, anchor="center")
                    self.p1_label_centered = True

        else:
            while not self.p1_label_centered:
                self.parent.update_idletasks()
                tag_width = float(self.p1_label.winfo_width())
                team_width = float(self.p1_team.winfo_width())

                center = ((20+tag_width+team_width) / 2) + 210 + right_shift
                if center == 355:
                    self.p1_label_centered = True
                    self.p1_team.place(x=(210 + right_shift), y=p1_label_height + 1, anchor="nw")
                    self.p1_label.place(x=(215 + team_width + right_shift), y=p1_label_height, anchor="nw")

                elif center > 355:
                    label_font_size -= 1
                    team_font_size -= 1
                    p1_label_height += 0.6
                    self.p1_label.config(font=("copperplate", label_font_size))
                    self.p1_team.config(font=("copperplate", team_font_size))

                elif center < 355:
                    right_shift = 355 - center
                    self.p1_team.place(x=(210+right_shift), y=p1_label_height+1, anchor="nw")
                    self.p1_label.place(x=(215+team_width+right_shift), y=p1_label_height, anchor="nw")



    def update_p2_label(self, team, tag):
        label_font_size = 28
        team_font_size = 28
        right_shift = 0
        self.p2_label_centered = False
        p2_label_height = 40
        self.p2_label.config(text=tag, font=("copperplate", label_font_size), bg="#53347b")
        self.p2_label.place(x=1115, y=56)
        self.p2_team.config(text=team, font=("copperplate", team_font_size), bg="#53347b")
        self.p2_team.place(x=2100, y=60)

        if team == "Team":
            while not self.p2_label_centered:
                p2_label_height = 56
                self.parent.update_idletasks()
                tag_width = float(self.p2_label.winfo_width())
                if tag_width > 270:
                    label_font_size -= 1
                    p2_label_height += 0.6
                    self.p2_label.config(font=("copperplate", label_font_size))
                else:
                    self.p2_label.place(x=1115, y=p2_label_height, anchor="center")
                    self.p2_label_centered = True

        else:
            while not self.p2_label_centered:
                self.parent.update_idletasks()
                tag_width = float(self.p2_label.winfo_width())
                team_width = float(self.p2_team.winfo_width())

                center = ((20 + tag_width + team_width) / 2) + 980 + right_shift
                if center == 1115:
                    self.p2_label_centered = True
                    self.p2_team.place(x=(980 + right_shift), y=p2_label_height + 1, anchor="nw")
                    self.p2_label.place(x=(985 + team_width + right_shift), y=p2_label_height, anchor="nw")

                elif center > 1115:
                    label_font_size -= 1
                    team_font_size -= 1
                    p2_label_height += 0.6
                    self.p2_label.config(font=("copperplate", label_font_size))
                    self.p2_team.config(font=("copperplate", team_font_size))

                elif center < 1115:
                    right_shift = 1115 - center
                    self.p2_team.place(x=(980 + right_shift), y=p2_label_height + 1, anchor="nw")
                    self.p2_label.place(x=(985 + team_width + right_shift), y=p2_label_height, anchor="nw")


    def update_p1_team(self, value):
        self.p1_team.config(text=value)

    def update_p2_team(self, value):
        self.p2_team.config(text=value)

    def update_p1_score(self, value):
        self.p1_score.config(text=value)

    def update_p2_score(self, value):
        self.p2_score.config(text=value)

    def update_tournament(self, value):
        self.tournament.config(text=value)

    def update_round(self, value):
        if len(value) > 14:
            self.round.config(text=value, font=('copperplate', 14))
        else:
            self.round.config(text=value, font=('copperplate', 18))
        self.parent.update_idletasks()
        print(self.round.winfo_width())


    def update_set_format(self, value):
        if value == "3":
            self.set_format.config(text="Bo3")
        else:
            self.set_format.config(text="Bo5")

    def get_parent(self):
        return self.parent



    def launch_stream_overlay(self):
        self.parent.mainloop()

    def update_anti_flash(self, tag, team):
        label_font_size = 28
        team_font_size = 28
        right_shift = 0
        self.p1_label_centered = False
        p1_label_height = 40
        self.p1_label.config(text=tag, font=("copperplate", label_font_size), bg="#53347b")
        self.p1_label.place(x=2100, y=60)
        self.p1_team.config(text=team, font=("copperplate", team_font_size), bg="#53347b")
        self.p1_team.place(x=2100, y=60)

        if team == "Team":
            while not self.p1_label_centered:
                p1_label_height = 58
                self.parent.update_idletasks()
                tag_width = float(self.p1_label.winfo_width())
                if tag_width > 290:
                    label_font_size -= 1
                    p1_label_height += 0.6
                    self.p1_label.config(font=("copperplate", label_font_size))
                else:
                    self.p1_label.place(x=2100, y=p1_label_height, anchor="center")
                    self.p1_label_centered = True

        else:
            while not self.p1_label_centered:
                self.parent.update_idletasks()
                tag_width = float(self.p1_label.winfo_width())
                team_width = float(self.p1_team.winfo_width())

                center = ((20 + tag_width + team_width) / 2) + 210 + right_shift
                if center == 355:
                    self.p1_label_centered = True
                    self.p1_team.place(x=(2100 + right_shift), y=p1_label_height + 1, anchor="nw")
                    self.p1_label.place(x=(2100 + team_width + right_shift), y=p1_label_height, anchor="nw")

                elif center > 355:
                    label_font_size -= 1
                    team_font_size -= 1
                    p1_label_height += 0.6
                    self.p1_label.config(font=("copperplate", label_font_size))
                    self.p1_team.config(font=("copperplate", team_font_size))

                elif center < 355:
                    right_shift = 355 - center
                    self.p1_team.place(x=(2100 + right_shift), y=p1_label_height + 1, anchor="nw")
                    self.p1_label.place(x=(2150 + team_width + right_shift), y=p1_label_height, anchor="nw")





