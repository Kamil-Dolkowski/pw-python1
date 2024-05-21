def skala_ocen(ilosc_punktow):
    print(f"3.0: {int(0.51*ilosc_punktow)}-{int(0.6*ilosc_punktow)}")
    print(f"3.5: {int(0.61*ilosc_punktow)}-{int(0.7*ilosc_punktow)}")
    print(f"4.0: {int(0.71*ilosc_punktow)}-{int(0.8*ilosc_punktow)}")
    print(f"4.5: {int(0.81*ilosc_punktow)}-{int(0.9*ilosc_punktow)}")
    print(f"5.0: {0.91*ilosc_punktow}-{ilosc_punktow}")
    
    
skala_ocen(20)