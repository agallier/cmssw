import FWCore.ParameterSet.Config as cms

postProcessorVertex = cms.EDAnalyzer("DQMGenericClient",
                                     subDirs = cms.untracked.vstring("Validation/Vertices/*"),
                                     efficiency = cms.vstring(
                                         "effic_vs_NumVertices 'Efficiency vs NumVertices' GenAllAssoc2RecoMatched_NumVertices GenAllAssoc2Reco_NumVertices",
                                         "effic_vs_Z 'Efficiency vs Z' GenAllAssoc2RecoMatched_Z GenAllAssoc2Reco_Z",
                                         "effic_vs_R 'Efficiency vs R' GenAllAssoc2RecoMatched_R GenAllAssoc2Reco_R",
                                         "effic_vs_Pt2 'Efficiency vs Sum p_{T}^{2}' GenAllAssoc2RecoMatched_Pt2 GenAllAssoc2Reco_Pt2",
                                         "effic_vs_NumTracks 'Efficiency vs NumTracks' GenAllAssoc2RecoMatched_NumTracks GenAllAssoc2Reco_NumTracks",
                                         "effic_vs_ClosestVertexInZ 'Efficiency vs ClosestVtx in Z' GenAllAssoc2RecoMatched_ClosestDistanceZ GenAllAssoc2Reco_ClosestDistanceZ",
                                         "merged_vs_NumVertices 'Merged vs NumVertices' RecoAllAssoc2GenMultiMatched_NumVertices RecoAllAssoc2Gen_NumVertices",
                                         "merged_vs_Z 'Merged vs Z' RecoAllAssoc2GenMultiMatched_Z RecoAllAssoc2Gen_Z",
                                         "merged_vs_R 'Merged vs R' RecoAllAssoc2GenMultiMatched_R RecoAllAssoc2Gen_R",
                                         "merged_vs_Pt2 'Merged vs Sum p_{T}^{2}' RecoAllAssoc2GenMultiMatched_Pt2 RecoAllAssoc2Gen_Pt2",
                                         "merged_vs_NumTracks 'Merged vs NumTracks' RecoAllAssoc2GenMultiMatched_NumTracks RecoAllAssoc2Gen_NumTracks",
                                         "merged_vs_ClosestVertexInZ 'Merged vs ClosestVtx in Z' RecoAllAssoc2GenMultiMatched_ClosestDistanceZ RecoAllAssoc2Gen_ClosestDistanceZ",
                                         "fakerate_vs_NumVertices 'Fakerate vs NumVertices' RecoAllAssoc2GenMatched_NumVertices RecoAllAssoc2Gen_NumVertices fake",
                                         "fakerate_vs_Z 'Fakerate vs Z' RecoAllAssoc2GenMatched_Z RecoAllAssoc2Gen_Z fake",
                                         "fakerate_vs_R 'Fakerate vs R' RecoAllAssoc2GenMatched_R RecoAllAssoc2Gen_R fake",
                                         "fakerate_vs_Pt2 'Fakerate vs Sum p_{T}^{2}' RecoAllAssoc2GenMatched_Pt2 RecoAllAssoc2Gen_Pt2 fake",
                                         "fakerate_vs_NumTracks 'Fakerate vs NumTracks' RecoAllAssoc2GenMatched_NumTracks RecoAllAssoc2Gen_NumTracks fake",
                                         "fakerate_vs_ClosestVertexInZ 'Fakerate vs ClosestVtx in Z' RecoAllAssoc2GenMatched_ClosestDistanceZ RecoAllAssoc2Gen_ClosestDistanceZ fake",
                                         "duplicate_vs_NumVertices 'Duplicate vs NumVertices' GenAllAssoc2RecoMultiMatched_NumVertices GenAllAssoc2Reco_NumVertices",
                                         "duplicate_vs_Z 'Duplicate vs Z' GenAllAssoc2RecoMultiMatched_Z GenAllAssoc2Reco_Z",
                                         "duplicate_vs_R 'Duplicate vs R' GenAllAssoc2RecoMultiMatched_R GenAllAssoc2Reco_R",
                                         "duplicate_vs_Pt2 'Duplicate vs Sum p_{T}^{2}' GenAllAssoc2RecoMultiMatched_Pt2 GenAllAssoc2Reco_Pt2",
                                         "duplicate_vs_NumTracks 'Duplicate vs NumTracks' GenAllAssoc2RecoMultiMatched_NumTracks GenAllAssoc2Reco_NumTracks",
                                         "duplicate_vs_ClosestVertexInZ 'Duplicate vs ClosestVtx in Z' GenAllAssoc2RecoMultiMatched_ClosestDistanceZ GenAllAssoc2Reco_ClosestDistanceZ",
                                     ),
                                     resolution = cms.vstring(),
                                     profile= cms.vstring(),
                                     outputFileName = cms.untracked.string(""),
                                     verbose = cms.untracked.uint32(5)
)

postProcessorVertexStandAlone = cms.Sequence(postProcessorVertex)
