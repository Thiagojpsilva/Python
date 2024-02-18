import requests
import sys
import xml.etree.ElementTree as ET


def call_api_ocs(acesso):

    url = "<URL>"
    querystring = {"": ""}
    payload = "payload"
    headers = {
        "Content-Type": "text/xml",
        "charset": "utf-8"
    }
    response = requests.request(
        "POST", url, data=payload, headers=headers, params=querystring)
    match = response.text

    if "Operation successfully." in match:
       # print("Existe")

        xml_val = match.encode('utf-8')
        root = ET.fromstring(xml_val)

        namespaces = {
            'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
            'bcs': 'http://www.huawei.com/bme/cbsinterface/bcservices',
            'cbs': 'http://www.huawei.com/bme/cbsinterface/cbscommon',
            'bcc': 'http://www.huawei.com/bme/cbsinterface/bccommon'
        }

        offering_id = root.find(
            './/bcs:Subscriber/bcs:PrimaryOffering/bcc:OfferingKey/bcc:OfferingID', namespaces).text
        # state = root.find('.//bcs:Subscriber/bcs:PrimaryOffering/bcc:Status', namespaces).text
        state = root.find(
            './/bcs:Subscriber/bcs:SubscriberInfo/bcc:Status', namespaces).text
        try:
            activation_time = root.find(
                './/bcs:Subscriber/bcs:SubscriberInfo/bcs:ActivationTime', namespaces).text
        except AttributeError:
            activation_time = '0'

        installation_time = root.find(
            './/bcs:Subscriber/bcs:PrimaryOffering/bcc:EffectiveTime', namespaces).text

        sub_identities = []

        for i in range(6):
            try:
                arg = './/bcs:Subscriber/bcs:SubscriberInfo/bcc:SubIdentity/['+str(
                    i)+']/bcc:SubIdentity'
                sub_identity = root.find(arg, namespaces).text
            except AttributeError:
                sub_identity = '0'
            sub_identities.append(sub_identity)

        SubIdentity1, SubIdentity2, SubIdentity3, SubIdentity4, SubIdentity5, SubIdentity6 = sub_identities

        values = [SubIdentity1, SubIdentity2, SubIdentity3,
                  SubIdentity4, SubIdentity5, SubIdentity6]

        IMSI = next((value for value in values if len(value) == 15), 0)
        ICCID = next((value for value in values if len(value) == 20), 0)

        return ("Existe", offering_id, state, IMSI, ICCID, installation_time, activation_time)

    elif "does not exist." in match:
        return ("Inexistente", "0", "0", "0", "0", "0", "0")

    else:
        return ("Falha", "0", "0", "0", "0", "0", "0")


msisdn_in = sys.argv[1]

return_list = []
return_list = call_api_ocs(msisdn_in)
print(msisdn_in, return_list[0], return_list[1], return_list[2],
      return_list[3], return_list[4], return_list[5], return_list[6])
