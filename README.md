# docker_webUI

### Steps to follow-
1. Download all the files in your rhel8 server.
2. Download httpd software using $yum install httpd -y
4. Save cgi-doc.py in /var/www/cgi-bin folder of httpd and save the remaining in /var/www/html. cgi-doc.py is our backend file and remaining are the frontend files.
5. Check your system's ip address using ifconfig. Use this ip address in index.html file instead of ip used to connect to servers ip.
6. Make cgi-doc.py file executable using $chmod 755 cgi-doc.py
7. Grant permission to apache group to execute commands in the server OS. Edit the file /etc/sudoers and add "apache ALL=(ALL) NOPASSWD:ALL" in line no 101 and save using :wq!
8. Start the httpd services using "$systemctl start httpd"  it can be made permanent using "$systemctl enable httpd" command
9. To disable selinux temporarily and stop the firewall, use the command "$setenforce 0" and "$systemctl stop firewalld" resp.
10. Now check the connectivity from the browser using the url format-"<protocol>://<ip>:<port>/index.html" EG- http://192.168.2.18/index.html
  
  Same server setup can be done in cloud services. Make sure to configure the security groups and ip address used in index.html. GIVE IT A TRY!!!
