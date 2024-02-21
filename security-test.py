"""
Copyright (C) 2024 Círculo de Crédito - All Rights Reserved

Unauthorized use, copy, modification and/or distribution 
of this software via any medium is strictly prohibited.

This software CAN ONLY be used under the terms and conditions 
established by 'Círculo de Crédito' company.

Proprietary software.
"""
import sys
import logging
import traceback

sys.path.append('./code')

from api_service import ApiSecurityTestService
from ecc_service import ECDSAService

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s %(name)s %(filename)s:%(lineno)d - %(message)s')
log = logging.getLogger()

class ApiSecurityTest:

    def __init__(self):
        # API cryptographic keys
        self.public_cert_path    = "/your-file-path/cdc_cert_xxxx.pem"
        self.pkcs12_path         = "/your-file-path/keystore.p12"
        self.pkcs12_password     = "your-keystore-secure-password"

        # API credentials
        self.api_key = "your-api-key"

        # Services
        self.ecdsa_service  = ECDSAService(self.public_cert_path, self.pkcs12_path, self.pkcs12_password, log)
        self.api_service    = ApiSecurityTestService(self.api_key, self.ecdsa_service, log)


    def securityTest(self):
        try:
            # Your can put any JSON payload to test
            # Security-Test data
            payload = {
                "message": "Hello Circulo de Credito"
            }

            response = self.api_service.securityTest(payload)

            log.info(f"API SecurityTest Response Body: {response.text}")

        except Exception as exception:
            log.error(f"Failed to execute the Security-Test. Cause: {exception}")
            traceback.print_exc()

api_securitytest = ApiSecurityTest()
api_securitytest.securityTest()
