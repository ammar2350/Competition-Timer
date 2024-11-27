from tkinter import Tk, Label, Button, StringVar, Frame
import time

class MatchTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Match Timer")
        
        # Set background root window ke putih
        self.master.configure(bg="white")
        
        # Konfigurasi layar
        self.master.geometry("960x540")
        
        # Konfigurasi timer
        self.match_duration = 90  # 1 menit 30 detik dalam detik

        # Variabel StringVar untuk tampilan waktu
        self.match_time_str = StringVar()
        self.match_time_str.set(self.time_format(self.match_duration * 1000))

        # Variabel untuk win time
        self.win_time_str = StringVar()
        self.win_time_str.set("")

        # Frame utama yang akan diatur di tengah
        self.main_frame = Frame(master, bg="white")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Buat bagian-bagian timer
        self.create_match_timer_section()
        self.create_buttons_section()

        # Flag aktif timer
        self.is_match_active = False

        # Waktu mulai
        self.match_start_time = None
        self.current_remaining_time = self.match_duration * 1000

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
              font=("Helvetica", 120, "bold"), 
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

    def reset_match_timer(self):
        self.match_start_time = None
        self.current_remaining_time = self.match_duration * 1000
        self.match_time_str.set(self.time_format(self.match_duration * 1000))
        self.is_match_active = False
        self.win_time_str.set("")  # Reset win time saat reset

# Jalankan GUI  
if __name__ == "__main__":
    root = Tk()
    app = MatchTimer(root)
    root.mainloop()
