import requests
import config
import logging
import http.server

def build_link(params):
    return config.U2_BASE_DOMAIN + '&'.join(params)

def replace_dl_link(content):
    return content.replace(config.U2_BASE_DOMAIN, config.MIRROR_DOMAIN)

def fetch_rss_feed(params):
    link = build_link(params)
    res = requests.get(link)
    if res.status_code == 200:
        content = res.text
        content = replace_dl_link(content)
        return content
    else:
        logging.WARNING("Error: " + str(res.status_code))

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/xml')
        self.end_headers()
        params = self.path.split("&")
        self.wfile.write(fetch_rss_feed(params).encode('utf-8'))

if __name__ == "__main__":
    server_address = ('', 43001)
    httpd = http.server.HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()