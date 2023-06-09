import os
import sys
import uproot
import vector
import numpy as np
import matplotlib.pyplot as plt

crystal_size = 2. * 3.1415927 / 360.

try:
    data = uproot.open(sys.argv[1] + ".root")
except Exception:
    data = uproot.open("2.root")

tree = data["l1NtupleSingleProducer/dispTree"]
crystals = tree["ecalTPGs"]
clusters = tree["newClusters"]
assert(crystals.num_entries == clusters.num_entries)
for event_no in range(0, crystals.num_entries):
    crystal = crystals.arrays()[event_no]
    crystal_px = crystal.ecalTPGs.fP.fX
    crystal_py = crystal.ecalTPGs.fP.fY
    crystal_pz = crystal.ecalTPGs.fP.fZ
    crystal = vector.awk({"px":crystal_px, "py":crystal_py, "pz":crystal_pz})
    # print("Crystal (pt, eta, phi):", crystal.pt, crystal.eta, crystal.phi)
    cluster = clusters.arrays()[event_no]
    cluster_px = cluster.newClusters.fP.fX
    cluster_py = cluster.newClusters.fP.fY
    cluster_pz = cluster.newClusters.fP.fZ
    cluster = vector.awk({"px":cluster_px, "py":cluster_py, "pz":cluster_pz})
    # print("Cluster (pt, eta, phi):", cluster.pt, cluster.eta, cluster.phi)
    fig, ax = plt.subplots(2)
    ax[0].scatter(crystal.eta, crystal.phi, c=crystal.pt, s=crystal.pt, alpha=0.5)
    ax[0].set_xlabel(r'$\eta$', fontsize=15)
    ax[0].set_ylabel(r'$\phi$', fontsize=15)
    ax[0].set_title(f'Crystal $E_T$ for event {event_no}')
    ax[0].grid(True)
    ax[1].scatter(cluster.eta, cluster.phi, c=cluster.pt, s=cluster.pt, alpha=0.5)
    ax[1].set_xlabel(r'$\eta$', fontsize=15)
    ax[1].set_ylabel(r'$\phi$', fontsize=15)
    ax[1].set_title(f'Cluster $E_T$ for event {event_no}')
    ax[1].grid(True)
    fig.tight_layout()
    plt.pause(1)
    event_no += 1


