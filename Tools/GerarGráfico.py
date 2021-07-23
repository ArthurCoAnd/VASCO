# ✠ VASCO
# "A LICENÇA BEER-WARE" ou "A LICENÇA DA CERVEJA" (Revisão 42):
# <arthurcoand@gmail.com>/<jg2001.avellar@gmail.com> escreveu este arquivo.
# Enquanto você manter este comentário, você poderá fazer o que quiser com este arquivo.
# Caso nos encontremos algum dia e você ache que este arquivo vale,
# você poderá me comprar uma cerveja em retribuição. Arthur Cordeiro Andrade e João Gabriel Silva de Avellar.

# Biblioteclas
import matplotlib.pyplot as pp
from numpy import linspace
# Ferramentas
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