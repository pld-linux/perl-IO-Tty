%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Tty
Summary:	IO-Tty perl module
Summary(pl):	Modu� perla IO-Tty
Name:		perl-IO-Tty
Version:	0.05
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO-Tty perl module.

%description -l pl
Modu� perla IO-Tty.

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
%dir %{perl_sitearch}/auto/IO/Tty
%{perl_sitearch}/auto/IO/Tty/Tty.bs
%attr(755,root,root) %{perl_sitearch}/auto/IO/Tty/Tty.so
%{_mandir}/man3/*
