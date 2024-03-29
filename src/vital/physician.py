"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from typing import Any, Optional
from vital import utils
from vital._hooks import HookContext
from vital.models import errors, operations, shared

class Physician:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def review_openloop_v2_physician_review_openloop_post(self, request: shared.OpenLoopEvent) -> operations.ReviewOpenloopV2PhysicianReviewOpenloopPostResponse:
        r"""Review Openloop"""
        hook_ctx = HookContext(operation_id='review_openloop_v2_physician_review_openloop_post', oauth2_scopes=[], security_source=None)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v2/physician/review/openloop'
        
        headers = {}
        
        req_content_type, data, form = utils.serialize_request_body(request, shared.OpenLoopEvent, "request", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('POST', url, data=data, files=form, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['422','4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        
        res = operations.ReviewOpenloopV2PhysicianReviewOpenloopPostResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.response_review_openloop_v2_physician_review_openloop_post = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    