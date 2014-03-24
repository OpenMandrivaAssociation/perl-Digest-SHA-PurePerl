%define	upstream_name	 Digest-SHA-PurePerl
%define upstream_version 5.88

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl implementation of SHA-1/224/256/384/512
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSHELOR/%{upstream_name}-%{upstream_version}.tar.gz
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


%changelog
* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 5.620.0-1mdv2011.0
+ Revision: 674800
- update to new version 5.62

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 5.610.0-1
+ Revision: 643378
- update to new version 5.61

* Fri Dec 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 5.500.0-1mdv2011.0
+ Revision: 622683
- update to new version 5.50

* Thu Jan 07 2010 Emmanuel Andry <eandry@mandriva.org> 5.480.0-1mdv2011.0
+ Revision: 487176
- import perl-Digest-SHA-PurePerl






