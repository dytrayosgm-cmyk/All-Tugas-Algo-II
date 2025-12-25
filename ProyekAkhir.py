import re  # [KONSEP: REGEX] Untuk validasi pola teks
import os  # Untuk cek file

# ==========================================
# BAGIAN 1: PENERAPAN OOP (Object Oriented Programming)
# ==========================================

# [KONSEP: KELAS INDUK / PARENT CLASS]
class Manusia:
    def __init__(self, nama):
        self.nama = nama

    # [KONSEP: METODE / METHOD]
    def info(self):
        return f"Nama: {self.nama}"

# [KONSEP: PEWARISAN / INHERITANCE]
# Kelas Mahasiswa mewarisi sifat dari kelas Manusia
class Mahasiswa(Manusia):
    def __init__(self, nama, nim, jurusan):
        super().__init__(nama) # Memanggil konstruktor induk
        self.nim = nim
        self.jurusan = jurusan
        self.__ipk = 0.0 # [KONSEP: ENKAPSULASI - Atribut Private]

    # [KONSEP: GETTER & SETTER]
    # Mengontrol akses ke variabel private __ipk
    def set_ipk(self, nilai):
        try:
            float_nilai = float(nilai)
            if 0.0 <= float_nilai <= 4.0:
                self.__ipk = float_nilai
            else:
                print("❌ Error: IPK harus antara 0.0 - 4.0")
        except ValueError:
            print("❌ Error: IPK harus berupa angka.")

    def get_ipk(self):
        return self.__ipk

    # [KONSEP: POLIMORFISME / OVERRIDING]
    # Mengubah perilaku metode info() milik induk
    def info(self):
        return f"NIM: {self.nim} | Nama: {self.nama:<20} | Jurusan: {self.jurusan} | IPK: {self.__ipk}"

# ==========================================
# BAGIAN 2: LOGIKA SISTEM & ALGORITMA
# ==========================================

class SistemAkademik:
    def __init__(self):
        # [KONSEP: ARRAY / LIST] Struktur data menyimpan objek
        self.data_mhs = []
        self.filename = "data_mahasiswa.txt"

    # [KONSEP: FILE I/O] Membaca dan Menulis Berkas
    def simpan_ke_file(self):
        with open(self.filename, "w") as f:
            for mhs in self.data_mhs:
                line = f"{mhs.nama},{mhs.nim},{mhs.jurusan},{mhs.get_ipk()}\n"
                f.write(line)
        print("💾 Data berhasil disimpan ke file.")

    def baca_dari_file(self):
        if os.path.exists(self.filename):
            self.data_mhs = []
            with open(self.filename, "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        mhs = Mahasiswa(data[0], data[1], data[2])
                        mhs.set_ipk(data[3])
                        self.data_mhs.append(mhs)
            print("📂 Data lama berhasil dimuat.")

    def tambah_mahasiswa(self):
        print("\n--- Tambah Data Mahasiswa ---")
        nama = input("Nama: ")
        
        # [KONSEP: REGEX] Validasi NIM harus angka
        while True:
            nim = input("NIM (Angka saja): ")
            if re.match(r"^[0-9]+$", nim):
                break
            print("⚠️ NIM tidak valid! Harus angka.")

        jurusan = input("Jurusan: ")
        
        # [KONSEP: EXCEPTION HANDLING] Menangani input error
        try:
            ipk_input = float(input("IPK (0.0 - 4.0): "))
        except ValueError:
            print("⚠️ Input IPK salah, dianggap 0.0")
            ipk_input = 0.0

        # [KONSEP: OBJEK] Membuat instansi objek baru
        mhs_baru = Mahasiswa(nama, nim, jurusan)
        mhs_baru.set_ipk(ipk_input)
        
        self.data_mhs.append(mhs_baru)
        print("✅ Data berhasil ditambahkan!")

    def tampilkan_data(self):
        print(f"\n{'='*60}")
        print(f"DAFTAR MAHASISWA (Total: {len(self.data_mhs)})")
        print(f"{'='*60}")
        if not self.data_mhs:
            print("(Data Kosong)")
        else:
            for i, mhs in enumerate(self.data_mhs):
                print(f"{i+1}. {mhs.info()}")

    # --- ALGORITMA SEARCHING ---

    def linear_search(self):
        # [KONSEP: LINEAR SEARCH] Mencari satu per satu
        keyword = input("Masukkan Nama yang dicari: ").lower()
        found = False
        print("\n🔍 Hasil Linear Search:")
        for mhs in self.data_mhs:
            if keyword in mhs.nama.lower():
                print(f"-> DITEMUKAN: {mhs.info()}")
                found = True
        if not found: print("Tidak ditemukan.")

    def binary_search(self):
        # [KONSEP: BINARY SEARCH] Mencari dengan membagi dua (Wajib data terurut)
        print("⚙️ Mengurutkan data berdasarkan NIM terlebih dahulu...")
        self.bubble_sort_nim() 
        
        target = input("Masukkan NIM yang dicari: ")
        low = 0
        high = len(self.data_mhs) - 1
        found = False
        
        while low <= high:
            mid = (low + high) // 2
            mid_val = self.data_mhs[mid].nim
            
            if mid_val == target:
                print(f"-> DITEMUKAN: {self.data_mhs[mid].info()}")
                found = True
                break
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
        
        if not found: print("NIM tidak ditemukan.")

    # --- ALGORITMA SORTING ---

    def bubble_sort_nim(self):
        # [KONSEP: BUBBLE SORT] Menukar elemen berdekatan
        n = len(self.data_mhs)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data_mhs[j].nim > self.data_mhs[j + 1].nim:
                    # Swap
                    self.data_mhs[j], self.data_mhs[j + 1] = self.data_mhs[j + 1], self.data_mhs[j]

    def shell_sort_ipk(self):
        # [KONSEP: SHELL SORT] Sorting menggunakan gap
        print("⚙️ Melakukan Shell Sort berdasarkan IPK...")
        n = len(self.data_mhs)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.data_mhs[i]
                j = i
                # Urutkan Descending (IPK Tertinggi di atas)
                while j >= gap and self.data_mhs[j - gap].get_ipk() < temp.get_ipk():
                    self.data_mhs[j] = self.data_mhs[j - gap]
                    j -= gap
                self.data_mhs[j] = temp
            gap //= 2
        print("✅ Data telah diurutkan berdasarkan IPK (Tertinggi -> Terendah)")

    def merge_sort_nama(self):
        # [KONSEP: MERGE SORT] Divide and Conquer (Rekursif)
        print("⚙️ Melakukan Merge Sort berdasarkan Nama...")
        self.data_mhs = self._merge_sort_algo(self.data_mhs)
        print("✅ Data telah diurutkan berdasarkan Nama (A-Z)")

    def _merge_sort_algo(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self._merge_sort_algo(arr[:mid])
        right = self._merge_sort_algo(arr[mid:])
        
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].nama.lower() < right[j].nama.lower():
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

# ==========================================
# PROGRAM UTAMA
# ==========================================
if __name__ == "__main__":
    app = SistemAkademik()
    app.baca_dari_file() # Muat data lama jika ada

    while True:
        print("\n=== APLIKASI FINAL PROJECT ===")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua")
        print("3. Cari (Linear Search - by Nama)")
        print("4. Cari (Binary Search - by NIM)")
        print("5. Urutkan IPK (Shell Sort)")
        print("6. Urutkan Nama (Merge Sort)")
        print("7. Simpan & Keluar")
        
        pilihan = input("Pilih Menu: ")

        if pilihan == '1': app.tambah_mahasiswa()
        elif pilihan == '2': app.tampilkan_data()
        elif pilihan == '3': app.linear_search()
        elif pilihan == '4': app.binary_search()
        elif pilihan == '5': app.shell_sort_ipk()
        elif pilihan == '6': app.merge_sort_nama()
        elif pilihan == '7': 
            app.simpan_ke_file()
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")