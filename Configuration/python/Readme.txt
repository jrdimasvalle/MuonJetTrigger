## GEN-SIM

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN,SIM \
--datatier GEN-SIM \
--conditions DES23_62_V1::All \
--beamspot HLLHC \
--mc \
--geometry Extended2023TTI,Extended2023TTIReco \
--eventcontent FEVTDEBUG \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI,Configuration/DataProcessing/Utils.addMonitoring \
--fileout out_sim.root \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN,SIM \
--datatier GEN-SIM \
--conditions DES23_62_V1::All \
--beamspot HLLHC \
--mc \
--geometry Extended2023TTI,Extended2023TTIReco \
--eventcontent FEVTDEBUG \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI,Configuration/DataProcessing/Utils.addMonitoring \
--fileout out_sim.root \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_5_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN,SIM \
--datatier GEN-SIM \
--conditions DES23_62_V1::All \
--beamspot HLLHC \
--mc \
--geometry Extended2023TTI,Extended2023TTIReco \
--eventcontent FEVTDEBUG \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_ctau_5_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI,Configuration/DataProcessing/Utils.addMonitoring \
--fileout out_sim.root \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_10_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN,SIM \
--datatier GEN-SIM \
--conditions DES23_62_V1::All \
--beamspot HLLHC \
--mc \
--geometry Extended2023TTI,Extended2023TTIReco \
--eventcontent FEVTDEBUG \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_ctau_10_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI,Configuration/DataProcessing/Utils.addMonitoring \
--fileout out_sim.root \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_20_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s GEN,SIM \
--datatier GEN-SIM \
--conditions DES23_62_V1::All \
--beamspot HLLHC \
--mc \
--geometry Extended2023TTI,Extended2023TTIReco \
--eventcontent FEVTDEBUG \
--evt_type MuonJetTrigger/Configuration/DarkSUSY_mH_125_mGammaD_0400_ctau_20_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI,Configuration/DataProcessing/Utils.addMonitoring \
--fileout out_sim.root \
-n 80000 \
--no_exec

## DIGI-RECO

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s DIGI:pdigi_valid,L1,L1TrackTrigger,DIGI2RAW,RECO:pixeltrackerlocalreco \
--datatier DIGI-RAW \
--conditions PH2_1K_FB_V3::All \
--geometry Extended2023TTI,Extended2023TTIReco \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI,Configuration/DataProcessing/Utils.addMonitoring \
--eventcontent FEVTDEBUGHLT \
--mc \
--filein out_sim.root \
--fileout out_reco.root \
--magField 38T_PostLS1 \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_05_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s DIGI:pdigi_valid,L1,L1TrackTrigger,DIGI2RAW,RECO:pixeltrackerlocalreco \
--datatier DIGI-RAW \
--conditions PH2_1K_FB_V3::All \
--geometry Extended2023TTI,Extended2023TTIReco \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI,Configuration/DataProcessing/Utils.addMonitoring \
--eventcontent FEVTDEBUGHLT \
--mc \
--filein out_sim.root \
--fileout out_reco.root \
--magField 38T_PostLS1 \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_5_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s DIGI:pdigi_valid,L1,L1TrackTrigger,DIGI2RAW,RECO:pixeltrackerlocalreco \
--datatier DIGI-RAW \
--conditions PH2_1K_FB_V3::All \
--geometry Extended2023TTI,Extended2023TTIReco \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI,Configuration/DataProcessing/Utils.addMonitoring \
--eventcontent FEVTDEBUGHLT \
--mc \
--filein out_sim.root \
--fileout out_reco.root \
--magField 38T_PostLS1 \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_10_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s DIGI:pdigi_valid,L1,L1TrackTrigger,DIGI2RAW,RECO:pixeltrackerlocalreco \
--datatier DIGI-RAW \
--conditions PH2_1K_FB_V3::All \
--geometry Extended2023TTI,Extended2023TTIReco \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI,Configuration/DataProcessing/Utils.addMonitoring \
--eventcontent FEVTDEBUGHLT \
--mc \
--filein out_sim.root \
--fileout out_reco.root \
--magField 38T_PostLS1 \
-n 80000 \
--no_exec

cmsDriver.py DarkSUSY_mH_125_mGammaD_0400_ctau_20_8TeV_madgraph452_bridge224_LHE_pythia6_cfi \
-s DIGI:pdigi_valid,L1,L1TrackTrigger,DIGI2RAW,RECO:pixeltrackerlocalreco \
--datatier DIGI-RAW \
--conditions PH2_1K_FB_V3::All \
--geometry Extended2023TTI,Extended2023TTIReco \
--customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI,Configuration/DataProcessing/Utils.addMonitoring \
--eventcontent FEVTDEBUGHLT \
--mc \
--filein out_sim.root \
--fileout out_reco.root \
--magField 38T_PostLS1 \
-n 80000 \
--no_exec
