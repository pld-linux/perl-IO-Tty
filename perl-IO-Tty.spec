#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pdir	IO
%define		pnam	Tty
Summary:	IO::Tty and IO::Pty - interface to pseudo-ttys
Summary(pl.UTF-8):	IO::Tty i IO::Pty - interfejs do pseudo-tty
Name:		perl-IO-Tty
Version:	1.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5ee30bf7c76f00cc69f92388ad776e2a
URL:		https://metacpan.org/dist/IO-Tty
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	perl-dirs >= 1.0-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Tty is used internally by IO::Pty to create a pseudo-tty.

IO::Pty provides an interface to allow the creation of a pseudo tty.

%description -l pl.UTF-8
Moduł IO::Tty jest używany wewnętrznie poprzez IO::Pty do tworzenia
pseudoterminali (pseudo-tty).

Moduł IO::Pty udostępnia interfejs pozwalający na utworzenie
pseudoterminala.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%{perl_vendorarch}/IO/Pty.pm
%{perl_vendorarch}/IO/Tty.pm
%{perl_vendorarch}/IO/Tty
%dir %{perl_vendorarch}/auto/IO/Tty
%attr(755,root,root) %{perl_vendorarch}/auto/IO/Tty/Tty.so
%{_mandir}/man3/IO::Pty.3pm*
%{_mandir}/man3/IO::Tty*.3pm*
