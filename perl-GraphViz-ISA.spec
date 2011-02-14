#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	GraphViz
%define		pnam	ISA
Summary:	GraphViz::ISA Perl module - graphing @ISA hierarchies at run-time
Summary(pl.UTF-8):	Moduł Perla GraphViz::ISA - wizualizacja hierarchii @ISA w czasie działania
Name:		perl-GraphViz-ISA
Version:	0.01
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	93b279c6fd57abd614ff71d34f8ed839
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GraphViz >= 0.11
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-GraphViz >= 0.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class constructs a graph showing the `@ISA' hierarchy (note: not
object hierarchies) from a package name or a blessed scalar.

%description -l pl.UTF-8
Ta klasa konstruuje graf obrazujący hierarchię @ISA (ale nie
hierarchie obiektów) z nazwy pakietu lub "pobłogosławionej" wielkości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
