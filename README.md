
Installation:

```
git clone https://github.com/SridharaDasu/UprootPyPlot.git
cd UprootPyPlot
virtualenv --python python3 venv
pip3 install --upgrade pip
pip3 install -r requirements.txt
export UprootPyPlot=$PWD
```

Data:

Obtain a Delphes root file from: https://pages.hep.wisc.edu/~dasu/physics535-data

for example:

```
curl https://pages.hep.wisc.edu/~dasu/physics535-data/e+e-ZH/Events/run_01/tag_1_delphes_events.root --output $UprootPyPlot/e+e-ZH.root
```

Analysis:

```
cd $UprootPyPlot
source venv/bin/activate
python plot_dimuon_mass.py e+e-ZH.root
```

The first command sets your directory.

The second command activates the virtual environment, which provides access to the Python libraries needed. You need to run those commands in a new shell when you open it.

The plot should show the invariant mass of dimuons in the data file, clearly showing the Z-mass peak if you use the e+e-ZH.root file. If you pick a file with different type of events, your plot may not show the Z peak. Here is how my plot looks like:

![plot](dimuon-invariant-mass.png)

Proposed Activities:

1) Create di-electron invariant mass plot - does it look similar to dimuon plot? Does the dimuon and dielectron production from the Z-bosons proceed at the same rate?

2) Create di-jet invariant mass - does this plot look similar to dimuon plot? If not, why is that?

3) What about the Higgs bosons in the events? Perhaps, take the Z-events in the dielectron and dimuon modes only, and make di-jet invariant mass for those events. Does that work better?

4) Determine rates of Z decays and H decays in the data sample provided and compare to the Standard Model expectation of the branching fractions. Discuss if there is a match with expectation or otherwise.


Event content:

In order to see what quantities you can access and analyze, the content of the event file can be dumped using the following command (when in the virtual environment):


```
python print_event_content.py e+e-ZH.root
```

The output of the command will look like:

```
(venv) DasuLaptop> python print_event_content.py e+e-ZH.root
Content of the file e+e-ZH.root
The content of the events = input["Delphes;1"] is:
Event
Event/Event.fUniqueID
Event/Event.fBits
Event/Event.Number
Event/Event.ReadTime
Event/Event.ProcTime
Event/Event.ProcessID
Event/Event.MPI
Event/Event.Weight
Event/Event.CrossSection
Event/Event.CrossSectionError
Event/Event.Scale
Event/Event.AlphaQED
Event/Event.AlphaQCD
Event/Event.ID1
Event/Event.ID2
Event/Event.X1
Event/Event.X2
Event/Event.ScalePDF
Event/Event.PDF1
Event/Event.PDF2
Event_size
Weight
Weight/Weight.fUniqueID
Weight/Weight.fBits
Weight/Weight.Weight
Weight_size
Particle
Particle/Particle.fUniqueID
Particle/Particle.fBits
Particle/Particle.PID
Particle/Particle.Status
Particle/Particle.IsPU
Particle/Particle.M1
Particle/Particle.M2
Particle/Particle.D1
Particle/Particle.D2
Particle/Particle.Charge
Particle/Particle.Mass
Particle/Particle.E
Particle/Particle.Px
Particle/Particle.Py
Particle/Particle.Pz
Particle/Particle.P
Particle/Particle.PT
Particle/Particle.Eta
Particle/Particle.Phi
Particle/Particle.Rapidity
Particle/Particle.T
Particle/Particle.X
Particle/Particle.Y
Particle/Particle.Z
Particle_size
Track
Track/Track.fUniqueID
Track/Track.fBits
Track/Track.PID
Track/Track.Charge
Track/Track.P
Track/Track.PT
Track/Track.Eta
Track/Track.Phi
Track/Track.CtgTheta
Track/Track.C
Track/Track.Mass
Track/Track.EtaOuter
Track/Track.PhiOuter
Track/Track.T
Track/Track.X
Track/Track.Y
Track/Track.Z
Track/Track.TOuter
Track/Track.XOuter
Track/Track.YOuter
Track/Track.ZOuter
Track/Track.Xd
Track/Track.Yd
Track/Track.Zd
Track/Track.L
Track/Track.D0
Track/Track.DZ
Track/Track.Nclusters
Track/Track.dNdx
Track/Track.ErrorP
Track/Track.ErrorPT
Track/Track.ErrorPhi
Track/Track.ErrorCtgTheta
Track/Track.ErrorT
Track/Track.ErrorD0
Track/Track.ErrorDZ
Track/Track.ErrorC
Track/Track.ErrorD0Phi
Track/Track.ErrorD0C
Track/Track.ErrorD0DZ
Track/Track.ErrorD0CtgTheta
Track/Track.ErrorPhiC
Track/Track.ErrorPhiDZ
Track/Track.ErrorPhiCtgTheta
Track/Track.ErrorCDZ
Track/Track.ErrorCCtgTheta
Track/Track.ErrorDZCtgTheta
Track/Track.Particle
Track/Track.VertexIndex
Track_size
Tower
Tower/Tower.fUniqueID
Tower/Tower.fBits
Tower/Tower.ET
Tower/Tower.Eta
Tower/Tower.Phi
Tower/Tower.E
Tower/Tower.T
Tower/Tower.NTimeHits
Tower/Tower.Eem
Tower/Tower.Ehad
Tower/Tower.Edges[4]
Tower/Tower.Particles
Tower_size
EFlowTrack
EFlowTrack/EFlowTrack.fUniqueID
EFlowTrack/EFlowTrack.fBits
EFlowTrack/EFlowTrack.PID
EFlowTrack/EFlowTrack.Charge
EFlowTrack/EFlowTrack.P
EFlowTrack/EFlowTrack.PT
EFlowTrack/EFlowTrack.Eta
EFlowTrack/EFlowTrack.Phi
EFlowTrack/EFlowTrack.CtgTheta
EFlowTrack/EFlowTrack.C
EFlowTrack/EFlowTrack.Mass
EFlowTrack/EFlowTrack.EtaOuter
EFlowTrack/EFlowTrack.PhiOuter
EFlowTrack/EFlowTrack.T
EFlowTrack/EFlowTrack.X
EFlowTrack/EFlowTrack.Y
EFlowTrack/EFlowTrack.Z
EFlowTrack/EFlowTrack.TOuter
EFlowTrack/EFlowTrack.XOuter
EFlowTrack/EFlowTrack.YOuter
EFlowTrack/EFlowTrack.ZOuter
EFlowTrack/EFlowTrack.Xd
EFlowTrack/EFlowTrack.Yd
EFlowTrack/EFlowTrack.Zd
EFlowTrack/EFlowTrack.L
EFlowTrack/EFlowTrack.D0
EFlowTrack/EFlowTrack.DZ
EFlowTrack/EFlowTrack.Nclusters
EFlowTrack/EFlowTrack.dNdx
EFlowTrack/EFlowTrack.ErrorP
EFlowTrack/EFlowTrack.ErrorPT
EFlowTrack/EFlowTrack.ErrorPhi
EFlowTrack/EFlowTrack.ErrorCtgTheta
EFlowTrack/EFlowTrack.ErrorT
EFlowTrack/EFlowTrack.ErrorD0
EFlowTrack/EFlowTrack.ErrorDZ
EFlowTrack/EFlowTrack.ErrorC
EFlowTrack/EFlowTrack.ErrorD0Phi
EFlowTrack/EFlowTrack.ErrorD0C
EFlowTrack/EFlowTrack.ErrorD0DZ
EFlowTrack/EFlowTrack.ErrorD0CtgTheta
EFlowTrack/EFlowTrack.ErrorPhiC
EFlowTrack/EFlowTrack.ErrorPhiDZ
EFlowTrack/EFlowTrack.ErrorPhiCtgTheta
EFlowTrack/EFlowTrack.ErrorCDZ
EFlowTrack/EFlowTrack.ErrorCCtgTheta
EFlowTrack/EFlowTrack.ErrorDZCtgTheta
EFlowTrack/EFlowTrack.Particle
EFlowTrack/EFlowTrack.VertexIndex
EFlowTrack_size
EFlowPhoton
EFlowPhoton/EFlowPhoton.fUniqueID
EFlowPhoton/EFlowPhoton.fBits
EFlowPhoton/EFlowPhoton.ET
EFlowPhoton/EFlowPhoton.Eta
EFlowPhoton/EFlowPhoton.Phi
EFlowPhoton/EFlowPhoton.E
EFlowPhoton/EFlowPhoton.T
EFlowPhoton/EFlowPhoton.NTimeHits
EFlowPhoton/EFlowPhoton.Eem
EFlowPhoton/EFlowPhoton.Ehad
EFlowPhoton/EFlowPhoton.Edges[4]
EFlowPhoton/EFlowPhoton.Particles
EFlowPhoton_size
EFlowNeutralHadron
EFlowNeutralHadron/EFlowNeutralHadron.fUniqueID
EFlowNeutralHadron/EFlowNeutralHadron.fBits
EFlowNeutralHadron/EFlowNeutralHadron.ET
EFlowNeutralHadron/EFlowNeutralHadron.Eta
EFlowNeutralHadron/EFlowNeutralHadron.Phi
EFlowNeutralHadron/EFlowNeutralHadron.E
EFlowNeutralHadron/EFlowNeutralHadron.T
EFlowNeutralHadron/EFlowNeutralHadron.NTimeHits
EFlowNeutralHadron/EFlowNeutralHadron.Eem
EFlowNeutralHadron/EFlowNeutralHadron.Ehad
EFlowNeutralHadron/EFlowNeutralHadron.Edges[4]
EFlowNeutralHadron/EFlowNeutralHadron.Particles
EFlowNeutralHadron_size
GenJet
GenJet/GenJet.fUniqueID
GenJet/GenJet.fBits
GenJet/GenJet.PT
GenJet/GenJet.Eta
GenJet/GenJet.Phi
GenJet/GenJet.T
GenJet/GenJet.Mass
GenJet/GenJet.DeltaEta
GenJet/GenJet.DeltaPhi
GenJet/GenJet.Flavor
GenJet/GenJet.FlavorAlgo
GenJet/GenJet.FlavorPhys
GenJet/GenJet.BTag
GenJet/GenJet.BTagAlgo
GenJet/GenJet.BTagPhys
GenJet/GenJet.TauTag
GenJet/GenJet.TauWeight
GenJet/GenJet.Charge
GenJet/GenJet.EhadOverEem
GenJet/GenJet.NCharged
GenJet/GenJet.NNeutrals
GenJet/GenJet.NeutralEnergyFraction
GenJet/GenJet.ChargedEnergyFraction
GenJet/GenJet.Beta
GenJet/GenJet.BetaStar
GenJet/GenJet.MeanSqDeltaR
GenJet/GenJet.PTD
GenJet/GenJet.FracPt[5]
GenJet/GenJet.Tau[5]
GenJet/GenJet.SoftDroppedJet
GenJet/GenJet.SoftDroppedSubJet1
GenJet/GenJet.SoftDroppedSubJet2
GenJet/GenJet.TrimmedP4[5]
GenJet/GenJet.PrunedP4[5]
GenJet/GenJet.SoftDroppedP4[5]
GenJet/GenJet.NSubJetsTrimmed
GenJet/GenJet.NSubJetsPruned
GenJet/GenJet.NSubJetsSoftDropped
GenJet/GenJet.ExclYmerge23
GenJet/GenJet.ExclYmerge34
GenJet/GenJet.ExclYmerge45
GenJet/GenJet.ExclYmerge56
GenJet/GenJet.Constituents
GenJet/GenJet.Particles
GenJet/GenJet.Area
GenJet_size
GenMissingET
GenMissingET/GenMissingET.fUniqueID
GenMissingET/GenMissingET.fBits
GenMissingET/GenMissingET.MET
GenMissingET/GenMissingET.Eta
GenMissingET/GenMissingET.Phi
GenMissingET_size
Jet
Jet/Jet.fUniqueID
Jet/Jet.fBits
Jet/Jet.PT
Jet/Jet.Eta
Jet/Jet.Phi
Jet/Jet.T
Jet/Jet.Mass
Jet/Jet.DeltaEta
Jet/Jet.DeltaPhi
Jet/Jet.Flavor
Jet/Jet.FlavorAlgo
Jet/Jet.FlavorPhys
Jet/Jet.BTag
Jet/Jet.BTagAlgo
Jet/Jet.BTagPhys
Jet/Jet.TauTag
Jet/Jet.TauWeight
Jet/Jet.Charge
Jet/Jet.EhadOverEem
Jet/Jet.NCharged
Jet/Jet.NNeutrals
Jet/Jet.NeutralEnergyFraction
Jet/Jet.ChargedEnergyFraction
Jet/Jet.Beta
Jet/Jet.BetaStar
Jet/Jet.MeanSqDeltaR
Jet/Jet.PTD
Jet/Jet.FracPt[5]
Jet/Jet.Tau[5]
Jet/Jet.SoftDroppedJet
Jet/Jet.SoftDroppedSubJet1
Jet/Jet.SoftDroppedSubJet2
Jet/Jet.TrimmedP4[5]
Jet/Jet.PrunedP4[5]
Jet/Jet.SoftDroppedP4[5]
Jet/Jet.NSubJetsTrimmed
Jet/Jet.NSubJetsPruned
Jet/Jet.NSubJetsSoftDropped
Jet/Jet.ExclYmerge23
Jet/Jet.ExclYmerge34
Jet/Jet.ExclYmerge45
Jet/Jet.ExclYmerge56
Jet/Jet.Constituents
Jet/Jet.Particles
Jet/Jet.Area
Jet_size
Electron
Electron/Electron.fUniqueID
Electron/Electron.fBits
Electron/Electron.PT
Electron/Electron.Eta
Electron/Electron.Phi
Electron/Electron.T
Electron/Electron.Charge
Electron/Electron.EhadOverEem
Electron/Electron.Particle
Electron/Electron.IsolationVar
Electron/Electron.IsolationVarRhoCorr
Electron/Electron.SumPtCharged
Electron/Electron.SumPtNeutral
Electron/Electron.SumPtChargedPU
Electron/Electron.SumPt
Electron/Electron.D0
Electron/Electron.DZ
Electron/Electron.ErrorD0
Electron/Electron.ErrorDZ
Electron_size
Photon
Photon/Photon.fUniqueID
Photon/Photon.fBits
Photon/Photon.PT
Photon/Photon.Eta
Photon/Photon.Phi
Photon/Photon.E
Photon/Photon.T
Photon/Photon.EhadOverEem
Photon/Photon.Particles
Photon/Photon.IsolationVar
Photon/Photon.IsolationVarRhoCorr
Photon/Photon.SumPtCharged
Photon/Photon.SumPtNeutral
Photon/Photon.SumPtChargedPU
Photon/Photon.SumPt
Photon/Photon.Status
Photon_size
Muon
Muon/Muon.fUniqueID
Muon/Muon.fBits
Muon/Muon.PT
Muon/Muon.Eta
Muon/Muon.Phi
Muon/Muon.T
Muon/Muon.Charge
Muon/Muon.Particle
Muon/Muon.IsolationVar
Muon/Muon.IsolationVarRhoCorr
Muon/Muon.SumPtCharged
Muon/Muon.SumPtNeutral
Muon/Muon.SumPtChargedPU
Muon/Muon.SumPt
Muon/Muon.D0
Muon/Muon.DZ
Muon/Muon.ErrorD0
Muon/Muon.ErrorDZ
Muon_size
FatJet
FatJet/FatJet.fUniqueID
FatJet/FatJet.fBits
FatJet/FatJet.PT
FatJet/FatJet.Eta
FatJet/FatJet.Phi
FatJet/FatJet.T
FatJet/FatJet.Mass
FatJet/FatJet.DeltaEta
FatJet/FatJet.DeltaPhi
FatJet/FatJet.Flavor
FatJet/FatJet.FlavorAlgo
FatJet/FatJet.FlavorPhys
FatJet/FatJet.BTag
FatJet/FatJet.BTagAlgo
FatJet/FatJet.BTagPhys
FatJet/FatJet.TauTag
FatJet/FatJet.TauWeight
FatJet/FatJet.Charge
FatJet/FatJet.EhadOverEem
FatJet/FatJet.NCharged
FatJet/FatJet.NNeutrals
FatJet/FatJet.NeutralEnergyFraction
FatJet/FatJet.ChargedEnergyFraction
FatJet/FatJet.Beta
FatJet/FatJet.BetaStar
FatJet/FatJet.MeanSqDeltaR
FatJet/FatJet.PTD
FatJet/FatJet.FracPt[5]
FatJet/FatJet.Tau[5]
FatJet/FatJet.SoftDroppedJet
FatJet/FatJet.SoftDroppedSubJet1
FatJet/FatJet.SoftDroppedSubJet2
FatJet/FatJet.TrimmedP4[5]
FatJet/FatJet.PrunedP4[5]
FatJet/FatJet.SoftDroppedP4[5]
FatJet/FatJet.NSubJetsTrimmed
FatJet/FatJet.NSubJetsPruned
FatJet/FatJet.NSubJetsSoftDropped
FatJet/FatJet.ExclYmerge23
FatJet/FatJet.ExclYmerge34
FatJet/FatJet.ExclYmerge45
FatJet/FatJet.ExclYmerge56
FatJet/FatJet.Constituents
FatJet/FatJet.Particles
FatJet/FatJet.Area
FatJet_size
MissingET
MissingET/MissingET.fUniqueID
MissingET/MissingET.fBits
MissingET/MissingET.MET
MissingET/MissingET.Eta
MissingET/MissingET.Phi
MissingET_size
ScalarHT
ScalarHT/ScalarHT.fUniqueID
ScalarHT/ScalarHT.fBits
ScalarHT/ScalarHT.HT
ScalarHT_size
You can access the elements as array = events["Particle"]["Particle.E"].array()
You may want to use np.squeeze(array)
```
