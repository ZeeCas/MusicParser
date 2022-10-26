#!/usr/bin/env python

import tidalapi

session = tidalapi.Session() # Create a session
session.login_oauth_simple() # Login to Tidal

token_type = session.token_type
access_token = session.access_token
refresh_token = session.refresh_token # Assign the token to variables
expiry_time = session.expiry_time

with open("token.txt", "w") as f:
      f.write(f"{token_type}\n{access_token}\n{refresh_token}\n{expiry_time}") # Write the token to token.txt