# Graylog Configuration Initial Brainstorming
Before starting to configuration Graylog, we conducted how we can orchestrate log collection with log server and Graylog server at the same time. 

# Graylog Server Configuration
For the graylog server we created seperate inputs for each of the network. Each of the networks configurations are as follows
**DMZ Network**
```
allow_override_date: true
bind_address: 0.0.0.0
expand_structured_data: false
force_rdns: false
number_worker_threads: 2
override_source: <empty>
port: 9000
recv_buffer_size: 262144
store_full_message: false
```

**External Client Network**
```
allow_override_date: true
bind_address: 0.0.0.0
expand_structured_data: false
force_rdns: false
number_worker_threads: 2
override_source: <empty>
port: 9000
recv_buffer_size: 262144
store_full_message: false
```

**Internal Client Network**
```
allow_override_date: true
bind_address: 0.0.0.0
expand_structured_data: false
force_rdns: false
number_worker_threads: 2
override_source: <empty>
port: 9000
recv_buffer_size: 262144
store_full_message: false
```

**Server Network**
```
allow_override_date: true
bind_address: 0.0.0.0
expand_structured_data: false
force_rdns: false
number_worker_threads: 2
override_source: <empty>
port: 9000
recv_buffer_size: 262144
store_full_message: false
```
# Client Configuration 
Once the the server is set we proceed to configure the necessary clients. These clients are as follows
- DMZ Network `100.100.6.0/24`
  - Proxy server 
  - Web server
- External Client Network `100.100.4.0/24`
  - Internal client
  - Fantastic coffe machine
- Client Network `100.100.2.0/24`
  - Kali
  - ARP Watch
- Servers Network `100.100.1.0/24`
  - DNS server
  - Log server
  
All of the above hosts of the ACME network have the same configurations which is as follows. Configurations are located in the same directory for all the clients which is `/etc/rsyslog.d/graylog.conf` 

```
$PreserveFQDN on
*.* 100.100.1.10:9000:RSYSLOGSyslogProtocol23Format
```

# Dashboard Configuration
Once we configured all the necessary clients and the server, we proceed to create a dashboard for the ACME network. We aim to capture specific traffic in the designated networks (DMZ, clients and server) such as 
- Targeted traffic 1
- Targeted traffic 2

