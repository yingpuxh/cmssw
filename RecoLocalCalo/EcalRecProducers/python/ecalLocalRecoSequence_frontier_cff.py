import FWCore.ParameterSet.Config as cms

# Calo geometry service model
#ECAL conditions
from RecoLocalCalo.EcalRecProducers.getEcalConditions_frontier_cff import *
#ECAL reconstruction
from RecoLocalCalo.EcalRecProducers.ecalUncalibRecHit_cfi import *
from RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi import *
from RecoLocalCalo.EcalRecProducers.ecalPreshowerRecHit_cfi import *
ecalLocalRecoSequence = cms.Sequence(ecalUncalibRecHit*ecalRecHit*ecalPreshowerRecHit)
