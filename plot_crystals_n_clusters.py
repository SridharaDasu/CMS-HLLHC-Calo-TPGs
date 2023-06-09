import os
import sys
import numpy
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
    crystal_iphi = numpy.floor_divide(crystal.phi, 0.0174) + 360 / 2
    crystal_ieta = numpy.floor_divide(crystal.eta, 0.0174) + 170 / 2
    cluster = clusters.arrays()[event_no]
    cluster_px = cluster.newClusters.fP.fX
    cluster_py = cluster.newClusters.fP.fY
    cluster_pz = cluster.newClusters.fP.fZ
    cluster = vector.awk({"px":cluster_px, "py":cluster_py, "pz":cluster_pz})
    cluster_iphi = numpy.floor_divide(cluster.phi, 0.0174) + 360 / 2
    cluster_ieta = numpy.floor_divide(cluster.eta, 0.0174) + 170 / 2
    fig, ax = plt.subplots(2)
    ax[0].scatter(crystal_ieta, crystal_iphi, c=crystal.pt, s=crystal.pt, alpha=0.5)
    ax[0].set_xlabel(r'$i_\eta$', fontsize=15)
    ax[0].set_ylabel(r'$i_\phi$', fontsize=15)
    ax[0].set_title(f'Crystal $E_T$ for event {event_no}')
    ax[0].grid(True)
    ax[1].scatter(cluster_ieta, cluster_iphi, c=cluster.pt, s=cluster.pt, alpha=0.5)
    ax[1].set_xlabel(r'$i_\eta$', fontsize=15)
    ax[1].set_ylabel(r'$i_\phi$', fontsize=15)
    ax[1].set_title(f'Cluster $E_T$ for event {event_no}')
    ax[1].grid(True)
    fig.tight_layout()
    plt.pause(1)
    event_no += 1


