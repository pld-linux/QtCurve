#
# ToDo:
#  - include /usr/share/themes/QtCurve/mozilla somewhere
#
# Conditional build:
%bcond_with	gtk	# build GTK styles
%bcond_without	gtk2	# don't build GTK+2 styles
#
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Name:		QtCurve
Version:	0.38
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.cpdrummond.freeuk.com/%{name}-%{version}.tar.gz
# Source0-md5:	1e9145e20e2df5a1f572767d158f66d5
URL:		http://www.kde-look.org/content/show.php?content=40492
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gtk:BuildRequires:	gtk+-devel}
%{?with_gtk2:BuildRequires:	gtk+2-devel}
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	pkgconfig
BuildRequires:	sed > 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free and corrected port of Red Hat's GTK+/Qt theme.

%description -l pl
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.

%package -n kde-style-QtCurve
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Group:		Themes
Requires:	kdelibs >= 3.1

%description -n kde-style-QtCurve
A free and corrected port of Red Hat's GTK+/Qt theme. KDE version.

%description -n kde-style-QtCurve -l pl
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Wersja pod KDE.

%package -n gtk-theme-QtCurve
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Group:		Themes
Requires:	theme-QtCurve-common = %{version}-%{release}

%description -n gtk-theme-QtCurve
A free and corrected port of Red Hat's GTK+/Qt theme. GTK+ version.

%description -n gtk-theme-QtCurve -l pl
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Wersja pod GTK+.

%package -n gtk2-theme-QtCurve
Summary:	A free and corrected port of Red Hat's GTK+/Qt theme
Summary(pl):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata
Group:		Themes
Requires:	theme-QtCurve-common = %{version}-%{release}

%description -n gtk2-theme-QtCurve
A free and corrected port of Red Hat's GTK+/Qt theme. GTK+2 version.

%description -n gtk2-theme-QtCurve -l pl
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Wersja pod GTK+2.

%package -n theme-QtCurve-common
Summary:	A free and corrected port of Redhats GTK+/Qt theme - common
Summary(pl):	Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata - common
Group:		Themes
Obsoletes:	theme-bluecurve-common
Obsoletes:	gtk2-theme-bluecurve
Obsoletes:	gtk-theme-bluecurve
Obsoletes:	kde-style-bluecurve
Obsoletes:	kde-theme-bluecurve

%description -n theme-QtCurve-common
A free and corrected port of Red Hat's GTK+/Qt theme.
Documentation and common files package.

%description -n theme-QtCurve-common -l pl
Darmowa i poprawiona wersja motywu GTK+/Qt zrobionego przez Red Hata.
Pakiet z dokumentacja i plikami wspó³dzielonymi.

%prep
%setup -q
sed -i "s#/lib/gtk/#/%{_lib}/gtk/#g" gtk/Makefile.am
sed -i "s#/lib/gtk-2.0/#/%{_lib}/gtk-2.0/#g" gtk2/Makefile.am

%build
cp /usr/share/automake/config.sub admin

%{__make} -f admin/Makefile.common cvs
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/themes/QtCurve*/gtk
%endif

%if %{with gtk2}
%files -n gtk2-theme-QtCurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/*/*/*.so
%{_datadir}/themes/QtCurve*/gtk-2.0
%endif

%files -n theme-QtCurve-common
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%dir %{_datadir}/themes/QtCurve*
