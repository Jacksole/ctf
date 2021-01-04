# Machine IP = 10.10.233.15
## RustScan Results
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-31 07:05 Eastern Standard Time
Nmap scan report for 10.10.233.15
Host is up (0.12s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 6b:ea:74:4f:3b:9a:f5:c4:29:ed:98:5f:e4:57:0a:e5 (RSA)
|   256 bc:63:fd:d5:94:f0:fd:14:c2:2e:7f:7a:52:16:78:d3 (ECDSA)
|_  256 e6:1b:43:06:72:df:1d:5b:41:85:b5:b3:1d:d6:75:49 (ED25519)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          38743/tcp   status
|   100024  1          46796/udp   status
|   100024  1          49701/tcp6  status
|_  100024  1          51487/udp6  status
3000/tcp open  http    Node.js Express framework
| http-title: Arctic Forum | Login
|_Requested resource was /login
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=12/31%OT=22%CT=1%CU=30842%PV=Y%DS=4%DC=I%G=Y%TM=5FEDBE
OS:BB%P=i686-pc-windows-windows)SEQ(SP=106%GCD=1%ISR=108%TI=Z%CI=Z%TS=A)SEQ
OS:(SP=107%GCD=1%ISR=108%TI=Z%CI=Z%II=I%TS=A)SEQ(CI=Z%II=I)OPS(O1=M506ST11N
OS:W6%O2=M506ST11NW6%O3=M506NNT11NW6%O4=M506ST11NW6%O5=M506ST11NW6%O6=M506S
OS:T11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=F
OS:F%W=6903%O=M506NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=FF%S=O%A=S+%F=AS%RD=0%Q=)T2(
OS:R=N)T3(R=N)T4(R=Y%DF=Y%T=FF%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=FF%
OS:W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=FF%W=0%S=A%A=Z%F=R%O=%RD=0%Q=
OS:)T7(R=Y%DF=Y%T=FF%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=FF%IPL=164%
OS:UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=FF%CD=S)

Network Distance: 4 hops

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.94 seconds
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.233.15:3000
[+] Threads:        10
[+] Wordlist:       /opt/wordlist/dirbuster/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/12/31 07:09:15 Starting gobuster
===============================================================
/Admin (Status: 302)
/Home (Status: 302)
/Login (Status: 200)
/admin (Status: 302)
/assets (Status: 301)
/css (Status: 301)
/home (Status: 302)
/js (Status: 301)
/login (Status: 200)
/logout (Status: 302)
/sysadmin (Status: 200)
===============================================================
2020/12/31 07:09:41 Finished
===============================================================
