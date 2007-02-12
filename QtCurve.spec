#
# ToDo:
#  - include /usr/share/themes/QtCurve/mozilla somewhere
#
# Conditional build:
%bcond_with	gtk	# build GTK styles
%bcond_without	gtk2	# don't build GTK+2 styles
#
%define		kde_ver		0.46.2
%define		gtk2_ver	0.46.2
%define		gtk1_ver	0.42.2
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Name:		QtCurve
Version:	0.46.2
Release:	1
License:	GPL
Group:		Themes
Source0:	http://home.freeuk.com/cpdrummond/%{name}-KDE3-%{kde_ver}.tar.gz
# Source0-md5:	928ff52cdb312275ee24363501faa5e2
Source1:	http://home.freeuk.com/cpdrummond/%{name}-Gtk2-%{gtk2_ver}.tar.gz
# Source1-md5:	ca4827f073ba93d517522d1c65a6d8f5
Source2:	http://home.freeuk.com/cpdrummond/%{name}-Gtk1-%{gtk1_ver}.tar.gz
# Source2-md5:	8219f58493ca4e65a8fe61ee76eca522
Patch0:		%{name}-amd64.patch
Patch1:		kde-am110.patch
Patch2:		kde-ac260-lt.patch
URL:		http://www.kde-look.org/content/show.php?content=40492
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gtk:BuildRequires:	gtk+-devel}
%{?with_gtk2:BuildRequires:	gtk+2-devel}
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed > 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free and corrected port of Red Hat's GTK+/Qt theme.

%description -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.

%package -n kde-style-QtCurve
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
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
Group:		Themes
Requires:	theme-QtCurve-common = %{version}-%{release}

%description -n gtk-theme-QtCurve
A free and corrected port of Red Hat's GTK+/Qt theme. GTK+ version.

%description -n gtk-theme-QtCurve -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Wersja pod GTK+.

%package -n gtk2-theme-QtCurve
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Group:		Themes
Requires:	theme-QtCurve-common = %{version}-%{release}

%description -n gtk2-theme-QtCurve
A free and corrected port of Red Hat's GTK+/Qt theme. GTK+2 version.

%description -n gtk2-theme-QtCurve -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Wersja pod GTK+2.

%package -n theme-QtCurve-common
Summary:	A free and corrected port of Redhats GTK+/Qt theme - common
Summary(pl.UTF-8):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata - common
Group:		Themes
Obsoletes:	theme-bluecurve-common
Obsoletes:	gtk2-theme-bluecurve
Obsoletes:	gtk-theme-bluecurve
Obsoletes:	kde-style-bluecurve
Obsoletes:	kde-theme-bluecurve

%description -n theme-QtCurve-common
A free and corrected port of Red Hat's GTK+/Qt theme.
Documentation and common files package.

%description -n theme-QtCurve-common -l pl.UTF-8
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Pakiet z dokumentacja i plikami współdzielonymi.

%prep
%setup -q -c -a1 -a2
%patch0 -p1
cd %{name}-KDE3-%{kde_ver}
%patch1 -p1
%patch2 -p1

%build
cd %{name}-KDE3-%{kde_ver}
cp /usr/share/automake/config.sub admin

%{__make} -f admin/Makefile.common cvs
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}
cd -

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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
cd -
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C %{name}-KDE3-%{kde_ver} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with gtk}
%{__make} -C %{name}-Gtk1-%{gtk1_ver} install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with gtk2}
%{__make} -C %{name}-Gtk2-%{gtk2_ver} install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

rm -f $RPM_BUILD_ROOT{%{_libdir}/gtk/themes/engines,%{_libdir}/gtk-2.0/*/*}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-style-QtCurve
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_qtcurve_config.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_qtcurve_config.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/qtcurve*.themerc
%{_datadir}/apps/qtcurve

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
%{_datadir}/themes/QtCurve/gtk-2.0
%endif

%files -n theme-QtCurve-common
%defattr(644,root,root,755)
%doc %{name}-KDE3-%{kde_ver}/{ChangeLog,README,TODO}
%dir %{_datadir}/themes/QtCurve
