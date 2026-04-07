namespace Conditionals
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string name = "Quentin";
            int x = 3;
            x = x + 17;
            double d = Math.PI / 2;
            MessageBox.Show("name is " + name + "\nx is " + x + "\nd is " + d );
        }
    }
}
