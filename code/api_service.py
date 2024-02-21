"""
Copyright (C) 2024 Círculo de Crédito - All Rights Reserved

Unauthorized use, copy, modification and/or distribution 
of this software via any medium is strictly prohibited.

This software CAN ONLY be used under the terms and conditions 
established by 'Círculo de Crédito' company.

Proprietary software.
"""
import requests
import json

from ecc_service import ECDSAService

class ApiSecurityTestService:
    """
    Class service to call the Subscriptions API of 'Círculo de Crédito'.

    :Author: Ricardo Rubio
    :Copyright: 2024 Círculo de Crédito
    """

    API_URL         = "https://services.circulodecredito.com.mx/v1/securitytest"
    
    X_API_KEY       = "x-api-key"
    X_SIGNATURE     = "x-signature"

    def __init__(self, api_key, ecdsa_service, log):
        """
        Constructor.
        
        :param api_key: The assigned key for the consumption of the 'Círculo de Crédito' APIs.
        :type api_key: str

        :param ecdsa_service: A service object to perform cryptographic functionality.
        :type ecdsa_service: ECDSAService

        :param log: A logger object to print logs.
        :type log: logging
        """

        self.api_key        = api_key
        self.ecdsa_service  = ecdsa_service
        self.log            = log

    def securityTest(self, payload):
        """
        Call the security test API.

        :param payload: The request body that will be send when calling the Security-Test API.
        :type payload: dict

        :return: If success, the HTTP response object of the API call is returned.
        :rtype: requests.Response
        """
        
        self.log.info("Starting x-signature generation")

        signature = self.ecdsa_service.sign_ecdsa_sha256(json.dumps(payload))

        self.log.info(f"x-signature: {signature.hex()}")

        headers = {
            self.X_API_KEY: self.api_key,
            self.X_SIGNATURE: signature.hex()
        }

        self.log.info("Calling Security-Test API")

        response = requests.post(self.API_URL, headers=headers, json=payload)

        self.log.info(f"API Security-Test Response: {response.reason} {response.status_code}")

        return response
