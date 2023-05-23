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
events = tree["ecalTPGs"]
for event in events.arrays():
    crystal_px = event.ecalTPGs.fP.fX
    crystal_py = event.ecalTPGs.fP.fY
    crystal_pz = event.ecalTPGs.fP.fZ
    crystal = vector.awk({"px":crystal_px, "py":crystal_py, "pz":crystal_pz})
    print("Crystal (pt, eta, phi):", crystal.pt, crystal.eta, crystal.phi)

events = tree["newClusters"]
for event in events.arrays():
    cluster_px = event.newClusters.fP.fX
    cluster_py = event.newClusters.fP.fY
    cluster_pz = event.newClusters.fP.fZ
    cluster = vector.awk({"px":cluster_px, "py":cluster_py, "pz":cluster_pz})
    print("Cluster (pt, eta, phi):", cluster.pt, cluster.eta, cluster.phi)

