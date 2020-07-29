import json
import requests

sfdc_url = input_data.get('sfdc-url', "")
booking_amount = input_data.get('booking_amount', "Not specified")

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
webhook_url = '<slack webhook url>'
slack_data = {
    "attachments": [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": "#EC1075",
            "title": "New Deal Closed!",
            "title_link": "https://<domain>.my.salesforce.com/{}".format(sfdc_url),
            "text": ":h1five: to {}".format(input_data['rep']),
            "image_url": "{}".format(input_data['gong']),
            "fields": [{
                "title": "{}".format(input_data['name']),
                "value": "Booking Amount: ${0}\nCompany: {1}\nOrder Type: {2}".format(booking_amount, input_data['team'], input_data['order_type']),
                }, {
                    "title": "Deal Team",
                    "value": "Sales Engineer: {0}\nSDR: {1}\nCS: {2}".format(input_data['sales_eng'], input_data['sdr'],input_data['cs_contact']),
                    }, {
                    "title": "Primary Competitor",
                    "value": "{}".format(input_data['competitor']),
                    }]


        }
    ]
}
print(slack_data)
response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
