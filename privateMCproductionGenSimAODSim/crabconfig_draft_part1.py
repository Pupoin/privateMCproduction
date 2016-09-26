from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "privateMCProductionAODSIM"
config.General.workArea = 'crab_privateMCProduction'
config.General.transferLogs = True

config.section_("JobType")
#config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'GenSimAODSim_step1_cfg.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.scriptExe = 'jobScript.sh'
config.JobType.outputFiles = ['MiniAOD.root', 'GenSimAODSim_step1.log', 'GenSimAODSim_step2.log', 'GenSimAODSim_step3.log', 'job.log']
config.JobType.inputFiles = ['jobScript.sh', 'GenSimAODSim_step1_cfg.py', 'GenSimAODSim_step2_cfg.py', 'GenSimAODSim_step3_cfg.py']

config.section_("Data")
config.Data.outputPrimaryDataset = 'privateMCProductionAODSIMMiniAOD'
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'FileBased'
#config.Data.unitsPerJob = 800
config.Data.unitsPerJob = 1
config.Data.totalUnits = #NUMBEREVENTS#
config.Data.publication = True
config.Data.outputDatasetTag = 'eventAODSIMMiniAOD'
config.Data.userInputFiles =[