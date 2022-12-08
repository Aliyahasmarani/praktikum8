class Datamahasiswa():
    def __init__(self, nim, nama, tugas, uts, uas, akhir):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.akhir = akhir

    def _set(self, nim, nama, tugas, uts, uas, akhir):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.akhir = akhir

    def _get(self):
        pass

r1 = Datamahasiswa('', '', '', '', '', '')

arr_nim = []
arr_nama = []
arr_tugas = []
arr_uts = []
arr_uas = []
arr_akhir = []

print('='*43)
print('             DATA MAHASISWA              ')
print('='*43)
print('Menu Utama Data Mahasiswa : ')
print('[I]nput Data Mahasiswa')
print('[T]ampilkan Data Mahasiswa')
print('[U]bah Data Mahasiswa')
print('[H]apus Data Mahasiswa')
print('[K]eluar')

lagi = True
while lagi:
    pilih = input('Input pilihan [I/T/U/H/K] : ')
    if pilih in ['Ii']:
        _nim    = input('Nim Mahasiswa          : ')
        _nama   = input('Nama Mahasiswa         : ')
        _tugas  = input('Masukkan Nilai Tugas   : ')
        _uts    = input('Masukkan Nilai UTS     : ')
        _uas    = input('Masukkan Nilai UAS     : ')
        _akhir  = _tugas*0.30+ _uts*0.35+ _uas*0.35
        
        r1._set(_nim, _nama, _tugas, _uts, _uas, _akhir)

        arr_nim.append(r1.nim)
        arr_nama.append(r1.nama)
        arr_tugas.append(r1.tugas)
        arr_uts.append(r1.uts)
        arr_uas.append(r1.uas)
        arr_akhir.append(r1.akhir)

    elif pilih in ('Kk'):
        print()
        print("---------------------------------------------------------------------------------")
        print("                           PROGRAM TELAH SELESAI                    ")
        print("---------------------------------------------------------------------------------")
        print(35*'=')
        print("NAMA\t: ALIYAH ASMARANI\nKELAS\t: TI.22.A.2\nNIM\t: 312210203")
        print(35*'=')
    elif pilih in ('Uu'):
        _nim        = input('Nim Mahasiswa      : ')
        if arr_nim.count(_nim) > 0:
            _idx = arr_nim.index(_nim)
            _nama   = input('Nama Mahasiswa         : ')
            _tugas  = input('Masukkan Nilai Tugas   : ')
            _uts    = input('Masukkan Nilai UTS     : ')
            _uas    = input('Masukkan Nilai UAS     : ')
            _akhir  = _tugas*0.30+ _uts*0.35+ _uas*0.35
        else:
            print('MAAF, DATA TIDAK DITEMUKAN')
    elif pilih in ('Hh'):
        _nim    = input('Nim Mahasiswa      : ')
        if arr_nim.count(_nim) > 0:
            _idx = arr_nim.index(_nim)
            arr_nama.pop(_idx)
            arr_tugas.pop(_idx)
            arr_uts.pop(_idx)
            arr_uas.pop(_idx)
            arr_akhir.pop(_idx)
        else:
            print('MAAF, DATA TIDAK DITEMUKAN')
    elif pilih in ('Tt'):
        print('==================================================================================================================')
        print('     NIM     |           NAMA            |       TUGAS       |       UTS     |       UAS     |       AKHIR       |')
        print('==================================================================================================================')
        for x in range(len(arr_nim)):
            print('%-25s%-25s%3s' % (arr_nim[x] + arr_nama[x] + arr_tugas[x] + ', ' + arr_uts[x] + arr_uas[x] + arr_akhir[x]))
        print('==================================================================================================================')
    else:
        print('MAAF, PILIHAN SALAH. SILAHKAN PILIH LAGI [I/T/U/H/K]')
    print()
    lagi = input('Input Data Lagi [Y/T] : ')
    while lagi not in ('YyTt'):
        lagi = input (' Input Data Lagi [Y/T] : ')

    if lagi in ('Tt'):
        lagi = False




