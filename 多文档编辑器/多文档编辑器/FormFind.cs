using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 多文档编辑器
{
    public partial class FormFind : Form
    {
        FormChild file;
        private static int index = 0;
        private static int count = 0;
        public FormFind()
        {
            InitializeComponent();
        }

        private void buttonFindNext_Click(object sender, EventArgs e)
        {
            string str = Convert.ToString(textBoxFind.Text);
            try
            {
                if (file.Sourse.Text.Contains(str))
                {
                    index = file.Sourse.Find(str, index, RichTextBoxFinds.None);
                    file.Sourse.Select(index, str.Length);
                    file.Sourse.Focus();
                    index++;
                }
            }
            catch (Exception ex)
            {
                if (index == -1)
                {
                    index = 0;
                }
            }
        }

        private void buttonReplace_Click(object sender, EventArgs e)
        {
            string strOld = Convert.ToString(textBoxFind.Text);
            string strNew = Convert.ToString(textBoxReplace.Text);
            string str = Convert.ToString(textBoxFind.Text);

            try
            {
                if (file.Sourse.Text.Contains(strOld))
                {
                    Clipboard.Clear();
                    count = file.Sourse.Find(strOld, index, RichTextBoxFinds.None);
                    file.Sourse.Select(count, str.Length);
                    Clipboard.SetText(file.Sourse.SelectedText.Replace(strOld, strNew));
                    file.Sourse.Paste();
                    count++;
                }
                else
                    return;
            }
            catch (Exception ex)
            {
                return;
            }
        }

        private void buttonCancle_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void buttonAllReplace_Click(object sender, EventArgs e)
        {
            string strOld = Convert.ToString(textBoxFind.Text);
            string strNew = Convert.ToString(textBoxReplace.Text);

            try
            {
                if (file.Sourse.Text.Contains(strOld))
                {
                    file.Sourse.Text = file.Sourse.Text.Replace(strOld, strNew);
                }
            }
            catch (Exception ex)
            {
                return;
            }
        }

        private void FormFind_Load(object sender, EventArgs e)
        {
            this.file = FormMain.GetDocTrun();
        }
    }
}
