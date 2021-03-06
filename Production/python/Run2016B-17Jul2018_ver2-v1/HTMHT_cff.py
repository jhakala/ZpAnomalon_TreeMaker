import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/00401916-418D-E811-9B06-AC1F6B23C77C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/00F87B46-F88A-E811-910C-AC1F6B23C94A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/021EEFCE-E28B-E811-9016-AC1F6B23C96E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/022C5693-DB8B-E811-B37D-00259021A0E2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/02415430-618D-E811-AC13-0CC47A5450FA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/025A8CD7-E88A-E811-BC7C-0CC47AB64A58.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/042119C2-878D-E811-8179-901B0E542962.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/06DBCE30-618D-E811-891C-0CC47AB58BE6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/06FD1C6B-D18B-E811-8B82-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/06FE538E-FC8C-E811-A356-AC1F6B23C7DA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/0838EAC5-3D8D-E811-8A34-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/087994EF-0F8D-E811-9576-0CC47AB64AE2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/0AA2FD9B-0C8C-E811-9100-AC1F6B23C738.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/0C916B95-228C-E811-9E9D-0025904CEC20.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/0CBF2420-C68A-E811-A288-0025904CF978.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/10190B2E-3A8D-E811-8150-AC1F6B23C806.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/103E2530-678D-E811-ACED-0CC47AB65046.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/107F3E93-7D8C-E811-9172-0CC47AB6503C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/12970E7E-F98B-E811-8CA8-AC1F6B23C738.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/129DDDDC-D88C-E811-9906-AC1F6B23C9D8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/12D0D018-8B8C-E811-854E-0CC47AFC3C9A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/16A9C161-378D-E811-91F0-00259021A14E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/16C59C4E-F48C-E811-98F8-AC1F6B23C808.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/185D6066-D08B-E811-86F4-AC1F6B23C93A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/1A0AAAD9-308D-E811-92F4-001E67504D2D.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/1A27E0D0-E28B-E811-9CD8-AC1F6B23C96C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/1A6DFBDB-4D8C-E811-9AFA-0CC47A544E12.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/1AD1CE23-738D-E811-B278-00259021A4C2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/1C2360A2-148D-E811-B108-B4E10FA31F49.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/1C56C860-D58B-E811-A603-AC1F6B23C93A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/1CCE737D-F98B-E811-A655-AC1F6B23C738.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/202BD259-528D-E811-851B-0CC47AB64FB0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/20751635-618D-E811-A5D2-AC1F6B23C93C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/20AB2B99-A88C-E811-B5BC-0CC47AFC3C98.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/22678DCB-828D-E811-9A74-001E675827DC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/2441729D-728D-E811-AB36-0025904CEBE0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/265471DE-E88A-E811-A660-0025904CF96A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/26A6A473-048C-E811-881F-00259021A306.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/2C9D133F-448D-E811-8797-AC1F6B23C9FE.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/2E7612CD-E28B-E811-B61C-AC1F6B23C830.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/2EA64702-5B8D-E811-A093-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/2ED85AA0-728D-E811-ADDD-0CC47A544F58.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/300A7CA0-728D-E811-9AAB-AC1F6B23C812.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/30726D34-3A8D-E811-ACAE-0CC47AB6503C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/30816A21-738D-E811-90B6-20CF3019DF08.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/32F65B08-DF8B-E811-BB0E-AC1F6B23C594.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/34160DE2-9F8C-E811-993E-AC1F6B23C96C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/343AFE50-C68C-E811-8308-AC1F6B23C7DC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/343B6D6D-F48B-E811-94F1-B4E10FA31EE1.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/36ACAC6A-D18B-E811-8534-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/3811BF95-228C-E811-B82F-0025904CEC20.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/38C9A477-1A8D-E811-8EC0-0025902D959A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/3C0E4F76-878D-E811-AA0A-0CC47AFC3CA0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/3C62FA83-DB8B-E811-9280-00259021A2AA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/3CDD407B-F48C-E811-9D43-10BF481A0245.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/40AA4A6A-D18B-E811-BEC3-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/40CDF343-C68C-E811-A32B-001E67504AA5.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/40CFE0CC-998C-E811-AB5C-AC1F6B23C82E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/4234D658-4C8D-E811-9FD2-0CC47AFC3CA0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/42FF48BD-D28C-E811-92B8-001E675047A5.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/4444355E-D78B-E811-8FDB-B4E10FD217E1.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/4A6BFB4C-F48C-E811-B4BC-0CC47AE0F33A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/4C2706A9-D48C-E811-815C-0025904CF978.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/4CAE6548-BD8C-E811-8391-AC1F6B239D7A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/4E9BF0A4-B48C-E811-9A70-0CC47AFC3CA6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/503A396E-578C-E811-A1D0-AC1F6B23C7DE.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/50C05A9D-768C-E811-9320-B4E10FD21863.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/52484F07-5B8D-E811-8115-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/52DFC165-A58A-E811-99DC-0CC47AB64EF6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/5464F630-638C-E811-9B7D-001E67504D15.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/54696672-1A8D-E811-BFB6-AC1F6B23C77C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/54A66960-148D-E811-A1B8-0CC47AFC3C98.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/560BCC03-2A8D-E811-966D-0CC47A544E12.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/5643609B-438D-E811-A498-AC1F6B23C77C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/56A36C33-E58C-E811-AF54-B4E10FA31F49.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/5A59DBD6-E88A-E811-8A1F-0CC47AB64A58.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/5ABCFC88-558D-E811-9CA1-0CC47A166D66.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/605D245E-F48B-E811-9BE1-B4E10FA31EE1.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/624977EF-7F8D-E811-B7E4-0CC47AB64AE0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/62A3FF92-B48C-E811-95A9-0CC47A545062.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/661FEA46-C38C-E811-BDA9-00259021A3D2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/688AA25B-4C8D-E811-978A-0025902D144E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/68B6F4BA-D88C-E811-B55B-002590189516.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/68F2E666-AE8C-E811-AD5E-0CC47AFC3C18.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/6A66ADC7-DE8C-E811-B413-0CC47AE0F33C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/6C31CC8A-DB8B-E811-B8E6-00259021A526.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/6C6E98A6-878D-E811-BCEB-0CC47AE0F33C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/706B1E06-D58B-E811-BFE7-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/72AFCF8A-DB8B-E811-B1D0-00259021A526.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/7402DD4C-D48C-E811-91E9-AC1F6B23C7DA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/74BC5893-DB8B-E811-9048-00259021A0E2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/76278DC2-4F8D-E811-A15D-0CC47AB64FB0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/7649AC83-DB8B-E811-BF49-00259021A2AA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/7800C7A8-B48C-E811-84EA-0CC47AE0F33A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/78FC5E91-008D-E811-8E3A-20CF3027A580.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/7CE46664-A58A-E811-BD22-B4E10FA31EFB.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/7E00CB77-778C-E811-AD93-0CC47AFC3C86.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/7E2B9E6B-D18B-E811-A61E-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/7E9EB7A0-0F8C-E811-A15B-AC1F6B23C94C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/80388F38-3A8D-E811-B04A-0025902D144E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/8075728A-378C-E811-859B-0CC47AFC3C9A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/8278E074-ED8C-E811-8483-AC1F6B23C82E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/8847EEDE-E88A-E811-8115-0025904CF96A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/8A6BB059-068D-E811-BDC6-0CC47AFC3CA6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/8C4A7916-C38C-E811-94E9-0CC47A544E12.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/8C6DC87F-928C-E811-B84E-AC1F6B23C94C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/8E1C9189-648C-E811-A88E-0CC47A545062.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/8E602C9E-A48A-E811-BB68-0CC47AB64AE2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/8E6B2F35-618D-E811-ADBE-AC1F6B23C96A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/90E30B9E-A48A-E811-B283-0CC47AB64AE2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/922F68BF-B08A-E811-83AD-10BF481A01ED.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/926FC565-D08B-E811-B621-AC1F6B23C93A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/94A77C36-678D-E811-B753-901B0E5427A4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/9682568A-D58C-E811-9805-0CC47AFC3C98.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/96BCA9C6-3D8D-E811-9511-0025902D144E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/98A54E43-468C-E811-9F25-0CC47AFC3C98.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/9AFCA0EF-D58B-E811-A8B4-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/9C4E8F99-0C8C-E811-9A7F-AC1F6B23C808.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/9CBEA0C4-4F8D-E811-BF8B-0025902D959A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/9E6615BE-788D-E811-935D-AC1F6B23C812.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/9EA04B29-178C-E811-B3E3-0CC47AB58BE6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A026A7C8-3D8D-E811-8986-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A054BBCF-408C-E811-81AB-AC1F6B23C88A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A2F17FCB-7C8C-E811-B5B0-001E6757CD34.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A4235C35-618D-E811-83A3-AC1F6B23C812.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A647C2C7-3D8D-E811-B0D6-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A655E8CA-3D8D-E811-AE20-001E675825D4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A69FFEA7-008D-E811-BC5D-B4E10FD21E87.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A6D60B71-A88C-E811-9D82-0CC47A545062.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A6EEA18B-D68B-E811-8849-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A832926F-1A8D-E811-B94B-0CC47AFC3C6E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A85F28A1-438D-E811-8637-001E67504AA5.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/A8D8DA42-E58C-E811-BF33-0CC47AFC3CA6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/AA338D93-DB8B-E811-BFF6-00259021A0E2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/AA577065-D08B-E811-B8A6-AC1F6B23C93A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/AC4BDA9C-148D-E811-8999-0CC47AE0F33C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/B2883E04-5B8D-E811-B4F3-001E675817A4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/B2BFE9CE-9F8C-E811-A4F2-901B0E6459DE.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/B2E6E0D5-3D8D-E811-B457-0025904B2C5E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/B2E9238F-7F8D-E811-BE8E-B4E10FA31FCF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/B4458E6B-8B8C-E811-9090-AC1F6B23C830.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/B488016B-D18B-E811-9B92-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/B6161F1C-638C-E811-B37F-901B0E6459DE.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/B6B19594-558D-E811-A735-002590189516.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/B862D7E3-528D-E811-BF61-0CC47AFC3CA6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/B8F35F1D-C68A-E811-A422-0CC47AB64AE0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/BAA25DDD-E88A-E811-9F93-0025904CF96A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/BC583F6D-BD8C-E811-97A5-AC1F6B23C80A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/BC58526A-D18B-E811-8D16-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/BC693A19-C68A-E811-A240-0CC47AFC3D34.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/BC816C39-468C-E811-9A79-0025904CEC28.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/BEA6DD9E-A48A-E811-91E6-0CC47AB64AE2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/BECC83C3-3D8D-E811-9CF7-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/C0447D3B-EB8A-E811-9C09-001E67504645.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/C2830420-C68A-E811-9EFE-AC1F6B239D7A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/C2A5C51E-C68A-E811-AE33-0CC47AB58BE6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/C2B010BE-788D-E811-95BE-AC1F6B23C812.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/C65E520E-AE8C-E811-A7E6-002590189516.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/C85C971C-C68A-E811-8AEC-0CC47AB64E80.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/CAC598B9-788D-E811-9A60-0025904CEBE0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/CC322168-ED8B-E811-BD24-0CC47A545096.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/CE1C8E6B-8B8C-E811-A4DF-AC1F6B23C96C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/CE32F35C-ED8B-E811-AD40-AC1F6B23CA00.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/D03D8199-928C-E811-B1FA-20CF305B050E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/D0A2A78D-BD8C-E811-A196-0CC47AFC3C9C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/D0FC2998-218D-E811-8D62-0CC47AB58E9C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/D48AF0D6-308C-E811-AA8C-0CC47AFC3C18.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/D60B2EFB-F18B-E811-B0AA-0CC47AFC3CA4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/DE21AC66-A58A-E811-8609-0CC47AB64EF6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/DEE88AEF-C98C-E811-9D95-AC1F6B239D7A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/E0BB0CBC-788D-E811-9D27-0025904CEBE0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/E0BE4D96-C98C-E811-BA80-0CC47AFC3CA6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/E2CDB324-5D8A-E811-AB6F-0CC47AB64AE2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/E4D7C072-A88C-E811-8DCC-AC1F6B23C96C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/E62A24C6-5B8C-E811-95B5-AC1F6B23C7DA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/E8370D04-2A8D-E811-BB37-0CC47A206FCA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/E84139A5-078D-E811-AD30-0CC47A5450DA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/E8F5C58E-558D-E811-80C0-AC1F6B23C812.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/EA887558-4C8D-E811-BB80-0CC47AB65046.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/EC82FBF2-078D-E811-AA18-B4E10FD21E87.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/ECCDDCD6-DE8C-E811-A150-AC1F6B23C7DA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/EE1B589A-728D-E811-82E0-AC1F6B23C812.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/F08045C3-4F8D-E811-9877-AC1F6B23C970.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/F081BF05-5B8D-E811-9FFD-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/F0AAA86A-D18B-E811-9A9F-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/F0D60298-BD8C-E811-9E1E-0CC47AFC3C74.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/F2504EC8-3D8D-E811-B770-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/F2695DC3-3D8D-E811-B13B-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/F663C16A-D18B-E811-8146-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/F69208C2-528D-E811-91FB-0025902D959A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/F6CBEBF7-F88A-E811-BA99-AC1F6B23C94A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/F86DF2BC-418C-E811-9B45-0CC47AE0F33C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/FA70DCE2-308D-E811-B009-901B0E5427BA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/FAFA8CD9-E88A-E811-81FC-0CC47AB58E9C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/FE45BBF6-1F8C-E811-A13B-901B0E542804.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/00000/FEC12F52-858A-E811-9A2A-0025904B302E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/02F6E9C0-588D-E811-B0EE-AC1F6B23C88A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/0A7DE1F0-588B-E811-9B9D-0CC47AFC3C86.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/0E63768D-0A8C-E811-8169-20CF300E9EC8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/0E893A3A-1E8C-E811-833D-0CC47A166D66.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/0EB06AD9-038D-E811-89E7-B4E10FA3213D.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/108D46BF-718D-E811-8533-0CC47AB58BE6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/12BB86FF-FA8A-E811-A465-0025902D959A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/12E60D0D-528D-E811-8E2D-0CC47AFC3CA2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/12F528AA-638C-E811-9842-0025902D144E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/145E4E0B-DB8C-E811-AAA0-20CF300E9EB7.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/16BDB2E9-F08C-E811-AC62-0CC47AFC3C18.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/16EF6446-4B8D-E811-B901-B4E10FD218CF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/182BEEF3-638C-E811-8668-AC1F6B23C88C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/18C29726-6D8D-E811-910E-B4E10FA31F63.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/1A50B6B4-6C8D-E811-82FE-AC1F6B23C812.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/1CCC6FF4-368D-E811-B90D-0CC47AFC3CA4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/1CF3BB99-5F8D-E811-958E-0025904CEC28.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/1E43353E-1E8C-E811-9F39-AC1F6B23C830.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/1E47B10E-418C-E811-BCF7-AC1F6B23C96C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/1ED533AC-BF8C-E811-87D3-901B0E5427B0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/2026CF15-F98C-E811-99C8-AC1F6B23C7DA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/22298220-1E8C-E811-817B-AC1F6B23C830.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/223B292A-E48A-E811-994C-0025904CF96A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/247A8CB4-6C8D-E811-A833-AC1F6B23C812.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/2691F6C2-588D-E811-9376-B4E10FD218CF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/26C41239-938D-E811-B0E1-AC1F6B23C80C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/26FFF2CA-FF8C-E811-A175-0025904CEC28.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/28772814-A78D-E811-8634-0CC47AB6503E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/28826722-0E8D-E811-9272-0CC47AFC3C98.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/28D22DA2-E18C-E811-A0FD-001E675817A4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/28F3707D-F28C-E811-8F82-B4E10FD218CF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/2A8018C0-798C-E811-839D-0025904CEBE0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/2AA5C7B7-3F8C-E811-A3AD-0CC47A5450D8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/2C07B090-9B8D-E811-9C9B-20CF3056170E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/2C0B40B9-3F8C-E811-95A3-0CC47A5450D8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/2C9E1ABA-3F8C-E811-B857-0CC47A5450F8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/2E5E82F9-DA8C-E811-81C1-AC1F6B23C9FE.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/2EF510BF-718D-E811-AA7A-0025904CEBE0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/328F0520-A68D-E811-844E-B4E10FA31FCF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/32E3240E-418C-E811-9AAB-AC1F6B23C94C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/344AAD59-9E8D-E811-AC94-0CC47A5451E4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/36A8D815-A78D-E811-8E17-AC1F6B23C80C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/381E7EF7-DA8C-E811-9B80-B4E10FD218CF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/3E699B91-228D-E811-9C76-B4E10FD217E1.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/3EB35214-FB8A-E811-80B9-AC1F6B23C80C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/3EBE2103-308D-E811-8A05-0CC47A5450D8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/44AB1C16-A78D-E811-A4BD-AC1F6B23C806.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/46EE7E47-798D-E811-85F3-0CC47AB58BE6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/48A09200-FB8A-E811-B172-0CC47A5450F8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/48EEA8A8-B98D-E811-B7FD-001E67504E7D.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/4E261A55-C88C-E811-A01E-AC1F6B23C592.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/4E71297C-E98A-E811-B04F-0025902D1214.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/4E731B25-6D8D-E811-9913-0CC47AB65046.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/4E7FC417-A78D-E811-A687-0CC47A166D64.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/4ED37D21-6D8D-E811-AB65-0CC47AE0F33C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/4EDED2B7-588D-E811-BD1F-0CC47AE0F33C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/4EEB292A-E48A-E811-9A8F-0025904CF96A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/54C2180F-418C-E811-9848-AC1F6B23C830.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/56B73B4E-7D8D-E811-82E1-0CC47A544E10.root',
] )
readFiles.extend( [
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/584FFDA0-888D-E811-BA47-10BF481A01EF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/5A275B11-418C-E811-B2D1-AC1F6B23CA00.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/5C2CBEBF-AF8C-E811-A3CF-AC1F6B23C7DC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/5CF67850-9E8D-E811-88A0-AC1F6B23C86C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/60D1C5DD-9A8C-E811-9F61-AC1F6B23C7DE.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/64C689AC-6D8D-E811-91B3-901B0E5427BA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/64CAD362-608C-E811-886D-AC1F6B23C594.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/6C0C3EB0-BC8D-E811-8555-0CC47AFC3C9C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/6C6D6E51-9A8C-E811-9BE6-00259021A39E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/6CD56F98-1B8D-E811-8135-0CC47AB58E9C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/6E09700A-7D8D-E811-A65B-0CC47AB64AE0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/6EAB2AB8-328C-E811-B558-001E67504B25.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/6ECCE0ED-438C-E811-8DAA-AC1F6B23C830.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/7016B20A-BD8D-E811-BD39-AC1F6B23C594.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/70F7421F-AA8D-E811-BD60-BCAEC5097201.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/72C6ECBA-3F8C-E811-BB99-0CC47A5450D8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/74A5F569-608C-E811-B938-0025902D144E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/762D8041-4B8D-E811-B88C-0CC47A544E10.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/7A8BA21D-3C8C-E811-9B73-20CF3019DF02.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/7EA61002-C08C-E811-8D35-0CC47A544E12.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/805D7835-938D-E811-9E04-0CC47AB65046.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/80E91BB9-A88D-E811-975D-B4E10FA31FCF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/8287A9C9-3D8D-E811-AE3D-B4E10FD21E87.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/84D7F85A-E88C-E811-A506-AC1F6B23C7DC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/86455B9D-148D-E811-8862-AC1F6B23C93C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/86DCE205-158D-E811-9B21-901B0E5427A6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/881E42C9-8F8D-E811-9484-AC1F6B23C77A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/88ECDB9B-5F8D-E811-BBCB-AC1F6B23C86C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/8A3D12DF-438C-E811-8B3B-AC1F6B239D7A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/90DE8A37-848D-E811-9D6C-20CF3019DF10.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/90E37C12-F98C-E811-A7C0-001E6757EAA4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/92569016-678D-E811-A00A-00259021A076.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/9407791D-A68D-E811-A398-B4E10FA31FCF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/94371751-1E8C-E811-8B15-0CC47A166D66.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/945096E1-B28D-E811-92E0-00259021A04E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/9488B6C4-AF8C-E811-A4F6-0CC47A5450F8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/9A175729-608D-E811-A198-20CF305616D1.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/9A55360E-418C-E811-93B9-AC1F6B239D7A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/9A77A3D7-7D8D-E811-9BD8-AC1F6B23C80C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/9A8C7DBB-8C8D-E811-AC49-0CC47A544E12.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/9AB6B5DC-9A8D-E811-B16D-0CC47AB65046.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/9CFB3953-A98D-E811-A945-AC1F6B23C806.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/9E3D770E-418C-E811-9214-AC1F6B23C9D8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/9EEC903B-1E8C-E811-A3BD-AC1F6B23C77C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/A654D637-448C-E811-9144-0CC47AB64AE2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/AA08E426-AC8D-E811-B90C-0CC47A166D64.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/AA984A35-938D-E811-A1BA-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/ACAB8F75-9E8D-E811-BA43-00259021A306.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/ACCA7D99-228D-E811-8858-001E67504D15.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/AED8192C-B68D-E811-B623-AC1F6B23C846.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/AEF7D0C8-B78C-E811-B619-485B398972FC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/AEFA540F-9F8C-E811-8C6E-0CC47AFC3C18.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/B0702D4F-AE8D-E811-A7EC-001E67504E7D.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/B2E97E56-9E8D-E811-B53A-0CC47A5451E4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/B2F4CD34-938D-E811-A4B0-AC1F6B23C594.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/B497A05D-8A8C-E811-A51C-001E67504FFD.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/B8A4D684-448C-E811-B8CE-0025902D957A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/BA39BC30-848D-E811-8773-AC1F6B23C806.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/BE9D1ABA-3F8C-E811-A27F-0CC47A5450F8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/BEBA42B5-6C8D-E811-8ECE-AC1F6B23C812.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C098941F-F98C-E811-BFE1-00259021A4C2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C0A309B3-8F8D-E811-A33F-0CC47A544E12.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C0C6CD11-418C-E811-845E-0CC47A545062.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C2A5D0BB-3F8C-E811-98DE-0CC47A5450D8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C2DDED87-E18C-E811-B8CC-0CC47AE0F33C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C4012202-FB8A-E811-8142-AC1F6B23C94C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C414E051-6A8C-E811-B757-AC1F6B23C832.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C4E07C48-4B8D-E811-83DE-20CF3027A5EF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C6559CE2-438C-E811-9123-AC1F6B23C738.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C844D8B0-798D-E811-A439-0025904CEC28.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/C8F6F704-728D-E811-86BB-001E67505105.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/CA680853-1E8C-E811-9A02-AC1F6B23C77C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/CE788563-CC8C-E811-96A6-AC1F6B23C96E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/CE9F4E5F-CC8C-E811-AD71-20CF3027A565.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/CEB36139-938D-E811-8CEC-001E67504A65.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/D6744949-4B8D-E811-906A-AC1F6B23C88C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/D6AFE780-638C-E811-85C5-AC1F6B23C594.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/D859F9A2-748C-E811-81A3-AC1F6B23C830.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/DEE53A04-308D-E811-88ED-0CC47AFC3D34.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/E22D7152-7D8D-E811-913F-0CC47AE0F33C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/E456E0BC-C38D-E811-93C2-20CF3019DF13.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/E62320DE-448C-E811-A3E7-B4E10FA31EE1.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/E626143D-8A8C-E811-B17B-AC1F6B23C848.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/E663A99A-AF8C-E811-AEAA-0CC47AFC3C6E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/EC2A08E6-D38C-E811-A8AB-B4E10FD21863.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/EC8BE74D-9E8D-E811-A58D-AC1F6B23C86C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/F09E3700-DB8C-E811-A921-20CF300E9EC8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/F632B40C-FB8A-E811-9E48-AC1F6B23C7E0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/F6C9A4EA-978D-E811-AB90-20CF3056170E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/FA4AB1CE-FF8C-E811-86A6-20CF300E9EDD.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/FC3A4F9F-CC8C-E811-A427-AC1F6B23C848.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/FC47074E-9E8D-E811-A77F-0CC47A166D64.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/FE16FEB0-928C-E811-9058-AC1F6B23C96E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/FE25BADC-9A8D-E811-BC7C-0CC47AB58BE4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver2-v1/20000/FEE8A4BD-3F8C-E811-8FAA-0CC47A5450F8.root',
] )
