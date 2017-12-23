''' <summary>
''' Open a window with a custom message in it.
''' </summary>
''' <param name="message">The message which will be included in the window.</param>

Set objArgs = WScript.Arguments
messageText = objArgs(0)
msgBox messageText
