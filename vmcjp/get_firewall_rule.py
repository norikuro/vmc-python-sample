#!/usr/bin/env python

import requests
import atexit
import json

from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from com.vmware.nsx_vmc_app_client_for_vmc import create_nsx_vmc_app_client_for_vmc

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

def list_firewall_rules(nsx_client):
  gateway_type = "cgw" #or "mgw"
  policies = nsx_client.infra.domains.GatewayPolicies.get(gateway_type, "default")
  rules = policies.get_field("rules")
  
  rules_list = [
    get_rules(rule) 
    for rule in rules
  ]
  
  print(json.dumps(rules_list, indent=2))
  
  
def get_rules(rule):
  return {"create_user": rule.get_field("create_user"),
          "display_name": rule.get_field("display_name"),
          "logged": rule.get_field("logged"),
          "destination_groups": rule.get_field("destination_groups"),
          "scope": rule.get_field("scope"),
          "services": rule.get_field("services"),
          "action": rule.get_field("action"),
          "source_groups": rule.get_field("source_groups"),
         }
  
def main():
  token = "VMC_Refresh_Token_xxxxxxx"
  org_id = "VMC Org ID"
  sddc_id = "VMC SDDC ID"

  nsx_policy_client = get_nsx_policy_client(
      token, 
      org_id, 
      sddc_id
  )
  list_firewall_rules(nsx_policy_client)

if __name__ == '__main__':
  main()
