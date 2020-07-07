import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_0.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_1.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_10.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_11.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_12.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_13.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_14.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_15.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_16.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_17.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_18.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_19.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_2.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_20.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_21.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_22.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_23.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_24.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_25.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_26.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_27.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_28.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_29.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_3.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_30.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_31.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_32.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_33.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_34.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_35.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_36.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_37.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_38.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_39.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_4.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_40.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_41.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_42.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_43.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_44.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_45.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_46.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_47.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_48.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_49.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_5.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_6.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_7.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_8.root',
        '/store/user/jhakala/ZpAnomalonHZ_Zp1200-ND175-NS1_v2/ZpAnomalonHZ_UFO-Zp1200-ND175-NS1_miniAOD_9.root'
] )
