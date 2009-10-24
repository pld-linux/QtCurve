# TODO:
# - kde4
# - gtk1 no longer updated. drop after dropping last gtk+ 1.x app
#
# Conditional build:
%bcond_without	gtk	# don't build GTK+ styles
%bcond_without	gtk2	# don't build GTK+2 styles
%bcond_without	kde	# don't build KDE styles
#
%define		ver		0.68.1
%define		kde_ver		0.68.1
%define		gtk2_ver	0.68.1
%define		gtk1_ver	0.42.2
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Name:		QtCurve
Version:	%{ver}
Release:	1
License:	GPL
Group:		Themes
Source0:	http://home.freeuk.com/cpdrummond/%{name}-KDE3-%{kde_ver}.tar.bz2
# Source0-md5:	2451c8e624f8e07bfaf5584f4208c9d7
Source1:	http://home.freeuk.com/cpdrummond/%{name}-Gtk2-%{gtk2_ver}.tar.bz2
# Source1-md5:	c7c2324e05aa09ecb26d1f9cc81a5e4a
Source2:	http://home.freeuk.com/cpdrummond/%{name}-Gtk1-%{gtk1_ver}.tar.gz
# Source2-md5:	8219f58493ca4e65a8fe61ee76eca522
Patch0:		%{name}-Gtk1-lib64.patch
URL:		http://www.kde-look.org/content/show.php?content=40492
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cmake
%{?with_gtk:BuildRequires:	gtk+-devel}
%{?with_gtk2:BuildRequires:	gtk+2-devel}
%{?with_kde:BuildRequires:	kdelibs-devel >= 3.1}
BuildRequires:	libtool
BuildRequires:	pkgconfig
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
Version:	%{kde_ver}
Group:		Themes
Requires:	kdelibs >= 3.1

%description -n kde-style-QtCurve
A free and corrected port of Red Hat's GTK+/Qt theme. KDE version.

%description -n kde-style-QtCurve -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Wersja pod KDE.

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
%setup -q -c -D %{?with_kde:-a0} %{?with_gtk2:-a1} %{?with_gtk:-a2}

%if %{with gtk}
%if "%{_lib}" == "lib64"
cd %{name}-Gtk1-%{gtk1_ver}
%patch0 -p1
cd -
%endif
%endif


%build
%if %{with kde}
cd %{name}-KDE3-%{kde_ver}
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	.

%{__make}
cd -
%endif

%if %{with gtk}
cd %{name}-Gtk1-%{gtk1_ver}
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

%if %{with kde}
%{__make} -C %{name}-KDE3-%{kde_ver} install \
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

%if %{with kde}
%files -n kde-style-QtCurve
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_qtcurve_config.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_qtcurve_config.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/qtcurve*.themerc
%{_datadir}/apps/kstyle/themes/qtc_klearlooks.themerc
%{_datadir}/apps/QtCurve
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
%attr(755,root,root) %{_datadir}/themes/QtCurve/gtk-2.0/map_kde_icons.pl
%dir %{_datadir}/themes/QtCurve/mozilla
%{_datadir}/themes/QtCurve/mozilla/QtCurve.css
%{_datadir}/themes/QtCurve/mozilla/QtCurve-KDEButtonOrder.css
%{_datadir}/themes/QtCurve/mozilla/preferences-rev.xml
%endif

%files -n theme-QtCurve-common
%defattr(644,root,root,755)
%doc %{name}-KDE3-%{kde_ver}/ChangeLog
%doc %{name}-KDE3-%{kde_ver}/README
%doc %{name}-KDE3-%{kde_ver}/TODO
%dir %{_datadir}/themes/QtCurve
