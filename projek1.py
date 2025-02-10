print("PERHITUNGAN BMI (BODY MASS INDEX)")
print("----------------------------------")
berat_badan = float (input("Masukkan berat badan (Kilogram): "))
tinggi_badan = float (input ("Masukkan tinggi badan (Meter): "))
#perhitungan
perhitungan = berat_badan/(tinggi_badan**2)
berat_badan_ideal = dict()
berat_badan_ideal ['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal ['atas'] = 25*(tinggi_badan**2)
# output
print(f"Nilai BMI anda adalah {perhitungan :.2f} kg/m^2") #mengambil 2 angka belakang koma
print("Nilai BMI normal adalah 18.5 - 24.9 kg/m^2")
print(f"Beta badan ideal anda adalah dalam rentang {berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:.2f} kg")
print('Terima kasih sudah menggunakan program ini :)')
