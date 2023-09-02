import imapclient
import pyzmail

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
rec_email = "hamzanasr412@gmail.com"
password = input(str("Please enter your pasword: "))

imapObj.login(rec_email, password)
import pprint
pprint.pprint(imapObj.list_folders())

imapObj.select_folder('INBOX', readonly=True)

UIOs = imapObj.search(['ALL'])
print(UIOs)

rowMessage = imapObj.fetch(UIOs, ['BODY[]'])
# pprint.pprint(rowMessage)
message = pyzmail.PyzMessage.factory(rowMessage[507][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))

print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part.get_payload().decode(message.text_part.charset))

imapObj.logout()