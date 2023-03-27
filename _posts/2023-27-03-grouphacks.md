---
toc: true
layout: base
description: Group Hacks
categories: [markdown, Week 20]
title: Group Hacks
---

# AWS Devolpment

### Basic Terms
- EC2: Amazon Web Services is a cloud computing platform that the PUSD district has provided for their students to serve our Web Application.
- GitHub: The leading open platform to share a code across the Internet.
Docker and docker-compose: Used to host a Web Application. A Docker container prepares an environment that contains the Web Application code and all the dependencies (requirements.txt for Python) Docker is an open platform for developing, shipping, and running applications.
- Nginx: In order to find a Web Application on a server, there needs to be a process that listens for the Web Application request and directs it to the Web Application service. Nginx is an open source software for web serving, reverse proxy, caching, load balancing, media streaming, and more.
- Certbot: Web traffic on internet is reliably served over Secure Hyper Text Transfer Protocol (https). Certbot is a free, open source software tool for automatically using Let’s Encrypt certifications.
- DNS: Natively, the web works off of IP addresses. Domain Name Services (DNS) allows the assignment of a friendly name to a Web Server. This name is built into Nginx/Certbot configuration files. Freenom is the cloud service described in this blog and has been used to register the nighthawkcodingsociety.com domain

###  Setting up the Server and Cloning the Project
- First connect to an Ubuntu EC2 instance on AWS and then begin the system and software setup.
- Once you get in the server, then you must start the upgrade, update, and delete process. Some commands include: sudo apt-get update, sudo apt-get upgrade
- Clone and Change Directory to project location. After all the update and upgrade commands are completed then clone the project in a single directory and change the directory to which the place is located
- After the flask server has been put in the server then check if it can run through various commands: python main.py
After running the command: "python main.py" It should say muliple stuff like "Debbuger Pin Activated" and a Link will show up