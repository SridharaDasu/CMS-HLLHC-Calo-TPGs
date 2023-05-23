import os
import sys
import uproot
import vector
import numpy as np
import matplotlib.pyplot as plt

try:
    data = uproot.open(sys.argv[1] + ".root")
except Exception:
    data = uproot.open("2.root")

tree = data["l1NtupleSingleProducer/dispTree"]
events = tree["ecalTPGs"]
for event in events.arrays():
    crystal_px = event.ecalTPGs.fP.fX
    crystal_py = event.ecalTPGs.fP.fY
    crystal_pz = event.ecalTPGs.fP.fZ
    print("Crystal (px, py, pz):", crystal_px, crystal_py, crystal_pz)

events = tree["newClusters"]
for event in events.arrays():
    cluster_px = event.newClusters.fP.fX
    cluster_py = event.newClusters.fP.fY
    cluster_pz = event.newClusters.fP.fZ
    print("Cluster (px, py, pz): ", cluster_px, cluster_py, cluster_pz)
