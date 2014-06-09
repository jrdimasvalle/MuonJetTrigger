##--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023Muon 

## make GEN configs using the LHE files

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_5_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN \
--datatier GEN \
--conditions auto:upgradePLS3 \
--eventcontent RECOSIM \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_ctau_5_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--fileout DarkSUSY_mH_125_mGammaD_0400_ctau_5_8TeV_madgraph452_bridge224_LHE_pythia6_GEN.root \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN \
--datatier GEN \
--conditions auto:upgradePLS3 \
--eventcontent RECOSIM \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--fileout DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_GEN.root \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN \
--datatier GEN \
--conditions auto:upgradePLS3 \
--eventcontent RECOSIM \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--fileout DarkSUSY_mH_125_mGammaD_0400_8TeV_madgraph452_bridge224_LHE_pythia6_GEN.root \
-n 80000 \
--no_exec


## submit the jobs

qsub -q hepxrt myserjob_0400_ctau_05_8TeV.pbs
qsub -q hepxrt myserjob_0400_ctau_02_8TeV.pbs
qsub -q hepxrt myserjob_0400_ctau_2_8TeV.pbs

## make SIM configs using the LHE files

--fileout /eos/uscms/store/user/dildick/MuonJetTrigger/DarkSUSY_mH_125_mGammaD_0400_8TeV_madgraph452_bridge224_LHE_pythia6_SIM.root \
--fileout /eos/uscms/store/user/dildick/MuonJetTrigger/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_SIM.root \
--fileout /eos/uscms/store/user/dildick/MuonJetTrigger/DarkSUSY_mH_125_mGammaD_0400_ctau_5_8TeV_madgraph452_bridge224_LHE_pythia6_SIM.root \

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s SIM \
--datatier SIM \
--conditions auto:upgradePLS3 \
--geometry Extended2023TTI \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI \
--eventcontent RECOSIM \
--filein file:/eos/uscms/store/user/dildick/MuonJetTrigger/DarkSUSY_mH_125_mGammaD_0400_8TeV_madgraph452_bridge224_LHE_pythia6_GEN.root \
--fileout out_sim.root \
--magField 38T_PostLS1 \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s SIM \
--datatier SIM \
--conditions auto:upgradePLS3 \
--geometry Extended2023TTI \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI \
--eventcontent RECOSIM \
--filein file:/eos/uscms/store/user/dildick/MuonJetTrigger/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_GEN.root \
--fileout out_sim.root \
--magField 38T_PostLS1 \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_5_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s SIM \
--datatier SIM \
--conditions auto:upgradePLS3 \
--geometry Extended2023TTI \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI \
--eventcontent RECOSIM \
--filein file:/eos/uscms/store/user/dildick/MuonJetTrigger/DarkSUSY_mH_125_mGammaD_0400_ctau_5_8TeV_madgraph452_bridge224_LHE_pythia6_GEN.root \
--fileout out_sim.root \
--magField 38T_PostLS1 \
-n 80000 \
--no_exec

## DIGI-RECO

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s DIGI,L1,RECO \
--datatier DIGI-RECO \
--conditions auto:upgradePLS3 \
--geometry Extended2023TTI \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI \
--eventcontent RECOSIM \
--filein out_sim.root \
--fileout out_reco.root \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s SIM \
--datatier SIM \
--conditions auto:upgradePLS3 \
--geometry Extended2023TTI \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI \
--eventcontent RECOSIM \
--filein out_sim.root \
--fileout out_reco.root \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_5_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s SIM \
--datatier SIM \
--conditions auto:upgradePLS3 \
--geometry Extended2023TTI \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI \
--eventcontent RECOSIM \
--filein out_sim.root \
--fileout out_reco.root \
-n 80000 \
--no_exec
