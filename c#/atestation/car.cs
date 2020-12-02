using System;

namespace atestation
{
    public abstract class Car
    {
        protected string CarBrand;
        protected string RegestrationNumber;
        protected int YearOfIssue;
        protected int Mileage;
        protected int FuelPer100km;
        protected Car(string CarBrand, string RegestrationNumber,
            int YearOfIssue, int Mileage, int FuelPer100km)
        {
            this.CarBrand = CarBrand;
            this.RegestrationNumber = RegestrationNumber;
            this.YearOfIssue = YearOfIssue;
            this.Mileage = Mileage;
            this.FuelPer100km = FuelPer100km;
        }
        public abstract double ComputeProfit();
        public int GetMileage()
        {
            return Mileage;
        }
    }
}
