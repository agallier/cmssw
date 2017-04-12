#ifndef TCCBLOCKFORMATTER_H
#define TCCBLOCKFORMATTER_H

#include <iostream>
#include <vector>
#include <map>

#include "DataFormats/EcalDigi/interface/EcalDigiCollections.h"
#include "DataFormats/FEDRawData/interface/FEDRawDataCollection.h"
#include "DataFormats/FEDRawData/interface/FEDRawData.h"
#include "EventFilter/EcalDigiToRaw/interface/BlockFormatter.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "Geometry/EcalMapping/interface/EcalElectronicsMapping.h"


// 
// The block containing the trigger towers for a given FED
//



class TCCBlockFormatter : public BlockFormatter {
 public :

        TCCBlockFormatter(EcalDigiToRaw* es) : BlockFormatter(es), AllTPsamples_(false) {};
	~TCCBlockFormatter();
        static const int kCardsPerTower = 5;     // Number of VFE cards per trigger tower
        void DigiToRaw(const EcalTriggerPrimitiveDigi& trigprim, FEDRawData& rawdata, const EcalElectronicsMapping* TheMapping, int bx, int lv1) const;

 private :
	const bool AllTPsamples_;

};



#endif


