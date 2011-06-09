=====
Usage
=====

Sample usage:::

    >>> from zbxsend import Metric, send_to_zabbix    
    >>> send_to_zabbix([Metric('localhost', 'bucks_earned', 99999)], 'localhost', 10051)
