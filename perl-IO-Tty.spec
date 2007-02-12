#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Tty
Summary:	IO::Tty Perl module - low-level allocate a pseudo-tty, import constants
Summary(pl.UTF-8):   Moduł Perla IO::Tty - niskopoziomowa alokacja pseudo-tty, ważne stałe
Name:		perl-IO-Tty
Version:	1.05
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	95c0aa8a1f75b1aff6c1fcaf0c1f7c29
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 1.0-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Tty is used internally by IO::Pty to create a pseudo-tty. You
wouldn't want to use it directly except to import constants, use
IO::Pty. For a list of importable constants, see IO::Tty::Constant.

%description -l pl.UTF-8
Moduł IO::Tty jest używany wewnętrznie poprzez IO::Pty do tworzenia
pseudo terminali (pseudo-tty). Nie należy używać go bezpośrednio do
celów innych niż zaimportowanie stałych - należy używać IO::Pty.
Lista dostępnych stałych znajduje się w IO::Tty::Constant.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/IO/*
%dir %{perl_vendorarch}/auto/IO/Tty
%{perl_vendorarch}/auto/IO/Tty/Tty.bs
%attr(755,root,root) %{perl_vendorarch}/auto/IO/Tty/Tty.so
%{_mandir}/man3/*
