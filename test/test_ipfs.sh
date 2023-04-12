#!/bin/sh

export EGET_IPFS_DB=/var/lib/eepm/eget-ipfs-db.txt

check_ok()
{
    echo "$ $*"
    ../$* && echo "   OK" || echo "FAILED"
}

check_ok eget --check https://cloudflare-ipfs.com/ipfs/QmYwf2GAMvHxfFiUFL2Mr6KUG6QrDiupqGc8ms785ktaYw

check_ok eget --check https://cloudflare-ipfs.com
