#!/usr/bin/env python3

from vapi_python import Vapi

PUBLIC_KEY = "e5587e95-3824-412a-a40b-e897f4e8291c"

vapi = Vapi(api_key=PUBLIC_KEY)

vapi.start(assistant_id='6cb7fd55-abdb-4bde-ab8b-c593e967c9a3')
