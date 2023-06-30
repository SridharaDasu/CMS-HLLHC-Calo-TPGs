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
    rows, cols = arr.shape
    new_rows = rows // N * N
    new_cols = cols // M * M
    arr_resized = arr[:new_rows, :new_cols]
    
    A = []
    for v in np.vsplit(arr_resized, N):
        A.extend([*np.hsplit(v, M)])
    
    return np.array(A)


def rescale(crystal):
    crystal_ieta_list = []
    crystal_iphi_list = []
    crystal_pt_list = []
    for i in range(len(crystal.pt)):
         if crystal.eta[i] >= - 1.479 and crystal.eta[i] <= 1.479:
                if crystal.phi[i] >= - 3.1415927 and crystal.phi[i] <= 3.1415927:
                    crystal_ieta = math.floor(crystal.eta[i] / crystal_size) 
                    crystal_iphi = math.floor(crystal.phi[i] / crystal_size) 
                    crystal_pt = crystal.pt[i]
                    #print(crystal_ieta, crystal_iphi, crystal_pt)
                    crystal_ieta_list.append(crystal_ieta)
                    crystal_iphi_list.append(crystal_iphi)
                    crystal_pt_list.append(crystal_pt)
                else:
                    continue
    return crystal_ieta_list, crystal_iphi_list, crystal_pt_list


def arr(crystal_pt, crystal_ieta, crystal_iphi):
    s = (360,150)
    crystal_arr = np.zeros(s)
    for i in range(len(crystal_pt)):
        if crystal_ieta[i] >= -75 and crystal_ieta[i] <= 75:
            if crystal_ieta[i] < 0:
                curr_ieta = crystal_ieta[i] + 75
            else:
                curr_ieta = crystal_ieta[i] + 74
            curr_pt = crystal_pt[i]
            curr_iphi = crystal_iphi[i] - 1
            crystal_arr[curr_iphi][curr_ieta] = curr_pt
        else:
            continue
    return crystal_arr


try:
    data = uproot.open(sys.argv[1] + ".root")
except Exception:
    data = uproot.open("2.root")

from tqdm import tqdm

# +
tree = data["l1NtupleSingleProducer/dispTree"]
events = tree["ecalTPGs"]
event_no = 0
data_array = []

for event in tqdm(events.arrays()):
    event_no += 1
    crystal_px = event.ecalTPGs.fP.fX
    crystal_py = event.ecalTPGs.fP.fY
    crystal_pz = event.ecalTPGs.fP.fZ
    crystal = vector.awk({"px":crystal_px, "py":crystal_py, "pz":crystal_pz})
    crystal_arr = rescale(crystal)
    crystal_ieta = crystal_arr[0]
    crystal_iphi = crystal_arr[1]
    crystal_pt = crystal_arr[2]
    crystal_arr_sized = arr(crystal_pt, crystal_ieta, crystal_iphi)
    resampled_crystal_arr = ressample(crystal_arr_sized, 36, 15)
    data_array.append(resampled_crystal_arr)
# +
main_data_array = data_array[0]
for ar in tqdm(data_array):
    main_data_array = np.append(main_data_array, ar, axis=0)
    
main_data_array.shape
crystal_data = 'crystal_array.npy'
np.save(crystal_data, main_data_array)
# -


counter = 0
variable = 0
for ar in main_data_array:
    counter += 1
    variable = 1
    if counter == 73:
        variable += 1
        counter = 0
    plt.imshow(1 - ((ar.T - np.min(ar))/np.max(ar)), cmap="gray")
    plt.ylabel(r'$i_\eta$', fontsize=15)
    plt.xlabel(r'$i_\phi$', fontsize=15)
    plt.title(f'Crystal $E_T$ for event {variable}')
    plt.show()
    plt.savefig('crystal_plots.png')

events = tree["newClusters"]
data_array_cluster = []
event_no = 0 
for event in tqdm(events.arrays()):
    event_no += 1
    cluster_px = event.newClusters.fP.fX
    cluster_py = event.newClusters.fP.fY
    cluster_pz = event.newClusters.fP.fZ
    cluster = vector.awk({"px":cluster_px, "py":cluster_py, "pz":cluster_pz})
    cluster_arr = rescale(cluster)
    cluster_ieta = cluster_arr[0]
    cluster_iphi = cluster_arr[1]
    cluster_pt = cluster_arr[2]
    cluster_arr_sized = arr(cluster_pt, cluster_ieta, cluster_iphi)
    resampled_cluster_arr = ressample(cluster_arr_sized, 36, 15)
    data_array_cluster.append(resampled_cluster_arr)

# +
main_data_array_cluster = data_array_cluster[0]
for ar in tqdm(data_array_cluster):
    main_data_array_cluster = np.append(main_data_array_cluster, ar, axis=0)
    
main_data_array_cluster.shape
cluster_data = 'cluster_array.npy'
np.save(cluster_data, main_data_array_cluster)
# -

counter = 0
variable = 0
for ar in main_data_array_cluster:
    counter += 1
    variable = 1
    if counter == 73:
        variable += 1
        counter = 0
    plt.imshow(1 - ((ar.T - np.min(ar))/np.max(ar)), cmap="gray")
    plt.ylabel(r'$i_\eta$', fontsize=15)
    plt.xlabel(r'$i_\phi$', fontsize=15)
    plt.title(f'Cluster $E_T$ for event {variable}')
    plt.show()
    plt.savefig('cluster_plots.png')

# + active=""
#



