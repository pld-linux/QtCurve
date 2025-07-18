# TODO:
# - gtk1 no longer updated. drop after dropping last gtk+ 1.x app
#
# Conditional build:
%bcond_without	gtk	# don't build GTK+ styles
%bcond_without	gtk2	# don't build GTK+2 styles
%bcond_with		kde3	# build KDE3 styles
%bcond_without	kde4	# don't build KDE4 styles

%define		ver		1.8.9
%define		kde4_ver	1.8.9
%define		kde3_ver	1.8.5
%define		gtk2_ver	1.8.12
%define		gtk1_ver	0.42.2
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Name:		QtCurve
Version:	%{ver}
Release:	1
License:	GPL
Group:		Themes
Source0:	http://craigd.wikispaces.com/file/view/%{name}-KDE3-%{kde3_ver}.tar.bz2
# Source0-md5:	d9cca99526079782f9fc7bd7ba432582
Source1:	http://craigd.wikispaces.com/file/view/%{name}-Gtk2-%{gtk2_ver}.tar.bz2
# Source1-md5:	e1b8b4a8444c0afe8ba291f623c6b713
Source2:	http://home.freeuk.com/cpdrummond/%{name}-Gtk1-%{gtk1_ver}.tar.gz
# Source2-md5:	8219f58493ca4e65a8fe61ee76eca522
Source3:	http://craigd.wikispaces.com/file/view/%{name}-KDE4-%{kde4_ver}.tar.bz2
# Source3-md5:	0028e3da714cd0932e16c7f937e487a1
Patch0:		%{name}-Gtk1-lib64.patch
URL:		http://www.kde-look.org/content/show.php?content=40492
%{?with_kde4:BuildRequires:	Qt3Support-devel}
%{?with_kde4:BuildRequires:	QtSvg-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_kde4:BuildRequires:	automoc4}
BuildRequires:	cmake
%{?with_gtk:BuildRequires:	gtk+-devel}
%{?with_gtk2:BuildRequires:	gtk+2-devel}
%{?with_kde4:BuildRequires:	kde4-kdebase-workspace-devel}
%{?with_kde4:BuildRequires:	kde4-kdelibs-devel}
%{?with_kde4:BuildRequires:	kde4-kdelibs}
%{?with_kde3:BuildRequires:	kdelibs-devel >= 3.1}
BuildRequires:	libtool
BuildRequires:	pkgconfig
%{?with_kde4:BuildRequires:	qt4-build}
%{?with_kde4:BuildRequires:	qt4-qmake}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	sed > 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free and corrected port of Red Hat's GTK+/Qt theme.

%description -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.

%package -n kde-style-QtCurve
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Version:	%{kde3_ver}
Group:		Themes
Requires:	kdelibs >= 3.1

%description -n kde-style-QtCurve
A free and corrected port of Red Hat's GTK+/Qt theme. KDE3 version.

%description -n kde-style-QtCurve -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Wersja pod KDE3.

%package -n kde4-style-QtCurve
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Version:	%{kde4_ver}
Group:		Themes
Requires:	kde4-kdebase >= 4.3.4

%description -n kde4-style-QtCurve
A free and corrected port of Red Hat's GTK+/Qt theme. KDE4 version.

%description -n kde4-style-QtCurve -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Wersja pod KDE4.

%package -n gtk-theme-QtCurve
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Version:	%{gtk1_ver}
Group:		Themes
Requires:	theme-QtCurve-common = %{ver}-%{release}

%description -n gtk-theme-QtCurve
A free and corrected port of Red Hat's GTK+/Qt theme. GTK+ version.

%description -n gtk-theme-QtCurve -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Wersja pod GTK+.

%package -n gtk2-theme-QtCurve
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Version:	%{gtk2_ver}
Group:		Themes
Requires:	theme-QtCurve-common = %{ver}-%{release}

%description -n gtk2-theme-QtCurve
A free and corrected port of Red Hat's GTK+/Qt theme. GTK+2 version.

%description -n gtk2-theme-QtCurve -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Wersja pod GTK+2.

%package -n theme-QtCurve-common
Summary:	A free and corrected port of Redhats GTK+/Qt theme - common
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata - common
Version:	%{ver}
Group:		Themes
Obsoletes:	gtk-theme-bluecurve
Obsoletes:	gtk2-theme-bluecurve
Obsoletes:	kde-style-bluecurve
Obsoletes:	kde-theme-bluecurve
Obsoletes:	theme-bluecurve-common

%description -n theme-QtCurve-common
A free and corrected port of Red Hat's GTK+/Qt theme. Documentation
and common files package.

%description -n theme-QtCurve-common -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Pakiet z dokumentacja i plikami współdzielonymi.

%prep
%setup -q -c -D %{?with_kde3:-a0} %{?with_gtk2:-a1} %{?with_gtk:-a2} %{?with_kde4:-a3}

%if %{with gtk}
%if "%{_lib}" == "lib64"
cd %{name}-Gtk1-%{gtk1_ver}
%patch -P0 -p1
cd -
%endif
%endif

%build
%if %{with kde3}
cd %{name}-KDE3-%{kde3_ver}
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	.

%{__make}
cd -
%endif

%if %{with kde4}
cd %{name}-KDE4-%{kde4_ver}
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	.

%{__make}
cd -
%endif

%if %{with gtk}
cd %{name}-Gtk1-%{gtk1_ver}
rm -f acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
cd -
%endif

%if %{with gtk2}
cd %{name}-Gtk2-%{gtk2_ver}
%cmake \
	-DQTC_ADD_EVENT_FILTER=true \
	-DQTC_MODIFY_MOZILLA=true \
	-DQTC_MODIFY_MOZILLA_USER_JS=true \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	.

%{__make}
cd -
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with kde3}
%{__make} -C %{name}-KDE3-%{kde3_ver} install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with kde4}
%{__make} -C %{name}-KDE4-%{kde4_ver} install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with gtk}
%{__make} -C %{name}-Gtk1-%{gtk1_ver} install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with gtk2}
%{__make} -C %{name}-Gtk2-%{gtk2_ver} install \
	DESTDIR=$RPM_BUILD_ROOT

chmod a+x $RPM_BUILD_ROOT%{_datadir}/themes/QtCurve/gtk-2.0/map_kde_icons.pl
%endif

rm -f $RPM_BUILD_ROOT{%{_libdir}/gtk/themes/engines,%{_libdir}/gtk-2.0/*/*}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with kde3}
%files -n kde-style-QtCurve
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_qtcurve_config.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_qtcurve_config.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/qtcurve*.themerc
%{_datadir}/apps/kdisplay/color-schemes/QtCurve.kcsrc
%{_datadir}/apps/QtCurve
%endif

%if %{with kde4}
%files -n kde4-style-QtCurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kstyle_qtcurve_config.so
%attr(755,root,root) %{_libdir}/kde4/kwin3_qtcurve.so
%attr(755,root,root) %{_libdir}/kde4/kwin_qtcurve_config.so
%attr(755,root,root) %{_libdir}/kde4/plugins/styles/qtcurve.so
%{_datadir}/apps/QtCurve
%{_datadir}/apps/color-schemes/QtCurve.colors
%{_datadir}/apps/color-schemes/QtCurveAgua.colors
%{_datadir}/apps/kstyle/themes/qtcurve.themerc
%{_datadir}/apps/kwin/qtcurve.desktop
%endif

%if %{with gtk}
%files -n gtk-theme-QtCurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*.so
%{_datadir}/themes/QtCurve/gtk
%endif

%if %{with gtk2}
%files -n gtk2-theme-QtCurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/*/*/*.so
%dir %{_datadir}/themes/QtCurve/gtk-2.0
%{_datadir}/themes/QtCurve/gtk-2.0/gtkrc
%{_datadir}/themes/QtCurve/gtk-2.0/icons3
%{_datadir}/themes/QtCurve/gtk-2.0/icons4
%{_datadir}/themes/QtCurve/gtk-2.0/kdeglobals
%attr(755,root,root) %{_datadir}/themes/QtCurve/gtk-2.0/map_kde_icons.pl
%dir %{_datadir}/themes/QtCurve/mozilla
%{_datadir}/themes/QtCurve/mozilla/QtCurve.css
%{_datadir}/themes/QtCurve/mozilla/QtCurve-KDEButtonOrder.css
%{_datadir}/themes/QtCurve/mozilla/preferences-rev.xml
%endif

%files -n theme-QtCurve-common
%defattr(644,root,root,755)
%doc %{name}-KDE3-%{kde3_ver}/ChangeLog
%doc %{name}-KDE3-%{kde3_ver}/README
%doc %{name}-KDE3-%{kde3_ver}/TODO
%dir %{_datadir}/themes/QtCurve
