using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace phonebook
{
    public partial class Form_Edit : Form
    {
        public int studentid_edit = 0;
        public Form_Edit()
        {
            InitializeComponent();
        }

        public void initControl()
        {
            StudentInfo studentinfo = function.GetStudentInfo(studentid_edit);
            if (studentinfo != null)
            {
                txt_studengid.Text = studentinfo.StudentID.ToString();
                txt_name.Text = studentinfo.Name.ToString();
                if (studentinfo.Sex == "男")
                {
                    rd_man.Checked = true;
                    rd_woman.Checked = false;
                }
                else
                {
                    rd_man.Checked = false;
                    rd_woman.Checked = true;
                }
                txt_age.Text = studentinfo.Age.ToString();
                dt_birthdate.Text = studentinfo.BirthDate.ToString();
                txt_phone.Text = studentinfo.Phone.ToString();
                txt_email.Text = studentinfo.Email.ToString();
                txt_homeaddress.Text = studentinfo.HomeAddress.ToString();
                txt_profession.Text = studentinfo.Profession.ToString();

            }
        }

        private void Form_Edit_Load(object sender, EventArgs e)
        {
            initControl();
        }

        private void btn_update_Click(object sender, EventArgs e)
        {
            StudentInfo studentinfo = function.GetStudentInfo(studentid_edit);
            studentinfo.StudentID = Int32.Parse(txt_studengid.Text);
            studentinfo.Name = txt_name.Text;
            if (rd_man.Checked)
                studentinfo.Sex = "男";
            else
                studentinfo.Sex = "女";
            studentinfo.Age = Int32.Parse(txt_age.Text);
            studentinfo.BirthDate = DateTime.Parse(dt_birthdate.Text);
            studentinfo.Phone = txt_phone.Text;
            studentinfo.Email = txt_email.Text;
            studentinfo.HomeAddress = txt_homeaddress.Text;
            studentinfo.Profession = txt_profession.Text;
            if (function.UpdateStudentInfo(studentinfo))
                MessageBox.Show("修改成功");
                this.Close();
        }

        private void btn_close_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
