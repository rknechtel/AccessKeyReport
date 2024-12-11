# Project: AccessKeyReport

## Description: This will genereate a CSV of an IAM Credential Report

---

**Pyhon Version Used:**  

Python 3.10.16  


**Note:**  
This project uses the [Amazon Boto3 Module](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).  
  
---  

**If using automated AWS Auth script - call this first**  
*For Dev/Test and Production in same AWS Account*  
source scripts/awsauth.sh <TOKEN_CODE>  

**Example:**  
source scripts/awsauth.sh 123456


*For production use with a Cross Account Role*
source scripts/awsswitchrolemfa.sh <ROLE_ARN> <AWS_SESSION_NAME> <TOKEN_CODE>  

**Note:** <TOKEN_CODE> comes from:
Keepass --> <Key Name> --> KeeOtp2 --> Copy TOTP

**Example:**  
source scripts/awsswitchrolemfa.sh arn:aws:iam::171325405593:role/production-admin-cross-account-role aws-session 123456  

---  

## Python Virtual Environment Setup (Linux)  

**Create the Virtual Environment (Example):**  
python3.10 -m venv ~/projects/Security/AccessKeyReport/v-env  
 


**Activate the Virtual Environment (Example):**  
source ~/projects/Security/AccessKeyReport/v-env/bin/activate  

**Generate Requirements for project:**  
To create requirements.txt:  

1) Setup virtual environment  
2) Install all python packages  
   Example:  
~/projects/Security/AccessKeyReport/v-env/bin/pip3.10 install <PACKAGE_NAME>  
3) Note: Make sure to upgrade pip  
~/projects/Security/AccessKeyReport/v-env/bin/pip3.10 install --upgrade pip  
4) run:  
[Path to Virtual Environment Bin Directory]/pip3.10 freeze > requirements.txt  
Example (Linux):  
~/projects/Security/AccessKeyReport/v-env/bin/pip3.10 freeze > requirements.txt  

**Install the Requirements/Dependancies (Example):**  
~/projects/Security/AccessKeyReport/v-env/bin/pip3.10 install -r requirements.txt  

**Test Call for testing wrapper class:**  
~/projects/Security/AccessKeyReport/v-env/bin/python3.10 generate-report.py  <Report_Output_Location>

~/projects/Security/AccessKeyReport/v-env/bin/python3.10 generate-report.py  '/home/user/temp'

---

## References  

[IAM Get Credentials Report](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)  

[IAM Boto3](https://boto3.amazonaws.com/v1/documentation/api/1.35.8/reference/services/iam.html)  

[IAM generate_credential_report Boto3](https://boto3.amazonaws.com/v1/documentation/api/1.35.8/reference/services/iam/client/generate_credential_report.html)  

[IAM get_credential_report Boto3](https://boto3.amazonaws.com/v1/documentation/api/1.35.8/reference/services/iam/client/get_credential_report.html)  

