Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-21 21:13 Eastern Standard Time
Nmap scan report for 10.10.233.150
Host is up (0.17s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 8b:30:f7:77:fa:3b:c4:a1:01:82:95:5e:0f:d0:d5:e8 (RSA)
|   256 d1:e8:e6:ea:3c:4f:5e:81:d4:65:5f:41:dd:fa:65:82 (ECDSA)
|_  256 2c:33:ac:61:50:a5:76:d9:ee:8e:f8:2a:a2:25:a3:2e (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: The Naughty or Nice List
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=12/21%OT=22%CT=1%CU=36524%PV=Y%DS=4%DC=I%G=Y%TM=5FE156
OS:7D%P=i686-pc-windows-windows)SEQ(SP=103%GCD=1%ISR=10E%TI=Z%CI=Z%II=I%TS=
OS:A)SEQ(SP=103%GCD=1%ISR=10E%TI=Z%CI=Z%TS=C)SEQ(CI=Z%II=I)OPS(O1=M506ST11N
OS:W6%O2=M506ST11NW6%O3=M506NNT11NW6%O4=M506ST11NW6%O5=M506ST11NW6%O6=M506S
OS:T11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=4
OS:0%W=F507%O=M506NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(
OS:R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%
OS:W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=
OS:)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%
OS:UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.49 seconds
