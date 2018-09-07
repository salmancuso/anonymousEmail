import subprocess

emailSubject = "This is only a test"
emailBody = "Hello World"
toAddress = "spm71@mac.com"
fromAddress = "DonaldTrump@alkfajdadfadff.com"
command = """echo '{0}' | mail -s '{1}' {2} -aFrom:{3}""".format(emailBody, emailSubject, toAddress, fromAddress)
print (command)
subprocess.call([command], shell=True)
