# Security-Test-Client-Python-3.9


## Requirements

 - Python >= 3.9.16
 - pip
 - System Linux/Unix
 - Git

### Additional Dependencies
You MUST have installed in your system the following dependencies:

- openssl ~ 3.0.7
- python cryptography ~ 41.0.2
- python requests ~ 2.31.0

```sh
# For RHEL or derivatives:
yum install openssl
dnf install openssl

# For Debian or derivatives:
apt install openssl
```
```sh
pip install cryptography
pip install requests
```
  

## Start Guide

### Step 1. Clone the repository
Clone this repository in your Linux/Unix system.
You can use the following command:
```sh
git clone <nombre_del_repositorio>
```

### Step 2. Generate the cryptographic keys

 - Run the bash file *crypto_keys_generator.sh* from the command line in your Unix/Linux system.
 - Store in a secure vault the chosen password for the PKCS12 keystore during the execution of the file *crypto_keys_generator.sh*
 - Identify from the output of the executed file *crypto_keys_generator.sh* the directory where the generated keys were stored.

### Step 3. Download the Círculo de Crédito public certificate

 1. Go to the Círculo de Crédito Developers web site
 2. Login in the web site
 3. Upload your own public certificate and Download the Círculo de Crédito public certificate
  

### Step 4. Add your credentials to call the API

 - Identify the *ApiSecurityTest* class in the module *security-test*.
 - Edit the class adding the path of your cryptographic keys and your API credentials.

```python
# ...
class  ApiSecurityTest:

def  __init__(self):
# API cryptographic keys
self.public_cert_path = "/your-file-path/cdc_cert_xxxx.pem"
self.pkcs12_path = "/your-file-path/keystore.p12"
self.pkcs12_password = "your-keystore-secure-password"

# API credentials
self.api_key = "your-api-key"
# ...
```

### Step 5. Call the API Subscriptions

Use the already defined payload or define a new one.

```python
# ...

    payload = {
        "message": "Hello Circulo de Credito"
    }

# ...

api_subscriptions = ApiSecurityTest()
api_subscriptions.securityTest()
# ...

Run the file security-test.py
```ssh
python3 security-test.py
```


[CONDICIONES DE USO, REPRODUCCIÓN Y DISTRIBUCIÓN](https://github.com/APIHub-CdC/licencias-cdc)