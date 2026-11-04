"""Latihan Mandiri 1 - Identitas Diri & Eksperimen print()."""

nama = "Yabes Situmorang"
nim = "124140067"
angkatan = "2024"
minat = "Web Development"

# Eksperimen parameter sep=' | '
print("Nama", nama, sep=" | ")
print("NIM", nim, sep=" | ")
print("Angkatan", angkatan, sep=" | ")
print("Minat Penelitian", minat, sep=" | ")

# Kartu identitas berbingkai karakter pagar (#) dengan escape character
print("\n" + "#" * 50)
print("#" + "KARTU IDENTITAS PRAKTIKAN".center(48) + "#")
print("#" * 50)
print(f"# {'Nama':<10}: {nama:<35}#")
print(f"# {'NIM':<10}: {nim:<35}#")
print(f"# {'Angkatan':<10}: {angkatan:<35}#")
print(f"# {'Minat':<10}: {minat:<35}#")
print("#" * 50)
