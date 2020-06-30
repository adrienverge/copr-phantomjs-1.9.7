# Copyright 2014 Eric Heydenberk
# Copyright 2017 Adrien Vergé

Summary:   A headless WebKit browser with a full JavaScript API.
Name:      phantomjs
Version:   1.9.7
License:   BSD
Release:   3%{?dist}
Source:    https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2

Requires:  fontconfig
Requires:  freetype
Requires:  libfreetype.so.6
Requires:  libfontconfig.so.1
Requires:  libstdc++.so.6
%if 0%{?el8}
Requires:  compat-openssl10
%endif

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep
%setup -n phantomjs-1.9.7-linux-x86_64 -q
# The pre-compiled PhantomJS binary used in this package dates from 2014 and is
# linked to use libcrypto.so and libssl.so from OpenSSL 1.0, but does not
# specify their version (e.g. libcrypto.so.1.0.0). Hence, running PhantomJS
# crashes (segmentation fault) on systems with OpenSSL 1.1 installed, because
# libcrypto.so and libssl.so refer to the new version 1.1. Removing
# /lib64/libssl.so from the system removes the crash, but of course it's not a
# real fix. I've tried multiple solutions including using LD_PRELOAD or
# patchelf, but the only working I've found is to alter PhantomJS binary to make
# it fail loading libcrypto.so and libssl.so. This is it:
test "$(dd if=bin/phantomjs bs=1 skip=$((0x01ca2c53)) count=6 status=none)" = "crypto"
printf "xxxxxx" | dd of=bin/phantomjs bs=1 seek=$((0x01ca2c53)) count=6 conv=notrunc

%install
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{_prefix}/share/phantomjs/examples
cp bin/phantomjs %{buildroot}%{_prefix}/bin/phantomjs
cp examples/* %{buildroot}%{_prefix}/share/phantomjs/examples/
cp ChangeLog %{buildroot}%{_prefix}/share/phantomjs/
cp LICENSE.BSD %{buildroot}%{_prefix}/share/phantomjs/
cp README.md %{buildroot}%{_prefix}/share/phantomjs/

%files
%defattr(0444,root,root)
%attr(0555,root,root)%{_prefix}/bin/phantomjs
%{_prefix}/share/phantomjs/ChangeLog
%{_prefix}/share/phantomjs/examples/*.coffee
%{_prefix}/share/phantomjs/examples/*.js
%{_prefix}/share/phantomjs/LICENSE.BSD
%{_prefix}/share/phantomjs/README.md

%changelog
* Tue Jun 30 2020 Adrien Vergé <adrienverge@gmail.com> 1.9.7-3
- Require OpenSSL 1.0 on CentOS 8, otherwise crash

* Fri Jun 12 2020 Adrien Vergé <adrienverge@gmail.com> 1.9.7-2
- Fix incompatibility with OpenSSL 1.1

* Tue Jan 31 2017 Adrien Vergé <adrienverge@gmail.com> 1.9.7-1
- Package for copr

* Fri Apr 18 2014 Eric Heydenberk <heydenberk@gmail.com>
- add missing filenames for examples to files section

* Tue Apr 30 2013 Eric Heydenberk <heydenberk@gmail.com>
- add missing filenames for examples to files section

* Wed Apr 24 2013 Robin Helgelin <lobbin@gmail.com>
- updated to version 1.9

* Thu Jan 24 2013 Matthew Barr <mbarr@snap-interactive.com>
- updated to version 1.8

* Thu Nov 15 2012 Jan Schaumann <jschauma@etsy.com>
- first rpm version
