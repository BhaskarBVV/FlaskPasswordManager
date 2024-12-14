from flask import make_response

class ResponseHandler:
    

    @staticmethod
    def send_response(http_status_code, message = None, error = None, **kwargs):
        response_dict = {
            "status": "failed" if error else "success",
            "message": error if error else message
        }
        response = make_response(response_dict, http_status_code)
        return response