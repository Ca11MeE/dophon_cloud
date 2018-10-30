import threading

from flask import jsonify

from dophon_cloud import enhance

c = enhance(import_name=__name__, properties={'service_name': 'xxx-service', 'host': '0.0.0.0', 'port': 8001,
                                              'reg_url': 'http://127.0.0.1:8300/reg/service/'})


@c.route('/c/test/another/test')
def another_test():
    return jsonify({'event': 200, 'msg': 'c服务被调用'})


threading.Thread(target=c.run).start()
