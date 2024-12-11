# ###################################################################################
# Script/module: modules\base64.py
# Author: Richard Knechtel
# Date: 12/11/2024
# Description: This is a module of base64 functions
# Python Version: 3.10.x
#
#
# LICENSE: 
# This script is in the public domain, free from copyrights or restrictions.
# Ref:
# https://github.com/rknechtel/Scripts/blob/master/Python/ProjectTemplate/modules/base64.py
#
# ###################################################################################
#from _overlapped import NULL


# ---------------------------------------------------------[Imports]------------------------------------------------------

import base64

# ---------------------------------------------------------[Initialisations]--------------------------------------------------------



# ---------------------------------------------------------[Functions]----------------------------------------------------

# ###################################################################################
# Function: Base64Encode
def Base64Encode(string_to_encode):
  """
  Function: Base64Encode
  Description:  Base64 Encodes a Str4ing
  Parameters: String to Base64 Encode
  Returns: Base64 Encoded String
  Exmaple Usage:
  """

  data_bytes = string_to_encode.encode('ascii')

  base64_bytes = base64.b64encode(data_bytes)
  base64_string = base64_bytes.decode('ascii')
  
  return base64_string

# ###################################################################################
# Function: Base64Decode
def Base64Decode(string_to_decode):
  """
  Function: Base64Decode
  Description:  Decodes a Base64 a Str4ing
  Parameters: Base64 String to Decode 
  Returns: Decoded Base64 String
  Exmaple Usage:
  """
  
  base64_bytes = string_to_decode.encode('ascii')

  data_bytes = base64.b64decode(base64_bytes)
  base64_string = data_bytes.decode('ascii')
  
  return base64_string


# This is a Function template:
# ###################################################################################
# Function:
def MyFuncation(Param1, Param2):
  """
  Function:
  Description:
  Parameters:
  Return: 
  """
  print("In MyFuncation():")

  try:
    # Do Something
    print("Doing Something")

  except Exception as e:
    print("Exception Information: ")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])

  return
