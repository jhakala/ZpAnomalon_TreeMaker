import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/002D3C80-82EC-E611-AF91-20CF3027A598.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/020800D3-4DEC-E611-B6D6-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/0287613F-65EC-E611-81C6-00259073E3FE.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/02878CA7-5EEC-E611-B733-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/02C80FB2-4EEC-E611-BE27-0090FAA569C4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/02F55EF0-66EC-E611-893F-0090FAA59ED4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/04BED259-82EC-E611-A82D-0090FAA576A0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/04BFB5BC-77EC-E611-94D6-00259073E3F2.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/04E4113D-71EC-E611-878C-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/04FC7517-66EC-E611-9393-E0071B749C40.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/06389814-72EC-E611-97B0-008CFA1111E0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/0697028F-6AEC-E611-81DA-A0369F310374.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/06CD42A4-70EC-E611-B852-0090FAA572B0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/08136840-71EC-E611-9D30-008CFA197A04.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/0A6A813E-65EC-E611-B656-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/0ACE09A2-6AEC-E611-88D7-E0071B7A58B0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/0AFA6F95-8FEC-E611-BBBD-B083FED40671.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/0C56DC51-54EC-E611-9B9D-00259073E3F2.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/0CA9F03A-5EEC-E611-9374-E0071B7A45D0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/0E3D85D5-4DEC-E611-AD23-E0071B7AC710.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/0E667B64-54EC-E611-9B06-24BE05C63741.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/10444AA6-5EEC-E611-9E4D-24BE05C6C741.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/10C97A73-54EC-E611-A13F-008CFA111330.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/10D7B726-6AEC-E611-A84A-D4AE527F338C.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/10E2E91D-72EC-E611-B2E5-008CFA197918.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/10E906F9-77EC-E611-B01A-1418774105B6.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/1225AFD3-4DEC-E611-9128-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/1254B48E-77EC-E611-891B-0090FAA57CD4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/12B76FD8-55EC-E611-982B-00259073E4E2.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/12B9F45C-54EC-E611-BFAB-00259073E51A.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/14111F02-71EC-E611-82AB-0090FAA58754.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/14EAD704-78EC-E611-8DBA-008CFA580778.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/1696E18E-77EC-E611-9608-0090FAA575C0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/16F005A7-5EEC-E611-B2B2-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/181388C6-88EC-E611-8ECF-141877411936.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/1859B719-66EC-E611-9AE4-E0071B7A7870.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/1A6C41F0-77EC-E611-B844-C81F66B7864D.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/1C03D824-64EC-E611-9B73-E0071B7A4550.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/1C186343-64EC-E611-8411-00259022277E.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/1C93DF9E-6BEC-E611-B4C2-0090FAA572B0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/1E54C7CB-66EC-E611-9E2B-E0071B7A58B0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/20074B78-63EC-E611-B37A-E0071B7A5650.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/200A096C-54EC-E611-AD44-E0071B740D80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/204FC3B2-5EEC-E611-AA50-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/20DD53DA-63EC-E611-B0D5-008CFA197AB0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/20E35506-71EC-E611-87CD-00259073E49A.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/223AE1BB-5EEC-E611-BEE9-00259073E322.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/226F65D2-4DEC-E611-BC7B-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/22BAEDD1-4DEC-E611-AE4A-5065F381E211.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/249EC0AD-5EEC-E611-9596-E0071B7A7870.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/24AE1A64-89EC-E611-82B6-008CFA111320.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/266715E9-5DEC-E611-8BC9-5065F381E151.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/289F6BAD-77EC-E611-9496-008CFA1111AC.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/28C6DDA3-7EEC-E611-9ABF-008CFA197D48.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/28E8A7F6-5DEC-E611-9726-002590D0AF54.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/2A2832B4-9CEC-E611-BC99-00259073E44E.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/2AB352AB-63EC-E611-9C42-008CFA197AC4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/2AEEFAF5-5DEC-E611-8069-008CFA1113F8.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/2C08FFE9-5DEC-E611-AF18-5065F381C1D1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/2C7EFD0D-66EC-E611-A0D7-00259073E322.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/2E89739D-67EC-E611-9300-0090FAA58754.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/300F8F40-71EC-E611-9E4F-008CFA111270.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/30211AED-63EC-E611-8E2A-008CFA197A04.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/30BD5C3D-71EC-E611-8CF5-B083FED40671.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/3297F443-7EEC-E611-A970-0090FAA57410.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/347F7B0F-6AEC-E611-9009-24BE05CECBD1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/36033964-54EC-E611-9891-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/36F0B1A8-5EEC-E611-B174-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/388FB6FE-5DEC-E611-9F5D-008CFA197918.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/38C681F8-70EC-E611-90CC-0090FAA57FA4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/3A1FC7AF-96EC-E611-ADE1-1866DAEA8218.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/3A26DBD6-54EC-E611-8AF0-008CFA197DC4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/3A417744-71EC-E611-ADBA-008CFA1111E0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/3A5EB247-89EC-E611-A86E-00259073E3FE.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/3CA76644-7EEC-E611-A0FB-0090FAA57C00.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/3CFE9F45-65EC-E611-AF5A-E0071B7AC5D0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/3E5D3A43-71EC-E611-88B5-008CFA110B08.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/3EAE5E15-66EC-E611-B501-E0071B7A9810.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/3EE77A63-54EC-E611-9D4F-24BE05C626B1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/407DCC34-71EC-E611-8B6A-24BE05C6B701.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/40AAB48D-8FEC-E611-ACFD-B083FED177B1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/40C43BBD-96EC-E611-B8C8-1866DAEB3370.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/42281A74-78EC-E611-B483-0090FAA58BF4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4240B5D7-4DEC-E611-986D-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/42A1FE42-7EEC-E611-9170-0090FAA57FA4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/44BB4564-54EC-E611-A1C1-24BE05CEEB61.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/46A06A40-71EC-E611-9A2B-008CFA111320.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/46EEB5D4-4DEC-E611-A5D5-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/48037291-77EC-E611-954F-00259073E49A.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/482162C4-77EC-E611-801F-0090FAA57F14.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/485F7C8F-77EC-E611-A9F5-0090FAA57B20.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/48770AD2-4DEC-E611-B346-24BE05C6E7C1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/488A9262-54EC-E611-B34B-5065F3817281.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/488DBDA7-5EEC-E611-835B-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4893D612-66EC-E611-B919-24BE05BD4F81.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/48ECCCB2-4EEC-E611-9CB5-0025907B4F46.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4A1A15D9-55EC-E611-9165-24BE05CE2E91.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4A6CBBAF-5EEC-E611-8291-E0071B7A4550.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4A9D9B1A-6AEC-E611-91F9-008CFA1111E0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4AE306F7-77EC-E611-B3C4-008CFA580778.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4C8FC102-5EEC-E611-8B0F-008CFA110B08.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4E86D541-71EC-E611-A3C3-008CFA197C58.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4EE2C702-71EC-E611-AA1A-0090FAA57C60.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4EF67F58-54EC-E611-A581-0090FAA573E0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/4EFA7266-54EC-E611-93D6-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/50928434-71EC-E611-B1A3-5065F3810301.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/50AB4469-54EC-E611-9016-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/5253C15E-6AEC-E611-A610-A0369F310374.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/526D7D07-78EC-E611-BBFF-008CFA197AA0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/52723F64-54EC-E611-8794-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/540AF746-89EC-E611-9866-00259073E4F6.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/54CE7FDB-4DEC-E611-899C-E0071B7A7870.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/54E4B8F0-66EC-E611-9F80-0090FAA57F14.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/5607CAD3-4DEC-E611-ACBA-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/564485D8-55EC-E611-8BC4-002590747E14.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/56EE1A90-77EC-E611-B214-002590D0AF54.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/58014A08-6BEC-E611-A9B3-0090FAA57380.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/5802DE3F-71EC-E611-B082-008CFA111330.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/582A9064-54EC-E611-93D0-24BE05CE2E91.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/58AE0FD8-55EC-E611-9CDF-5065F3812261.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/5A6629B0-77EC-E611-BFD5-008CFA197D48.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/5AA71BCA-66EC-E611-976E-24BE05C488E1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/5AB5B947-65EC-E611-8C2E-E0071B74AC00.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/5C0AFB08-6BEC-E611-8928-0090FAA582E4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/5C1266BB-5EEC-E611-BE55-00259073E50A.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/5C8927A3-6BEC-E611-84A1-00259073E4D4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/5EDFC6DF-7DEC-E611-8D71-549F3525E81C.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/60150DA1-6BEC-E611-83F9-20CF3019DF17.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/601C588E-77EC-E611-BB9C-0090FAA575B0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/603EEFF3-5DEC-E611-A2CE-E0071B7A7870.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/60E0BE63-54EC-E611-8C71-24BE05CE1E11.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/64CD3681-82EC-E611-9594-0025907277BE.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/66198F49-82EC-E611-B1F7-008CFA197D48.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/664D8544-71EC-E611-B530-008CFA1111AC.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/6666B080-82EC-E611-8632-00259074AE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/66C39D43-89EC-E611-B176-002590D0B0C8.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/66C5F7E2-6AEC-E611-9EE9-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/66DC1C63-54EC-E611-B9C2-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/66E767CA-46EC-E611-9EFD-A0369F310374.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/68218F7E-9DEC-E611-824D-008CFA197CA0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/68509DEE-77EC-E611-B479-1866DAEA6E00.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/68C413B9-5EEC-E611-8F1C-0025907B4FC0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/68D97AC7-88EC-E611-B5FA-141877410522.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/68EB6683-6AEC-E611-B572-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/6A1FBCFA-5DEC-E611-997E-008CFA580778.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/6A8AA7DE-7DEC-E611-BA8D-842B2B42BC3A.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/6C13AF03-71EC-E611-8DA0-002590D0AF54.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/6C45E9D8-4DEC-E611-86AF-E0071B7AC7B0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/6CD9ACDB-4DEC-E611-99B8-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/6CEB2F95-77EC-E611-BE5D-0090FAA576A0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/6E1AF662-5DEC-E611-B7E5-00259022277E.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/6E7EAEEF-63EC-E611-8965-008CFA111330.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/6EB1AA57-54EC-E611-8927-0090FAA58484.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/70B01FEB-63EC-E611-AFDE-008CFA111330.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/726FD867-54EC-E611-82F1-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/72F95ED1-4DEC-E611-95BD-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/747D07A6-5EEC-E611-B43D-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/7642CF58-54EC-E611-81D6-0090FAA573E0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/782D8ED8-55EC-E611-BD43-5065F381E271.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/786A3A42-71EC-E611-B547-008CFA111348.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/78DDC142-71EC-E611-BEB9-008CFA111320.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/7A0947D1-4DEC-E611-86E9-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/7A0FAE42-7EEC-E611-90BB-0090FAA57430.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/7A8612CA-66EC-E611-8659-24BE05C626C1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/7C21B088-77EC-E611-B8F7-008CFA111320.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/7C782864-54EC-E611-940F-E0071B7AE500.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/7E804007-71EC-E611-AEBD-00259074AE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/7EF3AE16-5DEC-E611-91C2-008CFA111320.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/803417FA-69EC-E611-8C68-0090FAA57E54.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/80432612-6BEC-E611-A554-00259077501E.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/80BA2E11-83EC-E611-96A5-1866DAEA7E64.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/826C95F8-5DEC-E611-BA57-008CFA197AC4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/84000FF7-77EC-E611-9CB9-008CFA1111E0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/84C7E30E-6AEC-E611-9FDB-24BE05C63791.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/84CE1F04-78EC-E611-84FF-008CFA197C58.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/84E56D63-54EC-E611-960B-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/862DCCD5-4DEC-E611-9722-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/86A58B55-64EC-E611-A008-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/884073FA-5DEC-E611-8E10-008CFA110B08.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/88950142-65EC-E611-9339-E0071B7A9810.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/88C694E9-5DEC-E611-B754-24BE05BD0F81.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/8A003743-71EC-E611-B07A-008CFA111244.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/8A229990-77EC-E611-9F55-0090FAA57430.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/8A287365-54EC-E611-859D-24BE05CECB71.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/8A6E3D44-7EEC-E611-BE4D-0090FAA579F0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/8AB08362-64EC-E611-9FCB-008CFA197C58.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/8C35B742-7EEC-E611-9C44-0090FAA57430.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/8C71B955-64EC-E611-84D8-008CFA197918.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/8C943F1D-5DEC-E611-9CE2-A0369F3102B6.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/8E095576-54EC-E611-B678-008CFA111244.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/8E2B8664-54EC-E611-9DC2-24BE05CE2D41.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/9030137F-82EC-E611-BEA6-0090FAA57710.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/90A62445-71EC-E611-B92D-008CFA197BD4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/925C1412-6BEC-E611-B523-00259077501E.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/926EB6B9-96EC-E611-BCA3-1866DAEB31E0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/9298BCCD-66EC-E611-A165-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/9298CA6D-54EC-E611-98EF-E0071B749CA0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/92BD9A8D-6CEC-E611-981F-0090FAA58754.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/92D60464-54EC-E611-8679-24BE05C488E1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/92E4171E-6AEC-E611-B480-008CFA111348.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/92ED603D-6CEC-E611-A181-20CF305616EC.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/94404E63-54EC-E611-B344-24BE05CE3C71.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/944B45D1-4DEC-E611-86B6-24BE05CEFDF1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/94960647-71EC-E611-AAB3-008CFA197D48.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/94BCF2A5-64EC-E611-BABD-24BE05CE2E81.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/94D24F13-66EC-E611-B22D-24BE05CE2EE1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/962E44E0-7DEC-E611-8E65-1866DAEB4284.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/96B959A5-5EEC-E611-B38D-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/96BDD363-54EC-E611-9EA4-5065F38122D1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/98902EA7-5EEC-E611-9BF0-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/9ABF8F15-72EC-E611-A9DA-008CFA111320.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/9E2F645E-63EC-E611-BAFB-008CFA197C58.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/9EBF9A1D-6AEC-E611-8AE0-008CFA111320.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/9ED7E08D-5FEC-E611-A4E8-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A00D81F8-5DEC-E611-BD32-008CFA197C58.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A046D345-71EC-E611-8110-008CFA197AA0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A0956546-71EC-E611-AE9F-008CFA110B08.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A0FD79C8-63EC-E611-A04C-008CFA580778.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A200A413-5DEC-E611-A96F-008CFA197BD4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A21BD7AF-77EC-E611-9659-008CFA197918.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A440E0F4-66EC-E611-AB07-0090FAA57E54.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A46B6092-5FEC-E611-8FB0-B8CA3A709028.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A6B9369A-67ED-E611-887C-842B2B18158E.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A6D3EE63-54EC-E611-ADA0-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A6E973EA-69EC-E611-A350-008CFA197A04.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A82AFFDA-69EC-E611-BA02-0CC47A4DED62.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A84A3642-7EEC-E611-BB25-0090FAA57620.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A89BE006-78EC-E611-A655-008CFA197A04.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A8CD627F-82EC-E611-AF16-0090FAA57EA4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/A8FE8C23-6AEC-E611-B1EF-008CFA111320.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/AA56E801-5EEC-E611-81C1-008CFA197C58.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/AABF93AB-5EEC-E611-96FF-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/AC07DE8F-77EC-E611-8BBB-0090FAA58294.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/AE584C3E-71EC-E611-9CB8-D4AE526DF64C.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/AE5A156D-54EC-E611-A272-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/AE66C352-5FEC-E611-A172-0090FAA597B4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/AE74CB76-4DEC-E611-A778-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/AE930942-61EC-E611-BC8D-00259074AE40.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/AEC13F90-77EC-E611-9936-0025907B4FC0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/AEF20350-54EC-E611-9D6E-0090FAA581E4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B04D26EE-63EC-E611-95DF-008CFA580778.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B0B0E651-5FEC-E611-8E91-0090FAA572B0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B224507F-4DEC-E611-BECD-E0071B7AF7C0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B29DD95C-54EC-E611-B07F-00259074AED2.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B2F40D03-78EC-E611-997E-008CFA110B08.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B2FE69F8-5DEC-E611-952F-008CFA111334.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B4174B51-54EC-E611-BA51-002590D0B06E.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B43CC764-54EC-E611-8212-5065F38162B1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B4DAE6F7-5DEC-E611-AEC3-008CFA197AB0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B62D57FA-77EC-E611-80B5-008CFA197BD4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B62D7DA7-5EEC-E611-9560-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B655B2D3-4DEC-E611-8556-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B6A1060B-71EC-E611-B990-0090FAA58BF4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B8CAAFC4-88EC-E611-B176-B083FECFEF7D.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/B8E77F57-54EC-E611-9A86-0090FAA57F44.root',
] )
readFiles.extend( [
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/BCB083D3-4DEC-E611-AB14-5065F381E151.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/BE4B8C5C-6AEC-E611-9C05-002590D0B0B6.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/BE510E4A-5EEC-E611-8209-B8CA3A709648.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/BE9AA648-65EC-E611-BBCF-A0369F301924.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C02CCB47-71EC-E611-BBEA-008CFA110C6C.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C064E6F7-77EC-E611-AA75-008CFA111330.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C095C2C9-66EC-E611-9292-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C43314F7-77EC-E611-BE4F-008CFA1111E0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C447580A-5DEC-E611-8CF3-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C46F416D-9DEC-E611-BE3D-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C4C16064-5DEC-E611-A592-00259073E3FE.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C62F7FA3-67EC-E611-B1AA-00259074AE8C.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C65B4208-78EC-E611-B2A7-008CFA1112B0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C6869AA0-6BEC-E611-9C24-0090FAA57FA4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C858F11A-5DEC-E611-983F-008CFA111330.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/C8F5E6A5-67EC-E611-AD5A-20CF3027A5F5.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/CA036310-5DEC-E611-A4E7-008CFA197D88.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/CA1B9205-71EC-E611-BAC2-00259073E500.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/CA2B0104-71EC-E611-9DE6-0090FAA581F4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/CA6DC154-5FEC-E611-B8D5-0CC47A4D99B0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/CA7F0591-77EC-E611-A4FC-0090FAA572B0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/CC2E6013-5DEC-E611-8A39-008CFA111348.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/CC5FF817-5DEC-E611-B11C-008CFA111330.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/CE3CB97D-4DEC-E611-8443-E0071B7AC760.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D2363A93-77EC-E611-AB63-00259073E3F2.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D25A8B81-82EC-E611-9936-002590D0B0C8.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D25F2731-78EC-E611-B1DB-008CFA111320.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D2C0D339-71EC-E611-A9FC-B083FECF837B.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D2D481D2-4DEC-E611-827C-24BE05C4D801.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D2DDA10D-67EC-E611-8466-00259073E3FE.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D42DD647-7EEC-E611-88EB-00259073E4E2.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D46879A0-7EEC-E611-A9DE-008CFA111270.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D626F557-54EC-E611-AB5D-0090FAA57F44.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D686B7F4-5DEC-E611-94BE-008CFA111330.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D69D19D6-8FEC-E611-9668-0090FAA57410.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D6F9D1D8-55EC-E611-9770-5065F381E1A1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D817161D-5DEC-E611-9FF4-008CFA5D2758.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/D8FDE763-54EC-E611-A245-24BE05C46B11.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/DC9CA6D2-6AEC-E611-8FDA-E0071B74AC00.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/DCCAECA5-64EC-E611-AACD-5065F3812291.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/DE13A13A-6CEC-E611-B80F-0090FAA57710.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/DE270577-A8EC-E611-86A7-1866DAEEB364.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/DE9F3903-66EC-E611-ACE3-A0369F301924.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E032E35B-6AEC-E611-BC7E-0025907B4FC0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E073D070-63EC-E611-A8E0-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E088DC08-55EC-E611-8454-00259073E4E6.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E0ACFE43-7EEC-E611-ADD9-0090FAA58754.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E0CC18D6-4DEC-E611-90B9-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E209D09B-64EC-E611-A181-E0071B7A7870.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E2D6FF7F-83EC-E611-9DCC-1866DAEB5C78.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E2FC2509-5EEC-E611-B993-008CFA11138C.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E43BE71D-6AEC-E611-AF5A-008CFA1111AC.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E450C6F4-5DEC-E611-AA65-E0071B7A5650.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E4589063-54EC-E611-AC76-5065F3816201.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E4F336E4-55EC-E611-80CA-008CFA197D88.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E658CB28-66EC-E611-8768-A0369F30FFD2.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E67440CC-77EC-E611-AE76-008CFA197C58.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E6871BAC-63EC-E611-9B7C-0090FAA57730.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E821253A-6CEC-E611-A3BA-0090FAA57F24.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E85F4594-77EC-E611-9AAA-00259073E3FE.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/E8E7D1D6-4DEC-E611-933E-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/EA1ED107-71EC-E611-9337-00259073E488.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/EA24C305-71EC-E611-A5DA-00259073E3F2.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/EC31213E-6CEC-E611-82C6-00259073E44E.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/EC9204F4-5DEC-E611-8FAA-008CFA197A04.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/EEC8E111-5DEC-E611-BAD1-D4AE527EDFE6.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F0486946-7EEC-E611-A522-00259073E50A.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F04F76D6-4DEC-E611-9968-E0071B7A9810.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F2617890-5FEC-E611-A120-A0000420FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F2A0EA62-54EC-E611-B028-5065F3818291.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F2B8BD12-78EC-E611-A935-008CFA197C70.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F2F8AF11-6AEC-E611-BA13-1418774105B6.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F415863F-65EC-E611-9DE1-24BE05C6D5B1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F4496457-54EC-E611-8DC3-0090FAA57F44.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F6410EF5-5DEC-E611-B1FC-0090FAA597B4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F65096EA-5DEC-E611-9AFC-A0000620FE80.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F6848943-7EEC-E611-92A2-0090FAA57A00.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F895F600-78EC-E611-A25F-008CFA111270.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/F89CAC62-54EC-E611-95F8-24BE05C648A1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/FAA95B63-54EC-E611-B2EA-24BE05C44BB1.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/FC1DD85C-54EC-E611-8012-00259074AED2.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/FC400E03-78EC-E611-AB9F-008CFA1113F4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/FCD9028E-5FEC-E611-9F71-24BE05C60641.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/FE648F5A-60EC-E611-A00B-00259073E3FE.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver2-v1/80000/FEF3E2B1-4EEC-E611-A3B8-0025907B4FC0.root',
] )