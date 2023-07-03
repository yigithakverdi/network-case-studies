# Graylog Server Configuration
For receving the logs we created Syslog UDP input with 6 agents on port 9000, configuration of the input is shown below 

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

Once we configured the clients and the server we immideately started to receive logs from the clients. Some of the logs received are shown below in the CSV format that we obtained from the Graylog dashboard

```
"2023-07-01T15:05:01.000Z","kali","kali CRON[34694]: pam_unix(cron:session): session closed for user root"
"2023-07-01T15:05:01.000Z","kali","kali CRON[34699]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)"
"2023-07-01T15:05:01.000Z","kali","kali CRON[34694]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)"
"2023-07-01T15:09:01.000Z","kali","kali systemd[1]: Finished Clean php session files."
"2023-07-01T15:09:01.000Z","kali","kali systemd[1]: phpsessionclean.service: Deactivated successfully."
"2023-07-01T15:09:01.000Z","kali","kali systemd[1]: Starting Clean php session files..."
"2023-07-01T15:09:01.000Z","kali","kali CRON[35658]: pam_unix(cron:session): session closed for user root"
"2023-07-01T15:09:01.000Z","kali","kali CRON[35659]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)"
"2023-07-01T15:09:01.000Z","kali","kali CRON[35658]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)"
"2023-07-01T15:10:37.000Z","kali","kali spice-vdagentd: closed vdagent virtio channel"
"2023-07-01T15:10:37.000Z","kali","kali spice-vdagentd: Error getting active session: No data available"
"2023-07-01T15:10:37.000Z","kali","kali spice-vdagentd: Error getting active session: No data available"
```

# Client Configuration 
Once the the server is set we proceed to configure the necessary client, for testing if we receive logs or not. We configured Kali machine with the IP address `100.100.2.100` on Clients Network as follows. Configurations are located in the same directory for all the clients which is `/etc/rsyslog.d/graylog.conf` 


```
$PreserveFQDN on
*.* 100.100.1.10:9000;RSYSLOG_SyslogProtocol23Format
```

# Dashboard Configuration
Once we configured all the necessary clients and the server, we proceed to create a meaningful dashboard for the ACME network. We aim to create dashboards that will tell us if something going on wrong in the network and is there any system failures. Below are the dashboards and pages with graphs and tables included in them

## DMZ Activity
This dashboard shows specifically DMZ acitivity, we included possible actions that could hint us malicious behaviour such as login activity and HTTP activity since we have a proxy and a web server there. For each of the contexts we created seperate pages as can be seen on the below images

![DMZ Activity](assets/../../../asset/dmz_login_activity_dashboard.png)

For capturing the login activities in DMZ, in the message table we configured to query with the following command

```
gl2_source_input:64a01c3e5e787f72d5e6934a, source:webserver.acme-22.test, application_name:"login", source:proxyserver.acme-22.test
``` 
And as can be seen from the figure we have two different pie, first pie charts counts the login activities and groups them by the source hence we will get a good understanding on how much these devices are used. For obtaining such information we applied following query. 
```
gl2_source_input:64a01c3e5e787f72d5e6934a, source:webserver.acme-22.test, application_name:"login", source:proxyserver.acme-22.test
```
Second pie chart groups the failured authenticaiton hence if we have a brute-force attack or unusual behaviour we will be able to see it. To collect such information we applied following query
```
gl2_source_input:64a01c3e5e787f72d5e6934a, source:webserver.acme-22.test, application_name:"login", source:proxyserver.acme-22.test, message:"authentication failure"
```


# Notification Configuration

