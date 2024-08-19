"""
ECS Python SDK Interface Class
"""
from ui.ecsmgmt import *


//write function tools here


def find_process_summary():
    """
    Get the ECS OS process summary.

    :returns: a dictionary of the process summary.

    :rtype: dict
    """

    summary = {}
    data = get_ecs_process_summary()
    root = ElementTree.fromstring(data)
    for item in root.findall('service-statistics'):
        for stats in item.findall('process-summary-stat'):
            for data in stats.findall('data'):
                summary[data.attrib['key']] = data.attrib['value']

    return summary
