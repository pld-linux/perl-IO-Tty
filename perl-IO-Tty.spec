%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Tty
Summary:	IO::Tty - Low-level allocate a pseudo-Tty, import constants.
Name:		perl-IO-Tty
Version:	1.02
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C<IO::Tty> is used internally by C<IO::Pty> to create a pseudo-tty.
You wouldn't want to use it directly except to import constants, use
C<IO::Pty>.  For a list of importable constants, see L<IO::Tty::Constant>.

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
