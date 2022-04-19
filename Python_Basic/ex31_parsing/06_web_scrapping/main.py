import requests
import re

req = requests.get('http://www.columbia.edu/~fdc/sample.html')

text = req.text

result = re.findall(r'<h3 .*?>(.*?)</h3>', text)

print(result)


# COMMENT мудреный вариант
# import requests
# import re
#
# req = requests.get('http://www.columbia.edu/~fdc/sample.html')
#
# req_list = re.split('\n', req.text)
#
# h_list = []
#
# for i_line in req_list:
#     if re.search(r'</h3>', i_line):
#         workflow = re.findall(r'>.*<', i_line)
#         workflow = workflow[0].replace('>', '', 1)
#         workflow = workflow.replace('<', '', 1)
#         h_list.append(workflow)
#
# print(h_list)