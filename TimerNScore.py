from tkinter import Tk, Label, Button, StringVar, Frame, OptionMenu
import time

class MatchTimer:
    def __init__(self, master):  
        self.master = master  
        self.master.title("Match Timer")  
        
        # Set background root window ke putih  
        self.master.configure(bg="white")  
        
        # Konfigurasi layar  
        self.master.geometry("800x1080")  
        
        # Daftar tim  
        self.team_list = [  
            "EL KECEPATAN", "AIGOO", "RMUHA", "VIMOUS", "Judat 2",   
            "Buwung Puyuh", "Restu ibu", "Nexus", "Ali Bengkel",   
            "Xavibot", "EL- JAMSUT", "sambal korek",   
            "Four Gamping Robot Team", "Tim Apel", "atom stel",   
            "Elite engineers", "Master netgame", "UPN Bot",   
            "Tsandiesta", "Unity", "Narac industries"  
        ]  
        
        # Konfigurasi timer  
        self.match_duration = 90  # 1 menit 30 detik dalam detik  

        # Variabel StringVar untuk tampilan waktu  
        self.match_time_str = StringVar()  
        self.match_time_str.set(self.time_format(self.match_duration * 1000))  

        # Variabel untuk win time  
        self.win_time_str = StringVar()  
        self.win_time_str.set("")  

        # Variabel untuk tim  
        self.team_a_var = StringVar()  
        self.team_b_var = StringVar()  
        self.team_a_var.set(self.team_list[0])  # Set default tim pertama  
        self.team_b_var.set(self.team_list[1])  # Set default tim kedua  

        # Frame utama yang akan diatur di tengah  
        self.main_frame = Frame(master, bg="white")  
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")  

        # Buat bagian-bagian timer  
        self.create_team_selection_section()  
        self.create_match_timer_section()  
        self.create_buttons_section()  
        self.create_score_section()  

        # Flag aktif timer  
        self.is_match_active = False  

        # Waktu mulai  
        self.match_start_time = None  
        self.current_remaining_time = self.match_duration * 1000  

        # Bind keyboard keys  
        self.master.bind('<s>', lambda event: self.start_match_timer())  
        self.master.bind('<d>', lambda event: self.stop_match_timer())  
        self.master.bind('<r>', lambda event: self.reset_match_timer())  

    def create_team_selection_section(self):  
        # Frame untuk seleksi tim  
        team_selection_frame = Frame(self.main_frame, bg="white")  
        team_selection_frame.pack(pady=10)  

        # Tim A Dropdown  
        Label(team_selection_frame, text="Team A", font=("Helvetica", 14), bg="white").pack(side="left", padx=(0,10))  
        team_a_dropdown = OptionMenu(team_selection_frame, self.team_a_var, *self.team_list)  
        team_a_dropdown.config(font=("Helvetica", 12), width=20)  
        team_a_dropdown.pack(side="left", padx=(0,20))  

        # Tim B Dropdown  
        Label(team_selection_frame, text="Team B", font=("Helvetica", 14), bg="white").pack(side="left", padx=(0,10))  
        team_b_dropdown = OptionMenu(team_selection_frame, self.team_b_var, *self.team_list)  
        team_b_dropdown.config(font=("Helvetica", 12), width=20)  
        team_b_dropdown.pack(side="left")  

    def create_match_timer_section(self):  
        # Judul Match Timer  
        Label(self.main_frame, text="Match Timer",   
              font=("Helvetica", 40),   
              bg="white",   
              fg="black",   
              anchor="center").pack(pady=0)  
        
        # Tampilan waktu match  
        Label(self.main_frame,   
              textvariable=self.match_time_str,   
              font=("Helvetica", 100, "bold"),   
              fg="red",   
              bg="white",   
              anchor="center").pack(pady=0)  

        # Tampilan win time  
        Label(self.main_frame,   
              text="Win Time:",   
              font=("Helvetica", 20),  
              bg="white",   
              fg="blue").pack(pady=(0, 0))  
        
        Label(self.main_frame,   
              textvariable=self.win_time_str,   
              font=("Helvetica", 24, "bold"),  
              bg="white",   
              fg="green").pack(pady=(0, 0))  

    def create_buttons_section(self):  
        # Frame untuk tombol  
        buttons_frame = Frame(self.main_frame, bg="white")  
        buttons_frame.pack(pady=0)  

        # Tombol START  
        self.start_button = Button(buttons_frame,   
                                   text="START",   
                                   command=self.start_match_timer,   
                                   font=("Helvetica", 14),  
                                   borderwidth=2,  
                                   relief="solid",  
                                   width=10,  
                                   height=1,  
                                   bg="lightgreen",  
                                   activebackground="green",  
                                   highlightthickness=0)  
        self.start_button.pack(side="left", padx=10)  

        # Tombol STOP  
        self.stop_button = Button(buttons_frame,   
                                  text="STOP",   
                                  command=self.stop_match_timer,   
                                  font=("Helvetica", 14),  
                                  borderwidth=2,  
                                  relief="solid",  
                                  width=10,  
                                  height=1,  
                                  bg="lightcoral",  
                                  activebackground="red",  
                                  highlightthickness=0)  
        self.stop_button.pack(side="left", padx=10)  

        # Tombol RESET  
        self.reset_button = Button(buttons_frame,   
                                   text="RESET",   
                                   command=self.reset_match_timer,   
                                   font=("Helvetica", 14),  
                                   borderwidth=2,  
                                   relief="solid",  
                                   width=10,  
                                   height=1,  
                                   bg="lightblue",  
                                   activebackground="deepskyblue",  
                                   highlightthickness=0)  
        self.reset_button.pack(side="left", padx=10)  

    def create_score_section(self):  
        # Frame untuk skor  
        score_frame = Frame(self.main_frame, bg="white")  
        score_frame.pack(pady=10)  

        # Tim A  
        team_a_frame = Frame(score_frame, bg="white")  
        team_a_frame.pack(side="left", padx=50)  

        self.team_a_score = 0  
        self.team_a_score_str = StringVar()  
        self.team_a_score_str.set(self.team_a_score)  

        # Label tim A dinamis dengan lebar tetap dan wrap  
        self.team_a_label = Label(team_a_frame,   
                                  textvariable=self.team_a_var,   
                                  font=("Helvetica", 24),   
                                  bg="white",   
                                  width=20,  # Lebar tetap  
                                  wraplength=300,  # Panjang wrap  
                                  justify='center')  # Rata tengah  
        self.team_a_label.pack(pady=(100, 0))  
        
        Label(team_a_frame, textvariable=self.team_a_score_str, font=("Helvetica", 100), bg="white").pack()  
        
        # Frame untuk tombol Tim A  
        team_a_button_frame = Frame(team_a_frame, bg="white")  
        team_a_button_frame.pack(anchor="center")  
        
        Button(team_a_button_frame, text="WIN", command=self.increment_team_a_score, font=("Helvetica", 14)).pack(side="left", padx=5)  
        Button(team_a_button_frame, text="-", command=self.decrement_team_a_score, font=("Helvetica", 14)).pack(side="left", padx=5)  

        # Tim B  
        team_b_frame = Frame(score_frame, bg="white")  
        team_b_frame.pack(side="right", padx=50)  

        self.team_b_score = 0  
        self.team_b_score_str = StringVar()  
        self.team_b_score_str.set(self.team_b_score)  

        # Label tim B dinamis dengan lebar tetap dan wrap  
        self.team_b_label = Label(team_b_frame,   
                                  textvariable=self.team_b_var,   
                                  font=("Helvetica", 24),   
                                  bg="white",   
                                  width=20,  # Lebar tetap  
                                  wraplength=300,  # Panjang wrap  
                                  justify='center')  # Rata tengah  
        self.team_b_label.pack(pady=(100, 0))  
        
        Label(team_b_frame, textvariable=self.team_b_score_str, font=("Helvetica", 100), bg="white").pack()  
        
        # Frame untuk tombol Tim B  
        team_b_button_frame = Frame(team_b_frame, bg="white")  
        team_b_button_frame.pack(anchor="center")  
        
        Button(team_b_button_frame, text="WIN", command=self.increment_team_b_score, font=("Helvetica", 14)).pack(side="left", padx=5)  
        Button(team_b_button_frame, text="-", command=self.decrement_team_b_score, font=("Helvetica", 14)).pack(side="left", padx=5)

    def increment_team_a_score(self):
        self.team_a_score += 1
        self.team_a_score_str.set(self.team_a_score)

    def decrement_team_a_score(self):
        if self.team_a_score > 0:
            self.team_a_score -= 1
            self.team_a_score_str.set(self.team_a_score)

    def increment_team_b_score(self):
        self.team_b_score += 1
        self.team_b_score_str.set(self.team_b_score)

    def decrement_team_b_score(self):
        if self.team_b_score > 0:
            self.team_b_score -= 1
            self.team_b_score_str.set(self.team_b_score)

    def reset_match_timer(self):
        self.match_start_time = None
        self.current_remaining_time = self.match_duration * 1000
        self.match_time_str.set(self.time_format(self.match_duration * 1000))
        self.is_match_active = False
        self.win_time_str.set("")  # Reset win time saat reset
        self.team_a_score = 0
        self.team_a_score_str.set(self.team_a_score)
        self.team_b_score = 0
        self.team_b_score_str.set(self.team_b_score)

    def time_format(self, time_milliseconds):
        minutes = int(time_milliseconds) // 60000
        seconds = (int(time_milliseconds) % 60000) // 1000
        milliseconds = int(time_milliseconds) % 1000
        return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

    def start_match_timer(self):
        if not self.is_match_active:
            self.is_match_active = True
            if self.current_remaining_time == self.match_duration * 1000:  # If it's the first start
                self.match_start_time = time.time() * 1000
            else:  # Continue from where we left off
                self.match_start_time = time.time() * 1000 - (self.match_duration * 1000 - self.current_remaining_time)
            self.win_time_str.set("")  # Reset win time saat memulai
            self.update_match_timer()

    def update_match_timer(self):
        if self.is_match_active:
            elapsed_time = (time.time() * 1000) - self.match_start_time
            remaining_time = self.match_duration * 1000 - elapsed_time
            self.current_remaining_time = remaining_time  # Simpan waktu tersisa saat ini
            
            if remaining_time <= 0:
                self.match_time_str.set(self.time_format(0))
                self.is_match_active = False
            else:
                self.match_time_str.set(self.time_format(remaining_time))
                self.master.after(50, self.update_match_timer)

    def stop_match_timer(self):
        if self.is_match_active:
            # Hitung win time sebagai selisih antara durasi total dan waktu tersisa
            win_time = self.match_duration * 1000 - self.current_remaining_time
            self.win_time_str.set(self.time_format(win_time))
            self.is_match_active = False

# Jalankan GUI  
if __name__ == "__main__":
    root = Tk()
    app = MatchTimer(root)
    root.mainloop()
