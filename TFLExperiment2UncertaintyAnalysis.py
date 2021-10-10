mdot = 6.16805217
mdotUncertainty = 0.26376105
T2 = 82.706
T1 = 78.278
TUncertainty = .1
A = 0.005454
Su = -83.84221796
SuUncertainty = 9.297747672

Pt1 = (mdotUncertainty*((T2-T1)/(A*Su)))**2
Pt2 = (TUncertainty*(mdot/(A*Su)))**2
Pt3 = (TUncertainty*(mdot/(A*Su)))**2
Pt4 = (SuUncertainty*((mdot*(T2-T1)/(A*(Su**2)))))**2

Final_Uncertainty = (Pt1 + Pt2 + Pt3 + Pt4)**(1/2)

print(Pt1)
print(Pt2)
print(Pt3)
print(Pt4)
print(Final_Uncertainty)
