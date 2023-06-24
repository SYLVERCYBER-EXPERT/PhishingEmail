"""
Python Phishing Email 
Purpose: Python-powered authomatic phishing email program.

Author: Benjamin Sylvester
Date: 21/20/2023
version 1.0
"""
import argparse

def argument_parser():
	"""allow user to specify target host and port"""
	parser = argparse.ArgumentParser(description="Take a pre-crafted Html email, autimatically replace the links with"
							"the desired address, and send the email.") 
	parser.add_argument("server", help="SMTP server that will send the email")
	parser.add_argument("port", help="SMTP server port number)
	parser.add_argument("username", help="username for the SMTP server")
	parser.add_argument("password", help="Password for the SMTP server")
	parser.add_argument("email", help="Pre-crafted email location")
	parser.add_argument("url", help="URL that will replace all link in the email")
	parser.add_argument("subject", help="Email subject")
	parser.add_argument("sender", help="Email sender")
	parser.add_argument("sendto", help="Target email address")
	Parser.add_argument("--tls", help"default=false, help="Attempt to use ssl/TLS^)
	
	var_args = vars(parse.parse_args()) #convert argument namespace to dictionary
	return var_args

def open_email_file(email_file):
	"""Open the Html-formation email file"""
	with open(email_file, 'r') as open_email:
		email_html = open_email.read()
	return email_html
def replac_links(url, message):
	"""Replace the visible email links with the desired URL.""""
	html_regex = re.compile(r'href=[\'"]?([^\'">]+)')
	html_output = html_regex.sub("href=\£{}".format(url), message)
	return html_output
def mine_message(email_subj, send_to, send_from, Html_email):
	"""Format the email message"""
	msg = MIMEMultipart('alternative')
	msg['To'] = send_to
	msg["From"] = send_from
	msg["Subject"] = email_subj
	msg.attach(message)

	return msg.as_string()

def send_email(server, port, userrname, password, send_from, send_to, message, tls)
	"""send the email to the email server"""
	pint("[+] Attempting to connect to server")
	start_server = smtplib.SMTP(server, port)
	if tls:
		print("[+] Attempting to use STARTTLS")
		start_server.starttls()
	print("[+] Attempting to say Hello")
	start_server.login(username, password)
	print("[+] Attempting to send mail")
	start_server.sendmail(send_from, send_to, message)
	print("[+] Done...")
	start_server.quite()

def go_phishing(server, port, username, password, email_loc, url_replace, subj, send_from, send_to, tls):
	"""tie everything together"""
	htnl_email = open_email_file(email_loc)
	html_output = replace_links(url_replace, html_output)
	message = mime_message(subj, send_to, send_from, html_email)
	send_email(server, port, username, password, sender, send_to, message, tls)

if __name__ == '__main__':
	try:
		user_args = argument_parser()
		email_server = user_args["server"]
		smtp_port = user_argd["port"]
		login = user_args["username"]
		pword = user_args["password"]
		email_path = user_args["email"]
		new_url = user_args["url"]
		email_subject = user_args["subject"]
		send = user_args["send"]
		receiver = user_args["sendto"]
		use_tls = user_args["tls"]
		go_phishing(email_server, smtp_port, login, pword, email_path, new_url, email_subject, sender, receiver, use_tls)
	except AttributeError:
		print("Error. Please provide the command line argument before running") 


#parameters: smtp.sendgrid.net 25 apikey SG.uc.rccl-RRGmyALisacnjeklknzcjksdclknd test_email.html https://www.gmail.com "Contract  Approval" "Attacker@gmail.com" "vitim@gmail.com"
#smtp.sendgrid.net is mailing server, in the above example we are using sendgrid.net. 25 is the port number.
#apikey is generated from the mailing server, in the above exaple it was generated from sendgrid.net
#attack your html file that contain your message, in the above example the file name is test_email.html 
#Enter to webpage you will like the vitim to be redirected to after clicking the your phishing link
#enter Email subject, in the above example the subject is " Contract approval"
# Next is the Attacker email address in ""
#Finally, the vitim email address in ""
