import tkinter as tk
import custom_widgets
import stream_overlay
from PIL import Image, ImageTk


class mainGUI:
    def __init__(self):
        self.parent = stream_overlay.streamGUI()
        self.root = tk.Toplevel(self.parent.get_parent())

        self.root.geometry("800x500")
        self.root.title("Mt. Battle Stream Tool")

        self.image = ImageTk.PhotoImage(Image.open('/Users/ryanjacobs/Desktop/Files/Mt. Battle Overlay/logo3.png'))
        self.logo = tk.Label(self.root, image=self.image)
        self.logo.place(x=266, y=120, width=275, height=400)

        self.p1_tag = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="Player 1 Tag")
        self.p1_tag.place(x=60, y=60)

        self.p2_tag = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="Player 2 Tag")
        self.p2_tag.place(x=598, y=60)

        self.p1_team = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="Team")
        self.p1_team.place(x=10, y=60, width=50)

        self.p2_team = custom_widgets.EntryWithPlaceholder(master=self.root,placeholder="Team")
        self.p2_team.place(x=548, y=60, width=50)

        self.update = tk.tk.Button(self.root, text="Update Display", font=("Copperplate", 20), fg='white', bg='#6110b3', command=self.update_display)
        self.update.place(x=304, y=460)

        self.reset = tk.tk.Button(self.root, text="Reset All", font=("Copperplate", 15), fg='white', bg='#6110b3', command=self.reset_text)
        self.reset.place(x=675,y=10)

        self.reset = tk.tk.Button(self.root, text="New Set", font=("Copperplate", 15), fg='white', bg='#6110b3', command=self.reset_set)
        self.reset.place(x=560, y=10)

        self.p1_games = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="0")
        self.p1_games.place(x=227, y=87, width=25)

        self.p2_games = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="0")
        self.p2_games.place(x=765, y=87, width=25)

        self.p1_plus = tk.tk.Button(self.root, text="+", font=("Copperplate", 24), fg='white', bg='#6110b3', command=self.p1_plus_clicked)
        self.p1_plus.place(x=155, y=87, width=35, height=25)

        self.p1_minus = tk.tk.Button(self.root, text="-", font=("Copperplate", 24), fg='white', bg='#6110b3', command=self.p1_minus_clicked)
        self.p1_minus.place(x=192, y=87, width=35, height=25)

        self.p2_plus = tk.tk.Button(self.root, text="+", font=("Copperplate", 24), fg='white', bg='#6110b3', command=self.p2_plus_clicked)
        self.p2_plus.place(x=692, y=87, width=35, height=25)

        self.p2_minus = tk.tk.Button(self.root, text="-", font=("Copperplate", 24), fg='white', bg='#6110b3', command=self.p2_minus_clicked)
        self.p2_minus.place(x=728, y=87, width=35, height=25)

        self.round = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="Round")
        self.round.place(x=10, y=435)

        self.bo3 = tk.tk.Button(self.root, text="Bo3", font=("Copperplate", 16), fg='white', bg='#6110b3', command=self.bo3_clicked)
        self.bo3.place(x=10, y=470, height=25, width=70)

        self.bo5 = tk.tk.Button(self.root, text="Bo5", font=("Copperplate", 16), fg='white', bg='gray', command=self.bo5_clicked)
        self.bo5.place(x=80, y=470, height=25, width=70)

        self.is_bo3 = True

        self.title = tk.Label(self.root, text="Mt. Battle Stream Tool!", font=("Copperplate", 18))
        self.title.place(x=275, y=10, width=250)

        self.credits = tk.Label(self.root, text="Mt. Battle > Spoontastic", font=("Copperplate", 11))
        self.credits.place(x=300, y=30, width=200)

        self.tournament_name = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="Tournament Name")
        self.tournament_name.place(x=10,y=405)

        self.notice = tk.Label(self.root, text="ALL of the purple tk.tk.Buttons update the stream (except the resets).", font=("Copperplate", 11))
        self.notice.place(x=235, y=430)

        self.c1 = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="Commentator 1 Tag")
        self.c1.place(x=598, y=360)

        self.c2 = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="Commentator 2 Tag")
        self.c2.place(x=598, y=430)

        self.c1T = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="Commentator 1 Twitter")
        self.c1T.place(x=598, y=390)

        self.c2T = custom_widgets.EntryWithPlaceholder(master=self.root, placeholder="Commentator 2 Twitter")
        self.c2T.place(x=598, y=460)

        self.check_state = tk.IntVar()

        self.idiot_box = tk.Checktk.tk.Button(self.root, text="Remove GUI Text Filters (on stream)", font=("Copperplate", 11), variable=self.check_state)
        self.idiot_box.place(x=5,y=5)

    def reset_text(self):
        self.p1_team.delete(0,'end')
        self.p1_team.foc_in()
        self.p1_team.foc_out()

        self.p2_team.delete(0, 'end')
        self.p2_team.foc_in()
        self.p2_team.foc_out()

        self.p1_tag.delete(0, 'end')
        self.p1_tag.foc_in()
        self.p1_tag.foc_out()

        self.p2_tag.delete(0, 'end')
        self.p2_tag.foc_in()
        self.p2_tag.foc_out()

        self.p1_games.delete(0, 'end')
        self.p1_games.foc_in()
        self.p1_games.foc_out()

        self.p2_games.delete(0, 'end')
        self.p2_games.foc_in()
        self.p2_games.foc_out()

        self.tournament_name.delete(0, 'end')
        self.tournament_name.foc_in()
        self.tournament_name.foc_out()

        self.round.delete(0, 'end')
        self.round.foc_in()
        self.round.foc_out()

        self.c1.delete(0, 'end')
        self.c1.foc_in()
        self.c1.foc_out()

        self.c2.delete(0, 'end')
        self.c2.foc_in()
        self.c2.foc_out()

        self.c1T.delete(0, 'end')
        self.c1T.foc_in()
        self.c1T.foc_out()

        self.c2T.delete(0, 'end')
        self.c2T.foc_in()
        self.c2T.foc_out()

    def update_display(self):

        #self.parent.update_anti_flash(tag=self.p2_tag.get(), team=self.p2_team.get())
        self.parent.update_p1_label(tag=self.p1_tag.get(), team=self.p1_team.get())
        self.parent.update_p2_label(tag=self.p2_tag.get(), team=self.p2_team.get())
        self.parent.update_p2_team(self.p2_team.get())
        self.parent.update_p1_score(self.p1_games.get())
        self.parent.update_p2_score(self.p2_games.get())
        self.parent.update_tournament(self.tournament_name.get())
        self.parent.update_round(self.round.get())

        if self.is_bo3:
            self.parent.update_set_format("3")
        else:
            self.parent.update_set_format("5")

        games1 = self.p1_games.get()
        games2 = self.p2_games.get()

        round_name = self.round.get()
        tournament_name = self.tournament_name.get()

        c1_tag = self.c1.get()
        c1_twitter = self.c1T.get()

        c2_tag = self.c2.get()
        c2_twitter = self.c2T.get()





    def bo3_clicked(self):

        if self.is_bo3:
            pass
        else:
            self.bo3.destroy()
            self.bo3 = tk.tk.Button(self.root, text="Bo3", font=("Copperplate", 16), fg='white', bg='#6110b3', command=self.bo3_clicked)
            self.bo3.place(x=10, y=470, height=25, width=70)

            self.bo5.destroy()
            self.bo5 = tk.tk.Button(self.root, text="Bo5", font=("Copperplate", 16), fg='white', bg='gray',command=self.bo5_clicked)
            self.bo5.place(x=80, y=470, height=25, width=70)

            self.is_bo3 = True
            self.update_display()

    def bo5_clicked(self):

        if not self.is_bo3:
            pass
        else:
            self.bo3.destroy()
            self.bo3 = tk.tk.Button(self.root, text="Bo3", font=("Copperplate", 16), fg='white', bg='gray', command=self.bo3_clicked)
            self.bo3.place(x=10, y=470, height=25, width=70)

            self.bo5.destroy()
            self.bo5 = tk.tk.Button(self.root, text="Bo5", font=("Copperplate", 16), fg='white', bg='#6110b3', command=self.bo5_clicked)
            self.bo5.place(x=80, y=470, height=25, width=70)

            self.is_bo3 = False
            self.update_display()

    def reset_set(self):
        self.p1_team.delete(0, 'end')
        self.p1_team.foc_in()
        self.p1_team.foc_out()

        self.p2_team.delete(0, 'end')
        self.p2_team.foc_in()
        self.p2_team.foc_out()

        self.p1_tag.delete(0, 'end')
        self.p1_tag.foc_in()
        self.p1_tag.foc_out()

        self.p2_tag.delete(0, 'end')
        self.p2_tag.foc_in()
        self.p2_tag.foc_out()

        self.p1_games.delete(0, 'end')
        self.p1_games.foc_in()
        self.p1_games.foc_out()

        self.p2_games.delete(0, 'end')
        self.p2_games.foc_in()
        self.p2_games.foc_out()

        self.round.delete(0, 'end')
        self.round.foc_in()
        self.round.foc_out()

    def p1_minus_clicked(self):
        score = int(self.p1_games.get())
        score -= 1
        val = tk.IntVar(value=score)
        self.p1_games.configure(textvariable=val, highlightcolor='white')
        self.update_display()

    def p1_plus_clicked(self):
        score = int(self.p1_games.get())
        score += 1
        val = tk.IntVar(value=score)
        self.p1_games.configure(textvariable=val)
        self.update_display()

    def p2_plus_clicked(self):
        score = int(self.p2_games.get())
        score += 1
        val = tk.IntVar(value=score)
        self.p2_games.configure(textvariable=val)
        self.update_display()

    def p2_minus_clicked(self):
        score = int(self.p2_games.get())
        score -= 1
        val = tk.IntVar(value=score)
        self.p2_games.configure(textvariable=val)
        self.update_display()


    def launch_control_panel(self):
        self.root.mainloop()

    def get_p1_tag(self):
        return self.p1_tag.get()
