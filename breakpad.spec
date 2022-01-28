Summary:	Open-source multi-platform crash reporting system
Summary(pl.UTF-8):	Wieloplatformowy system zgłaszania awarii o otwartych źródłach
Name:		breakpad
Version:	0.1.4
Release:	1
License:	BSD
Group:		Applications
Source0:	https://download.videolan.org/contrib/breakpad/%{name}-%{version}.tar.gz
# Source0-md5:	0639fce6177bd1f28101cae5b3e201c9
Patch0:		%{name}-types.patch
URL:		https://chromium.googlesource.com/breakpad/breakpad
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	curl-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open-source multi-platform crash reporting system.

%description -l pl.UTF-8
Wieloplatformowy system zgłaszania awarii o otwartych źródłach.

%package devel
Summary:	Open-source multi-platform crash reporting system - development libraries
Summary(pl.UTF-8):	Wieloplatformowy system zgłaszania awarii o otwartych źródłach - biblioteki programistyczne
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.7

%description devel
Open-source multi-platform crash reporting system - development
libraries.

%description devel -l pl.UTF-8
Wieloplatformowy system zgłaszania awarii o otwartych źródłach -
biblioteki programistyczne.

%prep
%setup -q
%patch0 -p1

%build
install -d autotools
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc, the rest is junk
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{AUTHORS,ChangeLog,INSTALL,LICENSE,NEWS,README.md}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_bindir}/core2md
%attr(755,root,root) %{_bindir}/dump_syms
%attr(755,root,root) %{_bindir}/dump_syms_mac
%attr(755,root,root) %{_bindir}/dump_syms_win
%attr(755,root,root) %{_bindir}/microdump_stackwalk
%attr(755,root,root) %{_bindir}/minidump-2-core
%attr(755,root,root) %{_bindir}/minidump_dump
%attr(755,root,root) %{_bindir}/minidump_stackwalk
%attr(755,root,root) %{_bindir}/minidump_upload
%attr(755,root,root) %{_bindir}/sym_upload

%files devel
%defattr(644,root,root,755)
%{_libdir}/libbreakpad.a
%{_libdir}/libbreakpad_client.a
%{_includedir}/breakpad
%{_pkgconfigdir}/breakpad.pc
%{_pkgconfigdir}/breakpad-client.pc
