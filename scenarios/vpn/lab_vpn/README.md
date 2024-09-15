# lab_vpn

Before setting up an OpenVPN instance, we have to generate the certificates for CA/clients/server. We will use the certificates we have generated in `lab_vpn_pki`. The required files are stored in `/root/` of every node.

---

In this laboratory you have two PCs, a router and a server with a public ip. 

The PCs are in a LAN, with private addresses: the server cannot reach them directly. On the server, you can try to ping one of the pc (e.g. pc1):
```
ping 192.168.1.100
```
and you can observe no response. This is because the firewall on the router is dropping packets of new connections coming from the outside and directed towards the pc in the LAN.

However, it is also configured openvpn on both pc, using as openvpn server the node s1 itself. On the server, now you can try to reach pc1, but this time using the address provided by openvpn (check `ip addr` output on pc1):
```
ping 10.8.0.2
```
This time, you can see that you can observe response from the pc. The packets are sent by the openvpn network interface and are tunnelled using the existing openvpn connection.
