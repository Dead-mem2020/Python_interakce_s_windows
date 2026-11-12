import zipfile

# tvoří kompresovaný .zip soubor se dvěma soubory
# "w" jako write (psaní), píšou se .zip soubory
with zipfile.ZipFile("files.zip", "w", compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write("test.txt")
    my_zip.write("radagast.jfif")

my_zip.close()

# vypíše a extrahuje soubory ze .zip souboru
# "r" jako read (čtení), čtou se .zip soubory
with zipfile.ZipFile("files.zip", "r") as my_zip:
    print(my_zip.namelist()) #Vyčte soubory uvnitř .zip souboru
    my_zip.extractall("soubory") #Extrahuje vše v .zip souboru do nové složky "soubory"
    my_zip.extract("radagast.jfif") #Extrahuje pouze jeden určitý soubor ze .zip souboru