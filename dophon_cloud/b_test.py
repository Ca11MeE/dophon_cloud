import threading

from flask import jsonify

from dophon_cloud import enhance
import time
b = enhance(import_name=__name__,
            properties={'111': 'aaa', 'service_name': 'dxh-service', 'host': '0.0.0.0', 'port': 81,
                        'reg_url': 'http://127.0.0.1:8301/reg/service/'})

@b.route('/test/test1')
def test():
    time.sleep(10)  # 阻塞10秒
    return jsonify({'msg': 'b服务被调用'})

threading.Thread(target=b.run).start()