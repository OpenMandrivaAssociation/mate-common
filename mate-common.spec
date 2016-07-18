%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Common files for MATE desktop environment
Name:		mate-common
Version:	1.14.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
Url:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
MATE is a fork of Gnome 2.

It provides an intuitive and attractive desktop to Linux users using
traditional metaphors.

%prep
%setup -q
NOCONFIGURE=yes ./autogen.sh

%build
%configure \
 	--build=%{_build}

%make

%install
%makeinstall_std
install -d %{buildroot}%{_docdir}/%{name}/

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/mate-*
%{_datadir}/%{name}
%{_datadir}/aclocal/mate-*.m4
%{_mandir}/man1/mate-autogen.1*
%{_mandir}/man1/mate-doc-common.1*

