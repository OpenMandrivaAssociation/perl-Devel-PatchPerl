%define upstream_name    Devel-PatchPerl
%define upstream_version 0.40

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Replacement 'hints' files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::pushd)
BuildRequires: perl(IO::File)
BuildRequires: perl(IPC::Cmd)
BuildRequires: perl(MIME::Base64)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Devel::PatchPerl is a modularisation of the patching code contained in the
Devel::PPort manpage's 'buildperl.pl'.

It does not build perls, it merely provides an interface to the source
patching functionality.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes META.yml META.json
%{_mandir}/man3/*
%{_mandir}/man1/patchperl.1*
%{_bindir}/patchperl
%perl_vendorlib/*


