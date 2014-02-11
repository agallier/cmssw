#include "EventFilter/L1TRawToDigi/interface/L1TRawToDigi.h"
#include "EventFilter/L1TRawToDigi/interface/UnpackerCollections.h"

namespace l1t {
   UnpackerCollections::UnpackerCollections(edm::Event& event) :
      event_(event)
   {
   }

   UnpackerCollections::~UnpackerCollections()
   {
      // For every member:
      // event_.put();
   }

   void
   UnpackerCollections::registerCollections(L1TRawToDigi *prod)
   {
      // For every member:
      prod->produces<int>();
   }
}
