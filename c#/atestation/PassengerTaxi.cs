using System;

namespace atestation
{
    public class PassengerTaxi : Car
    {
        int NumberOfPassengers { get; }
        int CostFor5km { get; }
        public PassengerTaxi(string CarBrand, string RegestrationNumber,
            int YearOfIssue, int Mileage, int FuelPer100km,
            int NumberOfPassengers, int CostFor5km) :
        base(CarBrand, RegestrationNumber, YearOfIssue, Mileage, FuelPer100km)
        {
            this.NumberOfPassengers = NumberOfPassengers;
            this.CostFor5km = CostFor5km;
        }
        public override double ComputeProfit()
        {

        }
    }
}
