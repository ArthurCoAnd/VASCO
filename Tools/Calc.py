# ✠ VASCO
# "A LICENÇA BEER-WARE" ou "A LICENÇA DA CERVEJA" (Revisão 42):
# <arthurcoand@gmail.com>/<ingridikremer@hotmail.com>/<jg2001.avellar@gmail.com> escreveu este arquivo.
# Enquanto você manter este comentário, você poderá fazer o que quiser com este arquivo.
# Caso nos encontremos algum dia e você ache que este arquivo vale, você poderá me comprar uma cerveja em retribuição.
# Arthur Cordeiro Andrade, Ingridi dos Santos Kremer e João Gabriel Silva de Avellar.

# Bibliotecas
from math import acos, degrees, sqrt, sin, cos, atan

# Gerador de ASCII:
# https://arthursonzogni.com/Diagon/#Math

def pol(c):
	return f"{abs(c)} < {degrees(atan(c.imag/c.real))}º"

def rec(rho, phi):
	x = rho * cos(phi)
	y = rho * sin(phi)
	return complex(x, y)

# =================================
# = Calculos Circuito Equivalente =
# =================================

#         2       2       2
#      Vvz    Rphi  + Xphi 
# Rc = ──── = ─────────────
#       Pvz       Rphi     
def cRc1(d):
	if d["lE"] == 0:
		return (d["Vvz"]**2)/d["Pvz"]
	else:
		return d["Rc2"]*(d["a"]**2)

#          2       2
#      Rphi  + Xphi 
# Xm = ─────────────
#          Xphi     
def cXm1(d):
	if d["lE"] == 0:
		return (d["Rphi"]**2 + d["Xphi"]**2)/d["Xphi"]
	else:
		return d["Xm2"]*(d["a"]**2)

#         2       2       2
#      Vvz    Rphi  + Xphi 
# Rc = ──── = ─────────────
#       Pvz       Rphi     
def cRc2(d):
	if d["lE"] == 1:
		return (d["Vvz"]**2)/d["Pvz"]
	else:
		return d["Rc1"]/(d["a"]**2)

#          2       2
#      Rphi  + Xphi 
# Xm = ─────────────
#          Xphi     
def cXm2(d):
	if d["lE"] == 1:
		return (d["Rphi"]**2 + d["Xphi"]**2)/d["Xphi"]
	else:
		return d["Xm1"]/(d["a"]**2)

#          Vvz
# |zphi| = ───
#          Ivz
def cZphi(d):
	return d["Vvz"]/d["Ivz"]

#         Pvz
# Rphi = ────
#           2
#        Ivz 
def cRphi(d):
	return d["Pvz"]/(d["Ivz"]**2)

#           _______________
#          ╱      2       2
# Xphi = ╲╱ |Zphi|  - Rphi 
def cXphi(d):
	return sqrt(d["Zphi"]**2 - d["Rphi"]**2)

#         Vcc
# |Zcc| = ───
#         Icc
def cZcc(d):
	return d["Vcc"]/d["Icc"]

#        Pcc
# Req = ────
#          2
#       Icc 
def cReq(d):
	return d["Pcc"]/(d["Icc"]**2)

#          _____________
#         ╱     2      2
# Xeq = ╲╱ |Zcc|  - Req 
def cXeq(d):
	return sqrt(d["Zcc"]**2 - d["Req"]**2)

#            Req
# R1 = R2' = ───
#             2 
def cR1(d):
	if d["lE"] == 1:
		return d["Req"]/2
	else:
		return d["R2"]*(d["a"]**2)

#            Xeq
# X1 = X2' = ───
#             2 
def cX1(d):
	if d["lE"] == 1:
		return d["Xeq"]/2
	else:
		return d["X2"]*(d["a"]**2)

#            R1
# R1' = R2 = ──
#             2
#            a 
def cR2(d):
	if d["lE"] == 0:
		return d["Req"]/2
	else:
		return d["R1"]/(d["a"]**2)

#            X1
# X1' = X2 = ──
#             2
#            a 
def cX2(d):
	if d["lE"] == 0:
		return d["Xeq"]/2
	else:
		return d["X1"]/(d["a"]**2)

# ====================================
# = Calculos Circuito Equivalente PU =
# ====================================

def cZ1b(d):
	return (d["V1b"]**2)/d["Sb"]

def cZ2b(d):
	return (d["V2b"]**2)/d["Sb"]

def cRcpu(d):
	return d["Rc2"]/d["Z2b"]

def cXmpu(d):
	return d["Xm2"]/d["Z2b"]

def cRpu(d):
	return d["R2"]/d["Z2b"]

def cXpu(d):
	return d["X2"]/d["Z2b"]

# ====================================
# = Calculos Eficiência e Rendimento =
# ====================================

def cI2(d):
	return rec(d["Sop"]/d["V2op"],d["ang"])

def cE2(d):
	return d["V2op"]+complex(d["R2"],d["X2"])*d["I2"]

def cIc(d):
	return d["E2"]/d["Rc2"]

def cIm(d):
	return d["E2"]/complex(0,d["Xm2"])

def cI1_(d):
	return d["I2"]+d["Ic"]+d["Im"]

def cI1(d):
	return d["I1_"]/d["a"]

def cV1_(d):
	return d["E2"]+complex(d["R2"],d["X2"])*d["I1_"]

def cV1op(d):
	return d["V1_"]*d["a"]

def cPcu1(d):
	return d["R2"]*(abs(d["I1_"])**2)

def cPcu2(d):
	return d["R2"]*(abs(d["I2"])**2)

def cPcu(d):
	return float(d["Pcu1"])+float(d["Pcu2"])

def cPnu(d):
	return (abs(d["E2"])**2)/d["Rc2"]

def cPt(d):
	return float(d["Pcu"])+float(d["Pnu"])

def cRt(d):
	return 100*(abs(d["V1_"])-d["V2op"])/d["V2op"]

def cNef(d):
	return 100*d["Sop"]*d["FP"]/(d["Pt"]+d["Sop"]*d["FP"])

# =======================================
# = Calculos Eficiência e Rendimento PU =
# =======================================

def cV1pu(d):
	return d["V1op"]/d["V1b"]

def cV2pu(d):
	return d["V2op"]/d["V2b"]

def cI1pu(d):
	return d["I1"]/d["I1b"]

def cI2pu(d):
	return d["I2"]/d["I2b"]

# ===================================
# = Calculos Valores Inicias e Base =
# ===================================

def ca(d):
	return d["V1"]/d["V2"]

def cFP(d):
	try: return float(d["FP"])
	except: return 1

def cang(d):
	if d["tFP"] == 0:
		return -acos(d["FP"])
	else:
		return acos(d["FP"])

def cSop(d):
	try:
		return float(d["C"])
	except:
		return d["Pn"]

def cV2op(d):
	try:
		return float(d["V2c"])
	except:
		return d["V2"]

def cSb(d):
	try:
		return float(d["Spu"])
	except:
		return d["Pn"]

def cV2b(d):
	try:
		return float(d["V2pue"])
	except:
		return d["V2"]

def cV1b(d):
	return d["V2b"]*d["a"]

def cI2b(d):
	return d["Sb"]/d["V2b"]

def cI1b(d):
	return d["Sb"]/d["V1b"]