eget is a wget like downloader wrapper. It supports download urls with wildcard.

It supports wget or curl as backend.

Options:
-q       - quiet mode"

-k|--no-check-certificate - skip SSL certificate chain support"

-U|-A|--user-agent - send browser like UserAgent"

-O file  - download to this file (use filename from server if missed)"

--list   - print files from url with mask"

--latest - print only latest version of file"


Examples:
  $ eget http://example.com/e/* - download all files in e/ dir
  $ eget http://example.com/list *.txt - download all *.txt files listed at list page
  $ eget --list --latest https://github.com/deemru/chromium-gost/releases "chromium-gost-*linux-*" - download latest release by mask

See also:

https://github.com/zyedidia/eget

https://github.com/yuwancumian/eget
