# ************************************************************************
# Script: chipplydb-lambda.py
# Author: Richard Knechtel
# Date: 07/20/2023
# Description: This lambda will call the functions in the 
#              Step Functions Class and the SQL Server Functions.
# Python Version: 3.8.x
#
# References:
# https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code/lambda/boto_client_examples
# https://aws-lambda-for-python-developers.readthedocs.io/en/latest/02_event_and_context
#
#
#************************************************************************

#---------------------------------------------------------[Imports]------------------------------------------------------

import pandas as pd

_modules = [
      'boto3',
      'botocore',
      'csv',
      'datetime',
      'errno',
      'logging',
      'os',
      'sys',
      'time',
       ]

for module in _modules:
  try:
    locals()[module] = __import__(module, {}, {}, [])
  except ImportError:
    print('Error importing %s.' % module)

# Custom Modules:
from config import AccessKeyconfig as config
from modules import genericfunctions as genfunc
from modules import base64 as base64

#---------------------------------------------------------[General Initializations]--------------------------------------------------------

# Logging:
global AccessKeyLogger

# For Info and up logging
config.LogLevel = logging.INFO
# For Debug and up Logging:
# config.LogLevel = logging.DEBUG

#----------------------------------------------------------[Declarations]----------------------------------------------------------

#Script Version
ScriptVersion = '0.0.1'

#---------------------------------------------------------[Logigng Initializations]--------------------------------------------------------

# Initialize Logging:
AccessKeyLogger= genfunc.InitScriptConsoleLogging('AccessKeyLogger', config.LogLevel)

#---------------------------------------------------------[Boto3 Initializations]--------------------------------------------------------
client = boto3.client('iam')

#---------------------------------------------------------[Functions]--------------------------------------------------------

# ###################################################################################
# Function: ProcessParams
# Description:  This will process any parameters to the Script
# Parameters: Param1  - Does
#             Param2  - Does
#
def ProcessParams(argv):
  # Set our Variables:

  # Check the total number of args passed - make sure we get 2 (1 + the script name that is passed by default).
  if(len(sys.argv) == 2):
    genfunc.ShowParams()
    config.ThisScript = sys.argv[0]
    config.ReportOutputLocation = sys.argv[1]

  else:
    config.ShowUsage()
    sys.exit(1)

  return

#-----------------------------------------------------------[Execution]------------------------------------------------------------

# ************************************
# Main Script Execution
# ************************************

# Note: Below is strickly for running from a command line call:
# Will only run if this file is called as primary file 
if __name__ == '__main__':
        
  print('Starting generate-report script.')
  
  try:
    # Initialize Logging:
    AccessKeyLogger = genfunc.InitScriptConsoleLogging('AccessKeyLogger', config.LogLevel)

    # Proccess Parameters
    ProcessParams(sys.argv)

    AccessKeyLogger.info("Generating Credential Report")
    response = client.generate_credential_report()
    
    time.sleep(10)

    AccessKeyLogger.info("Trying to Get Credential Report")
    reportResponse = client.get_credential_report()

    # Response format:
    # {
    #     'Content': b'bytes',
    #     'ReportFormat': 'text/csv',
    #     'GeneratedTime': datetime(2015, 1, 1)
    # }

    content = reportResponse["Content"].decode("utf-8")
    AccessKeyLogger.info(f"Report Content: {content}")
    
    content_lines = content.split("\n")
    creds_reader = csv.DictReader(content_lines, delimiter=",")
    creds_dict = dict(enumerate(list(creds_reader)))
    AccessKeyLogger.info(f"Report Dict: {creds_dict}")

    header_names = []
    creds_list = []
    iter_count = 0

    for i in creds_dict:
      if (iter_count == 0):
        header_names = list(creds_dict[i].keys())
        creds_list.append(creds_dict[i])
        iter_count += 1
      else:
        creds_list.append(creds_dict[i])
        iter_count += 1

    AccessKeyLogger.info("Writing Report CSV")
    with open(f'{config.ReportOutputLocation}/Status_report.csv', 'w' ) as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames = header_names)
      writer.writeheader()
      writer.writerows(creds_list)

    df = pd.read_csv(f'{config.ReportOutputLocation}/Status_report.csv')
    df.to_csv(f'{config.ReportOutputLocation}/Status_report.csv', index=False)

  except Exception as e:
    AccessKeyLogger.info("generate-report script Ended at " + genfunc.GetCurrentDateTime() + ".")
    AccessKeyLogger.error("Execution failed.")
    AccessKeyLogger.error("Exception Information = ")
    AccessKeyLogger.error(sys.exc_info()[0])
    AccessKeyLogger.error(sys.exc_info()[1])
    AccessKeyLogger.error(sys.exc_info()[2])
    AccessKeyLogger.error("")
    AccessKeyLogger.error("generate-report.py completed unsuccessfully at " + genfunc.GetCurrentDateTime() + ".")
    config.HasError = True
    sys.exit(1)


  if not config.HasError:
    # All Went well - exiting!
    AccessKeyLogger.info("generate-report script Ended at " + genfunc.GetCurrentDateTime() + ".")
    AccessKeyLogger.info("")
    AccessKeyLogger.info("generate-report.py completed successfully at " + genfunc.GetCurrentDateTime() + ".")
    AccessKeyLogger.info("")
    AccessKeyLogger.info("========================================================")
    AccessKeyLogger.info("")
    config.HasError = False
    sys.exit(0)
