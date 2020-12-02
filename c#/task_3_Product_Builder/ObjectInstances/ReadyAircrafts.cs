using System;
using Objects;

namespace ObjectInstances
{
    public static class ReadyAircrafts
    {
        public static LightAircraft Cessna172 = new LightAircraft("Cessna", "172", 3, 300, 200, -1);
        public static CargoAircraft BoeingC17 = new CargoAircraft("Boeing", "C-17", 10000, 4500, 7000, -1);
        public static CommercialAircraft Airbus320 = new CommercialAircraft("Airbus", "A320", 180, 1200, 4000, 2100, -1);
        public static CommercialAircraft Boeing737 = new CommercialAircraft("Boeing", "737", 190, 4500, 5000, 2300, -1);
    }
    
}