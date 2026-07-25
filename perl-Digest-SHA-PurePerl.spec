%define	upstream_name	 Digest-SHA-PurePerl
%define upstream_version 6.04

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Perl implementation of SHA-1/224/256/384/512




License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/Digest-SHA-PurePerl
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-PurePerl-%{upstream_version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel

BuildArch:	noarch

%description
Digest::SHA::PurePerl is a complete implementation of the NIST
Secure Hash Standard.  It gives Perl programmers a convenient way
to calculate SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message
digests.  The module can handle all types of input, including
partial-byte data.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor -d
%make

%check
%make test

%install

%makeinstall_std

%clean 

%files 
%doc README
%{perl_vendorlib}/Digest/SHA/PurePerl.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/*






