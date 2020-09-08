def acresToMetros(acres):
    return acres * 4048.58

acres = float(input("Quantos acres? " ))
print("{:.0f} acres são {:.2f} m2".format(acres, acresToMetros(acres)))