# Launchpad tools/curl
curl information and resources

# Commands
## Arguments
  * `-c` - Continue of interrupted
  * `-#` - Display progress bar

# Use Cases
## Open Ports
```
curl -v telnet://<host>:<port>
```

## Send email
```
curl --ssl-reqd --url "smtps://smtp.gmail.com:465" \
  --user "<username>@gmail.com:<password>" \
  --mail-from "<username>@gmail.com" \
  --mail-rcpt "<to@domain.com>" \
  --upload-file message.txt
```

## TFTP file upload
```
curl -T <filename> tftp://<hostname>
```

## SMB file download
```
curl -u "domain\user:pass" smb://<host>/<share>/<filename>
```

# Related Information
  * [curl man page](https://curl.se/docs/manpage.html)
  * [REQBIN curl examples](https://reqbin.com/req/c-1n4ljxb9/curl-get-request-example)
  * [Everything curl book](https://curl.se/book.html)
  * [5 uses of cuyrl that don't involve web requests](https://medium.com/geekculture/5-extra-uses-for-curl-that-dont-involve-web-requests-6780a345877f)