Summary:	KchmViewer - a CHM (MS HTML help file format) viewer
Summary(pl.UTF-8):	KchmViewer - przeglądarka CHM (formatu plików pomocy MS HTML)
Name:		kchmviewer
Version:	5.2
Release:	1
License:	GPL v2
Group:		Applications/Publishing
Source0:	http://downloads.sourceforge.net/kchmviewer/%{name}-%{version}.tar.gz
# Source0-md5:	9798c7f949d1137949e69a8c226415f9
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-i18n.patch
Patch2:		%{name}-missed_src.patch
Patch3:		%{name}-no_msits.patch
URL:		http://kchmviewer.sourceforge.net/
BuildRequires:	automoc4
BuildRequires:	chmlib-devel >= 0.37
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
Requires:	kio_msits
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
%setup -q -n build-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
	.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D packages/kchmviewer.png $RPM_BUILD_ROOT%{_pixmapsdir}/kchmviewer.png

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog FAQ README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde4/*.desktop
%{_pixmapsdir}/*.png
