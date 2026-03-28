from twilio.rest import Client

#twilio credential
account_sid = "ACf9181ba3886e735e8f595299c2a231fb"
auth_token = "c72928eefd24075132b4dccbf2f9261b"

#client intilization
client = Client(account_sid, auth_token)

#send sms
message =client.messages.create(
    body="Hello World",
    from_="+18303556733",
    to="+916201263902"
)

print("message sent sussessfully")
print("message Sid :",message.sid)
