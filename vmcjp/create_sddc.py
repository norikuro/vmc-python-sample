import requests
import atexit

from com.vmware.vmc.model_client import AwsSddcConfig, AccountLinkSddcConfig, SddcConfig, AccountLinkConfig, ErrorResponse
from com.vmware.vapi.std.errors_client import InvalidRequest
from vmware.vapi.vmc.client import create_vmc_client

def get_vmc_client(token):  
  session = requests.Session()
  vmc_client = create_vmc_client(token, session=session)
  atexit.register(session.close)
  return vmc_client

def create_sddc(
  org_id,
  region,
  sddc_name,
  sddc_type,
  vpc_cidr,
  provider,
  customer_subnet_id,
  connected_account_id,
  num_hosts,
  link_aws,
  vmc_client
):
  sddc_config = AwsSddcConfig(
    region=region,
    name=sddc_name,
    sddc_type=sddc_type,
    account_link_sddc_config=[
      AccountLinkSddcConfig(
        customer_subnet_ids=[customer_subnet_id],
        connected_account_id=connected_account_id
      )
    ] if link_aws else None,
    vpc_cidr=vpc_cidr,
    provider=provider,
    num_hosts=num_hosts,
    account_link_config=None if link_aws else AccountLinkConfig(True),
    deployment_type=SddcConfig.DEPLOYMENT_TYPE_SINGLEAZ
  )
  
  try:
    task = vmc_client.orgs.Sddcs.create(
      org=org_id, sddc_config=sddc_config
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
    task = create_sddc(
      "xxxxxxxxxxxxxxxxxxxxxxx", # ORG ID
      "AP_NORTHEAST_1", # AWS Region
      "TEST-SDDC", # SDDC NAME
      "1NODE", # This is option
      "10.2.0.0/16", # CIDR block for Management segment of VMC SDDC
      "AWS", # Fixed parameter, you can not change
      "subnet-xxxxxxxxxx", # AWS Subnet ID which you want to connect via ENI
      "xxxxxxxx-xxxx-xxxxx-xxxx-xxxxxxx", # Connected AWS account ID, you can get this id by using vmc_client.orgs.account_link.ConnectedAccounts.get(org_id)
      3, # Num host you want to deploy
      True, # Link AWS or not
      vmc_client
    )
  except Exception as e:
    print("Sorry, failed to create sddc.  {}".format(e.message))

if __name__ == '__main__':
  main()
