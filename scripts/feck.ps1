if ((Get-Command "feck").CommandType -eq "Function") {
	feck @args;
	[Console]::ResetColor()
	exit
}

"First time use of thefeck detected. "

if ((Get-Content $PROFILE -Raw -ErrorAction Ignore) -like "*thefeck*") {
} else {
	"  - Adding thefeck intialization to user `$PROFILE"
	$script = "`n`$env:PYTHONIOENCODING='utf-8' `niex `"`$(thefeck --alias)`"";
	Write-Output $script | Add-Content $PROFILE
}

"  - Adding feck() function to current session..."
$env:PYTHONIOENCODING='utf-8'
iex "$($(thefeck --alias).Replace("function feck", "function global:feck"))"

"  - Invoking feck()`n"
feck @args;
[Console]::ResetColor()
