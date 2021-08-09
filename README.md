# ~rip~ ![icon.png](etc/icon.png)


// Rip Info:
Path=~/money/bd
File=~/.local/share/Rip/bd
DeletionDate=2019-08-07_21:37:08



BUILD & RUN:
g++ -Wall -o "cache/bin/%e" "%f"
cppcheck --language=c++ --enable=warning,style --template=gcc "%f"
"./cache/bin/%e"

