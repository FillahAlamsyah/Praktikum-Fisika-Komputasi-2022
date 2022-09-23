Attribute VB_Name = "Module1"
Private Sub SimulasiGLBB()
 Range("B5").Value = 0  '0
  While Range("B5").Value < 30
  Range("B5").Value = Range("B5").Value + 0.01
  DoEvents
 Wend
End Sub
Sub Reset()
 Range("B5").Value = 0  '0
End Sub
