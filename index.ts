import createProxyServer from 'http-proxy';
import http from 'http';

const proxy = new createProxyServer();
const server = http.createServer((req, res) => {
    const url = "https://u2.dmhy.org/";

    req.headers.referer = url;
    delete req.headers.host;
    proxy.web(req, res, {target: url});
});

proxy.on('error', function(e) {
    console.error(e);
});
server.listen(43001);