using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Xml.Linq;
using System.Windows.Forms;
using System.IO;

namespace phonebook
{
    public partial class Form_Main : Form
    {
        private static string _bp = AppDomain.CurrentDomain.SetupInformation.ApplicationBase;
        public Form_Main()
        {
            InitializeComponent();
            function.CreateStudentXml();
            initContracts();
        }

        /// <summary>
        /// 使DataGridView的列自适应宽度
        /// </summary>
        /// <param name="dgViewFiles"></param>
        private void AutoSizeColumn(DataGridView dgViewFiles)
        {
            int width = 0;
            //使列自使用宽度
            //对于DataGridView的每一个列都调整
            for (int i = 0; i < dgViewFiles.Columns.Count; i++)
            {
                //将每一列都调整为自动适应模式
                dgViewFiles.AutoResizeColumn(i, DataGridViewAutoSizeColumnMode.AllCells);
                //记录整个DataGridView的宽度
                width += dgViewFiles.Columns[i].Width;
            }
            //判断调整后的宽度与原来设定的宽度的关系，如果是调整后的宽度大于原来设定的宽度，
            //则将DataGridView的列自动调整模式设置为显示的列即可，
            //如果是小于原来设定的宽度，将模式改为填充。
            if (width > dgViewFiles.Size.Width)
            {
                dgViewFiles.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.DisplayedCells;
            }
            else
            {
                dgViewFiles.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;
            }
            //冻结某列 从左开始 0，1，2
            dgViewFiles.Columns[1].Frozen = true;
        }

        void initContracts()
        {
            if (File.Exists(AppDomain.CurrentDomain.SetupInformation.ApplicationBase + @"student.xml"))
            {
                dataGridView1.DataSource = function.GetAllStudentInfo();
            }
            else
            {
                function.CreateStudentXml();
                dataGridView1.DataSource = function.GetAllStudentInfo();
            }

            dataGridView1.Columns[0].HeaderText = "学号";
            dataGridView1.Columns[1].HeaderText = "姓名";
            dataGridView1.Columns[2].HeaderText = "性别";
            dataGridView1.Columns[3].HeaderText = "年龄";
            dataGridView1.Columns[4].HeaderText = "出生日期";
            dataGridView1.Columns[5].HeaderText = "手机";
            dataGridView1.Columns[6].HeaderText = "家庭地址";
            dataGridView1.Columns[7].HeaderText = "电子邮箱";
            dataGridView1.Columns[8].HeaderText = "专业";
            AutoSizeColumn(dataGridView1);
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            Form_Add formadd = new Form_Add();
            formadd.ShowDialog();
            initContracts();
        }

        private void buttonEdit_Click(object sender, EventArgs e)
        {
            if (dataGridView1.SelectedRows.Count == 1)
            {
                int selectrow = Int32.Parse(dataGridView1.Rows[dataGridView1.CurrentCell.RowIndex].Cells[0].Value.ToString());
                Form_Edit formedit = new Form_Edit();
                formedit.studentid_edit = selectrow;
                formedit.ShowDialog();
            }
            else
                MessageBox.Show("未选择!");
            initContracts();
        }

        private void buttonDelete_Click(object sender, EventArgs e)
        {
            if (dataGridView1.SelectedRows.Count == 1)
            {
                if (MessageBox.Show("确定要删除此学生信息", "确认信息", MessageBoxButtons.YesNo, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button2) == DialogResult.Yes)
                {
                    int selectrow = Int32.Parse(dataGridView1.Rows[dataGridView1.CurrentCell.RowIndex].Cells[0].Value.ToString());
                    if (function.DeleteStudentInfo(selectrow))
                        MessageBox.Show("删除学生信息成功!");
                    else
                        MessageBox.Show("删除学生信息失败，请检查是否选中学生信息!");
                    initContracts();
                }
                else
                    MessageBox.Show("未选择");

            }
        }

        private void buttonSearch_Click(object sender, EventArgs e)
        {
            Form_Search formsearch = new Form_Search();
            formsearch.ShowDialog();
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {

        }

        private void buttonBackup_Click(object sender, EventArgs e)
        {
            Stream myStream;
            SaveFileDialog savefiledialog1 = new SaveFileDialog();
            savefiledialog1.Filter = "xml file (*.xml)|*.xml";//设置文件格式
            savefiledialog1.FilterIndex = 2;//选择系统样式
            savefiledialog1.RestoreDirectory = true;
            if (savefiledialog1.ShowDialog() == DialogResult.OK)
            {
                if ((myStream = savefiledialog1.OpenFile()) != null)
                {
                    using (StreamWriter sw = new StreamWriter(myStream))
                    {
                        string str = File.ReadAllText(_bp + @"student.xml");
                        sw.Write(str);
                    }
                }
                myStream.Close();
                MessageBox.Show("备份成功!");
            }
        }

        private void buttonRedo_Click(object sender, EventArgs e)
        {
            string fName;
            OpenFileDialog openFileDialog=new OpenFileDialog();
            openFileDialog.InitialDirectory=AppDomain.CurrentDomain.SetupInformation.ApplicationBase;   
            openFileDialog.Filter="xml file (*.xml)|*.xml";;   
            openFileDialog.RestoreDirectory=true;  
            openFileDialog.FilterIndex=1;
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                fName = openFileDialog.FileName;
                List<StudentInfo> studentList = new List<StudentInfo>();
                XElement xml = XElement.Load(fName);
                var studentVar = xml.Descendants("student");
                studentList = (from student in studentVar
                               select new StudentInfo
                               {
                                   StudentID = Int32.Parse(student.Attribute("studentid").Value),
                                   Name = student.Element("name").Value,
                                   Age = Int32.Parse(student.Element("age").Value),
                                   Sex = student.Element("sex").Value,
                                   BirthDate = DateTime.Parse(student.Element("birthdate").Value),
                                   Phone = student.Element("phone").Value,
                                   HomeAddress = student.Element("homeaddress").Value,
                                   Email = student.Element("email").Value,
                                   Profession = student.Element("profession").Value
                               }).ToList();
                dataGridView1.DataSource = studentList;
                MessageBox.Show("恢复成功!");
            }
        }

        private void Form_Main_Load(object sender, EventArgs e)
        {

        }
    }
}
