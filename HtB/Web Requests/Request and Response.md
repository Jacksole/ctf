## Request and Response

Note: You can follow along by spawning the target at the end of this section.

### Setting up Burp Suite

Before we move further, let's look at how to set up ![Burp Suite](https://portswigger.net/burp). Burp Suite is a tool that acts as a ![proxy server](https://en.wikipedia.org/wiki/Proxy_server) and can be used to examine and modify HTTP requests. It provides a proxy that can route traffic from the browser through the proxy and view the various requests and responses between the client (web browser) and the webserver.

Start the target instance from the Questions section below. Next, open your workstation instance and then click on the Burp icon on the bottom bar.

![startup](https://academy.hackthebox.eu/storage/modules/35/image-20201105133409364.png)

Close any of the prompts and then click on Next > Start Project. Now open Firefox and click on the FoxyProxy extension on the URL bar. Choose Burp from the list; this is the Burp proxy, which our requests will be routed through

![burp_select](https://academy.hackthebox.eu/storage/modules/35/burp_select.png)

In Burp, click on the Proxy tab and ensure that the Intercept is on button is enabled. Click on Next in case the request box is populated already until it's empty

![burp_intercepton](https://academy.hackthebox.eu/storage/modules/35/burp_intercepton.png)

Switch to the browser and enter the target URL into the URL bar (http://206.189.25.23:30147 in this case).

![burp_intercepted](https://academy.hackthebox.eu/storage/modules/35/burp_intercepted.png)

After this, the request should be intercepted by Burp and appear as above. In order to intercept responses, click on Options and tick Intercept Server responses

![intercept_server](https://academy.hackthebox.eu/storage/modules/35/intercept_server.png)

Now go back to the Proxy tab and click on Forward to forward the server's request.

![burp_resp](https://academy.hackthebox.eu/storage/modules/35/burp_resp.png)

This should present us with the server response, as shown above. Click on Forward to forward this to the browser.

**HTTP Request**

Let's look at a raw HTTP request, as seen from Burp.

![raw_request](https://academy.hackthebox.eu/storage/modules/35/raw_request.png)

The image above shows an HTTP GET request to the URL:

* http://inlanefreight.com/users/login.html

The first line of an HTTP request contains three fields separated by spaces.

|  Field  |                                                    Description                                                    |
|:-------:|:-----------------------------------------------------------------------------------------------------------------:|
| Method  | The first field stands for the HTTP method or verb, which specifies the type of action to perform.                |
| Path    | The second field is the path to the resource being accessed. This field can also be suffixed with a query string. |
| Version | The third and final field is used to denote the HTTP version.                                                     |

The next set of lines contain HTTP header value pairs. These are used to specify various attributes of a request. The headers are terminated with a new line, which is necessary for the server to validate the request. This can be followed by the request body, which we will analyze in later sections of this module.

**HTTP Response**

Next, let's look at a raw HTTP response.

![raw_response](https://academy.hackthebox.eu/storage/modules/35/raw_response.png)

Similar to the request, an HTTP response contains headers as well. The first line contains two fields separated by spaces. The first being the HTTP version, while the second denotes the HTTP response code. Response codes are used to determine if a request succeeded or not. The response body is present after the headers, separated by a new line. The response body is usually defined as HTML code. However, it can also respond with other code types such as JSON, website resources such as images, style sheets or scripts, or even a document such as a PDF document hosted on the webserver.

