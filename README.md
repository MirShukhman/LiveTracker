Live Traker

After deplying my previous projects in containers on Azure, I was presented with issue:
I need to be able to track that my containers are running properly and on the known IP addresses, 
as I had a container unexpectadly crash and rebuild itself on a new IP address. I had to ensure smooth
sailing as it is important for my potential emplyers to see my projects live, and I was uninterested to pay 
for a higher tier Azure subscription to do so for me or ensure that IP stays intact. 


So I wrote this nifty little traker that runs on my local machine and twice a day enters my projects' IP, 
preforms actions that I know will ensure that all components of the app are up and running (bd, backend and frontend) 
and sends me an email report. 


Note to self: for ruture projects leave a hook url to preform such checks more easely, instead of searching witch
 buttons it will be best to click retroactivly.