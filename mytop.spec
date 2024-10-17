%define name mytop
%define version 1.6 
%define release 6

Summary: A clone of top for MySQL 3.22.x to 4.x
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://jeremy.zawodny.com/mysql/mytop/%{name}-%{version}.tar.bz2
URL: https://jeremy.zawodny.com/mysql/mytop/
License: GPL
Group: Databases
BuildArch:  noarch
Prefix: %{_prefix}
BuildRequires: perl-Term-ReadKey
BuildRequires: perl-devel
Requires: perl-Term-ReadKey
Obsoletes: perl-mytop

%description
Mytop is a console-based (non-gui) tool for monitoring the threads and overall
performance of a MySQL 3.22.x, 3.23.x, and 4.x server.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
# beware to use _std macros 
%makeinstall_std

%files
%{_bindir}/mytop
%{_mandir}/man1/%{name}.*
%doc README
