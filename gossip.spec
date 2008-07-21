%define req_loudmouth_version 1.3.4

Summary: GNOME Jabber client
Name: gossip
Version: 0.30
Release: %mkrel 1
License: GPLv2+
Group: Networking/Instant messaging
URL: http://www.imendio.com/projects/gossip/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: loudmouth-devel >= %{req_loudmouth_version}
BuildRequires: libgnomeui2-devel
BuildRequires: libxscrnsaver-devel
BuildRequires: libxslt-devel
BuildRequires: libglade2.0-devel
BuildRequires: dbus-glib-devel
BuildRequires: libnotify-devel
BuildRequires: libgalago-devel
BuildRequires: gnome-panel-devel
BuildRequires: libxrender-devel
BuildRequires: libaspell-devel
BuildRequires: iso-codes
BuildRequires: scrollkeeper
BuildRequires: gnome-doc-utils
BuildRequires: intltool
BuildRequires: desktop-file-utils
Requires(post):	scrollkeeper
Requires(postun):scrollkeeper

%description
Gossip aims at making Jabber easy to use and tries to give GNOME users a
real user friendly way of chatting with their friends.

%prep
%setup -q

%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std _ENABLE_SK=false

%find_lang %{name} --with-gnome
for omf in %buildroot%_datadir/omf/*/*-??.omf;do
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed s!%buildroot!!)" >> %name.lang
done

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas %{name}
%{update_scrollkeeper}
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %{name}

%postun
%{clean_scrollkeeper}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog AUTHORS
%config(noreplace) %{_sysconfdir}/sound/events/*
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%_libexecdir/*applet
%_libdir/bonobo/servers/GNOME_Peekaboo_Applet.server
%{_datadir}/applications/*
%{_datadir}/gossip
%{_datadir}/sounds/gossip
%_datadir/icons/hicolor/*/apps/*
%dir %{_datadir}/omf/gossip
%{_datadir}/omf/gossip/gossip-C.omf
