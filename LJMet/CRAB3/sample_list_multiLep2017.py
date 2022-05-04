import os,sys

newsignaldict = {}
##tttt
newsignaldict['TTTT'] = '/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_correctnPartonsInBorn/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'

##X53
#newsignaldict['XX900R'] = '/X53X53_M-900_RH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#newsignaldict['XX1000R'] = '/X53X53_M-1000_RH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#newsignaldict['XX1100R'] = '/X53X53_M-1100_RH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#newsignaldict['XX1200R'] = '/X53X53_M-1200_RH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#newsignaldict['XX1300R'] = '/X53X53_M-1300_RH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#newsignaldict['XX1400R'] = '/X53X53_M-1400_RH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
##newsignaldict['XX1500R'] = '/X53X53_M-1500_RH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' #INVALID
#newsignaldict['XX1600R'] = '/X53X53_M-1600_RH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#newsignaldict['XX1700R'] = '/X53X53_M-1700_RH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'

#newsignaldict['XX1100L'] = '/X53X53_M-1100_LH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#newsignaldict['XX1200L'] = '/X53X53_M-1200_LH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#newsignaldict['XX1400L'] = '/X53X53_M-1400_LH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#newsignaldict['XX1500L'] = '/X53X53_M-1500_LH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#newsignaldict['XX1700L'] = '/X53X53_M-1700_LH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'

signaldict = {}

##VLQ TT
'''
signaldict['TpTp1800'] = '/TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
signaldict['TpTp1700'] = '/TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
signaldict['TpTp1600'] = '/TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
signaldict['TpTp1500'] = '/TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
signaldict['TpTp1400'] = '/TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
signaldict['TpTp1300'] = '/TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
signaldict['TpTp1200'] = '/TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
signaldict['TpTp1100'] = '/TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
signaldict['TpTp1000'] = '/TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM'
'''
signaldict['TpTp900'] = '/TprimeTprime_M-700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM'

##VLQ BB
'''
signaldict['BpBp1800'] = '/BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
signaldict['BpBp1700'] = '/BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
signaldict['BpBp1600'] = '/BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
signaldict['BpBp1500'] = '/BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
signaldict['BpBp1400'] = '/BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
signaldict['BpBp1300'] = '/BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
signaldict['BpBp1200'] = '/BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
signaldict['BpBp1100'] = '/BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
signaldict['BpBp1000'] = '/BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
signaldict['BpBp900']  = '/BprimeBprime_M-900_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
'''

bkgdict = {}

#bkgdict['WZ'] = '/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#bkgdict['ZZ'] = '/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
#bkgdict['WWW'] = '/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
#bkgdict['WWZ'] = '/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
###bkgdict['WZZ'] = '/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
bkgdict['WZZ_3L'] = '/WZZTo3L1Nu2Q_4f_TuneCP5_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
bkgdict['WZZ_4L'] = '/WZZJetsTo4L2Nu_4f_TuneCP5_13TeV_amcatnloFXFX_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
bkgdict['WZZ_ZTo2L'] = '/WZZ_ZTo2L_WToAll_4f_TuneCP5_13TeV_amcatnlo_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#bkgdict['ZZZ'] = '/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
#bkgdict['TTW'] = '/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
#bkgdict['TTZ'] = '/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
####bkgdict['WW'] = ''

bkghtdict ={}

ttbarbkgdict = {}
#ttbarbkgdict['TTToHadronic'] = '/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#ttbarbkgdict['TTToSemiLeptonic'] = '/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
ttbarbkgdict['TTTo2L2Nu'] = '/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM'
#ttbarbkgdict['TT_Mtt700'] = '/TT_Mtt-700to1000_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
#ttbarbkgdict['TT_Mtt1000'] = '/TT_Mtt-1000toInf_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'

datadict = {}

datadict['DoubleEGRun2017B']  = '/DoubleEG/Run2017B-31Mar2018-v1/MINIAOD'
datadict['DoubleEGRun2017C']  = '/DoubleEG/Run2017C-31Mar2018-v1/MINIAOD'
datadict['DoubleEGRun2017D']  = '/DoubleEG/Run2017D-31Mar2018-v1/MINIAOD'
datadict['DoubleEGRun2017E']  = '/DoubleEG/Run2017E-31Mar2018-v1/MINIAOD'
datadict['DoubleEGRun2017F']  = '/DoubleEG/Run2017F-31Mar2018-v1/MINIAOD'

datadict['DoubleMuonRun2017B']  = '/DoubleMuon/Run2017B-31Mar2018-v1/MINIAOD'
datadict['DoubleMuonRun2017C']  = '/DoubleMuon/Run2017C-31Mar2018-v1/MINIAOD'
datadict['DoubleMuonRun2017D']  = '/DoubleMuon/Run2017D-31Mar2018-v1/MINIAOD'
datadict['DoubleMuonRun2017E']  = '/DoubleMuon/Run2017E-31Mar2018-v1/MINIAOD'
datadict['DoubleMuonRun2017F']  = '/DoubleMuon/Run2017F-31Mar2018-v1/MINIAOD'

datadict['MuonEGRun2017B']  = '/MuonEG/Run2017B-31Mar2018-v1/MINIAOD'
datadict['MuonEGRun2017C']  = '/MuonEG/Run2017C-31Mar2018-v1/MINIAOD'
datadict['MuonEGRun2017D']  = '/MuonEG/Run2017D-31Mar2018-v1/MINIAOD'
datadict['MuonEGRun2017E']  = '/MuonEG/Run2017E-31Mar2018-v1/MINIAOD'
datadict['MuonEGRun2017F']  = '/MuonEG/Run2017F-31Mar2018-v1/MINIAOD'


