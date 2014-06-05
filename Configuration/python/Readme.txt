##--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023Muon 

## make GEN configs using the LHE files

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--step GEN \
--datatier GEN \
--conditions auto:upgradePLS3 \
--eventcontent RECOSIM \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--fileout DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV_madgraph452_bridge224_LHE_pythia6_537p4_GEN.root \
-n 88000 \
--no_exec

## make SIM configs using the LHE files
