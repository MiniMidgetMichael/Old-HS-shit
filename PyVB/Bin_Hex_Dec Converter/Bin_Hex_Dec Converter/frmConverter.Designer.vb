<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frmConverter
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.cmdConvert = New System.Windows.Forms.Button()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.txtBin = New System.Windows.Forms.TextBox()
        Me.txtHex = New System.Windows.Forms.TextBox()
        Me.txtDec = New System.Windows.Forms.TextBox()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.cmdQuit = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'cmdConvert
        '
        Me.cmdConvert.Location = New System.Drawing.Point(33, 251)
        Me.cmdConvert.Name = "cmdConvert"
        Me.cmdConvert.Size = New System.Drawing.Size(75, 23)
        Me.cmdConvert.TabIndex = 3
        Me.cmdConvert.Text = "&Convert"
        Me.cmdConvert.UseVisualStyleBackColor = True
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(30, 102)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(36, 13)
        Me.Label1.TabIndex = 4
        Me.Label1.Text = "Binary"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(206, 102)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(68, 13)
        Me.Label2.TabIndex = 5
        Me.Label2.Text = "Hexadecimal"
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(414, 102)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(45, 13)
        Me.Label3.TabIndex = 6
        Me.Label3.Text = "Decimal"
        '
        'txtBin
        '
        Me.txtBin.Location = New System.Drawing.Point(33, 155)
        Me.txtBin.Name = "txtBin"
        Me.txtBin.Size = New System.Drawing.Size(100, 20)
        Me.txtBin.TabIndex = 0
        '
        'txtHex
        '
        Me.txtHex.Location = New System.Drawing.Point(209, 155)
        Me.txtHex.Name = "txtHex"
        Me.txtHex.Size = New System.Drawing.Size(100, 20)
        Me.txtHex.TabIndex = 1
        '
        'txtDec
        '
        Me.txtDec.Location = New System.Drawing.Point(417, 155)
        Me.txtDec.Name = "txtDec"
        Me.txtDec.Size = New System.Drawing.Size(100, 20)
        Me.txtDec.TabIndex = 2
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Font = New System.Drawing.Font("Microsoft Sans Serif", 18.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label4.Location = New System.Drawing.Point(28, 9)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(172, 29)
        Me.Label4.TabIndex = 7
        Me.Label4.Text = "Enter a value:"
        '
        'cmdQuit
        '
        Me.cmdQuit.Location = New System.Drawing.Point(417, 251)
        Me.cmdQuit.Name = "cmdQuit"
        Me.cmdQuit.Size = New System.Drawing.Size(75, 23)
        Me.cmdQuit.TabIndex = 8
        Me.cmdQuit.Text = "E&xit"
        Me.cmdQuit.UseVisualStyleBackColor = True
        '
        'frmConverter
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(697, 319)
        Me.Controls.Add(Me.cmdQuit)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.txtDec)
        Me.Controls.Add(Me.txtHex)
        Me.Controls.Add(Me.txtBin)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.cmdConvert)
        Me.Name = "frmConverter"
        Me.Text = "Hex - Binary - Decimal"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents cmdConvert As System.Windows.Forms.Button
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents txtBin As System.Windows.Forms.TextBox
    Friend WithEvents txtHex As System.Windows.Forms.TextBox
    Friend WithEvents txtDec As System.Windows.Forms.TextBox
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents cmdQuit As System.Windows.Forms.Button

End Class
