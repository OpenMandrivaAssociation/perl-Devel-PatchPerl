%define upstream_name    Devel-PatchPerl
%define upstream_version 1.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Replacement 'hints' files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/Devel-PatchPerl-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(MIME::Base64)
BuildArch:	noarch

%description
Devel::PatchPerl is a modularisation of the patching code contained in the
Devel::PPort manpage's 'buildperl.pl'.

It does not build perls, it merely provides an interface to the source
patching functionality.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes META.yml META.json
%{_mandir}/man3/*
%{_mandir}/man1/patchperl.1*
%{_bindir}/patchperl
%{perl_vendorlib}/*

%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.400.0-1mdv2011.0
+ Revision: 684741
- update to new version 0.40

* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.360.0-1
+ Revision: 674798
- update to new version 0.36

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.340.0-1
+ Revision: 673796
- update to new version 0.34

* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.300.0-1
+ Revision: 672825
- import perl-Devel-PatchPerl




