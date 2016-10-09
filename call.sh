#!/bin/bash
mkfifo /tmp/pipe; exec 3<>/tmp/pipe; (trap '' TTIN TTOU; twinkle -c) <&3 & printf '\ncall sip:'timvansteenbergen@ekiga.net >&3

printf %s\\n 'call sip:timvansteenbergen@ekiga.net' | cat - /dev/tty |twinkle -c
printf %s\\n  'exit' |cat - /dev/tty
