This lab presents a use case for local port forwarding.

---

The node "server" has an application running on TCP port 8080 blocking all requests coming from r1, and accepts all request coming from r2. You can launch a netcat listener on port 8080 on the server and try to connect it from pc1 (you should observe no response). If you instead try to connect to the server via pc2 it all works.

__How to connect to the server from pc1?__  --> We can setup a SSH local port forwarding on pc1, which tunnels the connection to pc2 which finally forwards it to the server.

(The lab already configures a user on pc2 with username "myuser" and password "password")

On pc1 try to launch:  `ssh -NL 9000:10.0.3.5:8080 myuser@10.0.2.100`
The above command:
1. Creates an SSH connection from pc1 to pc2 using the user "myuser".
2. Opens port 9000 on pc1. Whatever packet we send through that port it gets redirected towards the server on port 8080

Run a netcat listener on server on port 8080. Open a new terminal on pc1 and launch:  `nc localhost 9000` You can observe that now we are connecting to the server from pc1, using the tunnelled connection



