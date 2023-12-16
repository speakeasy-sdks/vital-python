"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from datetime import datetime
from typing import Dict, List, Optional
from vital import utils
from vital.models import errors, operations, shared

class Link:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def check_token_state(self) -> operations.CheckLinkTokenStateV2LinkStateGetResponse:
        r"""Check Link Token State
        REQUEST_SOURCE: VITAL-LINK
        Check link token state - can be hit continuously used as heartbeat
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/link/state'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.CheckLinkTokenStateV2LinkStateGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CheckLinkTokenStateV2LinkStateGetResponseCheckLinkTokenStateV2LinkStateGet])
                res.response_check_link_token_state_v2_link_state_get = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def check_token_validity(self, request: shared.LinkTokenBase) -> operations.CheckTokenValidV2LinkTokenIsValidPostResponse:
        r"""Check Token Valid"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/link/token/isValid'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, shared.LinkTokenBase, "request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.CheckTokenValidV2LinkTokenIsValidPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CheckTokenValidV2LinkTokenIsValidPostResponseCheckTokenValidV2LinkTokenIsvalidPost])
                res.response_check_token_valid_v2_link_token_isvalid_post = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def connect_ble_provider(self, manual_connection_data: shared.ManualConnectionData, provider: operations.ProvidersThatAreManuallyAddedDevicesSuchAsBleDevicesAndGeneratedData) -> operations.ConnectBleProviderV2LinkProviderManualProviderPostResponse:
        r"""Connect Ble Provider
        REQUEST_SOURCE: CUSTOMER
        PROVIDER_TYPE: MANUAL-PROVIDER
        This connects auth providers that are password based.
        """
        request = operations.ConnectBleProviderV2LinkProviderManualProviderPostRequest(
            manual_connection_data=manual_connection_data,
            provider=provider,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ConnectBleProviderV2LinkProviderManualProviderPostRequest, base_url, '/v2/link/provider/manual/{provider}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, operations.ConnectBleProviderV2LinkProviderManualProviderPostRequest, "manual_connection_data", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ConnectBleProviderV2LinkProviderManualProviderPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Dict[str, bool]])
                res.response_connect_ble_provider_v2_link_provider_manual_provider_post = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def connect_email_auth(self, request: shared.EmailAuthLink) -> operations.ConnectEmailAuthV2LinkAuthEmailPostResponse:
        r"""Connect Email Auth
        REQUEST_SOURCE: VITAL-LINK
        PROVIDER_TYPE: EMAIL-AUTH
        This function is hit by vital-link to authenticate a email provider.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/link/auth/email'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, shared.EmailAuthLink, "request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ConnectEmailAuthV2LinkAuthEmailPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ConnectionStatus])
                res.connection_status = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def connect_email_provider(self, email_provider_auth_link: shared.EmailProviderAuthLink, provider: operations.EmailProvidersThatRequireEmailsFreestyleAuth) -> operations.ConnectEmailAuthProviderV2LinkProviderEmailProviderPostResponse:
        r"""Connect Email Auth Provider
        This connects auth providers that are email based.
        """
        request = operations.ConnectEmailAuthProviderV2LinkProviderEmailProviderPostRequest(
            email_provider_auth_link=email_provider_auth_link,
            provider=provider,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ConnectEmailAuthProviderV2LinkProviderEmailProviderPostRequest, base_url, '/v2/link/provider/email/{provider}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, operations.ConnectEmailAuthProviderV2LinkProviderEmailProviderPostRequest, "email_provider_auth_link", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ConnectEmailAuthProviderV2LinkProviderEmailProviderPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ConnectionStatus])
                res.connection_status = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def connect_individual_provider(self, individual_provider_data: shared.IndividualProviderData, provider: operations.ProvidersThatRequirePasswordAuthWhoopRenphoPelotonZwift, x_vital_link_client_region: Optional[str] = None) -> operations.ConnectIndividualProviderV2LinkProviderPasswordProviderPostResponse:
        r"""Connect Individual Provider
        This connects auth providers that are password based.
        """
        request = operations.ConnectIndividualProviderV2LinkProviderPasswordProviderPostRequest(
            individual_provider_data=individual_provider_data,
            provider=provider,
            x_vital_link_client_region=x_vital_link_client_region,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ConnectIndividualProviderV2LinkProviderPasswordProviderPostRequest, base_url, '/v2/link/provider/password/{provider}', request)
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, operations.ConnectIndividualProviderV2LinkProviderPasswordProviderPostRequest, "individual_provider_data", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ConnectIndividualProviderV2LinkProviderPasswordProviderPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ProviderLinkResponse])
                res.provider_link_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def connect_password_auth(self, password_auth_link: shared.PasswordAuthLink, x_vital_link_client_region: Optional[str] = None) -> operations.ConnectPasswordAuthV2LinkAuthPostResponse:
        r"""Connect Password Auth
        REQUEST_SOURCE: VITAL-LINK
        PROVIDER_TYPE: PASSWORD-AUTH
        This function is hit by vital-link to authenticate a password provider.
        """
        request = operations.ConnectPasswordAuthV2LinkAuthPostRequest(
            password_auth_link=password_auth_link,
            x_vital_link_client_region=x_vital_link_client_region,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/link/auth'
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, operations.ConnectPasswordAuthV2LinkAuthPostRequest, "password_auth_link", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ConnectPasswordAuthV2LinkAuthPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ConnectionStatus])
                res.connection_status = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def connect_provider(self, provider: str, x_vital_sdk_no_redirect: Optional[str] = None) -> operations.ConnectProviderV2LinkConnectProviderGetResponse:
        r"""Connect Provider
        REQUEST_SOURCE: VITAL-LINK
        PROVIDER_TYPE: OAUTH
        Connect oauth providers
        """
        request = operations.ConnectProviderV2LinkConnectProviderGetRequest(
            provider=provider,
            x_vital_sdk_no_redirect=x_vital_sdk_no_redirect,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ConnectProviderV2LinkConnectProviderGetRequest, base_url, '/v2/link/connect/{provider}', request)
        headers = utils.get_headers(request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ConnectProviderV2LinkConnectProviderGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ConnectProviderV2LinkConnectProviderGetResponseConnectProviderV2LinkConnectProviderGet])
                res.response_connect_provider_v2_link_connect_provider_get = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def create_demo_connection(self, request: shared.DemoConnectionCreationPayload) -> operations.CreateDemoConnectionV2LinkConnectDemoPostResponse:
        r"""Create Demo Connection
        POST Connect the given Vital user to a demo provider.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/link/connect/demo'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, shared.DemoConnectionCreationPayload, "request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.CreateDemoConnectionV2LinkConnectDemoPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DemoConnectionStatus])
                res.demo_connection_status = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def create_token(self, user_id: str, expires_at: Optional[datetime] = None) -> operations.CreateTokenV2LinkCodeCreatePostResponse:
        r"""Create Token
        Generate a token to invite a user of Vital mobile app to your team
        """
        request = operations.CreateTokenV2LinkCodeCreatePostRequest(
            user_id=user_id,
            expires_at=expires_at,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/link/code/create'
        headers = {}
        query_params = utils.get_query_params(operations.CreateTokenV2LinkCodeCreatePostRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.CreateTokenV2LinkCodeCreatePostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.VitalTokenCreatedResponse])
                res.vital_token_created_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def exchange_token(self, code: str) -> operations.ExchangeTokenV2LinkCodeExchangePostResponse:
        r"""Exchange Token
        Redeem an invite token for an api key
        """
        request = operations.ExchangeTokenV2LinkCodeExchangePostRequest(
            code=code,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/link/code/exchange'
        headers = {}
        query_params = utils.get_query_params(operations.ExchangeTokenV2LinkCodeExchangePostRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ExchangeTokenV2LinkCodeExchangePostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.VitalTokenExchangeResponse])
                res.vital_token_exchange_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def generate(self, request: shared.LinkTokenExchange) -> operations.GenerateVitalLinkTokenV2LinkTokenPostResponse:
        r"""Generate Vital Link Token
        Endpoint to generate a user link token, to be used throughout the vital
        link process. The vital link token is a one time use token, that
        expires after 10 minutes. If you would like vital-link widget to launch
        with a specific provider, pass in a provider in the body. If you would
        like to redirect to a custom url after successful or error connection,
        pass in your own custom redirect_url parameter.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/link/token'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, shared.LinkTokenExchange, "request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GenerateVitalLinkTokenV2LinkTokenPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.LinkTokenExchangeResponse])
                res.link_token_exchange_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_oauth_provider(self, oauth_provider: shared.OAuthProviders) -> operations.GetOauthProviderV2LinkProviderOauthOauthProviderGetResponse:
        r"""Get Oauth Provider
        This endpoint generates an OAuth link for oauth provider
        """
        request = operations.GetOauthProviderV2LinkProviderOauthOauthProviderGetRequest(
            oauth_provider=oauth_provider,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOauthProviderV2LinkProviderOauthOauthProviderGetRequest, base_url, '/v2/link/provider/oauth/{oauth_provider}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetOauthProviderV2LinkProviderOauthOauthProviderGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Source])
                res.source = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_providers(self) -> operations.GetProvidersV2LinkProvidersGetResponse:
        r"""Get Providers
        GET List of all available providers given the generated link token.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/link/providers'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetProvidersV2LinkProvidersGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.SourceLink]])
                res.response_get_providers_v2_link_providers_get = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def start_connect_process(self, request: shared.BeginLinkTokenRequest) -> operations.StartConnectProcessV2LinkStartPostResponse:
        r"""Start Connect Process
        REQUEST_SOURCE: VITAL-LINK
        Start link token process
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/link/start'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, shared.BeginLinkTokenRequest, "request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.StartConnectProcessV2LinkStartPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.StartConnectProcessV2LinkStartPostResponseStartConnectProcessV2LinkStartPost])
                res.response_start_connect_process_v2_link_start_post = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    