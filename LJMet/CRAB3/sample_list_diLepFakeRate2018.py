import os,sys


signaldict = {}

bkgdict = {}
bkgdict['DYM50'] = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'


ttbarbkgdict = {}
ttbarbkgdict['TTToHadronic'] = '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
ttbarbkgdict['TTToSemiLeptonic'] = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
ttbarbkgdict['TTTo2L2Nu'] = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
# ttbarbkgdict['TTMtt700'] = '/TT_Mtt-700to1000_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
# ttbarbkgdict['TTMtt1000'] = '/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'

datadict = {}

#datadict['EGammaRun2018A']  = '/EGamma/Run2018A-17Sep2018-v2/MINIAOD'
#datadict['EGammaRun2018B']  = '/EGamma/Run2018B-17Sep2018-v1/MINIAOD'
#datadict['EGammaRun2018C']  = '/EGamma/Run2018C-17Sep2018-v1/MINIAOD'
#datadict['EGammaRun2018D']  = '/EGamma/Run2018D-PromptReco-v2/MINIAOD'

#datadict['DoubleMuonRun2018A']  = '/DoubleMuon/Run2018A-17Sep2018-v2/MINIAOD'
#datadict['DoubleMuonRun2018B']  = '/DoubleMuon/Run2018B-17Sep2018-v1/MINIAOD'
#datadict['DoubleMuonRun2018C']  = '/DoubleMuon/Run2018C-17Sep2018-v1/MINIAOD'
#datadict['DoubleMuonRun2018D']  = '/DoubleMuon/Run2018D-PromptReco-v2/MINIAOD'

datadict['SingleElectronRun2018A']  = '/EGamma/Run2018A-17Sep2018-v2/MINIAOD'
datadict['SingleElectronRun2018B']  = '/EGamma/Run2018B-17Sep2018-v1/MINIAOD'
datadict['SingleElectronRun2018C']  = '/EGamma/Run2018C-17Sep2018-v1/MINIAOD'
#datadict['SingleElectronRun2018D']  = '/EGamma/Run2018D-PromptReco-v2/MINIAOD'
datadict['SingleElectronRun2018D_rereco'] = '/EGamma/Run2018D-22Jan2019-v2/MINIAOD' 

datadict['SingleMuonRun2018A']  = '/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD'
datadict['SingleMuonRun2018B']  = '/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD'
datadict['SingleMuonRun2018C']  = '/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD'
#datadict['SingleMuonRun2018D']  = '/SingleMuon/Run2018D-PromptReco-v2/MINIAOD'
datadict['SingleMuonRun2018D_rereco'] = '/SingleMuon/Run2018D-22Jan2019-v2/MINIAOD'

