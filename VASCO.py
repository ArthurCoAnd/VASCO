# ✠ VASCO
# "A LICENÇA BEER-WARE" ou "A LICENÇA DA CERVEJA" (Revisão 42):
# <arthurcoand@gmail.com>/<ingridikremer@hotmail.com>/<jg2001.avellar@gmail.com> escreveu este arquivo.
# Enquanto você manter este comentário, você poderá fazer o que quiser com este arquivo.
# Caso nos encontremos algum dia e você ache que este arquivo vale, você poderá me comprar uma cerveja em retribuição.
# Arthur Cordeiro Andrade, Ingridi dos Santos Kremer e João Gabriel Silva de Avellar.

# Bibliotecas
from pygame import mixer
from tkinter import *
import os
import sys
# Ferramentas
from Tools.Calc import *
from Tools.GerarGráfico import GerarGráfico as GG

class Vasco(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.config(padx=15, pady=15)
		self.dados = {}
		self.Entradas(self).grid(row=0,column=0)
		self.CircuitoEquivalente(self).grid(row=0, column=1)
		self.Saida(self).grid(row=0, column=3)

	def Calcular(self, *args):
		self.lerDados()
		self.calcularDados()
		print(self.dados)

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
		for i in range(len(self.entradas_pu_t)):
			try:
				self.dados[self.entradas_pu_t[i]] = float(self.entradas_pu_var[i].get())
				self.entradas_pu[i].config(bg="white")
			except:
				self.dados[self.entradas_pu_t[i]] = ""
				self.entradas_pu[i].config(bg="red")

	def calcularDados(self):
		calcs = ["a","FP","ang","Sop","V2op","Sb","V2b","V1b","Z2b","Z1b","I2b","I1b"]
		for i in range(len(calcs)):
			try:
				self.dados[calcs[i]] = eval("c"+calcs[i]+"(self.dados)")
			except: pass
		# Circuito Equivalente
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
		# Circuito Equivalente PU
		for i in range(len(self.CEpu_txt)):
			try:
				self.dados[self.CEpu_txt[i]] = eval("c"+self.CEpu_txt[i]+"(self.dados)")
				self.resultados_CEpu_var[i].set(str(self.dados[self.CEpu_txt[i]]))
			except:
				self.dados[self.CEpu_txt[i]] = "-"
				self.resultados_CEpu_var[i].set(self.dados[self.CEpu_txt[i]])
		# Saida
		saida_pol = ["I2","E2","Ic","Im","I1_","V1_","V1op","I1"]
		for i in range(len(self.saida_txt)):
			try:
				self.dados[self.saida_txt[i]] = eval("c"+self.saida_txt[i]+"(self.dados)")
				polar = False
				for ii in range(len(saida_pol)):
					if self.saida_txt[i] == saida_pol[ii]:
						polar = True
						break
				if polar:
					self.saida_var[i].set(pol(self.dados[self.saida_txt[i]]))
				else:
					self.saida_var[i].set(str(self.dados[self.saida_txt[i]]))
			except:
				self.dados[self.saida_txt[i]] = "-"
				self.saida_var[i].set(self.dados[self.saida_txt[i]])
		# Saida PU
		for i in range(len(self.saidaPU_txt)):
			try:
				self.dados[self.saidaPU_txt[i]] = eval("c"+self.saidaPU_txt[i]+"(self.dados)")
				self.saidaPU_var[i].set(pol(self.dados[self.saidaPU_txt[i]]))
			except:
				self.dados[self.saidaPU_txt[i]] = "-"
				self.saidaPU_var[i].set(self.dados[self.saidaPU_txt[i]])

	def CriarGráfico(self):
		d = self.dados.copy()
		try:
			GG(d)
		except: pass

	class Entradas(Frame):
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
				Label(self, text=raiz.entradas_nominais_txt[i]).grid(row=linha, column=0)
				raiz.entradas_nominais_var.append(StringVar())
				raiz.entradas_nominais_var[i].trace("w", raiz.Calcular)
				raiz.entradas_nominais.append(Entry(self, textvariable=raiz.entradas_nominais_var[i]))
				raiz.entradas_nominais[i].grid(row=linha, column=1)
				Label(self, text=raiz.entradas_nominais_unidades[i]).grid(row=linha, column=2)
				linha += 1
			# Entradas Ensaio
			raiz.lado_ensaio = IntVar()
			raiz.lado_ensaio.set(1)
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
						Radiobutton(self, text="Ensaio Vazio - "+raiz.lados_ensaio_txt[ii], variable=raiz.lado_ensaio, value=ii, command=raiz.Calcular).grid(row=linha, column=ii)
				else:
					Label(self, text="Ensaio Curto-Circuito").grid(row=linha, column=0, columnspan=3)
				linha += 1
				for ii in range(len(raiz.entradas_ensaio_txt)):
					Label(self, text=raiz.entradas_ensaio_txt[ii]+raiz.entradas_ensaio_tipo_txt[i]).grid(row=linha, column=0)
					raiz.entradas_ensaio_var[i].append(StringVar())
					raiz.entradas_ensaio_var[i][ii].trace("w", raiz.Calcular)
					raiz.entradas_ensaio[i].append(Entry(self, textvariable=raiz.entradas_ensaio_var[i][ii]))
					raiz.entradas_ensaio[i][ii].grid(row=linha, column=1)
					Label(self, text=raiz.entradas_ensaio_unidades[ii]).grid(row=linha, column=2)
					linha += 1
			# Entradas Saida
			raiz.tipo_FP = IntVar()
			raiz.tipo_FP_txt = ["Indutivo/Atrasado","Capacitivo/Adiantado"]
			for i in range(len(raiz.tipo_FP_txt)):
				Radiobutton(self, text="FP - "+raiz.tipo_FP_txt[i], variable=raiz.tipo_FP, value=i, command=raiz.Calcular).grid(row=linha, column=i)
			linha += 1
			raiz.entradas_saida = []
			raiz.entradas_saida_var = []
			raiz.entradas_saida_t = ["FP","C","V2c"]
			raiz.entradas_saida_txt = ["FP","Potência de Operação","Tensão de Operação"]
			raiz.entradas_saida_unidades = ["","VA","V"]
			for i in range(len(raiz.entradas_saida_txt)):
				Label(self, text=raiz.entradas_saida_txt[i]).grid(row=linha, column=0)
				raiz.entradas_saida_var.append(StringVar())
				raiz.entradas_saida_var[i].trace("w", raiz.Calcular)
				raiz.entradas_saida.append(Entry(self, textvariable=raiz.entradas_saida_var[i]))
				raiz.entradas_saida[i].grid(row=linha, column=1)
				Label(self, text=raiz.entradas_saida_unidades[i]).grid(row=linha, column=2)
				linha += 1
			raiz.entradas_pu = []
			raiz.entradas_pu_var = []
			raiz.entradas_pu_t = ["Spu","V2pue"]
			raiz.entradas_pu_txt = ["Potência Base","Tensão Secundário Base"]
			raiz.entradas_pu_unidades = ["VA","V"]
			for i in range(len(raiz.entradas_pu_txt)):
				Label(self, text=raiz.entradas_pu_txt[i]).grid(row=linha, column=0)
				raiz.entradas_pu_var.append(StringVar())
				raiz.entradas_pu_var[i].trace("w", raiz.Calcular)
				raiz.entradas_pu.append(Entry(self, textvariable=raiz.entradas_pu_var[i]))
				raiz.entradas_pu[i].grid(row=linha, column=1)
				Label(self, text=raiz.entradas_pu_unidades[i]).grid(row=linha, column=2)
				linha += 1
			# Botão Gerar Gráfico
			Button(self, text="Gerar Gráfico", command=raiz.CriarGráfico).grid(row=linha, column=0)
			
	class CircuitoEquivalente(Frame):
		def __init__(self, raiz):
			Frame.__init__(self, raiz)
			self.config(padx=25, pady=15)
			raiz.CE_txt = ["Rc1","Xm1","R1","X1","Rc2","Xm2","R2","X2"]
			raiz.CE_unidade = ["Ω","Ω","Ω","Ω","Ω","Ω","Ω","Ω"]
			raiz.resultados_CE_var = []
			linha = 0
			for i in range(len(raiz.CE_txt)):
				Label(self, text=raiz.CE_txt[i]).grid(row=linha, column=0)
				raiz.resultados_CE_var.append(StringVar())
				raiz.resultados_CE_var[i].set("-")
				Label(self, textvariable=raiz.resultados_CE_var[i]).grid(row=linha, column=1)
				Label(self, text=raiz.CE_unidade[i]).grid(row=linha, column=2)
				linha += 1
			# PU
			raiz.CEpu_txt = ["Rcpu","Xmpu","Rpu","Xpu"]
			raiz.CEpu_unidade = ["pu","pu","pu","pu"]
			raiz.resultados_CEpu_var = []
			for i in range(len(raiz.CEpu_txt)):
				Label(self, text=raiz.CEpu_txt[i]).grid(row=linha, column=0)
				raiz.resultados_CEpu_var.append(StringVar())
				raiz.resultados_CEpu_var[i].set("-")
				Label(self, textvariable=raiz.resultados_CEpu_var[i]).grid(row=linha, column=1)
				Label(self, text=raiz.CEpu_unidade[i]).grid(row=linha, column=2)
				linha += 1

	class Saida(Frame):
		def __init__(self, raiz):
			Frame.__init__(self, raiz)
			self.config(padx=25, pady=15)
			linha = 0
			raiz.saida_txt = ["I2","E2","Ic","Im","I1_","V1_","V1op","I1","Pcu1","Pcu2","Pcu","Pnu","Pt","Rt","Nef"]
			raiz.saida_unidades = ["A","V","A","A","A","V","V","A","W","W","W","W","W","%","%"]
			raiz.saida_var = []
			for i in range(len(raiz.saida_txt)):
				Label(self, text=raiz.saida_txt[i]).grid(row=linha, column=0)
				raiz.saida_var.append(StringVar())
				raiz.saida_var[i].set("-")
				Label(self, textvariable=raiz.saida_var[i]).grid(row=linha, column=1)
				Label(self, text=raiz.saida_unidades[i]).grid(row=linha, column=2)
				linha += 1
				# PU
			raiz.saidaPU_txt = ["V1pu","I1pu","V2pu","I2pu"]
			raiz.saidaPU_unidades = ["pu","pu","pu","pu"]
			raiz.saidaPU_var = []
			for i in range(len(raiz.saidaPU_txt)):
				Label(self, text=raiz.saidaPU_txt[i]).grid(row=linha, column=0)
				raiz.saidaPU_var.append(StringVar())
				raiz.saidaPU_var[i].set("-")
				Label(self, textvariable=raiz.saidaPU_var[i]).grid(row=linha, column=1)
				Label(self, text=raiz.saidaPU_unidades[i]).grid(row=linha, column=2)
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
	TocarHino()
	app = Vasco()
	app.resizable(False, False)
	app.title("VASCO")
	app.iconbitmap(resource_path("Images/Cruz-De-Malta.ico"))
	app.mainloop()