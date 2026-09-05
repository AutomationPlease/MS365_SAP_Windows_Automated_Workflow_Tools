'This is a base watcher template module that can be used for automating multiple workflows.
'I try to keep the base watcher module pretty clean by calling in other modules after the watcher makes a detection, then performs a specific task like an SAP automation script.

Option Explicit

Const WATCHED_FOLDER As String = "X:\Shared_Data_Drive\"    'This is an example path using the trailing "\", I like to use shared drives so other people can run their data sets without needing to create their custom report manually.
Const CHECK_INTERVAL = "00:00:10"    'The timer stops while it is running a called module, but I like for the scanning to happen quickly but not nonstop, and not to slow making the automation take longer than neccissary

Dim NextCheckTime As Date

Public Sub StartWatchingFolder()    'Start control
    CheckFolderAndScheduleNext
End Sub

Private Sub CheckFolderAndScheduleNext()    'Start the actual watcher from within this sub to turn on watcher, open immediate window for confirmation
    Dim FileToProcess As String
    Debug.Print Now & " - Checking Folder..."
    FileToProcess = Dir(WATCHED_FOLDER & "*.xlsx")
    Do While FileToProcess <> ""
        If LCase(FileToProcess) <> "*.xlsm" Then
        Call ProcessSingleFile(WATCHED_FOLDER & FileToProcess)
        Exit Do
    End If
    FileToProcess = Dir()
    Loop
    NextCheckTime = Now + TimeValue(CHECK_INTERVAL)
    Application.OnTime NextCheckTime, "CheckFolderAndScheduleNext"
End Sub

'Stop control.
Public Sub StopWatchingFolder()    'I usually stop all Excel.exe instances to kill my watchers at the end of the day, but this sub can be used to stop the watcher after performing a specific task instead of continually running.
    On Error Resume Next
    Application.OnTime NextCheckTime, "CheckFolderAndScheduleNext", , False
End Sub

Private Sub ProcessSingleFile(ByVal OriginalPath As String)    'File processing, run hidden excel instance to help processing, and calling other modules
    Dim FolderPath As String
    Dim NewFullPath As String
    Dim NewFileName As String
    Dim wb As Workbook
    
    On Error GoTo CleanExit
    
    Application.EnableCancelKey = xlDisabled
    
    Application.DisplayAlerts = False
    Application.ScreenUpdating = False
    Application.EnableEvents = False
    Application.DisplayStatusBar = False
    Application.StatusBar = False
    Application.AskToUpdateLinks = False

    FolderPath = Left(OriginalPath, InStrRev(OriginalPath, "\"))

    Dim OutputFolder As String
    OutputFolder = "X:\Shared_Data_Drive\Output Flow\"    'I usually create an output flow folder, and depending upon the amount of processing happening I'll add in sub folder creation/organization logic, but just having a single folder usually is good enough.
    
    If Dir(OutputFolder, vbDirectory) = "" Then MkDir OutputFolder    'If output folder not found, then create one.
    
    NewFileName = "Processed_" & Format(Now, "yyyymmdd_hhmm") & "_" & Dir(OriginalPath)
    NewFullPath = OutputFolder & NewFileName
    
    Set wb = Workbooks.Open(fileName:=OriginalPath, ReadOnly:=False, UpdateLinks:=False)
    
    wb.Application.Visible = False    'Redundant disable display/visuals, helps with keeping true hidden while processing.


    'This is where I call all of my other modules that are saved within this workbook. You can add as many as you want, but remember to keep indexing logic in place while adding your call lines if the scripts are compounding and build into each other.
    'I don't find it neccissary to add any time delays inbetween scripts. This setup can handle running x number of scripts. I really haven't found a limit yet. I have one watcher that takes a single dataset and creates 20 different very large complex reports, so sky is the limit.
    Call Macro            
                        

    wb.Application.StatusBar = False    'More redundancy, helps with processing.
    wb.Application.Interactive = False

    wb.SaveAs fileName:=NewFullPath, FileFormat:=xlOpenXMLWorkbook    'Save new processed dataset(s).
    
    wb.Application.Interactive = True    'Allow excel to interact with itself so it can properly save.

    wb.Close SaveChanges:=False    'Close new saved workbook, don't repeat save to prevent random pop up messages.
    
    On Error Resume Next
    Kill OriginalPath    'Begin deleting original processed file by removing path from scripting memory, and deleting original dataset.
    On Error GoTo CleanExit    'If success go to clean exit cleanup procedure and skip error clearing block, if error continue to next block.

    If Err.Number <> 0 Then
        Debug.Print "Could not delete original (likely still open by user): " & OriginalPath    
        Err.Clear                                                                               
    End If

    'I've found the error culprit is usually from the shared watched folder and the file that's being processed for someone, that person kept the file open while at the same time dropping it in the folder.
    'So the processing worked, and the new file got created + saved to the output path, but because of this error (person probably had file open during processing) the original file remains in place in drop folder.
    'The watcher will continue on with other files in folder, or rescan the undeleted file and restart the script, so its not wrong. Just had user error causing duplicate runs.
    
    GoTo NormalExit    'Error or not, once all modules are completed, exit private sub and go to exit cleanup procedures.

CleanExit:    'Cleaning exit procedure back to main watcher module, to clear any possible application messages.
    Application.EnableCancelKey = xlInterrupt
    If Err.Number <> 0 Then
        MsgBox "Error " & Err.Number & vbCrLf & Err.Description & vbCrLf & _
                "File: " & OriginalPath, vbCritical, "Conversion Failed"
        Err.Clear
    End If

    On Error Resume Next
    If Not wb Is Nothing Then wb.Close SaveChanges:=False
    On Error GoTo 0

NormalExit:    'After error clearing, exit cleaning, now return excel workbook settings back to normal.
    Application.EnableCancelKey = xlInterrupt
    Application.DisplayAlerts = True
    Application.ScreenUpdating = True
    Application.EnableEvents = True
    Application.DisplayStatusBar = True
    Application.StatusBar = False
    
    Set wb = Nothing

End Sub    'After clean ups are complete, exit private sub and go back to main watcher module.
