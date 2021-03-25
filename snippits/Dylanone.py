import numpy as np
import matplotlib.pyplot as plt
import math

PIX = 1000  # number of pixels sampled
DATA = 100  # number of data points
# Parameters
edn = 2  # e−/DN
RN_e = 3  # read noise (e−)
RN = RN_e/edn  # read noise (DN)
FW_e = 10**5  # full well (e−)
FW = FW_e/edn  # full well (DN)
SCALE = DATA/math.log10(FW)  # full well scale factor
PN = 0.01  # FPN factor

T = 300  # operating temperature (K)
k1 = 8.62*1e-05  # Boltzmann’s constant
DFM = 0.5  # dark current ﬁgure of merit (nA/cmˆ2)
DN = 0.30  # dark FPN factor
PA = (8*1e-04)**2  # pixel area (cmˆ2)
t = 0.3  # integration time
Eg = 1.1557-((T**2)*7.021*1e-04)/(1108+T)  # silicon band gap energy (eV)
DARK_e = t*2.55*(10**15)*PA*DFM*(T**1.5)*math.exp(-Eg/(2*k1*T))  # dark current (e−)
DARK = DARK_e/edn  # dark current (DN)​


C = np.random.randn(PIX, 1)  # random number generator for FPN
F = np.random.randn(PIX, 1)  # random number generator for dark FPN
# ​
SIG1 = np.ones((PIX, DATA))
SIG2 = np.ones((PIX, DATA))
SIG3 = np.ones((PIX, DATA))
SIG4 = np.ones((PIX, DATA))
SIG5 = np.ones((PIX, DATA))

for i in range(0, DATA):
    sig = 10**((i+1)/SCALE)  # signal step (DN)
    A = np.random.randn(PIX, DATA)  # random number generator
    B = np.random.randn(PIX, DATA)  # random number generator
    D = np.random.randn(PIX, DATA)  # random number generator
    read = RN*A[:, i]  # read noise (DN)
    shot = (sig/edn)**0.5*B[:, i]  # shot noise (DN)
    FPN = sig*PN*C[:, 0]  # FPN (DN)
    Dshot = (DARK/edn)**0.5*D[:, i]  # dark shot noise (DN)
    DFPN = DARK*DN*F[:, 0]  # dark FPN (DN)
    SIG1[:, i] = sig+read+shot+FPN+Dshot+DFPN  # read+shot+FPN+dark shot+dark FPN (DN)
    SIG2[:, i] = sig+read+shot+FPN+Dshot  # read+shot+FPN+dark shot (DN)
    SIG3[:, i] = sig+read+shot+Dshot  # read+shot+dark shot (DN)
    SIG4[:, i] = sig+read+shot  # read+shot (DN)
    SIG5[:, i] = sig+read+shot+FPN  # read+shot+FPN+dark shot +dark FPN (DN)

SIGNAL = np.mean(SIG1, axis=0)  # signal(DN)
NOISE2 = np.std(SIG2, axis=0)  # read+shot+FPN+dark shot (DN)
NOISE3 = np.std(SIG3, axis=0)  # read+shot+dark shot (DN)
NOISE1 = np.std(SIG1, axis=0)  # read+shot+FPN+dark shot+dark FPN (DN)
NOISE4 = np.std(SIG4, axis=0)  # read+shot (DN)
NOISE5 = np.std(SIG5, axis=0)  # read+shot+FPN (DN)

SIGNAL_e = np.mean(SIG1, axis=0)*edn  # signal (e−)
NOISE1_e = np.std(SIG1, axis=0)*edn  # read+shot+FPN+dark shot+dark FPN (e−)
NOISE2_e = np.std(SIG2, axis=0)*edn  # read+shot+FPN+dark shot (e−)
NOISE3_e = np.std(SIG3, axis=0)*edn  # read+shot+dark shot (e−)
NOISE4_e = np.std(SIG4, axis=0)*edn  # read+shot (e−)
NOISE5_e = np.std(SIG5, axis=0)*edn  # read+shot+FPN (e−)

# PTC Plot (DN)
plt.loglog(SIGNAL, NOISE1, 'r.', SIGNAL, NOISE2, 'g.', SIGNAL, NOISE3, 'b.', SIGNAL, NOISE4, 'y.', SIGNAL,NOISE5, 'k.')
plt.show()
plt.loglog(SIGNAL, NOISE5, 'k.')
plt.show()








