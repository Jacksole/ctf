## Headers

HTTP headers provide an additional way to pass information between the client and the server. There are headers specific to requests and responses as well as general headers common to both. Headers can have one or multiple values appended after the header name and separated by a colon. There are many headers used for different purposes, which are divided into different categories:

1.  General Headers
2.  Entity Headers
3.  Request Headers
4.  Response Headers
5.  Security Headers

1. General Headers

These headers don't belong specifically to a request or a response. They are contextual and are used to describe the message rather than its contents.

|   Header   |                                                                                                                                                                                 Description                                                                                                                                                                                |
|:----------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Date       | The Date header holds the date and time at which the message originated. It's preferred to convert the time to the standard UTC time zone.                                                                                                                                                                                                                                 |
| Connection | The Connection header dictates if the current network  connection should stay alive after the request finishes. Two commonly  used values for this header are close and keep-alive. The close value from either the client or server means that they would like to terminate the connection, while the keep-alive header indicates that the connection should remain open. |

General Headers - Example

> Le Aundre@htb[/htb]$ curl -I -X GET https://www.inlanefreight.com

> <SNIP>
> Date: Sun, 06 Aug 2020 08:49:37 GMT
> Connection: keep-alive

This ![link](https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html) provides additional information on general headers.

2. Entity Headers

Similar to general headers, entity headers can be common to both the request and response. These headers are used to describe the content (entity) being transferred by a message. They are usually found in responses and POST or PUT requests (for example, a file upload).
