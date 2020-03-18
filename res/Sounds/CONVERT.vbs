Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c CONVERT.bat"
oShell.Run strArgs, 0, false
Wscript.Quit