# General
debug_mode = True

# Postgresql
postgresql = 'postgresql://rcomp:password@localhost/rcomp'

# API Keys
riot_api_key = 'RGAPI-a1e35343-f66e-4756-80b7-646b0d7283e3'
championgg_api_key = 'e31f13db144c076cfff59aaa189da26e'

# Discord
discord_prefix = '!'
discord_token = 'NTIxMTYzMjg0NDE4Nzg5Mzc2.Du4axQ.fye4-oAQJy3SEob4Q7afMoL7fOo'
discord_emoji_pool_guild_ids = [
    528327713438826497,
    528327793843503156,
    528327910017335296,
    528327968838123520,
    528328028095512576,
    528328084227883050,
    528329259035656215,
    528329316124327936,
    528329366250323968,
    528329414275235870,
    528329453550436363,
    528329503790071818,
    528329549956513792,
    528329600842072065,
]

# OAuth2 for requesting access to a users connections
DISCORD_CLIENT_SECRET = 'kpyepL2xrOQ2d1dq5QbEPh0WuVh9ss9B'
DISCORD_REDIRECT_URI = 'http://localhost:5006/callback' # This must be registered to the application
SCOPES = ['identify', 'connections']
OAUTH2_PORT = 5006
