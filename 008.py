'''
Script to check requests package

Dummy API: https://reqres.in/
'''
from requests import get, post, put, delete

class ReQresTest:

    host:str = "https://reqres.in/"
    users_endpoint:str = "api/users"
    resources_endpoint:str = "api/unknown"

    @classmethod
    def make_get_request(cls, url:str=None, data:dict=None, params:dict=None):
        '''
        Make request to the API
        '''
        resp = get(url, data=data, params=params)
        if resp.status_code in (200, 201):
            return resp.json()
        else:
            return resp.content

    @classmethod
    def make_post_request(cls, url:str=None, data:dict=None, params:dict=None):
        '''
        Make request to the API
        '''
        resp = post(url, data=data, params=params)
        if resp.status_code in (200, 201):
            return resp.json()
        else:
            return resp.content

    
    @classmethod
    def get_all_users(cls, page:int=1):
        '''
        Get all users
        '''
        url = cls.host + cls.users_endpoint
        params = {
                'page': page
            }
        return cls.make_get_request(url, params=params)

    @classmethod
    def get_all_resources(cls, page:int=1):
        '''
        Get all resources
        '''
        url = cls.host + cls.resources_endpoint
        params = {
                'page': page
            }
        return cls.make_get_request(url, params=params)


if __name__ == "__main__":
    # resp = ReQresTest.get_all_users(page=2)
    resp = ReQresTest.get_all_resources(
            # page=2
        )
    print(resp)

    
        