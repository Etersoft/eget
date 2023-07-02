# eget is a wget like downloader wrapper

eget - wget like downloader wrapper with wildcard support in filename part of URL

It supports download urls with wildcard. It supports wget or curl as backend.

In common case you can install it via command
```
epm ei eget
```
Check https://github.com/Etersoft/eepm for universal instruction how to install epm on your distro.

Basic usage:
```
eget [options] http://somesite.ru/dir/file.log
```
or with wildcard in filename:
```
eget [options] http://somesite.ru/dir/na*.log
```
or with file mask for site page search:
```
eget [options] http://somesite.ru/page na*.log
```
latest form will retrieve the site page source, search for ahref with file by file mask and print out found url(s).

Options:
```
    -q                        - quiet mode
    -k|--no-check-certificate - skip SSL certificate chain support
    -U|-A|--user-agent        - send browser like UserAgent
    -4|--ipv4|--inet4-only    - use only IPV4
    -6|--ipv6|--inet6-only    - use only IPV6
    -O-|-O -                  - output downloaded file to stdout
    -O file                   - download to this file
    --latest                  - print only latest version of a file
    --second-latest           - print only second to latest version of a file
    --allow-mirrors           - check mirrors if url is not accessible
 
    --list|--list-only        - print only URLs
    --check URL               - check if the URL is accessible (returns HTTP 200 OK)
    --get-response URL        - get response with all headers (ever if HEAD is not acceptable)
    --get-filename URL        - print filename for the URL (via Content-Disposition if applicable)
    --get-real-url URL        - print URL after all redirects
```

Supported URLs:
```
ftp:// http:// https:// file:/ ipfs://
```

Supported backends (set like EGET_BACKEND=curl)
```
wget curl (todo: aria2c)
```

## Examples:
```
$ eget http://example.com/e/* - download all files in e/ dir
$ eget http://example.com/list *.txt - download all *.txt files listed at list page
$ eget --list --latest https://github.com/deemru/chromium-gost/releases "chromium-gost-*linux-*" - download latest release by mask
$ eget https://github.com/owner/project package*.ext
$ eget -O myname ipfs://QmVRUjnsnxHWkjq91KreCpUk4D9oZEbMwNQ3rzdjwND5dR
$ eget --check http://ftp.somesite.ru/test
```

## IPFS usage:

Download file from IPFS:
```
$ eget [-O filename ] ipfs://QmYwf2GAMvHxfFiUFL2Mr6KUG6QrDiupqGc8ms785ktaYw
```
or URL with filename 
```
$ eget ipfs://QmXpKuc3NHFuyjd7fGgxKQVewZZ6V1iDECHCRPxAcQ9q2E?filename=brave-browser-beta-1.51.84-1.x86_64.rpm
```

just download as regular file.

## Usage EGET IPFS DB:
```
$ EGET_IPFS_DB=/path/to/file.txt eget http://somesite.ru/somefile.dat
```

if the URL already exists in EGET IPFS DB, it will download via IPFS, otherwise it will download in a usual way and put to IPFS and EGET IPFS DB after it.

## IPFS related environment variables:
```
EGET_IPFS={disabled,auto,brave,local,gateway}
```
disabled by default (auto if EGET_IPFS_DB is set)
auto will check brave, local, gateway

```
EGET_IPFS_DB=/path/to/file.txt
```
file with text database of URL CID filename accordance

```
EGET_IPFS_API=
```
set IPFS api for ipfs command, by default `/ip4/127.0.0.1/tcp/5001`

```
EGET_IPFS_GATEWAY=
```
http(s) gateway for download ipfs if there is no ipfs command and local sources
default: https://cloudflare-ipfs.com/ipfs

# Common environment variables:
```
EGET_BACKEND= curl or wget
```

See also:

https://wiki.debian.org/debian/watch

https://github.com/zyedidia/eget

https://github.com/yuwancumian/eget
