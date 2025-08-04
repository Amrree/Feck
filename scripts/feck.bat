@set PYTHONIOENCODING=utf-8
@powershell -noprofile -c "cmd /c \"$(thefeck %* $(doskey /history)[-2])\"; [Console]::ResetColor();"
