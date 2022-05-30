# Didnt need this in the end

# import rest_framework.throttling
# import time
# from django.core.cache import cache as default_cache
# from django.core.exceptions import ImproperlyConfigured
# from rest_framework.settings import api_settings

# def parse_rate(self, rate):
#     """
#     Given the request rate string, return a two tuple of:
#     <allowed number of requests>, <period of time in seconds>
#     """
#     if rate is None:
#         return (None, None)
#     num, period = rate.split('/')
#     num_requests = float(num)
#     duration = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}[period[0]]
#     return (num_requests, duration)        

# rest_framework.throttling.SimpleRateThrottle.parse_rate = parse_rate    

