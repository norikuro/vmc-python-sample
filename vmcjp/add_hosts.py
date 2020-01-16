import requests
import atexit

from com.vmware.vmc.model_client import EsxConfig, ErrorResponse
from com.vmware.vapi.std.errors_client import InvalidRequest
from vmware.vapi.vmc.client import create_vmc_client

def get_vmc_client(token):  
  session = requests.Session()
  vmc_client = create_vmc_client(token, session=session)
  atexit.register(session.close)
  return vmc_client

def add_hosts(org_id, sddc_id, num_hosts, vmc_client):
  esx_config = EsxConfig(num_hosts=1)

  try:
    task = vmc_client.orgs.sddcs.Esxs.create(
      org=org_id, sddc=sddc_id, esx_config=esx_config
    )
  except InvalidRequest as err:
    error_response = err.data.convert_to(ErrorResponse)
    messages = error_response.error_messages
    message = None if len(messages) <= 0 else messages[0]
    raise Exception(message)
  return task.id

def main():
  vmc_client = get_vmc_client("VMC_Refresh_Token_xxxxxxx")

  try:
    task = add_hosts(
      "xxxxxxxxxxxxxxxxxxxxxxx", # ORG ID
      "xxxxxxxxxxxxxxxxxxxxxxx", # SDDC ID
      3, # Num host you want to add
      vmc_client
    )
  except Exception as e:
    print("Sorry, failed to create sddc.  {}".format(e.message))

if __name__ == '__main__':
  main()
