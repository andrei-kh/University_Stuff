using System;

namespace atestation
{
    public class CargoTaxi : Car
    {
        private int CarryingCapacity { get; }
        private int CostFor1Hour { get; }
        public CargoTaxi(string CarBrand, string RegestrationNumber,
            int YearOfIssue, int Mileage, int FuelPer100km, 
            int CarryingCapacity, int CostFor1Hour) : 
        base(CarBrand, RegestrationNumber, YearOfIssue, Mileage, FuelPer100km)
        {
            this.CarryingCapacity = CarryingCapacity;
            this.CostFor1Hour = CostFor1Hour;
        }
        public double ComputeProfit(int Hours)
        {
            return CostFor1Hour + (Hours - 1) * (0.5 * CostFor1Hour);
        }
    }
}
