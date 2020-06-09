# Copyright 2014 Eric Heydenberk
# Copyright 2017 Adrien Vergé

Summary:   A headless WebKit browser with a full JavaScript API.
Name:      phantomjs
Version:   1.9.7
License:   BSD
Release:   1%{?dist}
Source:    https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2

Requires:  fontconfig freetype libfreetype.so.6 libfontconfig.so.1 libstdc++.so.6

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep
%setup -n phantomjs-1.9.7-linux-x86_64 -q

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
