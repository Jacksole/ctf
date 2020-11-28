# Machine IP
10.10.137.123

Starting Nmap 7.91 ( https://nmap.org ) at 2020-11-28 12:55 Eastern Standard Time
Nmap scan report for 10.10.137.123
Host is up (0.10s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    PHP cli server 5.5 or later (PHP 7.0.33-0ubuntu0.16.04.7)
|_http-title: Add Record Form
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=11/28%OT=80%CT=1%CU=42132%PV=Y%DS=4%DC=T%G=Y%TM=5FC28F
OS:30%P=i686-pc-windows-windows)SEQ(SP=104%GCD=1%ISR=10D%TI=Z%CI=I%II=I%TS=
OS:8)SEQ(CI=I%II=I)OPS(O1=M506ST11NW6%O2=M506ST11NW6%O3=M506NNT11NW6%O4=M50
OS:6ST11NW6%O5=M506ST11NW6%O6=M506ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%
OS:W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O=M506NNSNW6%CC=Y%Q=)T1(R=Y%DF=
OS:Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%
OS:F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y
OS:%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%R
OS:D=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)I
OS:E(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   42.00 ms  10.6.0.1
2   ... 3
4   113.00 ms 10.10.137.123

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.49 seconds
