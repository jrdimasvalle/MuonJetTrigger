import FWCore.ParameterSet.Config as cms

source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('file:/home/sven.dildick/MuonJetTriggerPerformance/CMSSW_6_2_0_SLHC13/src/MuonJetTrigger/Configuration/data/DarkSUSY_mH_125_mGammaD_0400_ctau_2_8TeV_madgraph452_bridge224_events80k.lhe')
)

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

generator = cms.EDFilter("Pythia6HadronizerFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    # put here the efficiency of your filter (1. if no filter)
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    # put here the cross section of your process (in pb)
    crossSection = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    # Center-of-mass Energy
    comEnergy = cms.double(8000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
             'MSEL=0          ! User defined processes'
        ),
        parameterSets = cms.vstring(
            'pythiaUESettings',
            'processParameters'
        )
    )
)
