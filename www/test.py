import orm
from models import User, Blog, Comment
import asyncio

async def test():
    await orm.create_pool(loop=loop, host='127.0.0.1', user='root', password='password', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

# for x in test():
#     pass

# 获取EventLoop:
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test())

#关闭EventLoop
#loop.close()
