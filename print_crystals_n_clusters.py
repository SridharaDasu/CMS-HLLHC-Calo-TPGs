import os
import sys
import uproot
import vector
import math
import numpy as np
import awkward as ak
import numba as nb
import matplotlib.pyplot as plt

crystal_size = 2. * 3.1415927 / 360.
print(crystal_size)


def ressample(arr, N, M):
    A = []
    for v in np.vsplit(arr, arr.shape[0] // N):
        A.extend([*np.hsplit(v, arr.shape[1] // M)])
    return np.array(A)


def rescale(crystal):
    s = (170, 360)
    crystal_arr = np.zeros(s)
    crystal_ieta_list = []
    crystal_iphi_list = [] 
    crystal_pt_list = []
    for i in range(len(crystal.pt)):
         if crystal.eta[i] >= 0 and crystal.eta[i] <= 1.479:
                if crystal.phi[i] >= 0 and crystal.phi[i] <= 2. * 3.1415927:
                    crystal_ieta = math.floor(crystal.eta[i] // crystal_size)
                    crystal_iphi = math.floor(crystal.phi[i] // crystal_size)
                    crystal_pt = math.floor(crystal.pt[i])
                    crystal_arr[(crystal_ieta)][(crystal_iphi)]= (crystal_pt)
                else:
                    continue
    new_crystal_arr = np.unique(crystal_arr)
    return crystal_arr


try:
    data = uproot.open(sys.argv[1] + ".root")
except Exception:
    data = uproot.open("2.root")

from tqdm import tqdm

tree = data["l1NtupleSingleProducer/dispTree"]
events = tree["ecalTPGs"]
data_array = []
for event in tqdm(events.arrays()):
    crystal_px = event.ecalTPGs.fP.fX
    crystal_py = event.ecalTPGs.fP.fY
    crystal_pz = event.ecalTPGs.fP.fZ
    crystal = vector.awk({"px":crystal_px, "py":crystal_py, "pz":crystal_pz})
    #print("Crystal (pt, eta, phi):", crystal.pt, crystal.eta, crystal.phi)
    crystal_arr = rescale(crystal)
    resampled_crystal_arr = ressample(crystal_arr, 5, 6)
    data_array.append(resampled_crystal_arr)

    
main_data_array = data_array[0]
for ar in tqdm(data_array[1:]):
    main_data_array = np.append(main_data_array, ar, axis=0)

main_data_array.shape

for ar in tqdm(main_data_array):
    plt.imshow(1 - ((ar.T - np.min(ar))/np.max(ar)), cmap="gray")
    plt.xlabel(r'$i_\eta$', fontsize=15)
    plt.ylabel(r'$i_\phi$', fontsize=15)
    plt.title(f'Crystal $E_T$')
    plt.show()

events = tree["newClusters"]
data_array_cluster = []
for event in tqdm(events.arrays()):
    cluster_px = event.newClusters.fP.fX
    cluster_py = event.newClusters.fP.fY
    cluster_pz = event.newClusters.fP.fZ
    cluster = vector.awk({"px":cluster_px, "py":cluster_py, "pz":cluster_pz})
    cluster_arr = rescale(cluster)
    resampled_cluster_arr = ressample(cluster_arr, 5, 6)
    data_array_cluster.append(resampled_cluster_arr)


main_data_array_cluster = data_array_cluster[0]
for ar in tqdm(data_array[1:]):
    main_data_array_cluster = np.append(main_data_array_cluster, ar, axis=0)

main_data_array_cluster.shape


for ar in tqdm(main_data_array_cluster):
    plt.imshow(1 - ((ar.T - np.min(ar))/np.max(ar)), cmap="gray")
    plt.xlabel(r'$i_\eta$', fontsize=15)
    plt.ylabel(r'$i_\phi$', fontsize=15)
    plt.title(f'Cluster $E_T$')
    plt.show()


