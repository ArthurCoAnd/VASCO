# ✠ VASCO
# Importar Bibliotecas
from math import acos, degrees, sqrt

# Gerador de ASCII:
# https://arthursonzogni.com/Diagon/#Math

#     V1
# a = ──
#     V2
def ca(d):
	return d["V1"]/d["V2"]

# ang = acos(FP)
def cang(d):
	if d["eFP"] == 0:
		return degrees(acos(d["FP"]))
	else:
		return -degrees(acos(d["FP"]))

#         2       2       2
#      Vvz    Rphi  + Xphi 
# Rc = ──── = ─────────────
#       Pvz       Rphi     
def cRc(d):
	return (d["Vvz"]**2)/d["Pvz"]

#          2       2
#      Rphi  + Xphi 
# Xm = ─────────────
#          Xphi     
def cXm(d):
	return (d["Rphi"]**2 + d["Xphi"]**2)/d["Xphi"]

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
	return d["Req"]/2

#            R1
# R1' = R2 = ──
#             2
#            a 
def cR1_(d):
	return d["R1"]/(d["a"]**2)

#            Xeq
# X1 = X2' = ───
#             2 
def cX1(d):
	return d["Xeq"]/2

#            X1
# X1' = X2 = ──
#             2
#            a 
def cX1_(d):
	return d["X1"]/(d["a"]**2)
