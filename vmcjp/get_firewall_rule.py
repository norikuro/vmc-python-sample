#!/usr/bin/env python

import time
import requests
import atexit

#from datetime import datetime
#from pytz import timezone
from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from com.vmware.nsx_vmc_app_client_for_vmc import create_nsx_vmc_app_client_for_vmc

#from vmcjp.config import Config
#from vmcjp.utils.metadata import get_members
#from vmcjp.network.security_groups import get_security_groups
#from vmcjp.network.firewall_rules import get_firewall_rules
#from vmcjp.network.vpns import get_l3vpns

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
  security_groups = get_security_group_ids_and_names(gateway_type, nsx_client)
  policies = nsx_client.infra.domains.GatewayPolicies.get(gateway_type, "default")
  rules = policies.get_field("rules")
  
  rules_list = [
    get_rules(rule, gateway_type, security_groups) 
    for rule in rules
  ]
  
  print(rules_list)
  
def get_security_group_ids_and_names(gateway_type, nsx_client):
  security_groups = nsx_client.infra.domains.Groups.list(gateway_type).results
  return {sg.get_field("id"):sg.get_field("display_name") for sg in security_groups}
  
def get_rules(rule, gateway_type, security_groups):
  sn = rule.get_field("sequence_number")
  source_groups = rule.get_field("source_groups")
#  sg = replace_strings_in_list(source_groups, "/infra/domains/" + gateway_type + "/groups/")
  sg = [l.translate(None, "/infra/domains/" + gateway_type + "/groups/") for l in source_groups]
  sg_names = compare_list_and_dict(sg, security_groups)
  dest_groups = rule.get_field("destination_groups")
#  dg = replace_strings_in_list(dest_groups, "/infra/domains/" + gateway_type + "/groups/")
  dg = [l.translate(None, "/infra/domains/" + gateway_type + "/groups/") for l in dest_groups]
  dg_names = compare_list_and_dict(dg, security_groups)
  
  return {"create_user": rule.get_field("create_user"),
          "display_name": rule.get_field("display_name"),
          "logged": rule.get_field("logged"),
          "destination_groups": dest_groups,
          "destination_groups_names": dg_names,
          "scope": rule.get_field("scope"),
          "services": rule.get_field("services"),
          "sequence_number": sn,
          "action": rule.get_field("action"),
          "source_groups": source_groups,
          "source_group_names": sg_names
         }
  
def compare_list_and_dict(ls, dic):
  key_list = dic.keys()
  dup_list = set(key_list) & set(ls)
  return [dic[id] for id in dup_list]

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
