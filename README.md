# vmc-sample
## Abstract
This is sample of how to implement python scripts to manage VMware Cloud on AWS.
Current sample is as followis,
- create SDDC on VMC
## How to use
### clone this git to your desktop
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
- VMC API Docs  
  com.vmware.nsx_vmc_app.infra.direct_connect_client.Vifs  
  https://vmware.github.io/vsphere-automation-sdk-python/nsx/nsx_vmc_aws_integration/com.vmware.nsx_vmc_app.infra.html
