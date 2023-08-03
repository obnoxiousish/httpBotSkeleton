# httpBotSkeleton
This is using Trio &amp; HTTPX async to create a fully parallel http bot as fast as possible.

# Features

Proxy support (HTTP, HTTPS, SOCKS4, SOCKS5)
    Load from TXT into array
    Select random proxy from array
    Single rotating proxy
    Dynamic parsing

Parallelism (Trio & HTTPX)
    Choice of any "thread" count

Classes for common datatypes
    Account class
        Dynamic account parsing
    Proxy class
    Settings class

Automatic cookie handling with HTTPX Client

Default headers to a most common google chrome fingerprint

Captcha solving (Anti-captcha API, (cost per solve))

CSRF token helper

Cloudflare anti-bot solving w/ VeNoMouSNZ's cloud-scraper (only basic for free, have to pay him for the better version)

Optional Mongo account tracking
    So you dont process duplicate entries long term

Maybe:
    improved error handling
