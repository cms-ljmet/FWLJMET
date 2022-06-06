import os,sys


signaldict = {}


bkgdict = {}
bkgdict['DYM50'] = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'


ttbarbkgdict = {}
ttbarbkgdict['TTToHadronic'] = '/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'
ttbarbkgdict['TTToSemiLeptonic'] = '/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
ttbarbkgdict['TTTo2L2Nu'] = '/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM'
# ttbarbkgdict['TTMtt700'] = '/TT_Mtt-700to1000_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
# ttbarbkgdict['TTMtt1000'] = '/TT_Mtt-1000toInf_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'

datadict = {}

#datadict['DoubleEGRun2017B']  = '/DoubleEG/Run2017B-31Mar2018-v1/MINIAOD'
#datadict['DoubleEGRun2017C']  = '/DoubleEG/Run2017C-31Mar2018-v1/MINIAOD'
#datadict['DoubleEGRun2017D']  = '/DoubleEG/Run2017D-31Mar2018-v1/MINIAOD'
#datadict['DoubleEGRun2017E']  = '/DoubleEG/Run2017E-31Mar2018-v1/MINIAOD'
#datadict['DoubleEGRun2017F']  = '/DoubleEG/Run2017F-31Mar2018-v1/MINIAOD'

#datadict['DoubleMuonRun2017B']  = '/DoubleMuon/Run2017B-31Mar2018-v1/MINIAOD'
#datadict['DoubleMuonRun2017C']  = '/DoubleMuon/Run2017C-31Mar2018-v1/MINIAOD'
#datadict['DoubleMuonRun2017D']  = '/DoubleMuon/Run2017D-31Mar2018-v1/MINIAOD'
#datadict['DoubleMuonRun2017E']  = '/DoubleMuon/Run2017E-31Mar2018-v1/MINIAOD'
#datadict['DoubleMuonRun2017F']  = '/DoubleMuon/Run2017F-31Mar2018-v1/MINIAOD'

datadict['SingleElectronRun2017B']  = '/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD'
datadict['SingleElectronRun2017C']  = '/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD'
datadict['SingleElectronRun2017D']  = '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD'
datadict['SingleElectronRun2017E']  = '/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD'
datadict['SingleElectronRun2017F']  = '/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD'

datadict['SingleMuonRun2017B']  = '/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD'
datadict['SingleMuonRun2017C']  = '/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD'
datadict['SingleMuonRun2017D']  = '/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD'
datadict['SingleMuonRun2017E']  = '/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD'
datadict['SingleMuonRun2017F']  = '/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD'

