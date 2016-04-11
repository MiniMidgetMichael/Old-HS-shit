Public Class frmConverter
    'Michael Farwell
    '3rd Period
    '06-15-16
    '∏ + 1 Day!

    Private Sub frmConverter_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub cmdQuit_Click(sender As Object, e As EventArgs) Handles cmdQuit.Click
        End
    End Sub

    Private Sub cmdConvert_Click(sender As Object, e As EventArgs) Handles cmdConvert.Click
        Dim hexNum As Integer
        Dim binNum As Integer
        Dim decNum As Integer
        Dim goodHexValue As Boolean = Integer.TryParse(txtHex.Text, hexNum)
        Dim goodBinValue As Boolean = Integer.TryParse(txtBin.Text, binNum)
        Dim goodDecValue As Boolean = Integer.TryParse(txtDec.Text, decNum)
        Dim convHex As Boolean = False
        Dim convBin As Boolean = False
        Dim convDec As Boolean = False
        Dim hexList As Array = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"}
        Dim binList As Array = {0, 1}

        If Not (goodHexValue) And Not (txtHex.Text.Equals("")) Then
            MsgBox(txtHex.Text + " is not a valid integer")
            txtHex.Focus()
            txtHex.SelectAll()
        ElseIf Not (goodBinValue) And Not (txtBin.Text.Equals("")) Then
            MsgBox(txtBin.Text + " is not a valid integer")
            txtBin.Focus()
            txtBin.SelectAll()
        ElseIf Not (goodDecValue) And Not (txtDec.Text.Equals("")) Then
            MsgBox(txtDec.Text + " is not a valid integer")
            txtDec.Focus()
            txtDec.SelectAll()
        End If

        If Not (txtHex.Text.Equals("")) Then
            convHex = True
        ElseIf Not (txtBin.Text.Equals("")) Then
            convBin = True
        ElseIf Not (txtDec.Text.Equals("")) Then
            convDec = True
        Else
            MsgBox("Please give a value to convert")
        End If

        If convDec = True Then
            txtHex.Text = convert(decNum, "dec")
        End If
    End Sub

    Private Function convert(ByRef num As Integer, ByRef type As String)
        Dim hexValue As String
        Dim binValue As Array = {0, 0, 0, 0, 0, 0, 0, 0}
        Dim decValue As String
        Dim hexList As Array = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"}
        Dim hexPairs As Array = {0}
        Dim binList As Array = {0, 1}
        Dim place As Integer = 0
        Dim endValue As String = ""
        If type = "dec" Then
            If (num > 255) Then
                Do Until (num < 255)
                    hexPairs.SetValue(((num \ 16) + (num Mod 16)).ToString(), place)
                    place += 1
                Loop
            End If
            For Each item In hexPairs
                endValue += item.ToString()
            Next
            Return endValue
        ElseIf type.Equals("bin") Then

        End If
    End Function
End Class
