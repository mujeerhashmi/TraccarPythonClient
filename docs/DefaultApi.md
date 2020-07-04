# TraccarClient.DefaultApi

All URIs are relative to *https://platform.4csolutions.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributes_computed_get**](DefaultApi.md#attributes_computed_get) | **GET** /attributes/computed | Fetch a list of Attributes
[**attributes_computed_id_delete**](DefaultApi.md#attributes_computed_id_delete) | **DELETE** /attributes/computed/{id} | Delete an Attribute
[**attributes_computed_id_put**](DefaultApi.md#attributes_computed_id_put) | **PUT** /attributes/computed/{id} | Update an Attribute
[**attributes_computed_post**](DefaultApi.md#attributes_computed_post) | **POST** /attributes/computed | Create an Attribute
[**calendars_get**](DefaultApi.md#calendars_get) | **GET** /calendars | Fetch a list of Calendars
[**calendars_id_delete**](DefaultApi.md#calendars_id_delete) | **DELETE** /calendars/{id} | Delete a Calendar
[**calendars_id_put**](DefaultApi.md#calendars_id_put) | **PUT** /calendars/{id} | Update a Calendar
[**calendars_post**](DefaultApi.md#calendars_post) | **POST** /calendars | Create a Calendar
[**commands_get**](DefaultApi.md#commands_get) | **GET** /commands | Fetch a list of Saved Commands
[**commands_id_delete**](DefaultApi.md#commands_id_delete) | **DELETE** /commands/{id} | Delete a Saved Command
[**commands_id_put**](DefaultApi.md#commands_id_put) | **PUT** /commands/{id} | Update a Saved Command
[**commands_post**](DefaultApi.md#commands_post) | **POST** /commands | Create a Saved Command
[**commands_send_get**](DefaultApi.md#commands_send_get) | **GET** /commands/send | Fetch a list of Saved Commands supported by Device at the moment
[**commands_send_post**](DefaultApi.md#commands_send_post) | **POST** /commands/send | Dispatch commands to device
[**commands_types_get**](DefaultApi.md#commands_types_get) | **GET** /commands/types | Fetch a list of available Commands for the Device or all possible Commands if Device ommited
[**devices_get**](DefaultApi.md#devices_get) | **GET** /devices | Fetch a list of Devices
[**devices_id_accumulators_put**](DefaultApi.md#devices_id_accumulators_put) | **PUT** /devices/{id}/accumulators | Update total distance and hours of the Device
[**devices_id_delete**](DefaultApi.md#devices_id_delete) | **DELETE** /devices/{id} | Delete a Device
[**devices_id_put**](DefaultApi.md#devices_id_put) | **PUT** /devices/{id} | Update a Device
[**devices_post**](DefaultApi.md#devices_post) | **POST** /devices | Create a Device
[**drivers_get**](DefaultApi.md#drivers_get) | **GET** /drivers | Fetch a list of Drivers
[**drivers_id_delete**](DefaultApi.md#drivers_id_delete) | **DELETE** /drivers/{id} | Delete a Driver
[**drivers_id_put**](DefaultApi.md#drivers_id_put) | **PUT** /drivers/{id} | Update a Driver
[**drivers_post**](DefaultApi.md#drivers_post) | **POST** /drivers | Create a Driver
[**events_id_get**](DefaultApi.md#events_id_get) | **GET** /events/{id} | 
[**geofences_get**](DefaultApi.md#geofences_get) | **GET** /geofences | Fetch a list of Geofences
[**geofences_id_delete**](DefaultApi.md#geofences_id_delete) | **DELETE** /geofences/{id} | Delete a Geofence
[**geofences_id_put**](DefaultApi.md#geofences_id_put) | **PUT** /geofences/{id} | Update a Geofence
[**geofences_post**](DefaultApi.md#geofences_post) | **POST** /geofences | Create a Geofence
[**groups_get**](DefaultApi.md#groups_get) | **GET** /groups | Fetch a list of Groups
[**groups_id_delete**](DefaultApi.md#groups_id_delete) | **DELETE** /groups/{id} | Delete a Group
[**groups_id_put**](DefaultApi.md#groups_id_put) | **PUT** /groups/{id} | Update a Group
[**groups_post**](DefaultApi.md#groups_post) | **POST** /groups | Create a Group
[**maintenance_get**](DefaultApi.md#maintenance_get) | **GET** /maintenance | Fetch a list of Maintenance
[**maintenance_id_delete**](DefaultApi.md#maintenance_id_delete) | **DELETE** /maintenance/{id} | Delete a Maintenance
[**maintenance_id_put**](DefaultApi.md#maintenance_id_put) | **PUT** /maintenance/{id} | Update a Maintenance
[**maintenance_post**](DefaultApi.md#maintenance_post) | **POST** /maintenance | Create a Maintenance
[**notifications_get**](DefaultApi.md#notifications_get) | **GET** /notifications | Fetch a list of Notifications
[**notifications_id_delete**](DefaultApi.md#notifications_id_delete) | **DELETE** /notifications/{id} | Delete a Notification
[**notifications_id_put**](DefaultApi.md#notifications_id_put) | **PUT** /notifications/{id} | Update a Notification
[**notifications_post**](DefaultApi.md#notifications_post) | **POST** /notifications | Create a Notification
[**notifications_test_post**](DefaultApi.md#notifications_test_post) | **POST** /notifications/test | Send test notification to current user via Email and SMS
[**notifications_types_get**](DefaultApi.md#notifications_types_get) | **GET** /notifications/types | Fetch a list of available Notification types
[**permissions_delete**](DefaultApi.md#permissions_delete) | **DELETE** /permissions | Unlink an Object from another Object
[**permissions_post**](DefaultApi.md#permissions_post) | **POST** /permissions | Link an Object to another Object
[**positions_get**](DefaultApi.md#positions_get) | **GET** /positions | Fetches a list of Positions
[**reports_events_get**](DefaultApi.md#reports_events_get) | **GET** /reports/events | Fetch a list of Events within the time period for the Devices or Groups
[**reports_route_get**](DefaultApi.md#reports_route_get) | **GET** /reports/route | Fetch a list of Positions within the time period for the Devices or Groups
[**reports_stops_get**](DefaultApi.md#reports_stops_get) | **GET** /reports/stops | Fetch a list of ReportStops within the time period for the Devices or Groups
[**reports_summary_get**](DefaultApi.md#reports_summary_get) | **GET** /reports/summary | Fetch a list of ReportSummary within the time period for the Devices or Groups
[**reports_trips_get**](DefaultApi.md#reports_trips_get) | **GET** /reports/trips | Fetch a list of ReportTrips within the time period for the Devices or Groups
[**server_get**](DefaultApi.md#server_get) | **GET** /server | Fetch Server information
[**server_put**](DefaultApi.md#server_put) | **PUT** /server | Update Server information
[**session_delete**](DefaultApi.md#session_delete) | **DELETE** /session | Close the Session
[**session_get**](DefaultApi.md#session_get) | **GET** /session | Fetch Session information
[**session_post**](DefaultApi.md#session_post) | **POST** /session | Create a new Session
[**statistics_get**](DefaultApi.md#statistics_get) | **GET** /statistics | Fetch server Statistics
[**users_get**](DefaultApi.md#users_get) | **GET** /users | Fetch a list of Users
[**users_id_delete**](DefaultApi.md#users_id_delete) | **DELETE** /users/{id} | Delete a User
[**users_id_put**](DefaultApi.md#users_id_put) | **PUT** /users/{id} | Update a User
[**users_post**](DefaultApi.md#users_post) | **POST** /users | Create a User


# **attributes_computed_get**
> list[Attribute] attributes_computed_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)

Fetch a list of Attributes

Without params, it returns a list of Attributes the user has access to

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
all = true # bool | Can only be used by admins or managers to fetch all entities (optional)
user_id = 56 # int | Standard users can use this only with their own _userId_ (optional)
device_id = 56 # int | Standard users can use this only with _deviceId_s, they have access to (optional)
group_id = 56 # int | Standard users can use this only with _groupId_s, they have access to (optional)
refresh = true # bool |  (optional)

try:
    # Fetch a list of Attributes
    api_response = api_instance.attributes_computed_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->attributes_computed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Can only be used by admins or managers to fetch all entities | [optional] 
 **user_id** | **int**| Standard users can use this only with their own _userId_ | [optional] 
 **device_id** | **int**| Standard users can use this only with _deviceId_s, they have access to | [optional] 
 **group_id** | **int**| Standard users can use this only with _groupId_s, they have access to | [optional] 
 **refresh** | **bool**|  | [optional] 

### Return type

[**list[Attribute]**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attributes_computed_id_delete**
> attributes_computed_id_delete(id)

Delete an Attribute

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete an Attribute
    api_instance.attributes_computed_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->attributes_computed_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attributes_computed_id_put**
> Attribute attributes_computed_id_put(id, body)

Update an Attribute

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.Attribute() # Attribute | 

try:
    # Update an Attribute
    api_response = api_instance.attributes_computed_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->attributes_computed_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Attribute**](Attribute.md)|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attributes_computed_post**
> Attribute attributes_computed_post(body)

Create an Attribute

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Attribute() # Attribute | 

try:
    # Create an Attribute
    api_response = api_instance.attributes_computed_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->attributes_computed_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Attribute**](Attribute.md)|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendars_get**
> list[Calendar] calendars_get(all=all, user_id=user_id)

Fetch a list of Calendars

Without params, it returns a list of Calendars the user has access to

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
all = true # bool | Can only be used by admins or managers to fetch all entities (optional)
user_id = 56 # int | Standard users can use this only with their own _userId_ (optional)

try:
    # Fetch a list of Calendars
    api_response = api_instance.calendars_get(all=all, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->calendars_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Can only be used by admins or managers to fetch all entities | [optional] 
 **user_id** | **int**| Standard users can use this only with their own _userId_ | [optional] 

### Return type

[**list[Calendar]**](Calendar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendars_id_delete**
> calendars_id_delete(id)

Delete a Calendar

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a Calendar
    api_instance.calendars_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->calendars_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendars_id_put**
> Calendar calendars_id_put(id, body)

Update a Calendar

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.Calendar() # Calendar | 

try:
    # Update a Calendar
    api_response = api_instance.calendars_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->calendars_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Calendar**](Calendar.md)|  | 

### Return type

[**Calendar**](Calendar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendars_post**
> Calendar calendars_post(body)

Create a Calendar

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Calendar() # Calendar | 

try:
    # Create a Calendar
    api_response = api_instance.calendars_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->calendars_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Calendar**](Calendar.md)|  | 

### Return type

[**Calendar**](Calendar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_get**
> list[Command] commands_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)

Fetch a list of Saved Commands

Without params, it returns a list of Drivers the user has access to

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
all = true # bool | Can only be used by admins or managers to fetch all entities (optional)
user_id = 56 # int | Standard users can use this only with their own _userId_ (optional)
device_id = 56 # int | Standard users can use this only with _deviceId_s, they have access to (optional)
group_id = 56 # int | Standard users can use this only with _groupId_s, they have access to (optional)
refresh = true # bool |  (optional)

try:
    # Fetch a list of Saved Commands
    api_response = api_instance.commands_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Can only be used by admins or managers to fetch all entities | [optional] 
 **user_id** | **int**| Standard users can use this only with their own _userId_ | [optional] 
 **device_id** | **int**| Standard users can use this only with _deviceId_s, they have access to | [optional] 
 **group_id** | **int**| Standard users can use this only with _groupId_s, they have access to | [optional] 
 **refresh** | **bool**|  | [optional] 

### Return type

[**list[Command]**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_id_delete**
> commands_id_delete(id)

Delete a Saved Command

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a Saved Command
    api_instance.commands_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_id_put**
> Command commands_id_put(id, body)

Update a Saved Command

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.Command() # Command | 

try:
    # Update a Saved Command
    api_response = api_instance.commands_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Command**](Command.md)|  | 

### Return type

[**Command**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_post**
> Command commands_post(body)

Create a Saved Command

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Command() # Command | 

try:
    # Create a Saved Command
    api_response = api_instance.commands_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Command**](Command.md)|  | 

### Return type

[**Command**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_send_get**
> list[Command] commands_send_get(device_id=device_id)

Fetch a list of Saved Commands supported by Device at the moment

Return a list of saved commands linked to Device and its groups, filtered by current Device protocol support

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
device_id = 56 # int | Standard users can use this only with _deviceId_s, they have access to (optional)

try:
    # Fetch a list of Saved Commands supported by Device at the moment
    api_response = api_instance.commands_send_get(device_id=device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_send_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Standard users can use this only with _deviceId_s, they have access to | [optional] 

### Return type

[**list[Command]**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_send_post**
> Command commands_send_post(body)

Dispatch commands to device

Dispatch a new command or Saved Command if _body.id_ set

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Command() # Command | 

try:
    # Dispatch commands to device
    api_response = api_instance.commands_send_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Command**](Command.md)|  | 

### Return type

[**Command**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_types_get**
> list[CommandType] commands_types_get(device_id=device_id, protocol=protocol, text_channel=text_channel)

Fetch a list of available Commands for the Device or all possible Commands if Device ommited

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
device_id = 56 # int | Internal device identifier. Only works if device has already reported some locations (optional)
protocol = 'protocol_example' # str | Protocol name. Can be used instead of device id (optional)
text_channel = true # bool | When `true` return SMS commands. If not specified or `false` return data commands (optional)

try:
    # Fetch a list of available Commands for the Device or all possible Commands if Device ommited
    api_response = api_instance.commands_types_get(device_id=device_id, protocol=protocol, text_channel=text_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Internal device identifier. Only works if device has already reported some locations | [optional] 
 **protocol** | **str**| Protocol name. Can be used instead of device id | [optional] 
 **text_channel** | **bool**| When &#x60;true&#x60; return SMS commands. If not specified or &#x60;false&#x60; return data commands | [optional] 

### Return type

[**list[CommandType]**](CommandType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get**
> list[Device] devices_get(all=all, user_id=user_id, id=id, unique_id=unique_id)

Fetch a list of Devices

Without any params, returns a list of the user's devices

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
all = true # bool | Can only be used by admins or managers to fetch all entities (optional)
user_id = 56 # int | Standard users can use this only with their own _userId_ (optional)
id = 56 # int | To fetch one or more devices. Multiple params can be passed like `id=31&id=42` (optional)
unique_id = 'unique_id_example' # str | To fetch one or more devices. Multiple params can be passed like `uniqueId=333331&uniqieId=44442` (optional)

try:
    # Fetch a list of Devices
    api_response = api_instance.devices_get(all=all, user_id=user_id, id=id, unique_id=unique_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Can only be used by admins or managers to fetch all entities | [optional] 
 **user_id** | **int**| Standard users can use this only with their own _userId_ | [optional] 
 **id** | **int**| To fetch one or more devices. Multiple params can be passed like &#x60;id&#x3D;31&amp;id&#x3D;42&#x60; | [optional] 
 **unique_id** | **str**| To fetch one or more devices. Multiple params can be passed like &#x60;uniqueId&#x3D;333331&amp;uniqieId&#x3D;44442&#x60; | [optional] 

### Return type

[**list[Device]**](Device.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_accumulators_put**
> devices_id_accumulators_put(id, body)

Update total distance and hours of the Device

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.DeviceAccumulators() # DeviceAccumulators | 

try:
    # Update total distance and hours of the Device
    api_instance.devices_id_accumulators_put(id, body)
except ApiException as e:
    print("Exception when calling DefaultApi->devices_id_accumulators_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DeviceAccumulators**](DeviceAccumulators.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_delete**
> devices_id_delete(id)

Delete a Device

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a Device
    api_instance.devices_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->devices_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_put**
> Device devices_id_put(id, body)

Update a Device

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.Device() # Device | 

try:
    # Update a Device
    api_response = api_instance.devices_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devices_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Device**](Device.md)|  | 

### Return type

[**Device**](Device.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_post**
> Device devices_post(body)

Create a Device

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Device() # Device | 

try:
    # Create a Device
    api_response = api_instance.devices_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devices_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Device**](Device.md)|  | 

### Return type

[**Device**](Device.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drivers_get**
> list[Driver] drivers_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)

Fetch a list of Drivers

Without params, it returns a list of Drivers the user has access to

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
all = true # bool | Can only be used by admins or managers to fetch all entities (optional)
user_id = 56 # int | Standard users can use this only with their own _userId_ (optional)
device_id = 56 # int | Standard users can use this only with _deviceId_s, they have access to (optional)
group_id = 56 # int | Standard users can use this only with _groupId_s, they have access to (optional)
refresh = true # bool |  (optional)

try:
    # Fetch a list of Drivers
    api_response = api_instance.drivers_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->drivers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Can only be used by admins or managers to fetch all entities | [optional] 
 **user_id** | **int**| Standard users can use this only with their own _userId_ | [optional] 
 **device_id** | **int**| Standard users can use this only with _deviceId_s, they have access to | [optional] 
 **group_id** | **int**| Standard users can use this only with _groupId_s, they have access to | [optional] 
 **refresh** | **bool**|  | [optional] 

### Return type

[**list[Driver]**](Driver.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drivers_id_delete**
> drivers_id_delete(id)

Delete a Driver

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a Driver
    api_instance.drivers_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->drivers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drivers_id_put**
> Driver drivers_id_put(id, body)

Update a Driver

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.Driver() # Driver | 

try:
    # Update a Driver
    api_response = api_instance.drivers_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->drivers_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Driver**](Driver.md)|  | 

### Return type

[**Driver**](Driver.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drivers_post**
> Driver drivers_post(body)

Create a Driver

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Driver() # Driver | 

try:
    # Create a Driver
    api_response = api_instance.drivers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->drivers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Driver**](Driver.md)|  | 

### Return type

[**Driver**](Driver.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_id_get**
> Event events_id_get(id)



### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.events_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->events_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Event**](Event.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geofences_get**
> list[Geofence] geofences_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)

Fetch a list of Geofences

Without params, it returns a list of Geofences the user has access to

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
all = true # bool | Can only be used by admins or managers to fetch all entities (optional)
user_id = 56 # int | Standard users can use this only with their own _userId_ (optional)
device_id = 56 # int | Standard users can use this only with _deviceId_s, they have access to (optional)
group_id = 56 # int | Standard users can use this only with _groupId_s, they have access to (optional)
refresh = true # bool |  (optional)

try:
    # Fetch a list of Geofences
    api_response = api_instance.geofences_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geofences_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Can only be used by admins or managers to fetch all entities | [optional] 
 **user_id** | **int**| Standard users can use this only with their own _userId_ | [optional] 
 **device_id** | **int**| Standard users can use this only with _deviceId_s, they have access to | [optional] 
 **group_id** | **int**| Standard users can use this only with _groupId_s, they have access to | [optional] 
 **refresh** | **bool**|  | [optional] 

### Return type

[**list[Geofence]**](Geofence.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geofences_id_delete**
> geofences_id_delete(id)

Delete a Geofence

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a Geofence
    api_instance.geofences_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->geofences_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geofences_id_put**
> Geofence geofences_id_put(id, body)

Update a Geofence

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.Geofence() # Geofence | 

try:
    # Update a Geofence
    api_response = api_instance.geofences_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geofences_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Geofence**](Geofence.md)|  | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geofences_post**
> Geofence geofences_post(body)

Create a Geofence

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Geofence() # Geofence | 

try:
    # Create a Geofence
    api_response = api_instance.geofences_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geofences_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Geofence**](Geofence.md)|  | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get**
> list[Group] groups_get(all=all, user_id=user_id)

Fetch a list of Groups

Without any params, returns a list of the Groups the user belongs to

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
all = true # bool | Can only be used by admins or managers to fetch all entities (optional)
user_id = 56 # int | Standard users can use this only with their own _userId_ (optional)

try:
    # Fetch a list of Groups
    api_response = api_instance.groups_get(all=all, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Can only be used by admins or managers to fetch all entities | [optional] 
 **user_id** | **int**| Standard users can use this only with their own _userId_ | [optional] 

### Return type

[**list[Group]**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_delete**
> groups_id_delete(id)

Delete a Group

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a Group
    api_instance.groups_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_put**
> Group groups_id_put(id, body)

Update a Group

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.Group() # Group | 

try:
    # Update a Group
    api_response = api_instance.groups_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_post**
> Group groups_post(body)

Create a Group

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Group() # Group | 

try:
    # Create a Group
    api_response = api_instance.groups_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_get**
> list[Maintenance] maintenance_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)

Fetch a list of Maintenance

Without params, it returns a list of Maintenance the user has access to

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
all = true # bool | Can only be used by admins or managers to fetch all entities (optional)
user_id = 56 # int | Standard users can use this only with their own _userId_ (optional)
device_id = 56 # int | Standard users can use this only with _deviceId_s, they have access to (optional)
group_id = 56 # int | Standard users can use this only with _groupId_s, they have access to (optional)
refresh = true # bool |  (optional)

try:
    # Fetch a list of Maintenance
    api_response = api_instance.maintenance_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maintenance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Can only be used by admins or managers to fetch all entities | [optional] 
 **user_id** | **int**| Standard users can use this only with their own _userId_ | [optional] 
 **device_id** | **int**| Standard users can use this only with _deviceId_s, they have access to | [optional] 
 **group_id** | **int**| Standard users can use this only with _groupId_s, they have access to | [optional] 
 **refresh** | **bool**|  | [optional] 

### Return type

[**list[Maintenance]**](Maintenance.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_id_delete**
> maintenance_id_delete(id)

Delete a Maintenance

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a Maintenance
    api_instance.maintenance_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->maintenance_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_id_put**
> Maintenance maintenance_id_put(id, body)

Update a Maintenance

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.Maintenance() # Maintenance | 

try:
    # Update a Maintenance
    api_response = api_instance.maintenance_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maintenance_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Maintenance**](Maintenance.md)|  | 

### Return type

[**Maintenance**](Maintenance.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_post**
> Maintenance maintenance_post(body)

Create a Maintenance

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Maintenance() # Maintenance | 

try:
    # Create a Maintenance
    api_response = api_instance.maintenance_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maintenance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Maintenance**](Maintenance.md)|  | 

### Return type

[**Maintenance**](Maintenance.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_get**
> list[Notification] notifications_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)

Fetch a list of Notifications

Without params, it returns a list of Notifications the user has access to

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
all = true # bool | Can only be used by admins or managers to fetch all entities (optional)
user_id = 56 # int | Standard users can use this only with their own _userId_ (optional)
device_id = 56 # int | Standard users can use this only with _deviceId_s, they have access to (optional)
group_id = 56 # int | Standard users can use this only with _groupId_s, they have access to (optional)
refresh = true # bool |  (optional)

try:
    # Fetch a list of Notifications
    api_response = api_instance.notifications_get(all=all, user_id=user_id, device_id=device_id, group_id=group_id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Can only be used by admins or managers to fetch all entities | [optional] 
 **user_id** | **int**| Standard users can use this only with their own _userId_ | [optional] 
 **device_id** | **int**| Standard users can use this only with _deviceId_s, they have access to | [optional] 
 **group_id** | **int**| Standard users can use this only with _groupId_s, they have access to | [optional] 
 **refresh** | **bool**|  | [optional] 

### Return type

[**list[Notification]**](Notification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_delete**
> notifications_id_delete(id)

Delete a Notification

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a Notification
    api_instance.notifications_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_put**
> Notification notifications_id_put(id, body)

Update a Notification

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.Notification() # Notification | 

try:
    # Update a Notification
    api_response = api_instance.notifications_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Notification**](Notification.md)|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_post**
> Notification notifications_post(body)

Create a Notification

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Notification() # Notification | 

try:
    # Create a Notification
    api_response = api_instance.notifications_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Notification**](Notification.md)|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_test_post**
> notifications_test_post()

Send test notification to current user via Email and SMS

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))

try:
    # Send test notification to current user via Email and SMS
    api_instance.notifications_test_post()
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_test_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_types_get**
> list[NotificationType] notifications_types_get()

Fetch a list of available Notification types

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))

try:
    # Fetch a list of available Notification types
    api_response = api_instance.notifications_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NotificationType]**](NotificationType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_delete**
> permissions_delete(body)

Unlink an Object from another Object

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Permission() # Permission | 

try:
    # Unlink an Object from another Object
    api_instance.permissions_delete(body)
except ApiException as e:
    print("Exception when calling DefaultApi->permissions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Permission**](Permission.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_post**
> Permission permissions_post(body)

Link an Object to another Object

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Permission() # Permission | 

try:
    # Link an Object to another Object
    api_response = api_instance.permissions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->permissions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Permission**](Permission.md)|  | 

### Return type

[**Permission**](Permission.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_get**
> list[Position] positions_get(device_id=device_id, _from=_from, to=to, id=id)

Fetches a list of Positions

Without any params, it returns a list of last known positions for all the user's Devices. _from_ and _to_ fields are not required with _id_

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
device_id = 56 # int | _deviceId_ is optional, but requires the _from_ and _to_ parameters when used (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z` (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z` (optional)
id = 56 # int | To fetch one or more positions. Multiple params can be passed like `id=31&id=42` (optional)

try:
    # Fetches a list of Positions
    api_response = api_instance.positions_get(device_id=device_id, _from=_from, to=to, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| _deviceId_ is optional, but requires the _from_ and _to_ parameters when used | [optional] 
 **_from** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | [optional] 
 **to** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | [optional] 
 **id** | **int**| To fetch one or more positions. Multiple params can be passed like &#x60;id&#x3D;31&amp;id&#x3D;42&#x60; | [optional] 

### Return type

[**list[Position]**](Position.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, application/gpx+xml
 - **Accept**: application/json, text/csv, application/gpx+xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_events_get**
> list[Event] reports_events_get(_from, to, device_id=device_id, group_id=group_id, type=type)

Fetch a list of Events within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
to = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
device_id = [56] # list[int] |  (optional)
group_id = [56] # list[int] |  (optional)
type = ['type_example'] # list[str] | % can be used to return events of all types (optional)

try:
    # Fetch a list of Events within the time period for the Devices or Groups
    api_response = api_instance.reports_events_get(_from, to, device_id=device_id, group_id=group_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reports_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **device_id** | [**list[int]**](int.md)|  | [optional] 
 **group_id** | [**list[int]**](int.md)|  | [optional] 
 **type** | [**list[str]**](str.md)| % can be used to return events of all types | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_route_get**
> list[Position] reports_route_get(_from, to, device_id=device_id, group_id=group_id)

Fetch a list of Positions within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
to = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
device_id = [56] # list[int] |  (optional)
group_id = [56] # list[int] |  (optional)

try:
    # Fetch a list of Positions within the time period for the Devices or Groups
    api_response = api_instance.reports_route_get(_from, to, device_id=device_id, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reports_route_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **device_id** | [**list[int]**](int.md)|  | [optional] 
 **group_id** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**list[Position]**](Position.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_stops_get**
> list[ReportStops] reports_stops_get(_from, to, device_id=device_id, group_id=group_id)

Fetch a list of ReportStops within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
to = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
device_id = [56] # list[int] |  (optional)
group_id = [56] # list[int] |  (optional)

try:
    # Fetch a list of ReportStops within the time period for the Devices or Groups
    api_response = api_instance.reports_stops_get(_from, to, device_id=device_id, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reports_stops_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **device_id** | [**list[int]**](int.md)|  | [optional] 
 **group_id** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**list[ReportStops]**](ReportStops.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_summary_get**
> list[ReportSummary] reports_summary_get(_from, to, device_id=device_id, group_id=group_id)

Fetch a list of ReportSummary within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
to = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
device_id = [56] # list[int] |  (optional)
group_id = [56] # list[int] |  (optional)

try:
    # Fetch a list of ReportSummary within the time period for the Devices or Groups
    api_response = api_instance.reports_summary_get(_from, to, device_id=device_id, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reports_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **device_id** | [**list[int]**](int.md)|  | [optional] 
 **group_id** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**list[ReportSummary]**](ReportSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_trips_get**
> list[ReportTrips] reports_trips_get(_from, to, device_id=device_id, group_id=group_id)

Fetch a list of ReportTrips within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
to = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
device_id = [56] # list[int] |  (optional)
group_id = [56] # list[int] |  (optional)

try:
    # Fetch a list of ReportTrips within the time period for the Devices or Groups
    api_response = api_instance.reports_trips_get(_from, to, device_id=device_id, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reports_trips_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **device_id** | [**list[int]**](int.md)|  | [optional] 
 **group_id** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**list[ReportTrips]**](ReportTrips.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_get**
> Server server_get()

Fetch Server information

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))

try:
    # Fetch Server information
    api_response = api_instance.server_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->server_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Server**](Server.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_put**
> Server server_put(body)

Update Server information

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.Server() # Server | 

try:
    # Update Server information
    api_response = api_instance.server_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->server_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Server**](Server.md)|  | 

### Return type

[**Server**](Server.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_delete**
> session_delete()

Close the Session

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))

try:
    # Close the Session
    api_instance.session_delete()
except ApiException as e:
    print("Exception when calling DefaultApi->session_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_get**
> User session_get(token=token)

Fetch Session information

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
token = 'token_example' # str |  (optional)

try:
    # Fetch Session information
    api_response = api_instance.session_get(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->session_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_post**
> User session_post(email, password)

Create a new Session

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
email = 'email_example' # str | 
password = 'password_example' # str | 

try:
    # Create a new Session
    api_response = api_instance.session_post(email, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->session_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **password** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get**
> list[Statistics] statistics_get(_from, to)

Fetch server Statistics

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
to = '2013-10-20T19:20:30+01:00' # datetime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

try:
    # Fetch server Statistics
    api_response = api_instance.statistics_get(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->statistics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **datetime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 

### Return type

[**list[Statistics]**](Statistics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> list[User] users_get(user_id=user_id)

Fetch a list of Users

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
user_id = 'user_id_example' # str | Can only be used by admin or manager users (optional)

try:
    # Fetch a list of Users
    api_response = api_instance.users_get(user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Can only be used by admin or manager users | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_delete**
> users_id_delete(id)

Delete a User

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a User
    api_instance.users_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->users_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_put**
> User users_id_put(id, body)

Update a User

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
id = 56 # int | 
body = TraccarClient.User() # User | 

try:
    # Update a User
    api_response = api_instance.users_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> User users_post(body)

Create a User

### Example
```python
from __future__ import print_function
import time
import TraccarClient
from TraccarClient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = TraccarClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TraccarClient.DefaultApi(TraccarClient.ApiClient(configuration))
body = TraccarClient.User() # User | 

try:
    # Create a User
    api_response = api_instance.users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

