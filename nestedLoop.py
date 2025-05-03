rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbols = input("Enter the symbol that you want: ")

for x in range(rows):
    for w in range(columns):
        print(symbols, end='')  # Cetak simbol tanpa pindah baris
    print()  # Pindah baris setelah setiap baris selesai
