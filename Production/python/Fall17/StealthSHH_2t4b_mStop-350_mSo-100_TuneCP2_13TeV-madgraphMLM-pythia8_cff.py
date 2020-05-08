import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/06B6374F-DC08-EA11-83D5-00259073BB58.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/0E2729DC-FD08-EA11-AB01-0026B9277A25.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/164AA882-DA08-EA11-8ADD-C4346BC8D390.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/18E2766A-77F8-E911-8986-AC1F6BABF8E3.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/20394769-26F8-E911-9168-0CC47AFC3D32.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/208AE1FF-E709-EA11-A4DE-B02628346260.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/20C86154-D608-EA11-9118-008CFAC94280.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/2659191B-CCF8-E911-8FC9-0CC47AFF0260.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/2C86FF48-53F8-E911-8BC2-AC1F6B1AF1CE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/2E8F0058-96F9-E911-AE3B-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/36C0B4C1-FEF8-E911-BD2A-0090FAA581B4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/3AFA20B4-02F4-E911-ADAF-0CC47AB58BE4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/3E6FC3AE-DC08-EA11-88D0-AC1F6B1AF140.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/445AA8DF-E408-EA11-94AE-842B2B6F81C6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/5AE40A4A-EF04-EA11-B7E8-002590908286.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/5C71C496-0A09-EA11-A11D-AC1F6B0F71D2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/5E170385-CC08-EA11-A7D3-24BE05CEADA1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/80B14D3E-77F8-E911-8D46-AC1F6B0DE2E8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/80D5F9D0-5BF7-E911-8861-008CFAC93CB0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/846DB3AC-BAF8-E911-AF3F-7CD30ACE23E6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/84FD4B99-CC08-EA11-8E02-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/86BFD284-EB08-EA11-9E2B-0CC47AA992B2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/881C56D1-DBF3-E911-8B46-AC1F6B23C834.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/9675E2C9-15F6-E911-9963-00259090821E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/A0EBE23F-D508-EA11-8916-98039B3B01C2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/AC7498DC-0CF9-E911-9F40-B02628343440.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/ACCA558E-F108-EA11-A4EC-0CC47A57CD88.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B8726DF6-09F4-E911-8026-0025904AAADC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/BC2F2B6B-11F4-E911-845F-AC1F6B23C7DE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/BE6E9418-EBF4-E911-B09E-AC1F6B23C832.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D0671F82-61F7-E911-ABE4-0CC47A4D99A6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D08FB121-CC0A-EA11-8273-0242AC1C0507.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/DC40C9F7-DEF7-E911-BEBB-0CC47AD99238.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/E06F90C6-D9F7-E911-A622-F01FAFD69D8F.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/F25E979A-C5F3-E911-9DF6-AC1F6B23C9FE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/F8787943-E703-EA11-9C72-001E0B486068.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/F8E97EA5-3708-EA11-AE8E-0CC47A4C8EBA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/FA7115C2-DEF6-E911-86B4-002590908466.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/FAFC81C4-48FC-E911-9BB7-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/FAFF7759-2B04-EA11-8BE4-0242AC130002.root',
] )