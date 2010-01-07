%define	upstream_name	 Digest-SHA-PurePerl
%define	upstream_version 5.48

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Perl implementation of SHA-1/224/256/384/512
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSHELOR/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__make} test

%install
%{__rm} -rf %{buildroot}

%makeinstall_std

%clean 
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Digest/SHA/PurePerl.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/*
