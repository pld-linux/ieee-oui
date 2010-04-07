# TODO
# - packages to make use of this pkg:
# - hwdata-0.225-0.20090808.1.noarch
# - lshw-B.02.14-1.i686
# - ntop-3.3.10-3.i686
# - python-netaddr-0.7.3-1.noarch
Summary:	Ethernet OUI file from the IEEE
Summary(pl.UTF-8):	-
Name:		ieee-oui
Version:	20100407
Release:	1
License:	Public
Group:		Networking
Source0:	http://standards.ieee.org/regauth/oui/oui.txt
# Source0-md5:	e3e3760fabd22cb55704b8b037186a79
URL:		http://standards.ieee.org/regauth/oui/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OUI file contains all of the OUIs (Organizationally Unique
Identifiers) that have been registered with IEEE. Each OUI entry in
the file specifies the first 24-bits of the 48-bit Ethernet hardware
address, leaving the remaining 24-bits for use by the registering
organisation.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/oui.txt
