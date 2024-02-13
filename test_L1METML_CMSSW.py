import ROOT
from DataFormats.FWLite import Events, Handle
import numpy as np

events = Events('test.root')
handle_pf = Handle('vector<l1t::EtSum>')
handle_ml = Handle('vector<l1t::EtSum>')
handle_gen = Handle('vector<reco::GenMET>')
label_pf = 'l1tMETPFProducer'
label_ml = 'l1tMETMLProducer'
label_gen = 'genMetTrue'
met_ml_pt, met_ml_phi = [], []
met_pf_pt, met_pf_phi = [], []
met_gen_pt, met_gen_phi = [], []
for event in events:
    event.getByLabel(label_pf, handle_pf)
    event.getByLabel(label_ml, handle_ml)
    event.getByLabel(label_gen, handle_gen)
    sums_pf = handle_pf.product()
    sums_ml = handle_ml.product()
    sums_gen = handle_gen.product()
    met_ml_pt.append(sums_ml[0].pt())
    met_ml_phi.append(sums_ml[0].phi())
    met_pf_pt.append(sums_pf[0].pt())
    met_pf_phi.append(sums_pf[0].phi())
    met_gen_pt.append(sums_gen[0].pt())
    met_gen_phi.append(sums_gen[0].phi())

met_ml_pt = np.array(met_ml_pt)
met_ml_phi = np.array(met_ml_phi)
met_pf_pt = np.array(met_pf_pt)
met_pf_phi = np.array(met_pf_phi)
met_gen_pt = np.array(met_gen_pt)
met_gen_phi = np.array(met_gen_phi)


import seaborn
import pandas as pd
import matplotlib.pyplot as plt
import scipy

df = pd.DataFrame.from_dict({'Gen MET': met_gen_pt, 'PUPPI MET': met_pf_pt, 'ML MET': met_ml_pt})
#df = pd.DataFrame.from_dict({'PUPPI MET': met_pf_pt, 'ML MET': met_ml_pt})
plt.figure()
seaborn.pairplot(df, corner=True)
plt.savefig('profiling_MET.png', dpi=300)

df = pd.DataFrame.from_dict({'Gen MET x': met_gen_pt*np.cos(met_gen_phi), 'PUPPI MET x': met_pf_pt*np.cos(met_pf_phi), 'ML MET x': met_ml_pt*np.cos(met_ml_phi)})
#df = pd.DataFrame.from_dict({'PUPPI MET x': met_pf_pt*np.cos(met_pf_phi), 'ML MET x': met_ml_pt*np.cos(met_ml_phi)})
plt.figure()
seaborn.pairplot(df, corner=True)
plt.savefig('profiling_MET_x.png', dpi=300)

df = pd.DataFrame.from_dict({'Gen MET y': met_gen_pt*np.sin(met_gen_phi), 'PUPPI MET y': met_pf_pt*np.sin(met_pf_phi), 'ML MET y': met_ml_pt*np.sin(met_ml_phi)})
#df = pd.DataFrame.from_dict({'PUPPI MET y': met_pf_pt*np.sin(met_pf_phi), 'ML MET y': met_ml_pt*np.sin(met_ml_phi)})
plt.figure()
seaborn.pairplot(df, corner=True)
plt.savefig('profiling_MET_y.png', dpi=300)

response_pup = met_pf_pt / met_gen_pt
response_pred = met_ml_pt / met_gen_pt
bins = np.linspace(0, 2, 25)
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.hist(response_pup, bins=bins, label=f'PUPPI, median={np.median(response_pup):0.2f}, IQR={scipy.stats.iqr(response_pup):0.2f}')
plt.legend()
plt.xlabel("MET response $\hat{y}/y$")
plt.ylabel("Events")
plt.subplot(1, 2, 2)
plt.hist(response_pred, bins=bins, label=f'ML, median={np.median(response_pred):0.2f}, IQR={scipy.stats.iqr(response_pred):0.2f}')
plt.legend()
plt.xlabel("MET response $\hat{y}/y$")
plt.ylabel("Events")
plt.tight_layout()
plt.savefig("response_MET.png", dpi=300)
