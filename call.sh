#!/bin/bash
mkfifo /tmp/pipe; exec 3<>/tmp/pipe; (trap '' TTIN TTOU; twinkle -c) <&3 & printf '\ncall sip:'in06khattab@ekiga.net >&3

#printf %s\\n 'call sip:in06khattab@ekiga.net' | cat - /dev/tty |twinkle -c 
#printf %s\\n  'exit' |cat - /dev/tty
