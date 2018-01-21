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
    public partial class Form_Search : Form
    {
        public Form_Search()
        {
            InitializeComponent();
        }

        void InitHeadTitle()
        {
            dataGridView1.Columns[0].HeaderText = "学号";
            dataGridView1.Columns[1].HeaderText = "姓名";
            dataGridView1.Columns[2].HeaderText = "性别";
            dataGridView1.Columns[3].HeaderText = "年龄";
            dataGridView1.Columns[4].HeaderText = "出生日期";
            dataGridView1.Columns[5].HeaderText = "手机";
            dataGridView1.Columns[6].HeaderText = "家庭地址";
            dataGridView1.Columns[7].HeaderText = "电子邮箱";
            dataGridView1.Columns[8].HeaderText = "专业";
        }

        private void btn_search_Click(object sender, EventArgs e)
        {
            if (cb_searchitem.Text == string.Empty)
            {
                dataGridView1.DataSource = function.GetAllStudentInfo();
                InitHeadTitle();
            }
            else
            {
                if (txt_searchtext.Text != string.Empty)
                {
                    StudentInfo studentsearch = new StudentInfo();
                    switch (cb_searchitem.SelectedIndex)
                    {
                        case 0:
                            studentsearch.StudentID = Int32.Parse(txt_searchtext.Text);
                            break;
                        case 1:
                            studentsearch.Name = txt_searchtext.Text;
                            break;
                    }
                    dataGridView1.DataSource = function.GetStudentInfoList(studentsearch);
                    InitHeadTitle();
                }
                else
                    MessageBox.Show("请输入要查询的" + cb_searchitem.Text);
            }
        }

        private void btn_close_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Form_Search_Load(object sender, EventArgs e)
        {

        }
    }
}
