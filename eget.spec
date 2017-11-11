Name: eget
Version: 2.0
Release: alt1

Summary: wget wrapper with wildcard support

License: AGPLv3
Group: Networking/WWW
Url: https://github.com/Etersoft/eget

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/Etersoft/eget.git
Source: ftp://updates.etersoft.ru/pub/Korinf/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

Requires: wget

%description
eget is a wget wrapper. It supports download urls with wildcard.

%prep
%setup

%install
install -D eget %buildroot%_bindir/eget

%files
%_bindir/eget

%changelog
* Sat Nov 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- rewrite eget

* Fri Nov 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
