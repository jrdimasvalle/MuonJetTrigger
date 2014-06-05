##--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023Muon 

## make GEN configs using the LHE files

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN \
--datatier GEN \
--conditions auto:upgradePLS3 \
--eventcontent RECOSIM \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--fileout DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV_madgraph452_bridge224_LHE_pythia6_GEN.root \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_02_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN \
--datatier GEN \
--conditions auto:upgradePLS3 \
--eventcontent RECOSIM \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_ctau_02_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--fileout DarkSUSY_mH_125_mGammaD_0400_ctauExp_02_8TeV_madgraph452_bridge224_LHE_pythia6_GEN.root \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_2_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN \
--datatier GEN \
--conditions auto:upgradePLS3 \
--eventcontent RECOSIM \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_ctau_2_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--fileout DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_GEN.root \
-n 80000 \
--no_exec

## submit the jobs

qsub -q general myserjob_0400_ctau_05_8TeV.pbs
qsub -q general myserjob_0400_ctau_02_8TeV.pbs
qsub -q general myserjob_0400_ctau_2_8TeV.pbs

## make SIM configs using the LHE files
