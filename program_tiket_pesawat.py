
import tkinter as tk
from tkinter import messagebox

class ProgramPemesananTiket(tk.Tk):
    def __init__(self):
        super().__init__()

        self.harga = 0
        self.slide_pendaftaran_pengguna = PendaftaranPenggunaSlide(self)
        self.slide_pemesanan_tiket = PemesananTiketSlide(self)

        self.nama_pemesan = None  # Variabel untuk menyimpan nama pemesan

        self.create_widgets()

    def create_widgets(self):
        self.title("Program Pemesanan Tiket Pesawat")

        self.slide_pendaftaran_pengguna.pack()
        self.slide_pemesanan_tiket.pack_forget()  # Sembunyikan slide pemesanan tiket

    def switch_slide(self, target_slide):
        if target_slide == "Pendaftaran":
            self.slide_pendaftaran_pengguna.pack()
            self.slide_pemesanan_tiket.pack_forget()
        elif target_slide == "Pemesanan":
            self.slide_pendaftaran_pengguna.pack_forget()
            self.slide_pemesanan_tiket.pack()

    def set_nama_pemesan(self, nama):
        self.nama_pemesan = nama

class PendaftaranPenggunaSlide(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Login", font=("Roboto", 18))
        self.label.pack(pady=20)

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        self.daftar_button = tk.Button(self, text="Daftar", command=self.daftar_pengguna)
        self.daftar_button.pack(pady=20)

    def daftar_pengguna(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Simpan informasi pendaftaran pengguna ke database atau tempat penyimpanan lainnya
        # Implementasikan sesuai kebutuhan aplikasi Anda
        # (pada contoh ini, hanya menampilkan pesan konfirmasi)
        messagebox.showinfo("Pendaftaran Berhasil", f"Akun {username} berhasil didaftarkan!")

        # Setelah pendaftaran berhasil, beralih ke slide Pemesanan
        self.master.set_nama_pemesan(username)  # Set nama pemesan di kelas ProgramPemesananTiket
        self.master.switch_slide("Pemesanan")

class PemesananTiketSlide(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.harga = 0
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Pesan Tiket Pesawat", font=("Roboto", 18))
        self.label.pack(pady=20)

        self.nama_pemesan_label = tk.Label(self, text="Nama Pemesan:")
        self.nama_pemesan_label.pack(pady=5)
        self.nama_pemesan_entry = tk.Entry(self)
        self.nama_pemesan_entry.pack(pady=5)

        tujuan_options = ["Bali", "Jakarta", "Medan", "Makasar"]
        self.tujuan_var = tk.StringVar()
        self.tujuan_menu = tk.OptionMenu(self, self.tujuan_var, *tujuan_options)
        self.tujuan_menu.pack(pady=10)

        self.jumlah_tiket_label = tk.Label(self, text="Masukkan Jumlah Tiket:")
        self.jumlah_tiket_label.pack(pady=5)
        self.jumlah_tiket_entry = tk.Entry(self)
        self.jumlah_tiket_entry.pack(pady=5)

        self.pesan_button = tk.Button(self, text="Pesan Tiket", command=self.pesan_tiket)
        self.pesan_button.pack(pady=10)

        self.bukti_label = tk.Label(self, text="cetak Pesanan:")
        self.bukti_label.pack(pady=5)
        self.bukti_text = tk.Text(self, height=5, width=40)
        self.bukti_text.pack(pady=5)

    def pesan_tiket(self):
        tujuan = self.tujuan_var.get()
        if tujuan:
            nama_pemesan = self.nama_pemesan_entry.get()
            self.harga = self.get_harga(tujuan)
            jumlah_tiket = self.jumlah_tiket_entry.get()

            if nama_pemesan and jumlah_tiket.isdigit() and int(jumlah_tiket) > 0:
                total_harga = int(jumlah_tiket) * self.harga
                bukti_pesanan = f"Nama Pemesan: {nama_pemesan}\nTujuan: {tujuan}\nJumlah Tiket: {jumlah_tiket}\nTotal Harga: Rp.{total_harga}"
                self.bukti_text.delete(1.0, tk.END)  # Menghapus teks sebelumnya
                self.bukti_text.insert(tk.END, bukti_pesanan)
            else:
                messagebox.showinfo("Input Tidak Valid", "Masukkan data pemesanan yang valid.")
        else:
            messagebox.showinfo("Pilihan Tujuan", "Silakan pilih tujuan terlebih dahulu.")

    def get_harga(self, tujuan):
        harga_tujuan = {"Bali": 1500000, "Jakarta": 2000000, "Medan": 1000000, "Makasar": 1200000}
        return harga_tujuan.get(tujuan, 0)

if __name__ == "__main__":
    app = ProgramPemesananTiket()
    app.mainloop()
