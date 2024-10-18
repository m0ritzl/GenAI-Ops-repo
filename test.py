import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
    "question": "How can I request a refill for my prescription at Lamna Healthcare?",
    "chat_history": []
}

body = str.encode(json.dumps(data))

url = 'https://rag-4141-endpoint.northcentralus.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCIsImtpZCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzE2YjNjMDEzLWQzMDAtNDY4ZC1hYzY0LTdlZGEwODIwYjZkMy8iLCJpYXQiOjE3MjkyNTI0NjgsIm5iZiI6MTcyOTI1MjQ2OCwiZXhwIjoxNzI5MjU2ODgzLCJhY3IiOiIxIiwiYWlvIjoiQVpRQWEvOFlBQUFBQXpReVJxRmhVWHN6d29QQUtyNG9tc0NZUUtGa3J5NFBOS0VQSzZoRExVWEN0VjZyc1JiaVh4dTdPUEpqZTZ6cmRMemFSRkRSTytxNm5pUzVPZHhzSkgvdVRzS3NTckkyNzB4L2gveWxZZm5GemY4SFNWZEVUNlFJRWxNZndXTm1aaDRDSncrMG81aHBWdVpQYmRSTWhtaG9vM0NkQjBUNjhGV0ZUeXljTlhQUStSMUp4TEQxRExUai9SZXVUNGl4IiwiYWx0c2VjaWQiOiI1OjoxMDAzMjAwMjI0QkI2RUEwIiwiYW1yIjpbInJzYSIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiNWFiZDYzMzUtZmY5OS00N2QxLWEzZWItMWNhMTEyYTM4ZGMyIiwiZW1haWwiOiJtb3JpdHoucml0emxAbWljcm9zb2Z0LmNvbSIsImZhbWlseV9uYW1lIjoiUml0emwiLCJnaXZlbl9uYW1lIjoiTW9yaXR6IiwiZ3JvdXBzIjpbImIxMzA0MDIyLTA4ZTYtNDQ3ZC1iMDk0LTE1MzcwNTk3YzZiNiIsIjA5NTMxYTcyLTJjM2UtNGUwNi1iZTFlLTI1OTZiZDA4ZGNkZCIsIjAwNjAzYmI3LWRmNGEtNGZmYS05MjFiLWRhMmY1Y2RmNzUwMSIsImQzNGM0ZWJlLTQ5ODQtNDkwMy1hNjRkLThjMjAyODNkNTE2YiIsImUzMDk2ZGY3LWI2NWMtNGUzMi1hYjFhLTdhMzVkYzY4NGYwYSJdLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTcyLjIwMS43Ny40MyIsIm5hbWUiOiJNb3JpdHogUml0emwiLCJvaWQiOiI4NGM5YzllYy1lYTAxLTQzZjMtOWU1OC1iZDRmOTU4ZDFhZGQiLCJwdWlkIjoiMTAwMzIwMDJBRjIwNDYzQiIsInJoIjoiMC5BVVlBRThDekZnRFRqVWFzWkg3YUNDQzIwMTl2cGhqZjJ4ZE1uZGNXTkhFcW5MN3hBTXcuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiOWNTb1JPV2ZYM0t0NEh4MW5McmZFeWtibHVQb3hfSERvQkRoTU1Oc1R0SSIsInRpZCI6IjE2YjNjMDEzLWQzMDAtNDY4ZC1hYzY0LTdlZGEwODIwYjZkMyIsInVuaXF1ZV9uYW1lIjoibW9yaXR6LnJpdHpsQG1pY3Jvc29mdC5jb20iLCJ1dGkiOiI0dTQydWtKMnZrS01fN2tsVmR3Y0FBIiwidmVyIjoiMS4wIiwieG1zX2lkcmVsIjoiMSAyIn0.CnU5-YnmuIUDFeT0t1IcCQ6I56UrvbYEjEjp2wwPCSY9BYRgYKcZbTvTneUEV3C8N7iY21RJChHCwIaIKkEDwkQ-_NJO1lyx0IiO-bjdXMM_SNNb4LqvXcitvvsi_VDuSFeYbpSe-3bL8Gati2Vm8kLmXGTbqkke--URe8mO4Fv6BMaCh8NbPiKfScJeGCTUgLlAwoHeuCFTaYq9gTI9aZpvrsxnn74DrVbC5FA224WUY6ogeOSWcNTb18X0x7IVmTUM0DK3DYjKTjkxelhVFDNmoJ7iyTmmHxV9HMlgkVugjDIeNgzlQkh79IvSLrzukI1ZT6fbvguNcVuMtBs7jA'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))