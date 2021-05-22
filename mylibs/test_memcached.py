from big_file import MyLib
lib = MyLib()
filename = r"C:\Users\vuduy.nguyen\Documents\system-keyvault.csv"
file_obj = open(filename, 'rb')
res = lib.set_file('5MiB.dat', file_obj)
print(res)
file_obj.close()