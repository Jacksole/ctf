IP='10.10.160.118'

## Nmap Scan Results

Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-31 05:23 Eastern Standard Time
Nmap scan report for 10.10.160.118
Host is up (0.12s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 e2:e3:15:c4:a4:38:99:92:1e:ad:8f:ac:0f:5b:e8:9d (RSA)
|   256 f2:47:9b:fb:66:f0:fb:95:da:72:d1:31:5e:d6:b8:13 (ECDSA)
|_  256 c7:37:d3:d8:2a:31:f1:67:c9:38:ae:a2:7e:8e:41:39 (ED25519)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          40591/udp   status
|   100024  1          42767/tcp   status
|   100024  1          49383/udp6  status
|_  100024  1          50401/tcp6  status
3000/tcp open  http    Node.js Express framework
| http-title: Christmas Inventory List | Login
|_Requested resource was /login
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=12/31%OT=22%CT=1%CU=44468%PV=Y%DS=4%DC=I%G=Y%TM=5FEDA6
OS:DB%P=i686-pc-windows-windows)SEQ(SP=104%GCD=1%ISR=108%TI=Z%CI=Z%II=I%TS=
OS:A)SEQ(CI=Z%II=I)OPS(O1=M506ST11NW6%O2=M506ST11NW6%O3=M506NNT11NW6%O4=M50
OS:6ST11NW6%O5=M506ST11NW6%O6=M506ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%
OS:W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=FF%W=6903%O=M506NNSNW6%CC=Y%Q=)T1(R=Y%DF=
OS:Y%T=FF%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=FF%W=0%S=A%A=Z%
OS:F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=FF%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y
OS:%T=FF%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=FF%W=0%S=Z%A=S+%F=AR%O=%R
OS:D=0%Q=)U1(R=Y%DF=N%T=FF%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)I
OS:E(R=Y%DFI=N%T=FF%CD=S)

Network Distance: 4 hops

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 53.84 seconds
