v_otp="767"

print(__file__)

import os,sys
import csv
import logging

parent_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print("parent_dir: " + parent_dir)
sys.path.append(parent_dir)
from tradingapi_a.mconnect import *
from tradingapi_a import __config__
from SL import __sl_config__

v_user_id=__sl_config__.sl_user_id
v_user_pwd=__sl_config__.sl_user_pwd
v_api_key=__sl_config__.sl_api_key

v_checksum="W"

# Create and configure logger
logging.basicConfig(filename="SL\\sl.log", format='%(asctime)s %(message)s', filemode='a',)

# Creating an object
test_logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
test_logger.setLevel(logging.INFO)

#Testing NConnect API
#Object for NConnect API
mconnect_obj=MConnect()
#----------------------------------------------------------------------------------------------------

# #Generate access token by calling generate session
# gen_response=mconnect_obj.generate_session(__config__.API_KEY,"123","W")
# test_logger.info(f"Request : Generate Session. Response received : {gen_response.json()}")
# #----------------------------------------------------------------------------------------------------

#Generate access token by calling generate session
#	def generate_session(self,_api_key,_request_token,_checksum):
test_logger.info("")
print("")

msg=f"mconnect_obj.generate_session(api_key: {v_api_key}, otp: {v_otp}, checksum: {v_checksum})"
test_logger.info(msg)
print(msg)

v_response=mconnect_obj.generate_session(v_api_key, v_otp, v_checksum)
msg=f"..Response received: {v_response.json()}"
test_logger.info(msg)
print(msg)

msg=f"..data.user_name: {v_response.data.user_name}"
test_logger.info(msg)
print(msg)

msg=f"..data.access_token: {v_response.data.access_token}"
test_logger.info(msg)
print(msg)
#----------------------------------------------------------------------------------------------------

