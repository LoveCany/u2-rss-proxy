# U2-RSS-Proxy

A simple web proxy for u2 rss feeds.

Not only proxy the RSS request, but also redirect download links to proxy site.

## Requirements

Python only. There is no third-party dependencies used.

## Installation

Get a proxy site of U2 first. For example, you can build with [Reflare](https://github.com/xiaoyang-sde/reflare), which can be deployed on CloudFlare Workers directly.

After that, modify your proxy domain in `config.py`.

## Usage

Run `python3 main.py` to start the server. Using Nginx or other web servers to proxy the server is recommended.

## Warning

Example mirror in template config is usable. However, the log is recorded in the server. It's advised to build and use your own one.