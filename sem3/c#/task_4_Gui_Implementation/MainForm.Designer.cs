
namespace task_4_Gui_Implementation
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.flightDetailsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.addNewFlightToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.customerToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.searchCustomerToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.searchCustomerToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.ticketDetailsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.bookTicketToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.searchFlightsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.flightDetailsToolStripMenuItem,
            this.customerToolStripMenuItem,
            this.ticketDetailsToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1465, 28);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // flightDetailsToolStripMenuItem
            // 
            this.flightDetailsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.addNewFlightToolStripMenuItem,
            this.searchFlightsToolStripMenuItem});
            this.flightDetailsToolStripMenuItem.Name = "flightDetailsToolStripMenuItem";
            this.flightDetailsToolStripMenuItem.Size = new System.Drawing.Size(108, 24);
            this.flightDetailsToolStripMenuItem.Text = "Flight Details";
            // 
            // addNewFlightToolStripMenuItem
            // 
            this.addNewFlightToolStripMenuItem.Name = "addNewFlightToolStripMenuItem";
            this.addNewFlightToolStripMenuItem.Size = new System.Drawing.Size(211, 24);
            this.addNewFlightToolStripMenuItem.Text = "Add New Flight Info";
            this.addNewFlightToolStripMenuItem.Click += new System.EventHandler(this.addNewFlightToolStripMenuItem_Click);
            // 
            // customerToolStripMenuItem
            // 
            this.customerToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.searchCustomerToolStripMenuItem,
            this.searchCustomerToolStripMenuItem1});
            this.customerToolStripMenuItem.Name = "customerToolStripMenuItem";
            this.customerToolStripMenuItem.Size = new System.Drawing.Size(134, 24);
            this.customerToolStripMenuItem.Text = "Customer Details";
            // 
            // searchCustomerToolStripMenuItem
            // 
            this.searchCustomerToolStripMenuItem.Name = "searchCustomerToolStripMenuItem";
            this.searchCustomerToolStripMenuItem.Size = new System.Drawing.Size(204, 24);
            this.searchCustomerToolStripMenuItem.Text = "Add new Customer";
            this.searchCustomerToolStripMenuItem.Click += new System.EventHandler(this.searchCustomerToolStripMenuItem_Click);
            // 
            // searchCustomerToolStripMenuItem1
            // 
            this.searchCustomerToolStripMenuItem1.Name = "searchCustomerToolStripMenuItem1";
            this.searchCustomerToolStripMenuItem1.Size = new System.Drawing.Size(204, 24);
            this.searchCustomerToolStripMenuItem1.Text = "Search Customer";
            this.searchCustomerToolStripMenuItem1.Click += new System.EventHandler(this.searchCustomerToolStripMenuItem1_Click);
            // 
            // ticketDetailsToolStripMenuItem
            // 
            this.ticketDetailsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.bookTicketToolStripMenuItem});
            this.ticketDetailsToolStripMenuItem.Name = "ticketDetailsToolStripMenuItem";
            this.ticketDetailsToolStripMenuItem.Size = new System.Drawing.Size(110, 24);
            this.ticketDetailsToolStripMenuItem.Text = "Ticket Details";
            // 
            // bookTicketToolStripMenuItem
            // 
            this.bookTicketToolStripMenuItem.Name = "bookTicketToolStripMenuItem";
            this.bookTicketToolStripMenuItem.Size = new System.Drawing.Size(155, 24);
            this.bookTicketToolStripMenuItem.Text = "Book Ticket";
            this.bookTicketToolStripMenuItem.Click += new System.EventHandler(this.bookTicketToolStripMenuItem_Click);
            // 
            // searchFlightsToolStripMenuItem
            // 
            this.searchFlightsToolStripMenuItem.Name = "searchFlightsToolStripMenuItem";
            this.searchFlightsToolStripMenuItem.Size = new System.Drawing.Size(211, 24);
            this.searchFlightsToolStripMenuItem.Text = "Search Flights";
            this.searchFlightsToolStripMenuItem.Click += new System.EventHandler(this.searchFlightsToolStripMenuItem_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1465, 828);
            this.Controls.Add(this.menuStrip1);
            this.IsMdiContainer = true;
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "MainForm";
            this.Text = "MainForm";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem flightDetailsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem addNewFlightToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem customerToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem searchCustomerToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem ticketDetailsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem bookTicketToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem searchCustomerToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem searchFlightsToolStripMenuItem;
    }
}