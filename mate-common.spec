%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Common files for MATE desktop environment
Name:		mate-common
Version:	1.20.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
Url:		https://www.mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

Requires:	automake
Requires:	autoconf
Requires:	gettext
Requires:	intltool
Requires:	itstool
Requires:	libtool
Requires:	pkgconfig(glib-2.0)
Requires:	pkgconfig(gtk-doc)
Requires:	pkgconfig(pkg-config)
Requires:	yelp-tools

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package contains sample files required for building pretty much
every MATE application.

%files
%doc AUTHORS ChangeLog NEWS README COPYING
%{_bindir}/mate-autogen
%{_bindir}/mate-doc-common
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/aclocal/mate-*.m4
%{_mandir}/man1/mate-autogen.1*
%{_mandir}/man1/mate-doc-common.1*

#---------------------------------------------------------------------------

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

