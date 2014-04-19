import os
import smtplib

from ConfigParser import SafeConfigParser



def send_mail(subject, body, rctps=None):
	username='xxx'
	password ='xxx' 
	if rctps is None:
		rctps = parser.get('email', 'recipients').split(',')
		
	str_all_mails = ', '.join(rctps)
	headers = ["From: " + username,
		       "Subject: " + subject,
		       "To: " + str_all_mails,
		       "MIME-Version: 1.0",
               "Content-Type: text/html"]
	headers = "\r\n".join(headers)
	
	try:
		server_mail= 'smtp.gmail.com:587'
		server = smtplib.SMTP(server_mail)
		server.starttls()		
		server.login(username, password)
		server.sendmail(from_addr=username, to_addrs=rctps,
		msg=(headers + "\r\n\r\n" + body))		
		server.quit()
	except smtplib.SMTPException as e:
		log.error("Error: unable to send email %s", str(e))

send_mail('hello thanhnt','so stupid', ['ngtthanh1010@gmail.com'])