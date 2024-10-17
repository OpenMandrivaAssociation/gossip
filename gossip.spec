%define req_loudmouth_version 1.3.4

Summary: GNOME Jabber client
Name: gossip
Version: 0.31
Release: 3
License: GPLv2+
Group: Networking/Instant messaging
URL: https://live.gnome.org/Gossip/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0: gossip-0.31-format-strings.patch
Patch1: gossip-0.31-libnotify0.7.patch
BuildRequires: loudmouth-devel >= %{req_loudmouth_version}
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libgalago)
BuildRequires: gnome-panel-devel
BuildRequires: pkgconfig(xrender)
BuildRequires: aspell-devel
BuildRequires: iso-codes
BuildRequires: scrollkeeper
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: intltool
BuildRequires: desktop-file-utils

%description
Gossip aims at making Jabber easy to use and tries to give GNOME users a
real user friendly way of chatting with their friends.

%prep
%setup -q
%patch0 -p1 -b .str
%patch1 -p0 -b .libnotify

%build
%configure2_5x

%make

%install
%makeinstall_std _ENABLE_SK=false

%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog AUTHORS
%config(noreplace) %{_sysconfdir}/sound/events/*
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/gossip
%{_datadir}/sounds/gossip
%_datadir/icons/hicolor/*/apps/*


%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.31-3mdv2011.0
+ Revision: 677723
- rebuild to add gconftool as req

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.31-2
+ Revision: 656816
- build with libnotify 0.7

* Mon Aug 03 2009 Götz Waschk <waschk@mandriva.org> 0.31-1mdv2011.0
+ Revision: 408226
- fix format strings
- update URL

* Sat Aug 02 2008 Funda Wang <fwang@mandriva.org> 0.31-1mdv2009.0
+ Revision: 260901
- update to new version 0.31

  + Michael Scherer <misc@mandriva.org>
    - new url

* Mon Jul 21 2008 Götz Waschk <waschk@mandriva.org> 0.30-1mdv2009.0
+ Revision: 239312
- new version
- update deps

* Thu May 08 2008 Götz Waschk <waschk@mandriva.org> 0.29-1mdv2009.0
+ Revision: 204539
- new version
- drop patch

* Mon Mar 17 2008 Frederic Crozat <fcrozat@mandriva.com> 0.28-3mdv2008.1
+ Revision: 188411
- Patch0 (SVN): ensure contact which are offline are not displayed in online list

* Wed Jan 23 2008 Funda Wang <fwang@mandriva.org> 0.28-2mdv2008.1
+ Revision: 156980
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 12 2007 Funda Wang <fwang@mandriva.org> 0.28-1mdv2008.1
+ Revision: 108158
- New version 0.28

* Sun Aug 19 2007 Götz Waschk <waschk@mandriva.org> 0.27-1mdv2008.0
+ Revision: 67037
- new version

* Fri Jun 01 2007 Götz Waschk <waschk@mandriva.org> 0.26-1mdv2008.0
+ Revision: 33488
- new version
- fix buildrequires

* Wed Apr 18 2007 Götz Waschk <waschk@mandriva.org> 0.24-1mdv2008.0
+ Revision: 14448
- drop legacy menu
- new version


* Sun Mar 04 2007 Götz Waschk <waschk@mandriva.org> 0.23-1mdv2007.0
+ Revision: 132137
- new version

* Fri Jan 12 2007 Götz Waschk <waschk@mandriva.org> 0.22-2mdv2007.1
+ Revision: 107779
- bump release
- fix buildrequires

* Fri Jan 12 2007 Götz Waschk <waschk@mandriva.org> 0.22-1mdv2007.1
+ Revision: 107759
- new version

* Sat Jan 06 2007 Götz Waschk <waschk@mandriva.org> 0.21-1mdv2007.1
+ Revision: 104813
- new version

* Sat Dec 09 2006 Götz Waschk <waschk@mandriva.org> 0.20-1mdv2007.1
+ Revision: 94107
- new version
- fix buildrequires

* Fri Nov 10 2006 Götz Waschk <waschk@mandriva.org> 0.19-1mdv2007.0
+ Revision: 80521
- new version

* Wed Oct 18 2006 Götz Waschk <waschk@mandriva.org> 0.18-3mdv2007.1
+ Revision: 65889
- fix buildrequires
- rebuild
- new version
  add new files
- Import gossip

* Mon Sep 25 2006 Götz Waschk <waschk@mandriva.org> 0.17-1mdv2007.0
- New version 0.17

* Mon Sep 18 2006 Götz Waschk <waschk@mandriva.org> 0.16-1mdv2007.0
- drop patch
- New version 0.16

* Mon Sep 11 2006 Frederic Crozat <fcrozat@mandriva.com> 0.15-2mdv2007.0
- Patch0 (CVS): various bug fixes from CVS

* Sat Aug 26 2006 Götz Waschk <waschk@mandriva.org> 0.15-1mdv2007.0
- update file list
- New release 0.15

* Sat Aug 05 2006 Götz Waschk <waschk@mandriva.org> 0.14-1mdv2007.0
- New release 0.14

* Tue Aug 01 2006 Götz Waschk <waschk@mandriva.org> 0.13-1mdv2007.0
- New release 0.13

* Thu Jul 06 2006 Götz Waschk <waschk@mandriva.org> 0.12-1mdv2007.0
- reenable dbus and libnotify
- New release 0.12

* Sat Jun 24 2006 Götz Waschk <waschk@mandriva.org> 0.11.2-4mdv2007.0
- fix buildrequires

* Sat Jun 24 2006 Götz Waschk <waschk@mandriva.org> 0.11.2-3mdv2007.0
- fix buildrequires

* Tue Jun 13 2006 Götz Waschk <waschk@mandriva.org> 0.11.2-1
- New release 0.11.2

* Wed May 31 2006 Götz Waschk <waschk@mandriva.org> 0.11.1-1mdv2007.0
- New release 0.11.1

* Wed May 03 2006 Götz Waschk <waschk@mandriva.org> 0.11-1mdk
- update file list
- New release 0.11

* Wed Apr 12 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-2mdk
- fix buildrequires

* Sun Mar 19 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdk
- fix installation
- New release 0.10.2

* Sun Feb 26 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdk
- disable notification
- New release 0.10.1

* Tue Feb 21 2006 Götz Waschk <waschk@mandriva.org> 0.10-2mdk
- add icons
- remove redundant Requires(post)
- fix buildrequires

* Mon Feb 20 2006 Frederic Crozat <fcrozat@mandriva.com> 0.10-1mdk
- Release 0.10
- robustify preun script
- Remove patch 0

* Thu Sep 15 2005 Frederic Crozat <fcrozat@mandriva.com> 0.9-2mdk 
- Patch0: remove some debug output
- use new syntax for prereq

* Wed Aug 17 2005 Frederic Crozat <fcrozat@mandriva.com> 0.9-1mdk 
- Release 0.9

* Wed Mar 02 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8-3mdk 
- Don't own /usr/share/applications

* Wed Jan 05 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8-2mdk 
- Rebuild with latest howl

* Tue Dec 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8-1mdk
- New release 0.8

* Sat Sep 04 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.8-1mdk
- New release 0.7.8

* Mon Aug 30 2004 Jerome Soyer <saispo@mandrake.org> 0.7.7-3mdk
- Fix BuildRequires

* Sat Aug 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.7-2mdk
- Really fix menu

* Sat Aug 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.7-1mdk
- New release 0.7.7
- Fix menu

* Sun Aug 22 2004 Jerome Soyer wsaispo@mandrake.org> 0.7.6-2mdk
- fix menu entry

* Fri Jun 25 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.6-1mdk
- New release 0.7.6
- Enable libtoolize

* Thu Apr 29 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.5-1mdk
- New release 0.7.5

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.4-2mdk
- Rebuild against latest gnutls/loudmouth

* Sat Apr 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.4-1mdk
- Release 0.7.4

