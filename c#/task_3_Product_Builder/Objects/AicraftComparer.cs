using System;
using System.Collections.Generic;

namespace Objects
{
    class AicraftComparerByFlightRange : IComparer<Aircraft>
    {
        public int Compare(Aircraft a, Aircraft b)
        {
            return a.flightRange.CompareTo(b.flightRange);
        }
    }
}
