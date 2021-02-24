using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace task_4_Gui_Implementation
{
    public partial class Customer_Form : Form
    {
        AirlineDBEntities db;
        static int id = 0;
        public Customer_Form([Optional] int ? Id)
        {
            InitializeComponent();
            if(Id != null)
            {
                button1.Text = "Update";
                button2.Visible = true;
                db = new AirlineDBEntities();
                Customer_Details customer = db.Customer_Details.Where(x => x.Id == Id).FirstOrDefault();
                id = customer.Id;
                fnametext.Text = customer.FirstName;
                snametext.Text = customer.SurName;
                birthdate.Value = (DateTime)customer.BirthDate;
                emailtext.Text = customer.Email;
                phonetext.Text = customer.PhoneNumber;
                addresstext.Text = customer.Address;
            }
            else
            {
                button1.Text = "Save";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (UtilityClass.TextBoxesAreNullorEmpty(this))
                return;
            db = new AirlineDBEntities();
            Customer_Details customer = new Customer_Details
            {
                FirstName = fnametext.Text,
                SurName = snametext.Text,
                BirthDate = birthdate.Value,
                Email = emailtext.Text,
                PhoneNumber = phonetext.Text,
                Address = addresstext.Text
            };
            if (button1.Text == "Save")
            {
                db.Customer_Details.Add(customer);
                db.SaveChanges();
                UtilityClass.traverseControlsAndSetTextEmpty(this);
                MessageBox.Show("Successfully added a customer");
            }
            else
            {
                Customer_Details oldcustomer = db.Customer_Details.Where(x => x.Id == id).FirstOrDefault();
                oldcustomer.FirstName = customer.FirstName;
                oldcustomer.SurName = customer.SurName;
                oldcustomer.BirthDate = customer.BirthDate;
                oldcustomer.Email = customer.Email;
                oldcustomer.PhoneNumber = customer.PhoneNumber;
                oldcustomer.Address = customer.Address;
                db.SaveChanges();
                MessageBox.Show("Record was updated");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            db = new AirlineDBEntities();
            var to_remove = (Customer_Details)db.Customer_Details.Where(x => x.Id == id).FirstOrDefault();
            db.Customer_Details.Remove(to_remove);
            db.SaveChanges();
            UtilityClass.traverseControlsAndSetTextEmpty(this);
            MessageBox.Show("Flight Details Deleted Successfully");
        }
    }
}
