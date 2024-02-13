# DeepMET_emulator

Setup

```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_14_0_0_pre3
cd CMSSW_14_0_0_pre3/src
cmsenv
git cms-addpkg L1Trigger/Phase2L1ParticleFlow
git cms-addpkg L1Trigger/Configuration
git cms-checkout-topic -u jmduarte:l1metml_1330pre3
scram b -j 8
# get grid certificate with voms-proxy-init --voms cms
cmsDriver.py step1 --conditions 131X_mcRun4_realistic_v9 -n -1 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT -s RAW2DIGI,L1,L1TrackTrigger,L1P2GT --datatier GEN-SIM-DIGI-RAW-MINIAOD --fileout file:test.root --customise "SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2.addHcalTriggerPrimitives,L1Trigger/Configuration/customisePhase2FEVTDEBUGHLT.customisePhase2FEVTDEBUGHLT,L1Trigger/Configuration/customisePhase2TTNoMC.customisePhase2TTNoMC" --geometry Extended2026D95 --nThreads 8 --filein "/store/mc/Phase2Spring23DIGIRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v1/50000/005bc30b-cf79-4b3b-9ec1-a80e13072afd.root" --mc --inputCommands='keep *, drop l1tPFJets_*_*_*' --outputCommands="drop l1tPFJets_*_*_*" --no_exec
cmsRun step1_RAW2DIGI_L1_L1TrackTrigger_L1P2GT.py
```
