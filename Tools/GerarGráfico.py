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
	
	x = linspace(0,d["Pn"],10000)
	yrt = []
	yef = []
	for c in x:
		d["Sop"] = c
		for i in range(len(oCalc)):
			d[oCalc[i]] = eval("c"+oCalc[i]+"(d)")
		yrt.append(d["Rt"])
		yef.append(d["Nef"])
	
	pp.subplot(1,2,1)
	pp.plot(x,yrt,"-k",linewidth=3)
	pp.title(f"Regulação de Tensão")
	pp.xlabel("Carga Saída (VA)")
	pp.ylabel("Rendimento (%)")
	pp.grid(True)
	
	pp.subplot(1,2,2)
	pp.plot(x,yef,"-k",linewidth=3)
	pp.title(f"Curva de Rendimento")
	pp.xlabel("Carga Saída (VA)")
	pp.ylabel("Rendimento (%)")
	pp.grid(True)
	
	pp.show()