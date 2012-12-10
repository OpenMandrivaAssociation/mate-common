Summary:	Common files for MATE desktop environment
Name:		mate-common
Version:	1.4.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
MATE is a fork of Gnome 2.

It provides an intuitive and attractive desktop to Linux users using
traditional metaphors.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
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



%changelog
* Fri Jul 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811302
- new version 1.4.0

* Tue May 29 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.2.2-1
+ Revision: 801063
- update to 1.2.2

* Mon Apr 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.2.1-1
+ Revision: 792948
- imported package mate-common

