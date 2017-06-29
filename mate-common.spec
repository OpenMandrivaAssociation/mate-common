%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Common files for MATE desktop environment
Name:		mate-common
Version:	1.18.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
Url:		https://www.mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
MATE is a fork of Gnome 2.

It provides an intuitive and attractive desktop to Linux users using
traditional metaphors.

This package contains sample files userful for building much every MATE
application.

%prep
%setup -q


%build
NOCONFIGURE=yes ./autogen.sh
%configure \
	--build=%{_build} \
	%{nil}
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README COPYING
%{_bindir}/mate-autogen
%{_bindir}/mate-doc-common
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/aclocal/mate-*.m4
%{_mandir}/man1/mate-autogen.1*
%{_mandir}/man1/mate-doc-common.1*

