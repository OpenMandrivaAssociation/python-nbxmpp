%global srcname nbxmpp

Name:           python-%{srcname}
Version:        3.0.2
Release:        1
Summary:        Non blocking Jabber/XMPP module
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/nbxmpp/
Source0:        https://pypi.io/packages/source/n/nbxmpp/%{srcname}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

Requires:       python3dist(precis-i18n)

%{?python_provide:%python_provide python3-%{srcname}}

BuildArch:      noarch

%description
The goal of this python library is to provide a way for python applications
to use Jabber/XMPP networks in a non-blocking way. This library is initialy
a fork of xmpppy one, but using non-blocking sockets.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%doc ChangeLog
%{python_sitelib}/%{srcname}/
%{python_sitelib}/%{srcname}*.egg-info
