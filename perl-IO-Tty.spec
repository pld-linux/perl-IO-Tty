%include	/usr/lib/rpm/macros.perl
Summary:	IO-Tty perl module
Summary(pl):	Modu³ perla IO-Tty
Name:		perl-IO-Tty
Version:	0.05
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/IO-Tty-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO-Tty perl module.

%description -l pl
Modu³ perla IO-Tty.

%prep
%setup -q -n IO-Tty-%{version}

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
