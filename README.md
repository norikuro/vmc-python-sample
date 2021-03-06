# vmc-python-sample
## Abstract
This is sample of how to implement python scripts to automate and manage VMware Cloud on AWS.  
Current sample is as followings,
- create SDDC on VMC
- add hosts to SDDC
- get Edge firewall rules
- attach AWS Direct Connect Private VIFs to SDDC  

This sample is using "VMware vSphere Automation SDK for Python" library.  
If you want to know detail of "VMware vSphere Automation SDK for Python", please see section of Reference below.
## How to use
### clone this git to your desktop
I'm testing these scrips on AWS EC2 (aws linux).  
And I can run fine these scripts with associated python libraries on aws linux.  
If you run other kind of environment, you might need some python libraries to run scripts successfully.
```cmd
# git clone https://github.com/norikuro/vmc-sample
```
### Set PYTHONPATH to be able to import librarys
```cmd
# cd vmc-sample
# export PYTHONPATH=${PWD}:$PYTHONPATH
```
### Run scripts
```cmd
# python vmcjp/create_sddc.py
```
## Reference
- VMware vSphere Automation SDK for Python  
  https://github.com/vmware/vsphere-automation-sdk-python
- VMC API Docs  
  com.vmware.nsx_vmc_app.infra.direct_connect_client.Vifs  
  https://vmware.github.io/vsphere-automation-sdk-python/nsx/nsx_vmc_aws_integration/com.vmware.nsx_vmc_app.infra.html
