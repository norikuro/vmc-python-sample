#!/usr/bin/env python

import time
import requests
import atexit

from datetime import datetime
from pytz import timezone
from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from com.vmware.nsx_vmc_app_client_for_vmc import create_nsx_vmc_app_client_for_vmc

from vmcjp.config import Config
from vmcjp.utils.metadata import get_members
from vmcjp.network.security_groups import get_security_groups
from vmcjp.network.firewall_rules import get_firewall_rules
from vmcjp.network.vpns import get_l3vpns

def get_nsx_policy_client(token, org_id, sddc_id):
  session = requests.Session()
  nsx_policy_client = create_nsx_policy_client_for_vmc(
      refresh_token=token,
      org_id=org_id,
      sddc_id=sddc_id,
      session=session
  )
  atexit.register(session.close)
  return nsx_policy_client

def list_firewall_rules():
  network_config = [
      get_firewall_rules("mgw", self.nsx_policy_client),
      get_firewall_rules("cgw", self.nsx_policy_client)
  ]
    
def main():
  token = "VMC_Refresh_Token_xxxxxxx"
  org_id = "VMC Org ID"
  sddc_id = "VMC SDDC ID"

  nsx_policy_client = get_nsx_policy_client(
      token, 
      org_id, 
      sddc_id
  )
  list_firewall_rules()

if __name__ == '__main__':
  main()
