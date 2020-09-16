def librasParaQuilos(libs):
    return libs * 0.45


libs = float(input("Peso em Libras: "))
print("O peso de {}libs é {} kg".format(libs, librasParaQuilos(libs)))