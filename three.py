def gaji(perjam, liburan_semester):
    # gaji kotor
    perhari = 24 * perjam
    perminggu = 7 * perhari
    gaji_kotor = perminggu * liburan_semester
    # pajak
    pajak = 14/100
    # gaji bersih
    gaji_bersih = gaji_kotor-(gaji_kotor * pajak)
    return gaji_kotor,gaji_bersih

def pakaian_alat_tulis(gaji_bersih):
    # jumlah yang dikeluarkan untuk pakaian
    pakaian = gaji_bersih*(10/100)
    # jumlah yang dikeluarkan untuk alat tulis
    altul = gaji_bersih*(1/100)
    #sisa uang setelah membeli pakaian dan alat tulis
    total_sisa = gaji_bersih - (pakaian+altul)
    return pakaian,altul,total_sisa

def sedekah_yatim_dhaufa(total_sisa):
    # total sedekah
    total_sedekah = total_sisa*(25/100)
    # sedekah anak yatim
    yatim = round(((total_sedekah/1000)*(30/100))*1000)
    # sedekah dhaufa
    dhaufa = total_sedekah - yatim
    return total_sedekah, yatim, dhaufa

def main():
    perjam = float(input("gaji per jam yang anda inginkan: ")) # membuat input untuk user
    liburan_semester = 5 # liburan semester = 5 minggu
    gaji(perjam, liburan_semester) #memasukan input user ke fungsi gaji
    
    gaji_kotor, gaji_bersih = gaji(perjam, liburan_semester)
    print("Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak: Rp.", gaji_kotor) #soal 1
    print("Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: Rp.", gaji_bersih, "\n") #soal 2

    pakaian,altul,total_sisa = pakaian_alat_tulis(gaji_bersih)
    print("Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp.", pakaian) #soal 3
    print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp.", altul) #soal 4
    print("Sisa uang setelah membeli alat tulis, pakaian dan aksesoris: Rp.", total_sisa, "\n") #sisa pertama

    total_sedekah, yatim, dhaufa = sedekah_yatim_dhaufa(total_sisa)
    print("Jumlah uang yang akan Budi sedekahkan: Rp.", total_sedekah) #soal 5
    print("Jumlah uang yang akan diterima anak yatim:  Rp.", yatim)#soal 6
    print("Jumlah uang yang akan diterima kaum dhuafa: Rp.", dhaufa)#soal 7

    yang_tersisa = total_sisa - total_sedekah
    print("Yang tersisa: Rp.", yang_tersisa) #sisa akhir
    
if __name__ == "__main__":
    main()