# Importar Biblioteclas
import matplotlib.pyplot as pp
from numpy import linspace
# Importar Ferramentas
from Tools.Calc import *

def GerarGráfico(d):
	oCalc = ["I2","E2","Ic","Im","I1_","V1_","Pcu1","Pcu2","Pcu","Pnu","Pt","Rt","Nef"]
	Ci = d["C"]
	Nefi = d["Nef"]
	# pp.style("ggplot")
	pp.grid()
	pp.title(f"Curva de Rendimento: FP = {d['FP']}")
	pp.xlabel("Carga Saída (VA)")
	pp.ylabel("Rendimento (%)")
	x = linspace(0,d["Pn"],10000)
	y = []
	for c in x:
		d["C"] = c
		for i in range(len(oCalc)):
			d[oCalc[i]] = eval("c"+oCalc[i]+"(d)")
		y.append(d["Nef"])
	pp.plot(x,y,"-k",linewidth=3)
	pp.plot(Ci,Nefi,"or",linewidth=5, label=f"C = {Ci} VA")
	pp.legend()
	pp.show()