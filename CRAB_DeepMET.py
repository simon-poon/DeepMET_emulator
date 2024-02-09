from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName = "DeepMET_emulator_run9"
config.General.workArea = "crab_projects"

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step1_RAW2DIGI_L1_L1TrackTrigger_L1P2GT.py"
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores=1
config.JobType.maxMemoryMB=5000

config.section_("Data")
config.Data.ignoreLocality = True
config.Data.inputDataset = "/TT_TuneCP5_14TeV-powheg-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v1/GEN-SIM-DIGI-RAW-MINIAOD"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = "L1DeepMET_study"
config.Data.publication    = True
config.Data.allowNonValidInputDataset = True

config.section_("Site")
config.Site.whitelist = ["T2_US_UCSD"]
config.Site.storageSite = "T2_US_UCSD"
