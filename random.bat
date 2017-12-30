:: Name: random.bat
::
:: Purpose: Generate a random integer between 0 and 32767. You can also pass
:: one parameter to set the maximum random number possible, or two parameters
:: to set the range of the random number.
::
:: Usage :
:: random.bat
:: random.bat <MAX_EXCLUSIVE>
:: random.bat <MIN_INCLUSIVE> <MAX_EXCLUSIVE>
::
:: Author: BIZZOZZERO Nicolas


@ECHO off

SETLOCAL

IF "%1" == "" GOTO :args_0
IF "%2" == "" GOTO :args_1
IF "%3" == "" GOTO :args_2
echo Error, two many parameters
GOTO :end

:args_0
    ECHO %RANDOM%
    GOTO :end

:args_1
    SET /A RESULT = %RANDOM% %% %1
    ECHO %RESULT%
    GOTO :end

:args_2
    SET /A RESULT = %RANDOM% %% (%2 - 1) + %1
    ECHO %RESULT%
    GOTO :end

:end
