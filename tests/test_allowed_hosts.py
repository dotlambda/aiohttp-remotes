from aiohttp import web

from aiohttp_remotes import AllowedHosts


async def test_allowed_hosts_ok(test_client):
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_get('/', handler)
    app.middlewares.append(AllowedHosts({'example.com'}))
    cl = await test_client(app)
    resp = await cl.get('/', headers={'Host': 'example.com'})
    assert resp.status == 200


async def test_allowed_hosts_forbidden(test_client):
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_get('/', handler)
    app.middlewares.append(AllowedHosts({'example.com'}))
    cl = await test_client(app)
    resp = await cl.get('/', headers={'Host': 'not-allowed.com'})
    assert resp.status == 400


async def test_allowed_hosts_star(test_client):
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_get('/', handler)
    app.middlewares.append(AllowedHosts({'*'}))
    cl = await test_client(app)
    resp = await cl.get('/', headers={'Host': 'example.com'})
    assert resp.status == 200


async def test_allowed_hosts_default(test_client):
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_get('/', handler)
    app.middlewares.append(AllowedHosts())
    cl = await test_client(app)
    resp = await cl.get('/', headers={'Host': 'example.com'})
    assert resp.status == 200
