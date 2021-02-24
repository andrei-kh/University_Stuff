using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace task_4_Gui_Implementation
{
    public partial class Flight_info : Form
    {
        AirlineDBEntities db;
        static int id = 0;
        public Flight_info([Optional] int ? Id)
        {
            InitializeComponent();
            if(Id != null)
            {
                button1.Text = "Update";
                button2.Visible = true;
                db = new AirlineDBEntities();
                Flight_Details flight = db.Flight_Details.Where(x => x.Id == Id).FirstOrDefault();
                id = flight.Id;
                flightnametext.Text = flight.Flight_Name;
                sourcetext.Text = flight.Source;
                desttext.Text = flight.Destination;
                deptext.Text = flight.Departure_Time;
                arrivaltext.Text = flight.Arrival_Time;
                classtext.Text = flight.Flight_Class;
                chargestext.Text = flight.Flight_Charges.ToString();
                seatstext.Text = flight.Seats.ToString();
            }
            else
            {
                button1.Text = "Add Flight";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(UtilityClass.TextBoxesAreNullorEmpty(this))
            {
                MessageBox.Show("Please Fill all fields");
            }
            else
            {
                db = new AirlineDBEntities();
                Flight_Details fd = new Flight_Details
                {
                    Flight_Name = flightnametext.Text,
                    Source = sourcetext.Text,
                    Destination = desttext.Text,
                    Departure_Time = deptext.Text,
                    Arrival_Time = arrivaltext.Text,
                    Flight_Class = classtext.Text,
                    Flight_Charges = Convert.ToDecimal(chargestext.Text),
                    Seats = Convert.ToInt32(seatstext.Text)
                };
                if (button1.Text == "Add Flight")
                {
                    db.Flight_Details.Add(fd);
                    db.SaveChanges();
                    UtilityClass.traverseControlsAndSetTextEmpty(this);
                    MessageBox.Show("Flight Details Saved Successfully");
                }
                else
                {
                    Flight_Details olddetails = db.Flight_Details.Where(x => x.Id == id).FirstOrDefault();
                    olddetails.Flight_Name = fd.Flight_Name;
                    olddetails.Source = fd.Source;
                    olddetails.Destination = fd.Source;
                    olddetails.Departure_Time = fd.Departure_Time;
                    olddetails.Arrival_Time = fd.Arrival_Time;
                    olddetails.Flight_Class = fd.Flight_Class;
                    olddetails.Flight_Charges = fd.Flight_Charges;
                    olddetails.Seats = fd.Seats;
                    db.SaveChanges();
                    MessageBox.Show("Record was updated");
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            db = new AirlineDBEntities();
            var to_remove = (Flight_Details)db.Flight_Details.Where(x => x.Id == id).FirstOrDefault();
            db.Flight_Details.Remove(to_remove);
            db.SaveChanges();
            UtilityClass.traverseControlsAndSetTextEmpty(this);
            MessageBox.Show("Flight Details Deleted Successfully");
        }
    }
}
