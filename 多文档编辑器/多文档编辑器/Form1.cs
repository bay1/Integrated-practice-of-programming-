using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Printing;

namespace 多文档编辑器
{
    public partial class FormMain : Form
    {
        private static FormChild fileSend;
        private RichTextBoxStreamType oldFile;
        private FormChild file;
        List<FormChild> listFormChild = new List<FormChild>();
        private int fileCount = 0;
        private string fileName = string.Empty;
        private string filePath = string.Empty;

        private int childFormCount = 0;// 用来记录子窗口的数量
        public int ChildFormCount
        {
            get
            {
                return childFormCount;
            }
            set
            {
                childFormCount = value;
            }
        }
        public FormMain()
        {
            InitializeComponent();
        }

        public static FormChild GetDocTrun()
        {
            return fileSend;
        }

        private void 自动换行WToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                if (自动换行WToolStripMenuItem.CheckState == CheckState.Checked)
                {
                    自动换行WToolStripMenuItem.CheckState = CheckState.Unchecked;
                    FormChild df = (FormChild)this.ActiveMdiChild;
                    df.Sourse.WordWrap = false;
                }
                else
                {
                    自动换行WToolStripMenuItem.CheckState = CheckState.Checked;
                    FormChild df = (FormChild)this.ActiveMdiChild;
                    df.Sourse.WordWrap = true;
                }
            }
            catch (Exception ex)
            {
                return;
            }
        }
        private void 字体ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                if (fontDialog.ShowDialog() == DialogResult.OK && file != null)
                {
                    FormChild df = (FormChild)this.ActiveMdiChild;
                    df.Sourse.SelectionFont = fontDialog.Font;
                }
            }
            catch (Exception ex)
            {
                return;
            }
        }
        private void 颜色CToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                if (colorDialog.ShowDialog() == DialogResult.OK && file != null)
                {
                    FormChild df = (FormChild)this.ActiveMdiChild;
                    df.Sourse.SelectionColor = colorDialog.Color;
                }
            }
            catch (Exception ex)
            {
                return;
            }
        }
        private void 时间日期ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                FormChild df = (FormChild)this.ActiveMdiChild;
                Clipboard.SetText(DateTime.Now.ToString());
                df.Sourse.Paste();
            }
            catch (Exception ex)
            {
                return;
            }
        }

        private void 全选CtrlAToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                FormChild df = (FormChild)this.ActiveMdiChild;
                df.Sourse.SelectAll();
            }
            catch (Exception ex)
            {
                return;
            }
        }
        private void 页面设置ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            pageSetupDialog.Document = new PrintDocument();

            this.pageSetupDialog.AllowMargins = true;
            this.pageSetupDialog.AllowOrientation = true;
            this.pageSetupDialog.AllowPaper = true;
            this.pageSetupDialog.AllowPrinter = true;

            this.pageSetupDialog.ShowDialog();
        }
        private void 保存SCtrlSToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FormChild df = (FormChild)this.ActiveMdiChild;
            try
            {
                if (df.GetFilePath() == "")
                {
                    SaveFile(df);
                    MessageBox.Show("保存成功", "温馨提示");
                }
                else
                {
                    RichTextBoxStreamType fileType = TrunFileType(df.GetFileTypeIndex());
                    df.Sourse.SaveFile(df.GetFilePath(), fileType);
                    MessageBox.Show("保存成功", "温馨提示");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("保存失败，请重新保存！", "温馨提示");
            }
        }
        private void 打开OCtrlOToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    RichTextBoxStreamType fileType = TrunFileType(openFileDialog.FilterIndex);
                    fileCount++;
                    file = new FormChild(fileType, openFileDialog.FileName, openFileDialog.FilterIndex);
                    file.MdiParent = this;
                    file.Show();
                    listFormChild.Add(file);
                }
            }
            catch (Exception ex)
            {
                return;
            }

            string str = openFileDialog.FileName;
            string[] sArray = str.Split('\\');
            file.Text = sArray[sArray.Length - 1];

            file.WindowState = FormWindowState.Maximized;
        }
        private void 新建NCtrlNToolStripMenuItem_Click(object sender, EventArgs e)
        {
            file = new FormChild();//新建一个子窗体
            file.MdiParent = this; //定义此窗体的父窗体，使之成为MDI窗体
            ++ChildFormCount;
            file.Text = "子窗体" + ChildFormCount.ToString();
            file.Show();
        }
        private void 窗口层叠ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.LayoutMdi(MdiLayout.Cascade);
        }
        private void 水平平铺ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.LayoutMdi(MdiLayout.TileHorizontal);
        }
        private void 垂直平铺ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.LayoutMdi(MdiLayout.TileVertical);
        }

        private void 退出ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {

        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {

        }

        private void 关于ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("                       八一\n\n      http://blog.flywinky.top");
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void 打印ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PrintDialog pd = new PrintDialog();
            pd.ShowDialog();
        }

        private void 查找ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            fileSend = (FormChild)this.ActiveMdiChild;
            FormFind find = new FormFind();
            find.Show();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void 另存为ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FormChild df = (FormChild)this.ActiveMdiChild;
            try
            {
                SaveFile(df);
                filePath = df.GetFilePath();
                MessageBox.Show("保存成功", "温馨提示");
            }
            catch (Exception ex)
            {
                return;
            }
        }
        public RichTextBoxStreamType TrunFileType(int i)   //数据转换
        {
            RichTextBoxStreamType fileType;
            switch (i)
            {
                case 1: fileType = RichTextBoxStreamType.PlainText;
                    break;
                case 2: fileType = RichTextBoxStreamType.RichText;
                    break;
                default: fileType = RichTextBoxStreamType.UnicodePlainText;
                    break;
            }
            return fileType;
        }
        public void SaveFile(FormChild df)                    //保存文件
        {
            SaveFileDialog sfd = new SaveFileDialog();
            sfd.Filter = "文本文件（*.txt）|*.txt|RTF文件|*.rtf|所有文件（*.*）|*.*";

            if (sfd.ShowDialog() == DialogResult.OK)
            {
                RichTextBoxStreamType fileType = TrunFileType(sfd.FilterIndex);
                file.SetFileTypeIndex(sfd.FilterIndex);
                file.SetFilePath(saveFileDialog.InitialDirectory);
                df.Sourse.SaveFile(sfd.FileName, fileType);

                df.SetFilePath(sfd.FileName);
                oldFile = fileType;
            }
            string str = df.GetFilePath();

            string[] sArray = str.Split('\\');
            fileName = sArray[sArray.Length - 1];

            for (int i = 0; i < sArray.Length - 1; i++)
            {
                filePath += sArray[i];
            }
        }

    }
}
