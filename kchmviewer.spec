#
# Conditional build:
%bcond_with     kde		# enable KDE support
%bcond_without	arts		# build without aRts default=no
#
Summary:	KchmViewer is a chm (MS HTML help file format) viewer
Name:		kchmviewer
Version:	1.0
Release:	0.6
License:	GPL v2
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/kchmviewer/%{name}-%{version}.tar.gz
# Source0-md5:	0f9595cbb13eb950261e660c168dc033
URL:		http://kchmviewer.sourceforge.net/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
%{?with_kde:BuildRequires:	kdelibs-devel}
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KchmViewer is a chm (MS HTML help file format) viewer, written in C++.
Unlike most existing CHM viewers for Unix, it uses Trolltech Qt widget
library, and does not depend on KDE or Gnome. However, it may be
compiled with full KDE support, including KDE widgets and KIO/KHTML.

%prep
%setup -q

%build
%configure \
	%{?with_kde:--with-kde}
	%{?without_arts:--without-arts}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
