#!/usr/bin/env python

import time
import requests
import atexit

from com.vmware.nsx_vmc_app_client_for_vmc import create_nsx_vmc_app_client_for_vmc

def get_nsx_app_client(token, org_id, sddc_id):
  session = requests.Session()
  nsx_app_client = create_nsx_vmc_app_client_for_vmc(
      refresh_token=token,
      org_id=org_id,
      sddc_id=sddc_id,
      session=session
  )
  atexit.register(session.close)
  return nsx_app_client

def attach_vifs(vifs):
  #we will attach all available VIFs to SDDC.
  for vif in vifs:
    try:
      vifs.create(vif.id, "ATTACH")
      print("VIF id:{} is attached to this SDDC".format(vif.id))
    except Exception as e:
      print("Failed to attach VIF, {}".format(e.message))

def check_vif_status(vifs):
  #wait 3 minuites until attached VIF status will be available.
  wait_time = 3 * 60 
  start = time.time()
  elapsed_time = 0
  
  for vif in vifs:
    while elapsed_time < wait_time:
      vif_id = vif.id
      vif_state = vif.state
      
      if vif_state == "AVAILABLE":
        print("VIF of id:{} is available!".format(vif_id))
        break
      else:
        #sleep 10 secs
        time.sleep(10)
        elapsed_time = time.time() - start
        if elapsed_time >= wait_time:
          print("Timed out for waiting VIF of id:{} is available".format(vif_id))
          print("Please see VMC console if VIF is up later.")

def check_bgp_status(vifs):
  #wait 10 minuites until attached VIF BGP status will be up.
  wait_time = 10 * 60   
  start = time.time()
  elapsed_time = 0
  
  for vif in vifs:
    while elapsed_time < wait_time:
      vif_id = vif.id
      vif_bgp_state = vif.bgp_status
      
      if vif_bgp_state == "UP":
        print("VIF of id:{} BGP status is UP!".format(vif_id))
        break
      else:
        #sleep 10 secs
        time.sleep(10)
        elapsed_time = time.time() - start
        if elapsed_time >= wait_time:
          print("Timed out for waiting VIF of id:{} BGP is up".format(vif_id))
          print("Please see VMC console if VIF BGP is up later.")

def main():
  token = "VMC_Refresh_Token_xxxxxxx"
  org_id = "VMC Org ID"
  sddc_id = "VMC SDDC ID"

  nsx_app_client = get_nsx_app_client(
    token, 
    org_id, 
    sddc_id
  )
  
  vifs = nsx_app_client.infra.direct_connect.Vifs.list().results
  num_vfs = nsx_app_client.infra.direct_connect.Vifs.list().result_count
  
  if num_vfs > 0:
    attach_vifs(vifs)
    check_vif_status(vifs)
    check_bgp_status(vifs)
  else:
    print("There is no VIF to attach to this SDDC!")
  
if __name__ == '__main__':
  main()
