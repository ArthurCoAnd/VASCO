# ✠ VASCO
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
		self.dados = {"Pn":"","V1":"","V2":"","FP":"","tFP":"","lE":"","Vvz":"","Ivz":"","Pvz":"","Vcc":"","Icc":"","Pcc":"","a":"","ang":"","Rc1":"","Xm1":"","Rc2":"","Xm2":"","Zphi":"","Rphi":"","Xphi":"","Zcc":"","Req":"","Xeq":"","R1":"","X1":"","R2":"","X2":"","E2":"","Pcu1":"","Pcu2":"","Pcu":"","Pnu":"","Pt":"","Rt":"","Nef":"","C":"","I2":"","E2":"","Ic":"","Im":"","I1_":"","V1_":""}
		self.Ensaio(self).grid(row=0,column=0)
		self.CircuitoEquivalente(self).grid(row=0, column=1)
		self.Saida(self).grid(row=0, column=2)

	def Calcular(self, *args):
		self.lerDados()
		self.calcularDados()

	def lerDados(self):
		self.dados["lE"] = self.lado_ensaio.get()
		self.dados["tFP"] = self.tipo_FP.get()
		for i in range(len(self.entradas_nominais_t)):
			try:
				self.dados[self.entradas_nominais_t[i]] = float(self.entradas_nominais_var[i].get())
				self.entradas_nominais[i].config(bg="white")
			except:
				self.dados[self.entradas_nominais_t[i]] = ""
				self.entradas_nominais[i].config(bg="red")
		for i in range(len(self.entradas_ensaio_tipo_txt)):
			for ii in range(len(self.entradas_ensaio_t)):
				try:
					self.dados[self.entradas_ensaio_t[ii]+self.entradas_ensaio_tipo_txt[i]] = float(self.entradas_ensaio_var[i][ii].get())
					self.entradas_ensaio[i][ii].config(bg="white")
				except:
					self.dados[self.entradas_ensaio_t[ii]+self.entradas_ensaio_tipo_txt[i]] = ""
					self.entradas_ensaio[i][ii].config(bg="red")
		for i in range(len(self.entradas_saida_t)):
			try:
				self.dados[self.entradas_saida_t[i]] = float(self.entradas_saida_var[i].get())
				self.entradas_saida[i].config(bg="white")
			except:
				self.dados[self.entradas_saida_t[i]] = ""
				self.entradas_saida[i].config(bg="red")

	def calcularDados(self):
		try: self.dados["a"] = ca(self.dados)
		except: pass
		try: self.dados["ang"] = cang(self.dados)
		except: pass 
		if self.dados["lE"] == 0:
			CE_calc = ["Rc1","Rc2","Zphi","Rphi","Xphi","Xm1","Xm2","Zcc","Req","Xeq","R2","R1","X2","X1"]
			for i in range(len(CE_calc)):
				try:
					self.dados[CE_calc[i]] = eval("c"+CE_calc[i]+"(self.dados)")
					for ii in range(len(self.CE_txt)):
						if self.CE_txt[ii] == CE_calc[i]:
							self.resultados_CE_var[ii].set(str(self.dados[CE_calc[i]]))
							break
				except:
					self.dados[CE_calc[i]] = "-"
					for ii in range(len(self.CE_txt)):
						if self.CE_txt[ii] == CE_calc[i]:
							self.resultados_CE_var[ii].set(self.dados[CE_calc[i]])
		elif self.dados["lE"] == 1:
			CE_calc = ["Rc2","Rc1","Zphi","Rphi","Xphi","Xm2","Xm1","Zcc","Req","Xeq","R1","R2","X1","X2"]
			for i in range(len(CE_calc)):
				try:
					self.dados[CE_calc[i]] = eval("c"+CE_calc[i]+"(self.dados)")
					for ii in range(len(self.CE_txt)):
						if self.CE_txt[ii] == CE_calc[i]:
							self.resultados_CE_var[ii].set(str(self.dados[CE_calc[i]]))
							break
				except:
					self.dados[CE_calc[i]] = "-"
					for ii in range(len(self.CE_txt)):
						if self.CE_txt[ii] == CE_calc[i]:
							self.resultados_CE_var[ii].set(self.dados[CE_calc[i]])
		saida_calc = ["I2","E2","Ic","Im","I1_","V1_","Pcu1","Pcu2","Pcu","Pnu","Pt","Rt","Nef"]
		for i in range(len(saida_calc)):
			try:
				self.dados[saida_calc[i]] = eval("c"+saida_calc[i]+"(self.dados)")
				for ii in range(len(self.saida_txt)):
					if self.saida_txt[ii] == saida_calc[i]:
						self.saida_var[ii].set(str(self.dados[saida_calc[i]]))
						break
			except:
				self.dados[saida_calc[i]] = "-"
				for ii in range(len(self.saida_txt)):
					if self.saida_txt[ii] == saida_calc[i]:
						self.saida_var[ii].set(self.dados[saida_calc[i]])

	class Ensaio(Frame):
		def __init__(self, raiz):
			Frame.__init__(self, raiz)
			self.config(padx=25, pady=15)
			linha = 0
			# Entradas Nominais
			raiz.entradas_nominais = []
			raiz.entradas_nominais_var = []
			raiz.entradas_nominais_txt = ["Potência Nominal","Tensão Primário","Tensão Secundário"]
			raiz.entradas_nominais_t = ["Pn","V1","V2"]
			raiz.entradas_nominais_unidades = ["VA","V","V"]
			for i in range(len(raiz.entradas_nominais_txt)):
				Label(self, text=raiz.entradas_nominais_txt[i], width=l*3).grid(row=linha, column=0)
				raiz.entradas_nominais_var.append(StringVar())
				raiz.entradas_nominais_var[i].trace("w", raiz.Calcular)
				raiz.entradas_nominais.append(Entry(self, textvariable=raiz.entradas_nominais_var[i], width=l*4))
				raiz.entradas_nominais[i].grid(row=linha, column=1)
				Label(self, text=raiz.entradas_nominais_unidades[i], width=l*1).grid(row=linha, column=2)
				linha += 1
			# Entradas Ensaio
			raiz.lado_ensaio = IntVar()
			raiz.lados_ensaio_txt = ["Primário","Secundário"]
			raiz.entradas_ensaio = []
			raiz.entradas_ensaio_var = []
			raiz.entradas_ensaio_txt = ["Tensão - V","Corrente - I","Potência - P"]
			raiz.entradas_ensaio_t = ["V","I","P"]
			raiz.entradas_ensaio_unidades = ["V","A","W"]
			raiz.entradas_ensaio_tipo_txt = ["vz","cc"]
			for i in range(len(raiz.entradas_ensaio_tipo_txt)):
				raiz.entradas_ensaio.append([])
				raiz.entradas_ensaio_var.append([])
				if i == 0:
					for ii in range(len(raiz.lados_ensaio_txt)):
						Radiobutton(self, text="Ensaio Vazio - "+raiz.lados_ensaio_txt[ii], variable=raiz.lado_ensaio, value=ii, command=raiz.Calcular, width=l*4).grid(row=linha, column=ii)
				else:
					Label(self, text="Ensaio Curto-Circuito", width=l*8).grid(row=linha, column=0, columnspan=3)
				linha += 1
				for ii in range(len(raiz.entradas_ensaio_txt)):
					Label(self, text=raiz.entradas_ensaio_txt[ii]+raiz.entradas_ensaio_tipo_txt[i], width=l*3).grid(row=linha, column=0)
					raiz.entradas_ensaio_var[i].append(StringVar())
					raiz.entradas_ensaio_var[i][ii].trace("w", raiz.Calcular)
					raiz.entradas_ensaio[i].append(Entry(self, textvariable=raiz.entradas_ensaio_var[i][ii], width=l*4))
					raiz.entradas_ensaio[i][ii].grid(row=linha, column=1)
					Label(self, text=raiz.entradas_ensaio_unidades[ii], width=l*1).grid(row=linha, column=2)
					linha += 1

	class CircuitoEquivalente(Frame):
		def __init__(self, raiz):
			Frame.__init__(self, raiz)
			self.config(padx=25, pady=15)
			raiz.CE_txt = ["Rc1","Xm1","Rc2","Xm2","R1","X1","R2","X2"]
			raiz.CE_unidade = ["Ω","Ω","Ω","Ω","Ω","Ω","Ω","Ω"]
			raiz.resultados_CE_var = []
			linha = 0
			for i in range(len(raiz.CE_txt)):
				Label(self, text=raiz.CE_txt[i], width=l*2).grid(row=linha, column=0)
				raiz.resultados_CE_var.append(StringVar())
				raiz.resultados_CE_var[i].set("-")
				Label(self, textvariable=raiz.resultados_CE_var[i], width=l*5).grid(row=linha, column=1)
				Label(self, text=raiz.CE_unidade[i], width=l*1).grid(row=linha, column=2)
				linha += 1

	class Saida(Frame):
		def __init__(self, raiz):
			Frame.__init__(self, raiz)
			self.config(padx=25, pady=15)
			linha = 0
			raiz.entradas_saida = []
			raiz.entradas_saida_var = []
			raiz.entradas_saida_t = ["C","FP"]
			raiz.entradas_saida_txt = ["Carga Saída","FP"]
			raiz.entradas_saida_unidades = ["VA",""]
			for i in range(len(raiz.entradas_saida_txt)):
				Label(self, text=raiz.entradas_saida_txt[i], width=l*3).grid(row=linha, column=0)
				raiz.entradas_saida_var.append(StringVar())
				raiz.entradas_saida_var[i].trace("w", raiz.Calcular)
				raiz.entradas_saida.append(Entry(self, textvariable=raiz.entradas_saida_var[i], width=l*4))
				raiz.entradas_saida[i].grid(row=linha, column=1)
				Label(self, text=raiz.entradas_saida_unidades[i], width=l*1).grid(row=linha, column=2)
				linha += 1
			raiz.tipo_FP = IntVar()
			raiz.tipo_FP_txt = ["Indutivo/Atrasado","Capacitivo/Adiantado"]
			for i in range(len(raiz.tipo_FP_txt)):
				Radiobutton(self, text=raiz.tipo_FP_txt[i], variable=raiz.tipo_FP, value=i, command=raiz.Calcular, width=l*4).grid(row=linha, column=i)
			linha += 1
			raiz.saida_txt = ["Pcu1","Pcu2","Pcu","Pnu","Pt","Rt","Nef"]
			raiz.saida_unidades = ["W","W","W","W","W","%","%"]
			raiz.saida_var = []
			for i in range(len(raiz.saida_txt)):
				Label(self, text=raiz.saida_txt[i], width=l*2).grid(row=linha, column=0)
				raiz.saida_var.append(StringVar())
				raiz.saida_var[i].set("-")
				Label(self, textvariable=raiz.saida_var[i], width=l*5).grid(row=linha, column=1)
				Label(self, text=raiz.saida_unidades[i], width=l*1).grid(row=linha, column=2)
				linha += 1

def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def TocarHino():
	mixer.music.load(resource_path("Sounds/Hino-Vasco.mp3"))
	mixer.music.play(loops=-1)

if __name__ == "__main__":
	mixer.init()
	# TocarHino()
	app = Vasco()
	app.resizable(False, False)
	app.title("VASCO")
	app.iconbitmap(resource_path("Images/Cruz-De-Malta.ico"))
	app.mainloop()