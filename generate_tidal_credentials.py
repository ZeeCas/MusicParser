#!/usr/bin/env python

import tidalapi

session = tidalapi.Session()
session.login_oauth_simple()

token_type = session.token_type
access_token = session.access_token
refresh_token = session.refresh_token # Not needed if you don't care about refreshing
expiry_time = session.expiry_time

with open("token.txt", "w") as f:
      f.write(f"{token_type}\n{access_token}\n{refresh_token}\n{expiry_time}")