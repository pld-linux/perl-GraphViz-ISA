#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	GraphViz
%define		pnam	ISA
Summary:	GraphViz::ISA Perl module - Graphing @ISA hierarchies at run-time
Summary(pl):	Modu³ Perla GraphViz::ISA - wizualizacja hierarchii @ISA w czasie dzia³ania
Name:		perl-GraphViz-ISA
Version:	0.01
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GraphViz >= 0.11
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-GraphViz >= 0.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class constructs a graph showing the `@ISA' hierarchy (note: not
object hierarchies) from a package name or a blessed scalar.

%description -l pl
Ta klasa konstruuje graf obrazuj±cy hierarchiê @ISA (ale nie
hierarchie obiektów) z nazwy pakietu lub "pob³ogos³awionej" wielko¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/GraphViz/ISA.pm
%{_mandir}/man3/*
