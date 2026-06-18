
from django.utils.deprecation import MiddlewareMixin

class ResponseCodeCounterMiddleware(MiddlewareMixin):
    counter_2xx = 0
    counter_3xx = 0
    counter_4xx = 0
    counter_5xx = 0
    
    def process_response(self, request, response):
        status_code = response.status_code
        
        if 200 <= status_code < 300:
            self.__class__.counter_2xx += 1
        elif 300 <= status_code < 400:
            self.__class__.counter_3xx += 1
        elif 400 <= status_code < 500:
            self.__class__.counter_4xx += 1
        elif 500 <= status_code < 600:
            self.__class__.counter_5xx += 1
        
        with open('metrics.log', 'a', encoding='utf-8') as f:
            f.write(f"2xx: {self.__class__.counter_2xx} 3xx: {self.__class__.counter_3xx} 4xx: {self.__class__.counter_4xx} 5xx: {self.__class__.counter_5xx}\n")
        
        return response
