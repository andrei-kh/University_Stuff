using System;
using System.Collections.Generic;
using System.Linq;

namespace atestation
{
    public class TaxiPark
    {
        List<Car> cars;
        public TaxiPark()
        {
            cars = new List<Car>();
        }
        public void AddCar(Car car)
        {
            cars.Add(car);
        }
        public void RemoveCar(Func<Car, bool> func)
        {
            cars.RemoveAll(x => func(x));
        }
        public int ComputeProfit(int Km, int Hours)
        {
            
        }
    }

    public class MilageComparator : IComparer<Car>
    {
        public int Compare(Car a, Car b)
        {
            return a.GetMileage().CompareTo(b.GetMileage());
        }
    }
}
