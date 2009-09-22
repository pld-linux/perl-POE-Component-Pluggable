#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Pluggable
Summary:	POE::Component::Pluggable - A base class for creating plugin-enabled POE Components
Summary(pl.UTF-8):	POE::Component::Pluggable - klasa bazowa do tworzenia komponentów POE jako wtyczek
Name:		perl-POE-Component-Pluggable
Version:	1.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6627cbbb234c1295b63e23f88b8de976
URL:		http://search.cpan.org/dist/POE-Component-Pluggable/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-POE >= 1.004
BuildRequires:	perl-Task-Weaken
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Pluggable is a base class for creating plugin enabled
POE Components. It is a generic port of POE::Component::IRC's plugin
system.

If your component dispatches events to registered POE sessions, then
POE::Component::Pluggable may be a good fit for you.

%description -l pl.UTF-8
POE::Component::Pluggable jest klasą bazową dla tworzenia komponentów
POE jako wtyczek. Jest to ogólny port systemu wtyczek
POE::Component::IRC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/*.pm
%{perl_vendorlib}/POE/Component/Pluggable
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
