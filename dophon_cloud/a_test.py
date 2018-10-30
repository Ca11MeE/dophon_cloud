import threading

from flask import jsonify

from dophon_cloud import enhance, micro_cell_list

a = enhance(import_name=__name__,
            properties={'111': 'aaa', 'service_name': 'dxh-service', 'host': '0.0.0.0', 'port': 80,
                        'reg_url': 'http://127.0.0.1:8301/reg/service/'})

m_c_list = micro_cell_list(a, properties={
    'dxh-service': [
        {
            '/test': [
                '/test1'
            ]
        }
    ],
    'xxx-service': [
        {
            '/c/test': [
                '/another/test'
            ]
        }
    ]
})

@a.route('/b')
def enter_b():
    result = m_c_list.request('dxh-service', ['/test', '/test1'])
    print(result)
    return jsonify(result)

@a.route('/c')
def enter_c():
    result = m_c_list.request('xxx-service', ['/c/test', '/another/test'])
    print(result)
    return jsonify(result)

threading.Thread(target=a.run).start()
