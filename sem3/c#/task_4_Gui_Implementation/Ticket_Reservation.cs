using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace task_4_Gui_Implementation
{
    public partial class Ticket_Reservation : Form
    {
        AirlineDBEntities db;
        public Ticket_Reservation()
        {
            InitializeComponent();
            db = new AirlineDBEntities();
            BindSourceCombo();
            BindDestCombo();
        }

        private void BindDestCombo()
        {
            var items = db.Flight_Details.ToList();
            DestCombo.DataSource = items;
            DestCombo.DisplayMember = "Destination";
        }

        private void BindSourceCombo()
        {
            var items = db.Flight_Details.ToList();
            SourceCombo.DataSource = items;
            SourceCombo.DisplayMember = "Source";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(SourceCombo.Text != DestCombo.Text)
            {
                dataGridView1.DataSource = db.Flight_Details.Where(x => x.Source.Equals(SourceCombo.Text) && x.Destination.Equals(DestCombo.Text)).ToList();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (customeridtext.Text != String.Empty)
            {
                var id = Convert.ToInt32(customeridtext.Text);
                var item = db.Customer_Details.Where(x => x.Id == id).FirstOrDefault();
                if (item != null)
                {
                    customerfnametext.Text = item.FirstName;
                    customersnametext.Text = item.SurName;
                    birthdate.Value = (DateTime)item.BirthDate;
                    emailtext.Text = item.Email;
                    pnumbertext.Text = item.PhoneNumber;
                    addresstext.Text = item.Address;
                }
            }
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            var flightid = dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[0].Value;
            flightidtext.Text = flightid.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (!UtilityClass.TextBoxesAreNullorEmpty(this))
            {
                int flightid = Convert.ToInt32(flightidtext.Text);
                int seatno = Convert.ToInt32(seatnotext.Text);
                var flightbyid = db.Flight_Details.Where(x => x.Id == flightid).FirstOrDefault();
                if (flightbyid == null)
                {
                    MessageBox.Show("Invalid Flight id");
                }
                else if (seatno <= flightbyid.Seats)
                {
                    if (AvailibleSeat(flightid, seatno) == true)
                    {
                        Booking booking = new Booking();
                        booking.Customerid = Convert.ToInt32(customeridtext.Text);
                        booking.DateOfJourney = dateofjourney.Value;
                        booking.Flightid = flightid;
                        booking.Seatno = Convert.ToInt32(seatnotext.Text);
                        db.Booking.Add(booking);
                        db.SaveChanges();
                        MessageBox.Show("Added ticket");
                        UtilityClass.traverseControlsAndSetTextEmpty(this);
                    }
                    else
                    {
                        MessageBox.Show("Seat is already booked");
                    }
                }
                else
                {
                    MessageBox.Show("No seat with this number");
                }
            }
        }
        private bool AvailibleSeat(int flightid, int seatno)
        {
            var dateofdep = dateofjourney.Value;//.ToString("dd/MM/YYYY");
            var item = db.Booking.Where(x => x.Flightid == flightid && x.Seatno == seatno).FirstOrDefault();
            if (item != null)
            {
                var leavingdate = ((DateTime)item.DateOfJourney);//.ToString("dd/MM/YYYY");
                if (leavingdate < dateofdep)
                    return false;
                else
                    return true;
            }
            else
                return true;
        }
    }
}
