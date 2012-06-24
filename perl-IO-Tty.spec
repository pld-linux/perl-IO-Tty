%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Tty
Summary:	IO::Tty Perl module
Summary(cs):	Modul IO::Tty pro Perl
Summary(da):	Perlmodul IO::Tty
Summary(de):	IO::Tty Perl Modul
Summary(es):	M�dulo de Perl IO::Tty
Summary(fr):	Module Perl IO::Tty
Summary(it):	Modulo di Perl IO::Tty
Summary(ja):	IO::Tty Perl �⥸�塼��
Summary(ko):	IO::Tty �� ����
Summary(no):	Perlmodul IO::Tty
Summary(pl):	Modu� Perla IO::Tty
Summary(pt):	M�dulo de Perl IO::Tty
Summary(pt_BR):	M�dulo Perl IO::Tty
Summary(ru):	������ ��� Perl IO::Tty
Summary(sv):	IO::Tty Perlmodul
Summary(uk):	������ ��� Perl IO::Tty
Summary(zh_CN):	IO::Tty Perl ģ��
Name:		perl-IO-Tty
Version:	1.02
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Tty perl module.

%description -l cs
Modul IO::Tty pro Perl.

%description -l da
Perlmodul IO::Tty.

%description -l de
IO::Tty Perl Modul.

%description -l es
M�dulo de Perl IO::Tty.

%description -l fr
Module Perl IO::Tty.

%description -l it
Modulo di Perl IO::Tty.

%description -l ja
IO::Tty Perl �⥸�塼��

%description -l ko
IO::Tty �� ����.

%description -l no
Perlmodul IO::Tty.

%description -l pl
Modu� perla IO::Tty.

%description -l pt
M�dulo de Perl IO::Tty.

%description -l pt_BR
M�dulo Perl IO::Tty.

%description -l ru
������ ��� Perl IO::Tty.

%description -l sv
IO::Tty Perlmodul.

%description -l uk
������ ��� Perl IO::Tty.

%description -l zh_CN
IO::Tty Perl ģ��

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
%doc ChangeLog README
%{perl_sitearch}/IO
%dir %{perl_sitearch}/auto/IO
%dir %{perl_sitearch}/auto/IO/Tty
%{perl_sitearch}/auto/IO/Tty/Tty.bs
%attr(755,root,root) %{perl_sitearch}/auto/IO/Tty/Tty.so
%{_mandir}/man3/*
