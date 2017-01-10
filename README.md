# websocket_loadtest
## 介绍
- websocket_loadtest是用python编写的一个压力测试框架，用来测试websocket协议
- 使用了[websocket-client](websocket-client)库来模拟websocket协议
- 通过python的threading库来实现多线程，模拟负载

## 使用
- 提供了两种运行模式，` mode = 1 `表示按照次数运行，` mode = 2 `表示按照时间运行
- 运行前需要安装websocket-client，命令为` pip install websocket-client`
- 根据所选模式需要配置相关参数，如果为次数运行模式，需要配置count（运行次数）、thread_count（线程数）、sleeptime（思考时间）、mode（运行模式）
- 根据所选模式需要配置相关参数，如果为时间运行模式，需要配置total_time（运行时间）、thread_count（线程数）、sleeptime（思考时间）、mode（运行模式）
- websocket的业务代码需要在websocketLogic中自行实现
- websocketLogic为模式1的执行方法；websocketLogic2为模式2的执行方法

## 效果图
![](http://ogbrn31xz.bkt.clouddn.com/QQ%E6%88%AA%E5%9B%BE20170110151513.jpg)
