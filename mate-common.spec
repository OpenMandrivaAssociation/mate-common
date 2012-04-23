Name:		mate-common
Summary:	Common files for MATE desktop environment
Version:	1.2.1
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/mate-common-1.2.1.tar.xz
BuildArch:	noarch

%description
MATE is a fork of Gnome 2.

It provides an intuitive and attractive desktop to Linux users using
traditional metaphors.

%prep
%setup -q

%build
./autogen.sh --prefix=%{_prefix}
%make

%install
%makeinstall_std
%__install -d %{buildroot}%{_docdir}/%{name}/

%files
%{_bindir}/mate-*
%{_datadir}/%{name}
%{_datadir}/aclocal/mate-*.m4
%doc AUTHORS ChangeLog NEWS README
