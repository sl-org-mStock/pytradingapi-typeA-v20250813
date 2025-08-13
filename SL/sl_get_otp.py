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

# #Login Via Tasc API, Receive Token in response
# login_response=mconnect_obj.login("RAHUL","Macm@123")
# test_logger.info(f"Request : Login. Response received : {login_response.json()}")
#----------------------------------------------------------------------------------------------------

#Login Via Tasc API, Receive Token in response
#	def login(self,user_id,password):
test_logger.info("")
print("")

msg=f"mconnect_obj.login(user_id: {v_user_id}, password: {v_user_pwd})"
test_logger.info(msg)
print(msg)

v_response=mconnect_obj.login(v_user_id, v_user_pwd)
	#{'status': 'success', 'data': {'ugid': '1598477b-9d15-4df1-aa8c-0da73551184a', 'is_kyc': True, 'is_activate': False, 'is_password_reset': True, 'is_error': False, 'cid': 'MA2188008', 'nm': 'SUSHANT PRAKASH LOTLIKAR', 'flag': 0}}
msg=f"..Response received: {v_response.json()}"
test_logger.info(msg)
print(msg)
# msg=f"..mconnect_obj.json(): {mconnect_obj.json()}"
# test_logger.info(msg)
# print(msg)
# Traceback (most recent call last):
  # File "C:\SUSHANT\My_Code\GitHub\Repositories\pytradingapi-typeA\examples\api_connect_test.py", line 53, in <module>
    # msg=f"..mconnect_obj.json(): {mconnect_obj.json()}"
                                  # ^^^^^^^^^^^^^^^^^
# AttributeError: 'MConnect' object has no attribute 'json'
#----------------------------------------------------------------------------------------------------

