Option Explicit

Sub ListAllFilesInFolder()
    Dim fso As Object    'File system object is used to work with files and folders
    Dim baseFolder As Object    'Main folder object for the folder(s) we are processing
    Dim ws As Worksheet    'I usually start macros from a BAT file, so just write details to this workbook for simplicity
    Dim startRow As Long    'Write details in correct row order
    
    On Error GoTo CleanUp    'If error go to cleanup procedure
    
    Dim basePath As String
    basePath = "C:\Desktop\Data\"    'Starting folder
    
    Set fso = CreateObject("Scripting.FileSystemObject")    'Get access to file system
    Set baseFolder = fso.GetFolder(basePath)    'Get folder object for base path
    
    Set ws = ThisWorkbook.Sheets("Sheet1")    'Reference point for first tab in this workbook
    
    With ws
        .Cells.Clear    'Clear everything from previous run before adding new details. Prevent creating massive file.
        .Range("A1").Value = "File Path"    'Column header names
        .Range("B1").Value = "File Name"
        .Range("C1").Value = "Size (bytes)"
        .Range("D1").Value = "File Type"
        .Range("E1").Value = "Last Modified"
        .Range("A1:E1").Font.Bold = True    'Make bold for readability.
        .Activate    'Bring excel sheet to active window object to freeze panes
        ActiveWindow.FreezePanes = .Range("A2")    'Freeze row 1
    End With
    
    Application.ScreenUpdating = False
    
    startRow = 2    'Write details after header row, don't overwrite headers
    Call ListSubFolders(baseFolder, ws, fso, startRow)
    
CleanUp:    'Cleanup procedure after script completes, or if encounting error.
    Application.ScreenUpdating = True    'Return excel back to normal state

    If Err.Number = 0 Then    'Check for error
        MsgBox "Finished listing files." & vbCrLf & _
               "Total files found: " & (startRow - 2), vbInformation, "Done"    'Success message, with file list count.
    Else
        MsgBox "An error occurred:" & vbCrLf & Err.Description, vbCritical, "Error"    'If error occured give error description.
    End If
End Sub    'Exit main sub


Private Sub ListSubFolders(folder As Object, ws As Worksheet, fso As Object, ByRef rowNum As Long)    'Recursive sub that actually does the work
    Dim fil As Object
    Dim subFolder As Object
    
    For Each fil In folder.Files
        ws.Cells(rowNum, 1).Value = fil.Path    'Full path
        ws.Cells(rowNum, 2).Value = fil.Name    'File name
        ws.Cells(rowNum, 3).Value = fil.Size    'File size in bytes
        ws.Cells(rowNum, 4).Value = fso.GetExtensionName(fil.Name)    'File type
        ws.Cells(rowNum, 5).Value = fil.DateLastModified    'Last modified date/time
        rowNum = rowNum + 1    'Always move to next row for next entry
    Next fil
    
    For Each subFolder In folder.SubFolders    'Go into every subfolder and repeat the process.
        ListSubFolders subFolder, ws, fso, rowNum
    Next subFolder
End Sub    'exit recursive sub
