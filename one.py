#mencari berat badan
def bb_calculator(expected_bmi, tinggi_cm):
    tinggi_m = tinggi_cm/100
    berat_badan = round(expected_bmi * tinggi_m**2)
    return berat_badan

# mencari bmi
def bmi_calculator(berat_badan_kg, tinggi_cm):
    tinggi_m = tinggi_cm/100
    bmi = berat_badan_kg/tinggi_m**2
    return bmi

def main():
    print("1.BMI calculator")
    print("2.berat badan calculator")
    user_input = input("pilih salah 1 dari 2 pilihan di atas(1/2): ")
    
    if user_input == '1':
        berat_badan_kg = float(input("masukan berat badan dalam (kg): "))
        tinggi_cm = float(input("masukkan tinggi badan (cm): "))
        hasil_bmi = bmi_calculator(berat_badan_kg, tinggi_cm)
        print("BMI anda: %.1f" % hasil_bmi)
        
    elif user_input == '2':
        expected_bmi = float(input("masukan bmi: "))
        tinggi_cm = float(input("masukkan tinggi badan (cm): "))
        hasil_bb = bb_calculator(expected_bmi, tinggi_cm)
        print("berat badan anda: ",hasil_bb,"kg")
        
    else: print("pilihan tidak valid!")
        
if __name__ == "__main__":
    main()