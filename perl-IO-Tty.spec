%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Tty
Summary:	IO::Tty perl module
Summary(pl):	Modu³ perla IO::Tty
Name:		perl-IO-Tty
Version:	1.02
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Tty perl module.

%description -l pl
Modu³ perla IO::Tty.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/IO/*.pm
%{perl_sitearch}/IO/Tty
%{perl_sitearch}/auto/IO/Tty
%{_mandir}/man3/*
