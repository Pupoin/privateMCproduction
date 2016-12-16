# privateMCproduction for Moriond2017
Private MC production for CMS

## Note: Moriond2017 settings
**Note**
This configuration is using the settings which are used for the Moriond2017 production. 

## Note: T2_Beijing
**Note**
This configuration writes the files to the T3_Beijing storage.

Table of Contents
=================

  * [privateMCproduction](#privatemcproduction)
    * [Requirements](#requirements)
    * [Recipe for LHEGENSIM level production](#recipe-for-lhegensim-level-production)
      * [Overview](#overview)
      * [Recipe](#recipe)
      * [Notes](#notes)
      * [Overview of files in framework](#overview-of-files-in-framework)
    * [Recipe for MiniAOD level production](#recipe-for-miniaod-level-production)
      * [Overview](#overview-1)
      * [Recipe](#recipe-1)
      * [Important Notes](#important-notes)
      * [Overview of files in framework](#overview-of-files-in-framework-1)



## Requirements
* CMSSW environment
* Sufficient storage space -- either local or on a grid site
* Optional access to grid and crab scripts



## Recipe for LHEGENSIM level production

### Overview
 * This recipe will produce GenSim level events from a POWHEG gridpack using the same configuration as in the official CMSSW 2016 tranche3 production.

### Recipe
1. Clone this repository to any folder
1. Open the trancheprivateproduction.sh script contained in the folder
1. Adjust the first four parameters until "Do not change anything
behind this line" according to your local setup.
  1. NUMBEREVENTS: Defines how many events you want to produce
  1. WORKDIR: Defines in which directory CMSSW installation is set up and where in local production events are stored
  1. GRIDPACKLOC: Defines which gridpack is used, you can choose the Powheg ttbar, semileptonic decay or Powheg ttbar, dileptonic decay gridpack. 
  1. USECRAB: False means local production, True results in crab submission
1. Additional step for crab submission: Check and modify crabconfig_draft.py script:
  1. config.Site.storageSite: Set your grid storage site, e.g. 'T2_DE_DESY' for german users
  1. config.User.voGroup: If you a non-german user, you should comment out this section.
1. Start the production via ./trancheprivateproduction.sh

### Notes
* The current settings are optimized for a grid submission during which you should produce roughly 400k events per day.
* If you would like to use other gridpacks, contact me first since the python config file has to be updated then.

###  Overview of files in framework
* trancheprivateproduction.sh: Main steering script. Only script which should be edited by user.
* run_generic_tarball_cvmfs.sh: Generic script to produce LHE events out of gridpacks
* pythonLHEGEN_cfg_draft.py: CMSSW python run script
* crabconfig_draft.py: Crab submission script, can be adjusted by user.


## Recipe for MiniAOD level production
### Overview
 * This recipe will use the GenSim level samples generated by the recipe above and will produce MiniAOD samples out of them using the same configuration as in the official CMSSW 2016 tranche3 production.

### Recipe
1. Clone this repository to any folder
1. Navigate to the subfolder privateMCproductionGenSimAODSim
1. Open the trancheGenSimAODSimstep.sh script contained in the folder
1. Adjust the parameter GENSIMLOC and leave all the other parts untouched.
1. **Important notes** before proceeding (**you can break the grid otherwise**, by mistake we did this already once), please read carefully:
  * Use the **DAS dataset name** as GENSIMLOC location, e.g.
  
  ```
  /privateMCProductionLHEGEN/satoshi-eventLHEGEN-TTToSemiLepton_hvq_ttHtranche3-962bade98c5fada66831bc83bbc241c7/USER
  ```
  This dataset name can be obtained via
  
  ```
  https://cmsweb.cern.ch/das/request?view=list&instance=prod%2Fphys03&input=dataset%3D%2F*privateMCProduction*%2F*%2FUSER
  ```
  
  * Make sure that you process an GenSim sample only once, otherwise you will have two exactly identical MiniAOD samples. In principle, the script should warn you if you try to do this. But take care anyway.
  * Do not submit more than 10.000 jobs simultaneously since the crab scheduler cannot handle more than that.
  * Process per job only one file. Meaning do not change 
  
  ```
  config.Data.splitting = 'FileBased'
  config.Data.unitsPerJob = 1
  ```
  in the crabconfig_draft_part1.py file.
  * The processing of 100 events will take roughly 40 to 60 minutes, while each GenSim sample file should contain roughly 1000 to 1200 events. Meaning your single jobs will take roughly 10 hours.
1. Start the production via ./trancheGenSimAODSimstep.sh

### Important Notes
See step 5. It is really important to read them carefully!

###  Overview of files in framework
* trancheGenSimAODSimstep.sh: Main steering script. Only script which should be edited by user.
* jobScript.sh: Script which combines the three necessary cmsRun steps to go from GenSim to MiniAOD in one step.
* crabconfig_draft_part1.py: First part of crab submission script, can be adjusted by user.
* crabconfig_draft_part2.py: Second part of crab submission script, the two parts will put together during the preprocessing steps.
* GenSimAODSim_step1_cfg_draft_part1.py: First part of the first cmsRun step
* GenSimAODSim_step1_cfg_draft_part2.py: Second part of the first cmsRun step, the two parts will be combined together after the input files is written into the config.
* GenSimAODSim_step2_cfg_draft.py: Second cmsRun step, if one would stop after this step, one would have AODSim level events.
* GenSimAODSim_step3_cfg_draft.py: Third cmsRun step, which generates MiniAOD samples out of the AODSim events.




