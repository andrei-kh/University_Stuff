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
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void addNewFlightToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Flight_info flightForm = new Flight_info();
            flightForm.MdiParent = this;
            flightForm.Show();
        }

        private void searchCustomerToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Customer_Form customerForm = new Customer_Form();
            customerForm.MdiParent = this;
            customerForm.Show();
        }

        private void searchCustomerToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            Search_Customer searchForm = new Search_Customer();
            searchForm.MdiParent = this;
            searchForm.Show();
        }

        private void bookTicketToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Ticket_Reservation ticketForm = new Ticket_Reservation();
            ticketForm.MdiParent = this;
            ticketForm.Show();
        }

        private void searchFlightsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Search_flight searchform = new Search_flight();
            searchform.MdiParent = this;
            searchform.Show();
        }
    }
}
