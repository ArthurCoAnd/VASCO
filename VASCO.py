##     ##    ###     ######   ######   #######  
##     ##   ## ##   ##    ## ##    ## ##     ## 
##     ##  ##   ##  ##       ##       ##     ## 
##     ## ##     ##  ######  ##       ##     ## 
 ##   ##  #########       ## ##       ##     ## 
  ## ##   ##     ## ##    ## ##    ## ##     ## 
   ###    ##     ##  ######   ######   #######  

# ===================================
# = VAriable tranSformer CalculatOr =
# ===================================

# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁
# ⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁
# ⣿⣿⣿⣿⣿⣿⠟⠁⠀⢤⣤⣤⣤⣤⣤⣤⠄
# ⣿⣿⣿⣿⠟⠁⠀⡀⠀⠀⠙⣿⣿⣿⡟⠁⠀⢀⡄
# ⣿⣿⡟⠁⠀⠀⠀⣿⣦⣀⡀⢹⣿⡟⠀⣀⣴⣿⡇
# ⡿⠋⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀ ⠀ ⠀⠀⣠
#         ⣿⠿⠋⠉⣸⣿⣧⠈⠙⠻⣿⡇⠀ ⠀⢀⣴⣿⣿
#         ⠁⠀⠀⣰⣿⣿⣿⣦⠀⠀ ⠈⠃⢀⣴⣿⣿⣿⣿
#            ⠚⠛⠛⠛⠛⠛⠓ ⢀⣴⣿⣿⣿⣿⣿⣿
#                    ⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿
#                 ⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#              ⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

# Importar Bibliotecas
from Calc.Calc import *
from math import acos, degrees, sqrt
from pygame import mixer
from tkinter import *
import os
import sys

l = 5

class Vasco(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.config(padx=15, pady=15)
		self.dados = {"Pn":"","V1":"","V2":"","FP":"","eFP":"","lE":"","Vvz":"","Ivz":"","Pvz":"","Vcc":"","Icc":"","Pcc":"","a":"","ang":"","Rc":"","Xm":"","Zphi":"","Rphi":"","Xphi":"","Zcc":"","Req":"","Xeq":"","R1":"","R1'":"","X1":"","X1'":""}
		Entradas(self).grid(row=0,column=0)
		CircuitoEquivalente(self).grid(row=0, column=1)

	def Calcular(self, *args):
		self.lerDados()
		self.calcularCE()

	def lerDados(self):
		for i in range(len(self.entradas_nominais_t)):
			try:
				self.dados[self.entradas_nominais_t[i]] = float(self.var_entradas_nominais[i].get())
				self.entradas_nominais[i].config(bg="white")
			except:
				self.dados[self.entradas_nominais_t[i]] = ""
				self.entradas_nominais[i].config(bg="red")
		self.dados["eFP"] = self.tipo_fator.get()
		self.dados["lE"] = self.lado_ensaio.get()
		for i in range(len(self.entradas_ensaio_tipo_txt)):
			for ii in range(len(self.entradas_ensaio_t)):
				try:
					self.dados[self.entradas_ensaio_t[ii]+self.entradas_ensaio_tipo_txt[i]] = float(self.var_entradas_ensaio[i][ii].get())
					self.entradas_ensaio[i][ii].config(bg="white")
				except:
					self.dados[self.entradas_ensaio_t[ii]+self.entradas_ensaio_tipo_txt[i]] = ""
					self.entradas_ensaio[i][ii].config(bg="red")

	def calcularCE(self):
		for i in range(len(self.CE_t)):
			try:
				self.dados[self.CE_t[i]] = eval("c"+self.CE_t[i]+"(self.dados)")
				self.var_resultados_CE[i].set(str(self.dados[self.CE_t[i]]))
			except:
				self.dados[self.CE_t[i]] = "-"
				self.var_resultados_CE[i].set(self.dados[self.CE_t[i]])

class Entradas(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		self.config(padx=25, pady=15)
		raiz.entradas_nominais = []
		raiz.var_entradas_nominais = []
		raiz.entradas_nominais_txt = ["Potência Nominal","Tensão de Entrada","Tensão de Saida","Fator de Potência"]
		raiz.entradas_nominais_t = ["Pn","V1","V2","FP"]
		raiz.entradas_nominais_unidades = ["VA","V","V",""]
		raiz.tipo_fator = IntVar()
		raiz.tipo_fator_txt = ["Adiantado","Atrasado"]
		raiz.lado_ensaio = IntVar()
		raiz.lados_ensaio_txt = ["Primário","Secundário"]
		raiz.entradas_ensaio = []
		raiz.var_entradas_ensaio = []
		raiz.entradas_ensaio_txt = ["Tensão - V","Corrente - I","Potência - P"]
		raiz.entradas_ensaio_t = ["V","I","P"]
		raiz.entradas_ensaio_unidades = ["V","A","W"]
		raiz.entradas_ensaio_tipo_txt = ["vz","cc"]
		linha = 0
		for i in range(len(raiz.entradas_nominais_txt)):
			Label(self, text=raiz.entradas_nominais_txt[i], width=l*3).grid(row=linha, column=0)
			raiz.var_entradas_nominais.append(StringVar())
			raiz.var_entradas_nominais[i].trace("w", raiz.Calcular)
			raiz.entradas_nominais.append(Entry(self, textvariable=raiz.var_entradas_nominais[i], width=l*4))
			raiz.entradas_nominais[i].grid(row=linha, column=1)
			Label(self, text=raiz.entradas_nominais_unidades[i], width=l*1).grid(row=linha, column=2)
			linha += 1
		for i in range(len(raiz.tipo_fator_txt)):
			Radiobutton(self, text="FP "+raiz.tipo_fator_txt[i], variable=raiz.tipo_fator, value=i, command=raiz.Calcular, width=l*4).grid(row=linha, column=i)
		linha += 1
		for i in range(len(raiz.lados_ensaio_txt)):
			Radiobutton(self, text="Ensaio lado "+raiz.lados_ensaio_txt[i], variable=raiz.lado_ensaio, value=i, command=raiz.Calcular, width=l*4).grid(row=linha, column=i)
		linha += 1
		for i in range(len(raiz.entradas_ensaio_tipo_txt)):
			raiz.entradas_ensaio.append([])
			raiz.var_entradas_ensaio.append([])
			if i == 0:
				Label(self, text="Ensaio Vazio", width=l*8).grid(row=linha, column=0, columnspan=3)
			else:
				Label(self, text="Ensaio Curto-Circuito", width=l*8).grid(row=linha, column=0, columnspan=3)
			for ii in range(len(raiz.entradas_ensaio_txt)):
				linha += 1
				Label(self, text=raiz.entradas_ensaio_txt[ii]+raiz.entradas_ensaio_tipo_txt[i], width=l*3).grid(row=linha, column=0)
				raiz.var_entradas_ensaio[i].append(StringVar())
				raiz.var_entradas_ensaio[i][ii].trace("w", raiz.Calcular)
				raiz.entradas_ensaio[i].append(Entry(self, textvariable=raiz.var_entradas_ensaio[i][ii], width=l*4))
				raiz.entradas_ensaio[i][ii].grid(row=linha, column=1)
				Label(self, text=raiz.entradas_ensaio_unidades[ii], width=l*1).grid(row=linha, column=2)
			linha += 1
	
class CircuitoEquivalente(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		self.config(padx=25, pady=15)
		raiz.CE_t = ["a","ang","Zphi","Rphi","Xphi","Rc","Xm","Zcc","Req","Xeq","R1","X1","R1_","X1_"]
		raiz.CE_txt = ["a","ang","|Zphi|","Rphi","Xphi","Rc","Xm","|Zcc|","Req","Xeq","R1 = R2'","X1 = X2'","R1' = R2","X1' = X2"]
		raiz.CE_unidade = ["","º","Ω","Ω","Ω","Ω","Ω","Ω","Ω","Ω","Ω","Ω","Ω","Ω"]
		raiz.var_resultados_CE = []
		linha = 0
		for i in range(len(raiz.CE_txt)):
			Label(self, text=raiz.CE_txt[i], width=l*2).grid(row=linha, column=0)
			raiz.var_resultados_CE.append(StringVar())
			raiz.var_resultados_CE[i].set("-")
			Label(self, textvariable=raiz.var_resultados_CE[i], width=l*5).grid(row=linha, column=1)
			Label(self, text=raiz.CE_unidade[i], width=l*1).grid(row=linha, column=2)
			linha += 1

def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def TocarHino():
	mixer.music.load(resource_path("Sounds/HinoVasco.mp3"))
	mixer.music.play(loops=-1)

if __name__ == "__main__":
	mixer.init()
	TocarHino()
	app = Vasco()
	app.resizable(False, False)
	app.title("VASCO")
	app.iconbitmap(resource_path("Images/CruzDeMalta.ico"))
	app.mainloop()