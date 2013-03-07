set PATH=%PATH%;"C:\Program Files\Microsoft SDKs\Windows\v6.1\Bin"
rem make zc.buildout happy:
set PYTHON24=c:\Python24_32_clean\python.exe
set PYTHON26=c:\Python26_32_clean\python.exe
set PYTHON25=c:\Python25_32_clean\python.exe
call "C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\VCVARSALL.bat" x86
%*