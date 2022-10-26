# Main Idea
1. Take in a playlist or track link (Youtube, Spotify, Tidal, Soundcloud)
2. Parse it using the services API
3. Return a human-readable text format of the playlist including youtube links for each song with meta datas (length, artist, etc)
4. ???
5. Profit

# Usage
Place Youtube and Spotify credentials in your ".env" file.
Run "generate_tidal_credentials.py" to initialize your credentials for Tidal.

# Status
Currently : Youtube, Spotify, and Tidal playlists can be extracted and converted to a text format of each track/artist. Having trouble with google API quotas, I imagine its a loop issue. Youtube, Spotify, Tidal, and Soundcloud track resolution to plaintext should work without issue.

