Summary:	Python module to customize a process title
Name:		python-setproctitle
Version:	1.1.10
Release:	9
License:	BSD
Group:		Development/Languages/Python
URL:		http://pypi.python.org/pypi/setproctitle
BuildRequires:	rpmbuild(macros) >= 1.710
Source0:	https://pypi.debian.net/setproctitle/setproctitle-%{version}.tar.gz
# Source0-md5:	2dcdd1b761700a5a13252fea3dfd1977
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module allowing a process to change its title as displayed by
system tool such as ps and top.

It's useful in multiprocess systems, allowing to identify tasks each
forked process is busy with. This technique has been used by
PostgreSQL and OpenSSH.

It's based on PostgreSQL implementation which has proven to be
portable.

%prep
%setup -q -n setproctitle-%{version}

%build
%{__python} setup.py \
	build -b build-2

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--root $RPM_BUILD_ROOT

chmod 0755 $RPM_BUILD_ROOT%{py_sitedir}/setproctitle.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{py_sitedir}/setproctitle.so
%{py_sitedir}/setproctitle-*.egg-info
