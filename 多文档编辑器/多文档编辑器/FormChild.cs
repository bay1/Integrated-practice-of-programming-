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
    public partial class FormChild : Form
    {
        FormChild file;
        public FormChild()
        {
            InitializeComponent();
        }
        public RichTextBox Sourse
        {
            get
            {
                return richTextBox;
            }
            set
            {
                richTextBox = value;
            }
        }

        private string _filePath = string.Empty;
        private int _index;

        public int GetFileTypeIndex()
        {
            return _index;
        }
        public void SetFileTypeIndex(int i)
        {
            _index = i;
        }


        public string GetFilePath()
        {
            return this._filePath;
        }
        public void SetFilePath(string value)
        {
            _filePath = value;
        }
        public FormChild(RichTextBoxStreamType fileType, string filePath,int i)
        {
            InitializeComponent();

            this.SetFilePath(filePath);
            this.richTextBox.LoadFile(filePath, fileType);
            this.SetFileTypeIndex(i);
        }

        //复制  
        public void 复制ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.richTextBox.Copy();
        }
        //粘贴  
        public void 粘贴ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.richTextBox.Paste();
        }
        //剪贴  
        public void 剪切ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.richTextBox.Cut();
        }

        //撤消 
        public void 撤销ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.richTextBox.Undo();
        }
        //删除
        public void 删除ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.richTextBox.SelectedText = "";
        } 

        private void FormChild_Load(object sender, EventArgs e)
        {
            this.file = (FormChild)FormMain.GetDocTrun();
        }
    }
}
