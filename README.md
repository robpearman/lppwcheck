# lppwcheck
Check LastPass passwords against haveibeenpwned.com

## Background
Check whether any passwords contained in your LastPass vault are
present in haveibeenpwned.com

Note the shell script is Linux only; the python script is probably
executable on other platforms, but untested on anything other than
Linux

## Usage
Execute the shell script. This creates an in-memory filesystem
and prompts the user to save their exported vault here. It then
invoked the python script that checks the passwords against the 
haveibeenpwned API
