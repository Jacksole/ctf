## HTTPS Overview

One of the major drawbacks of HTTP is that all data is transferred in clear text, meaning anyone between the source and destination can perform a Man-in-the-middle (MiTM) attack to view the transferred data. This is a major issue with banking and government websites, which contain sensitive user data.

This can be examined by using a network analyzer such as Wireshark. The following example demonstrates the effect of not enforcing secure communications between a web browser and a web application. If we attempt to log in to an insecure website while monitoring the network traffic using a graphical packet network protocol analyzer such as ![Wireshark](https://en.wikipedia.org/wiki/Wireshark), we can see that the login credentials can be intercepted in cleartext. This would make it easy for someone on the same network (such as a public wireless network) to capture them and use them for malicious purposes.

![https_clear](https://academy.hackthebox.eu/storage/modules/35/https_clear.png)

As seen below, an attacker who captures the network traffic would be able to view the entire login sequence, showing the login request (along with the supplied username and password) and the redirection to an administrative dashboard page after a successful login attempt.

![https_clear_convo](https://academy.hackthebox.eu/storage/modules/35/https_clear_convo.png)

These drawbacks gave rise to the ![HTTPS (HTTP Secure) protocol](https://tools.ietf.org/html/rfc2660). When this protocol is enabled, all communication between the client (user accessing a web application via their web browser), and the webserver that hosts the web application, is encrypted. When HTTPS is implemented on a web application, it becomes impossible for anyone to intercept and analyze the traffic and capture information such as credentials and other sensitive data.

Websites that enforce HTTPS can be identified through https:// in the ![URL]((https://en.wikipedia.org/wiki/URL)) (i.e., https://www.google.com) as well as the lock icon in the address bar of the web browser, to the left of the URL.

![https_google](https://academy.hackthebox.eu/storage/modules/35/https_google.png)

The default ![port](https://en.wikipedia.org/wiki/Port_(computer_networking)) for HTTPS is 443, which is preferred by browsers over HTTP port 80, provided there are no misconfigurations that allow a user to browse an insecure HTTP version of a website instead of the HTTPS version. Running Wireshark while browsing to https://google.com shows traffic passing over the network encrypted.

![https_google_enc](https://academy.hackthebox.eu/storage/modules/35/https_google_enc.png)

In the example above, we can see that all traffic when browsing to https://google.com is encrypted

**HTTPS Flow**
![https_flow](https://academy.hackthebox.eu/storage/modules/35/HTTPS_Flow.png)

Let's look at how HTTPS operates at a high level. Upon browsing to http://inlanefreight.com, the browser attempts to resolve the domain and redirects the user to the webserver hosting the target website. A request is sent to port 80 first, which is the unencrypted HTTP protocol. The server detects this and redirects the client to secure HTTPS port 443 instead. This is done via the 301 Moved Permanently response code. We will discuss the various types of response codes returned by an HTTP server later in this module.

Next, the client (web browser) sends a "client hello" packet, giving information about itself. After this, the server replies with "server hello", followed by a  ![key exchange](https://en.wikipedia.org/wiki/Key_exchange).The client verifies this key and sends one of its own. After this, an encrypted handshake is initiated to verify if the encryption and transfer are working properly.

Once the handshake completes successfully, normal HTTP communication is continued, which is encrypted thereafter. This is a very high-level overview of the ![key exchange](https://en.wikipedia.org/wiki/Key_exchange), which is beyond this module's scope.

Depending on the circumstances, an attacker may be able to perform an HTTP downgrade attack, which downgrades HTTPS communication to HTTP. This is done by setting up a ![man-in-the-middle (MITM)](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attack and proxying (passing) all traffic through the attacker's host without the user's knowledge. A successful downgrade attack would result in the cleartext transfer of HTTP data, which the attacker can log and later examine or manipulate for malicious purposes
