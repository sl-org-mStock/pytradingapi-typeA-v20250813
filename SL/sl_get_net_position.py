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

import SL.__sl_config__ as cfg
print(dir(cfg))

v_api_key=__sl_config__.sl_api_key
v_access_token=__sl_config__.sl_access_token

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

# #Get Net position for logged in user
# get_net_pos=mconnect_obj.get_net_position()
# test_logger.info(f"Request : Get Net Positions. Response received : {get_net_pos.json()}")
#----------------------------------------------------------------------------------------------------

#Get Net position for logged in user
mconnect_obj.set_api_key(v_api_key)
mconnect_obj.set_access_token(v_access_token)

test_logger.info("")
print("")

msg=f"mconnect_obj.get_net_position()"
test_logger.info(msg)
print(msg)

v_response=mconnect_obj.get_net_position()
msg=f"..Response received: {v_response.json()}"
test_logger.info(msg)
print(msg)
#----------------------------------------------------------------------------------------------------

