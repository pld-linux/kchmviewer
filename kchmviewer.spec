#
# Conditional build:
%bcond_with	kde		# enable KDE support
%bcond_without	arts		# build without aRts default=no
#
Summary:	KchmViewer - a CHM (MS HTML help file format) viewer
Summary(pl.UTF-8):	KchmViewer - przeglądarka CHM (formatu plików pomocy MS HTML)
Name:		kchmviewer
Version:	3.1
Release:	1	
License:	GPL v2
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/kchmviewer/%{name}-%{version}.tar.gz
# Source0-md5:	6666e32415e0e91f963190a25d5767fb
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-i18n.patch
URL:		http://kchmviewer.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	chmlib-devel >= 0.37
%{?with_kde:BuildRequires:	kdelibs-devel >= 9:3.0}
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

%description -l pl.UTF-8
KchmViewer to przeglądarka CHM (formatu plików pomocy MS HTML)
napisana w C++. W przeciwieństwie do większości istniejących
przeglądarek CHM dla Uniksa używa biblioteki widgetów Trolltecha Qt i
nie zależy od KDE czy GNOME. Jednak może być skompilowana z pełnym
wsparciem dla KDE, włącznie z widgetami KDE i KIO/KHTML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
	%{!?with_arts:--without-arts} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D lib/kio-msits/kchmviewer.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde/kchmviewer.desktop
install -D src/pics/cr48-app-kchmviewer.png $RPM_BUILD_ROOT%{_pixmapsdir}/kchmviewer.png

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog FAQ README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*.desktop
%{_pixmapsdir}/*.png
%exclude /usr/share/locale/du
