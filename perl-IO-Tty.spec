#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Tty
Summary:	IO::Tty Perl module - low-level allocate a pseudo-tty, import constants
Summary(pl):	Modu³ Perla IO::Tty - niskopoziomowa alokacja pseudo-tty, wa¿ne sta³e
Name:		perl-IO-Tty
Version:	1.02
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	875a8bc6e0643f4fc892dbe113e43286
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Tty is used internally by IO::Pty to create a pseudo-tty. You
wouldn't want to use it directly except to import constants, use
IO::Pty. For a list of importable constants, see IO::Tty::Constant.

%description -l pl
Modu³ IO::Tty jest u¿ywany wewnêtrznie poprzez IO::Pty do tworzenia
pseudo terminali (pseudo-tty). Nie nale¿y u¿ywaæ go bezpo¶rednio do
celów innych ni¿ zaimportowanie sta³ych - nale¿y u¿ywaæ IO::Pty.
Lista dostêpnych sta³ych znajduje siê w IO::Tty::Constant.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/IO
%dir %{perl_vendorarch}/auto/IO
%dir %{perl_vendorarch}/auto/IO/Tty
%{perl_vendorarch}/auto/IO/Tty/Tty.bs
%attr(755,root,root) %{perl_vendorarch}/auto/IO/Tty/Tty.so
%{_mandir}/man3/*
