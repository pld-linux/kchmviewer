#
# Conditional build:
%bcond_with	kde		# enable KDE support
%bcond_without	arts		# build without aRts default=no
#
Summary:	KchmViewer - a CHM (MS HTML help file format) viewer
Summary(pl):	KchmViewer - przegl±darka CHM (formatu plików pomocy MS HTML)
Name:		kchmviewer
Version:	2.5
Release:	1
License:	GPL v2
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/kchmviewer/%{name}-%{version}.tar.gz
# Source0-md5:	31aa10f89b92ec5323fef7c26b1e1eed
Source1:	%{name}.png
Patch0:		%{name}-desktop.patch
URL:		http://kchmviewer.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	chmlib-devel >= 0.37
%{?with_kde:BuildRequires:	kdelibs-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	qt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KchmViewer is a CHM (MS HTML help file format) viewer, written in C++.
Unlike most existing CHM viewers for Unix, it uses Trolltech Qt widget
library, and does not depend on KDE or GNOME. However, it may be
compiled with full KDE support, including KDE widgets and KIO/KHTML.

%description -l pl
KchmViewer to przegl±darka CHM (formatu plików pomocy MS HTML)
napisana w C++. W przeciwieñstwie do wiêkszo¶ci istniej±cych
przegl±darek CHM dla Uniksa u¿ywa biblioteki widgetów Trolltecha Qt i
nie zale¿y od KDE czy GNOME. Jednak mo¿e byæ skompilowana z pe³nym
wsparciem dla KDE, w³±cznie z widgetami KDE i KIO/KHTML.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__perl} am_edit
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{?with_kde:--with-kde} \
	%{?without_arts:--without-arts} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D kio-msits/kchmviewer.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde/kchmviewer.desktop
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/kchmviewer.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*
%{_pixmapsdir}/*
