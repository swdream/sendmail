# Send mail from your terminal


$ lsb_release -r
Release:        12.04

## hostname
thanhnguyen@thanhnguyen:~$ hostname 
thanhnguyen


$ whatis ssmtp
ssmtp (8)            - send a message using smtp
# install ssmtp
$ apt-get install ssmtp -y 

configure for ssmtp in /etc/ssmtp

#Test
##user thanhnguyen
$ echo `send mail using ssmtp` | mail -s "TEST" ngtthanh1010@gmail.com

## for debug, using -v option
$ echo `send mail using ssmtp` | mail -v -s "TEST" ngtthanh1010@gmail.com
