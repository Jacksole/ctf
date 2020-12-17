# Machine IP is 10.10.189.188 

## NMAP Results
```
Host discovery disabled (-Pn). All addresses will be marked 'up' and
scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org  ) at 2020-12-16 21:34 Eastern S
tandard Time
Nmap scan report for 10.10.189.188
Host is up (0.13s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE  VERSION
8000/tcp open  http-alt uvicorn
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.1 404 Not Found
|     date: Thu, 17 Dec 2020 02:34:29 GMT
|     server: uvicorn
|     content-length: 22
|     content-type: application/json
|     Connection: close
|     {"detail":"Not Found"}
|   GetRequest:
|     HTTP/1.1 200 OK
|     date: Thu, 17 Dec 2020 02:34:23 GMT
|     server: uvicorn
|     content-type: text/html; charset=utf-8
|     content-length: 6992
|     last-modified: Mon, 23 Nov 2020 00:31:30 GMT
|     etag: 43d617909830c0d0a48bbbe8ea26ae39
|     Connection: close
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <meta charset="utf-8">
|     <meta http-equiv="X-UA-Compatible" content="IE=edge">
|     <meta name="viewport" content="width=device-width, initial-scal
e=1">
|     <title>Santa's Tracker</title>
|     <link rel="shortcut icon" href="" type="image/x-icon">
|     <link rel="stylesheet" href="bulma.css">
|     <!-- Bulma Version 0.9.0-->
|     <link rel="stylesheet" type="text/css" href="../css/hero.css">
|     <!-- <link rel="stylesheet" href="https://unpkg.com/bulma-modal
-fx/dist/css/modal-fx.min.css" /> -->
|     </head>
|     <body>
|     <section class="hero is-info is-medium is-bold">
|   HTTPOptions:
|     HTTP/1.1 405 Method Not Allowed
|     date: Thu, 17 Dec 2020 02:34:34 GMT
|     server: uvicorn
|     content-length: 31
|     content-type: application/json
|     Connection: close
|_    {"detail":"Method Not Allowed"}
|_http-server-header: uvicorn
|_http-title: Santa's Tracker
1 service unrecognized despite returning data. If you know the servic
e/version, please submit the following fingerprint at https://nmap.or
g/cgi-bin/submit.cgi?new-service :
SF-Port8000-TCP:V=7.91%I=7%D=12/16%Time=5FDAC3B0%P=i686-pc-windows-wi
ndows
SF:%r(GetRequest,1C40,"HTTP/1\.1\x20200\x20OK\r\ndate:\x20Thu,\x2017\
x20De
SF:c\x202020\x2002:34:23\x20GMT\r\nserver:\x20uvicorn\r\ncontent-type
:\x20
SF:text/html;\x20charset=utf-8\r\ncontent-length:\x206992\r\nlast-mod
ified
SF::\x20Mon,\x2023\x20Nov\x202020\x2000:31:30\x20GMT\r\netag:\x2043d6
17909
SF:830c0d0a48bbbe8ea26ae39\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x
20htm
SF:l>\n<html>\n\x20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x
20<me
SF:ta\x20charset=\"utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x2
0http
SF:-equiv=\"X-UA-Compatible\"\x20content=\"IE=edge\">\n\x20\x20\x20\x
20\x2
SF:0\x20\x20\x20<meta\x20name=\"viewport\"\x20content=\"width=device-
width
SF:,\x20initial-scale=1\">\n\x20\x20\x20\x20\x20\x20\x20\x20<title>Sa
nta's
SF:\x20Tracker</title>\n\x20\x20\x20\x20\x20\x20\x20\x20<link\x20rel=
\"sho
SF:rtcut\x20icon\"\x20href=\"\"\x20type=\"image/x-icon\">\n\x20\x20\x
20\x2
SF:0\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"bulma\.css\
">\n\
SF:x20\x20\x20\x20\x20\x20\x20\x20<!--\x20Bulma\x20Version\x200\.9\.0
-->\n
SF:\x20\x20\x20\x20\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20typ
e=\"t
SF:ext/css\"\x20href=\"\.\./css/hero\.css\">\n\x20\x20\x20\x20\x20\x2
0\x20
SF:\x20\x20<!--\x20<link\x20rel=\"stylesheet\"\x20href=\"https://unpk
g\.co
SF:m/bulma-modal-fx/dist/css/modal-fx\.min\.css\"\x20/>\x20-->\n\x20\
x20\x
SF:20\x20</head>\n\x20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x2
0\x20
SF:<section\x20class=\"hero\x20is-info\x20is-medium\x20is-bold\">\n\x
20\x2
SF:0\x20\x20\x20\x20\x20\x20")%r(FourOhFourRequest,AD,"HTTP/1\.1\x204
04\x2
SF:0Not\x20Found\r\ndate:\x20Thu,\x2017\x20Dec\x202020\x2002:34:29\x2
0GMT\
SF:r\nserver:\x20uvicorn\r\ncontent-length:\x2022\r\ncontent-type:\x2
0appl
SF:ication/json\r\nConnection:\x20close\r\n\r\n{\"detail\":\"Not\x20F
ound\
SF:"}")%r(HTTPOptions,BF,"HTTP/1\.1\x20405\x20Method\x20Not\x20Allowe
d\r\n
SF:date:\x20Thu,\x2017\x20Dec\x202020\x2002:34:34\x20GMT\r\nserver:\x
20uvi
SF:corn\r\ncontent-length:\x2031\r\ncontent-type:\x20application/json
\r\nC
SF:onnection:\x20close\r\n\r\n{\"detail\":\"Method\x20Not\x20Allowed\
"}");
No exact OS matches for host (If you know what OS is running on it, s
ee https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=12/16%OT=8000%CT=1%CU=31387%PV=Y%DS=4%DC=I%G=Y%T
M=5FDA
OS:C451%P=i686-pc-windows-windows)SEQ(SP=105%GCD=1%ISR=10C%TI=Z%CI=Z%
II=I%T
OS:S=A)SEQ(CI=Z%II=I)SEQ(SP=104%GCD=1%ISR=10C%TI=Z%CI=Z%TS=A)OPS(O1=M
506ST1
OS:1NW6%O2=M506ST11NW6%O3=M506NNT11NW6%O4=M506ST11NW6%O5=M506ST11NW6%
O6=M50
OS:6ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%
DF=Y%T
OS:=40%W=F507%O=M506NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=
0%Q=)T
OS:2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF
=Y%T=4
OS:0%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=
%RD=0%
OS:Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%
IPL=16
OS:4%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops

OS and Service detection performed. Please report any incorrect resul
ts at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 181.41 seconds}")}")")
```
